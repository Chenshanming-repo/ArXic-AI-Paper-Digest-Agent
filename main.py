"""ArXiv digest orchestrator.

Run from the GitHub Action (or locally) to:
  1. Fetch the most recent ArXiv submissions in the configured categories.
  2. Drop any papers we have already digested on a previous day.
  3. Summarise all matching papers, or up to MAX_PAPERS if a cap is configured.
  4. Append the result to digest/digest.md and overwrite digest/latest.md.
  5. Archive each generated digest as an individual Markdown file.
  6. On schedule, create Chinese weekly/monthly rollups from digest history.

Exits with code 0 on success (including the "no new papers today" case)
and code 1 on a fatal error so the Action shows as failed.
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import sys
from collections.abc import Sequence
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from dotenv import load_dotenv

# Load local .env values before config.py reads environment-backed defaults.
load_dotenv()

import config
from src.rollup import (
    parse_digest_sections,
    previous_calendar_month,
    previous_iso_week,
    records_between,
)
from src.writer import (
    append_archive_file,
    append_period_summary,
    append_to_digest,
    period_summary_exists,
    read_seen_arxiv_ids,
    render_digest,
    render_period_summary,
    write_archive_file,
    write_latest,
)

logger = logging.getLogger("arxiv_digest")


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate ArXiv digest files.")
    subparsers = parser.add_subparsers(dest="command")

    fetch_parser = subparsers.add_parser("fetch", help="Fetch arXiv metadata.")
    fetch_parser.add_argument("--query", required=True, help="Raw arXiv search query.")
    fetch_parser.add_argument("--max-results", type=int, default=100)
    fetch_parser.add_argument("--start", type=int, default=0)
    fetch_parser.add_argument("--sort-by", default="submittedDate")
    fetch_parser.add_argument("--sort-order", default="descending")
    fetch_parser.add_argument("--db", type=Path, default=config.METADATA_DB_FILE)
    fetch_parser.add_argument("--api-url", default=config.ARXIV_API_URL)
    fetch_parser.add_argument("--user-agent", default=config.ARXIV_USER_AGENT)
    fetch_parser.add_argument(
        "--min-interval",
        type=float,
        default=config.ARXIV_RATE_LIMIT_SECONDS,
        help="Minimum seconds between arXiv API requests.",
    )
    fetch_parser.add_argument(
        "--max-retries", type=int, default=config.ARXIV_MAX_RETRIES
    )

    daily_parser = subparsers.add_parser(
        "fetch-daily", help="Fetch recent submitted/updated arXiv metadata."
    )
    daily_parser.add_argument("--days", type=int, default=1)
    daily_parser.add_argument("--query", default=None)
    daily_parser.add_argument("--max-results", type=int, default=config.ARXIV_PAGE_SIZE)
    daily_parser.add_argument("--db", type=Path, default=config.METADATA_DB_FILE)
    daily_parser.add_argument("--api-url", default=config.ARXIV_API_URL)
    daily_parser.add_argument("--user-agent", default=config.ARXIV_USER_AGENT)
    daily_parser.add_argument(
        "--min-interval",
        type=float,
        default=config.ARXIV_RATE_LIMIT_SECONDS,
        help="Minimum seconds between arXiv API requests.",
    )
    daily_parser.add_argument(
        "--max-retries", type=int, default=config.ARXIV_MAX_RETRIES
    )

    parser.add_argument(
        "--mode",
        choices=[
            "daily",
            "weekly",
            "monthly",
            "archive",
            "email-test",
            "ai-email-test",
        ],
        default="daily",
        help=(
            "daily fetches and summarises new papers; weekly/monthly generate "
            "only the previous completed period rollup; archive backfills "
            "per-day archive files from digest history; email-test sends a "
            "Chinese Markdown test digest without API calls; ai-email-test "
            "generates a Chinese AI summary and emails it."
        ),
    )
    parser.add_argument(
        "--force-rollups",
        action="store_true",
        help="With --mode daily, generate weekly and monthly rollups even if not due.",
    )
    parser.add_argument(
        "--email-to",
        help=(
            "Comma-separated recipients for --mode email-test or "
            "ai-email-test. Overrides EMAIL_RECIPIENTS for that test send."
        ),
    )
    return parser.parse_args(argv)


def _require_api_key() -> str:
    api_key = os.getenv("API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "API_KEY or OPENAI_API_KEY is not set. Add it as a GitHub Actions "
            "secret or to your local .env file."
        )
    return api_key


def _build_openai_client(api_key: str):
    from openai import OpenAI

    kwargs: dict[str, str] = {"api_key": api_key}
    if config.OPENAI_BASE_URL:
        base_url = _normalise_openai_base_url(config.OPENAI_BASE_URL)
        kwargs["base_url"] = base_url
        logger.info("Using OpenAI-compatible base URL: %s", base_url)
    return OpenAI(**kwargs)


def _extract_model_ids(models_response) -> list[str]:
    data = getattr(models_response, "data", None)
    if data is None and isinstance(models_response, dict):
        data = models_response.get("data")
    if not data:
        return []

    model_ids: list[str] = []
    for item in data:
        model_id = getattr(item, "id", None)
        if model_id is None and isinstance(item, dict):
            model_id = item.get("id")
        if model_id:
            model_ids.append(str(model_id))
    return model_ids


def _is_text_model(model_id: str) -> bool:
    lowered = model_id.lower()
    blocked_terms = [
        "image",
        "embedding",
        "moderation",
        "whisper",
        "tts",
        "audio",
        "rerank",
    ]
    return not any(term in lowered for term in blocked_terms)


def _model_power_score(model_id: str) -> int:
    lowered = model_id.lower()
    score = 0
    match = re.search(r"gpt-(\d)(?:\.(\d))?", lowered)
    if match:
        major = int(match.group(1))
        minor = int(match.group(2) or 0)
        score = major * 1000 + minor * 100
    elif "claude" in lowered or "gemini" in lowered:
        score = 3000

    if "mini" in lowered:
        score -= 50
    if "compact" in lowered:
        score -= 60
    if "codex" in lowered:
        score -= 100
    if "spark" in lowered:
        score -= 120
    return score


def _rank_auto_models(model_ids: list[str]) -> list[str]:
    text_models = [model_id for model_id in model_ids if _is_text_model(model_id)]
    if not text_models:
        raise RuntimeError("OPENAI_MODEL=auto could not find any text models.")
    return sorted(text_models, key=_model_power_score, reverse=True)


def _model_accepts_chat_completion(client, model: str) -> bool:
    from src.summariser import _extract_response_content

    try:
        response = client.chat.completions.create(
            model=model,
            max_tokens=8,
            messages=[
                {"role": "system", "content": "Reply briefly."},
                {"role": "user", "content": "ping"},
            ],
        )
    except Exception as exc:
        logger.info("Auto model candidate failed: %s (%s)", model, exc)
        return False

    try:
        _extract_response_content(response)
    except RuntimeError as exc:
        logger.info("Auto model candidate returned invalid content: %s (%s)", model, exc)
        return False
    return True


def _resolve_openai_model(client) -> str:
    configured = config.OPENAI_MODEL.strip()
    if configured and configured.lower() not in {"auto", "default"}:
        return configured

    models_response = client.models.list()
    model_ids = _extract_model_ids(models_response)
    candidates = _rank_auto_models(model_ids)
    logger.info("Auto model candidates by preference: %s", candidates)
    for model in candidates:
        if _model_accepts_chat_completion(client, model):
            logger.info("Auto-selected OpenAI-compatible model: %s", model)
            return model

    raise RuntimeError("OPENAI_MODEL=auto could not find a usable chat model.")


def _normalise_openai_base_url(raw_base_url: str) -> str:
    """Append /v1 when a provider host is given without an API path."""
    parsed = urlsplit(raw_base_url.strip().rstrip("/"))
    if not parsed.scheme or not parsed.netloc:
        return raw_base_url
    if parsed.path in {"", "/"}:
        return urlunsplit((parsed.scheme, parsed.netloc, "/v1", "", ""))
    return raw_base_url.rstrip("/")


def _daily_archive_path(digest_date) -> Path:
    return config.DAILY_ARCHIVE_DIR / f"{digest_date.isoformat()}.md"


def _weekly_archive_path(start_date, end_date) -> Path:
    return (
        config.WEEKLY_ARCHIVE_DIR
        / f"{start_date.isoformat()}_to_{end_date.isoformat()}.md"
    )


def _monthly_archive_path(start_date) -> Path:
    return config.MONTHLY_ARCHIVE_DIR / f"{start_date.strftime('%Y-%m')}.md"


def _send_digest_email(
    *,
    subject: str,
    rendered: str,
    attachment_name: str,
    recipients: list[str] | None = None,
) -> bool:
    from src.emailer import send_markdown_email

    try:
        return send_markdown_email(
            subject=subject,
            markdown=rendered,
            attachment_name=attachment_name,
            recipients=recipients or config.EMAIL_RECIPIENTS,
            email_from=config.EMAIL_FROM,
            smtp_host=config.SMTP_HOST,
            smtp_port=config.SMTP_PORT,
            smtp_username=config.SMTP_USERNAME,
            smtp_password=config.SMTP_PASSWORD,
            use_tls=config.SMTP_USE_TLS,
            use_ssl=config.SMTP_USE_SSL,
        )
    except Exception as exc:
        logger.error("Failed to send digest email '%s': %s", subject, exc)
        return False


def _send_subscription_emails(
    *,
    entries,
    found_in_category: dict[str, str],
    digest_date,
    subscriptions,
) -> None:
    """Send one filtered daily digest per Subscription.

    Subscribers with zero matched papers receive nothing.
    """
    from src.models import Digest

    for sub in subscriptions:
        wanted = set(sub.categories)
        filtered = [
            entry
            for entry in entries
            if found_in_category.get(entry.paper.arxiv_id) in wanted
        ]
        if not filtered:
            logger.info(
                "Subscription %s has no matched papers today, skipping",
                sub.email,
            )
            continue

        rendered = render_digest(
            Digest(digest_date=digest_date, entries=filtered),
            category_by_id=found_in_category,
            category_order=list(sub.categories),
        )
        category_label = ",".join(sub.categories)
        _send_digest_email(
            subject=f"ArXiv 每日论文摘要 [{category_label}] {digest_date.isoformat()}",
            rendered=rendered,
            attachment_name=f"arxiv-daily-{digest_date.isoformat()}.md",
            recipients=[sub.email],
        )


def _run_daily_digest(now: datetime, client, model: str) -> int:
    from src.fetcher import fetch_recent_papers
    from src.models import Digest
    from src.summariser import summarise_papers

    arxiv_args = argparse.Namespace(
        api_url=config.ARXIV_API_URL,
        user_agent=config.ARXIV_USER_AGENT,
        min_interval=config.ARXIV_RATE_LIMIT_SECONDS,
        max_retries=config.ARXIV_MAX_RETRIES,
    )
    with _build_arxiv_client(arxiv_args) as arxiv_client:
        fetched, found_in_category = fetch_recent_papers(
            categories=config.CATEGORIES,
            topic_keywords=config.TOPIC_KEYWORDS,
            page_size=config.ARXIV_PAGE_SIZE,
            api_url=config.ARXIV_API_URL,
            arxiv_client=arxiv_client,
        )

    if not fetched:
        logger.info(
            "ArXiv returned no parsable papers for categories %s, exiting "
            "cleanly without writing.",
            config.CATEGORIES,
        )
        return 0

    try:
        new_count, updated_count = _store_fetched_papers(fetched, config.METADATA_DB_FILE)
        logger.info(
            "Cached daily metadata in %s (%d new, %d already cached/updated)",
            config.METADATA_DB_FILE,
            new_count,
            updated_count,
        )
    except Exception as exc:
        logger.warning("Could not update local arXiv metadata cache: %s", exc)

    seen_ids = read_seen_arxiv_ids(config.DIGEST_FILE)
    fresh = [p for p in fetched if p.arxiv_id not in seen_ids]
    logger.info(
        "Filtered %d fetched papers against %d already-digested ids -> %d new",
        len(fetched),
        len(seen_ids),
        len(fresh),
    )

    if not fresh:
        logger.info(
            "All %d most-recent ArXiv papers have already been digested, "
            "exiting cleanly without writing.",
            len(fetched),
        )
        return 0

    if config.MAX_PAPERS > 0:
        papers = fresh[: config.MAX_PAPERS]
        logger.info(
            "Summarising %d/%d fresh papers with model %s",
            len(papers),
            len(fresh),
            model,
        )
    else:
        papers = fresh
        logger.info(
            "Summarising all %d fresh matching papers with model %s",
            len(papers),
            model,
        )

    entries = summarise_papers(
        papers,
        client=client,
        model=model,
        max_tokens=config.OPENAI_MAX_TOKENS,
    )

    if not entries:
        logger.warning(
            "All %d papers failed to summarise, exiting without writing.",
            len(papers),
        )
        return 0

    digest = Digest(digest_date=now.date(), entries=entries)
    rendered = render_digest(
        digest,
        category_by_id=found_in_category,
        category_order=list(config.CATEGORIES),
    )

    append_to_digest(config.DIGEST_FILE, rendered)
    write_latest(config.LATEST_FILE, rendered)
    append_archive_file(
        _daily_archive_path(digest.digest_date),
        rendered,
        f"ArXiv 每日论文摘要 {digest.digest_date.isoformat()}",
    )
    if config.EMAIL_SEND_DAILY:
        _send_digest_email(
            subject=f"ArXiv 每日论文摘要 {digest.digest_date.isoformat()}",
            rendered=rendered,
            attachment_name=f"arxiv-daily-{digest.digest_date.isoformat()}.md",
        )

    logger.info(
        "Digest complete: %d/%d papers summarised for %s",
        len(entries),
        len(papers),
        digest.digest_date.isoformat(),
    )
    return 0


def _period_label(start_date, end_date) -> str:
    return f"{start_date.isoformat()} 至 {end_date.isoformat()}"


def _run_period_summary(kind: str, now: datetime, client, model: str) -> bool:
    from openai import OpenAIError

    from src.summariser import summarise_period

    if kind == "weekly":
        start_date, end_date = previous_iso_week(now)
        output_file = config.WEEKLY_DIGEST_FILE
        latest_file = config.LATEST_WEEKLY_FILE
        archive_file = _weekly_archive_path(start_date, end_date)
        title = "ArXiv 每周论文综述"
        period_name = f"{_period_label(start_date, end_date)} 这一周"
    elif kind == "monthly":
        start_date, end_date = previous_calendar_month(now)
        output_file = config.MONTHLY_DIGEST_FILE
        latest_file = config.LATEST_MONTHLY_FILE
        archive_file = _monthly_archive_path(start_date)
        title = "ArXiv 每月论文综述"
        period_name = f"{_period_label(start_date, end_date)} 这个月"
    else:
        raise ValueError(f"Unsupported period summary kind: {kind}")

    period_label = _period_label(start_date, end_date)
    if period_summary_exists(output_file, period_label):
        logger.info("%s summary for %s already exists, skipping", kind, period_label)
        return False

    records = records_between(config.DIGEST_FILE, start_date, end_date)
    if not records:
        logger.info(
            "No daily digest records found for %s summary range %s",
            kind,
            period_label,
        )
        return False

    logger.info(
        "Generating %s summary for %s from %d papers",
        kind,
        period_label,
        len(records),
    )

    try:
        summary = summarise_period(
            [record.as_prompt_record() for record in records],
            period_name=period_name,
            client=client,
            model=model,
            max_tokens=config.ROLLUP_MAX_TOKENS,
        )
    except (OpenAIError, RuntimeError, ValueError) as exc:
        logger.error("Failed to generate %s summary for %s: %s", kind, period_label, exc)
        return False

    rendered = render_period_summary(period_label, summary, len(records))
    append_period_summary(output_file, rendered, title)
    write_latest(latest_file, rendered)
    write_archive_file(archive_file, rendered, f"{title} {period_label}")
    if kind == "weekly" and config.EMAIL_SEND_WEEKLY:
        _send_digest_email(
            subject=f"{title} {period_label}",
            rendered=rendered,
            attachment_name=f"arxiv-weekly-{start_date.isoformat()}_to_{end_date.isoformat()}.md",
        )
    if kind == "monthly" and config.EMAIL_SEND_MONTHLY:
        _send_digest_email(
            subject=f"{title} {period_label}",
            rendered=rendered,
            attachment_name=f"arxiv-monthly-{start_date.strftime('%Y-%m')}.md",
        )
    return True


def _run_due_rollups(
    now: datetime, client, model: str, *, force: bool = False
) -> None:
    if config.ENABLE_WEEKLY_SUMMARY and (force or now.weekday() == 0):
        _run_period_summary("weekly", now, client, model)
    if config.ENABLE_MONTHLY_SUMMARY and (force or now.day == 1):
        _run_period_summary("monthly", now, client, model)


def _run_archive_backfill() -> int:
    sections = parse_digest_sections(config.DIGEST_FILE)
    grouped: dict[str, list[str]] = {}
    for section in sections:
        grouped.setdefault(section.digest_date.isoformat(), []).append(section.rendered)

    for digest_date, rendered_sections in sorted(grouped.items()):
        rendered = "\n".join(section.rstrip() for section in rendered_sections) + "\n"
        write_archive_file(
            config.DAILY_ARCHIVE_DIR / f"{digest_date}.md",
            rendered,
            f"ArXiv 每日论文摘要 {digest_date}",
        )

    logger.info("Backfilled %d daily archive files", len(grouped))
    return 0


def _build_arxiv_client(args: argparse.Namespace):
    from src.arxiv_client import ArxivApiClient, ArxivRateLimiter

    limiter = ArxivRateLimiter(
        min_interval_seconds=args.min_interval,
        jitter_seconds=config.ARXIV_RATE_LIMIT_JITTER_SECONDS,
    )
    return ArxivApiClient(
        api_url=args.api_url,
        user_agent=args.user_agent,
        max_retries=args.max_retries,
        rate_limiter=limiter,
    )


def _store_fetched_papers(papers, db_path: Path) -> tuple[int, int]:
    from src.storage import PaperMetadataStore

    with PaperMetadataStore(db_path) as store:
        return store.upsert_papers(papers)


def _run_fetch_command(args: argparse.Namespace) -> int:
    from src.fetcher import fetch_papers_by_query

    try:
        with _build_arxiv_client(args) as arxiv_client:
            papers = fetch_papers_by_query(
                query=args.query,
                max_results=args.max_results,
                api_url=args.api_url,
                sort_by=args.sort_by,
                sort_order=args.sort_order,
                start=args.start,
                arxiv_client=arxiv_client,
            )
    except Exception:
        logger.exception("arXiv fetch command failed")
        return 1

    new_count, updated_count = _store_fetched_papers(papers, args.db)
    logger.info(
        "Stored %d papers in %s (%d new, %d already cached/updated)",
        len(papers),
        args.db,
        new_count,
        updated_count,
    )
    return 0


def _run_fetch_daily_command(args: argparse.Namespace) -> int:
    from src.fetcher import build_category_query, build_recent_date_query

    base_query = args.query or build_category_query(config.CATEGORIES)
    query = build_recent_date_query(base_query, days=args.days)
    logger.info("Daily arXiv metadata query: %s", query)

    fetch_args = argparse.Namespace(
        query=query,
        max_results=args.max_results,
        start=0,
        sort_by="lastUpdatedDate",
        sort_order="descending",
        db=args.db,
        api_url=args.api_url,
        user_agent=args.user_agent,
        min_interval=args.min_interval,
        max_retries=args.max_retries,
    )
    return _run_fetch_command(fetch_args)


def _run_email_test(email_to: str | None) -> int:
    recipients = (
        [item.strip() for item in email_to.split(",") if item.strip()]
        if email_to
        else config.EMAIL_RECIPIENTS
    )
    rendered = (
        "---\n"
        "## 邮件发送测试\n\n"
        "### 1. ArXiv 摘要邮件中文测试\n"
        "**作者:** ArXiv Digest Agent\n"
        "**链接:** https://arxiv.org/\n"
        "**摘要:** 这是一封中文 Markdown 测试邮件，用于验证 SMTP 配置、"
        "收件人列表和附件发送是否正常。正式的每日、每周和每月邮件会使用"
        "模型新生成的中文论文摘要；旧的历史 digest 文件如果原本是英文，"
        "不会在测试模式中被直接发送。\n"
    )

    sent = _send_digest_email(
        subject="ArXiv 摘要邮件测试",
        rendered=rendered,
        attachment_name="arxiv-email-test.md",
        recipients=recipients,
    )
    return 0 if sent else 1


def _run_ai_email_test(email_to: str | None, client, model: str) -> int:
    from src.models import Digest, DigestEntry, Paper
    from src.summariser import summarise_paper

    recipients = (
        [item.strip() for item in email_to.split(",") if item.strip()]
        if email_to
        else config.EMAIL_RECIPIENTS
    )
    now = datetime.now(timezone.utc)
    paper = Paper(
        arxiv_id="test-ai-email",
        url="https://arxiv.org/abs/test-ai-email",
        title="Sample Deployment Test for AI Paper Digest",
        authors=["ArXiv Digest Agent"],
        abstract=(
            "This deployment test checks whether an ArXiv digest system can "
            "send paper metadata to an OpenAI-compatible model, receive a "
            "concise technical summary, render it as Markdown, and deliver "
            "the generated digest through SMTP email. The test focuses on "
            "verifying the production path rather than evaluating a real "
            "research contribution."
        ),
        published=now,
        primary_category="cs.AI",
    )
    summary = summarise_paper(
        paper,
        client=client,
        model=model,
        max_tokens=config.OPENAI_MAX_TOKENS,
    )
    rendered = render_digest(
        Digest(
            digest_date=now.date(),
            entries=[DigestEntry(paper=paper, summary=summary)],
        )
    )
    sent = _send_digest_email(
        subject="ArXiv AI 摘要邮件测试",
        rendered=rendered,
        attachment_name="arxiv-ai-email-test.md",
        recipients=recipients,
    )
    return 0 if sent else 1


def run(argv: Sequence[str] | None = None) -> int:
    """Main entry point. Returns the desired process exit code."""
    args = _parse_args(argv)
    load_dotenv()
    _configure_logging()

    if args.command == "fetch":
        return _run_fetch_command(args)
    if args.command == "fetch-daily":
        return _run_fetch_daily_command(args)

    if args.mode == "archive":
        return _run_archive_backfill()
    if args.mode == "email-test":
        return _run_email_test(args.email_to)

    api_key = _require_api_key()
    client = _build_openai_client(api_key)
    model = _resolve_openai_model(client)

    now = datetime.now(timezone.utc)
    logger.info("Starting %s digest run at %s", args.mode, now.isoformat())

    if args.mode == "ai-email-test":
        return _run_ai_email_test(args.email_to, client, model)
    if args.mode == "weekly":
        _run_period_summary("weekly", now, client, model)
        return 0
    if args.mode == "monthly":
        _run_period_summary("monthly", now, client, model)
        return 0

    exit_code = _run_daily_digest(now, client, model)
    _run_due_rollups(now, client, model, force=args.force_rollups)
    return exit_code


def main() -> None:
    try:
        sys.exit(run())
    except Exception:
        logger.exception("Fatal error during digest run")
        sys.exit(1)


if __name__ == "__main__":
    main()
