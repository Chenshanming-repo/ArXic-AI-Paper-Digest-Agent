"""ArXiv digest orchestrator.

Run from the GitHub Action (or locally) to:
  1. Fetch the most recent ArXiv submissions in the configured categories.
  2. Drop any papers we have already digested on a previous day.
  3. Summarise up to MAX_PAPERS of the remainder with an OpenAI-compatible API.
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
import sys
from collections.abc import Sequence
from datetime import datetime, timezone
from pathlib import Path

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
    parser.add_argument(
        "--mode",
        choices=["daily", "weekly", "monthly", "archive"],
        default="daily",
        help=(
            "daily fetches and summarises new papers; weekly/monthly generate "
            "only the previous completed period rollup; archive backfills "
            "per-day archive files from digest history."
        ),
    )
    parser.add_argument(
        "--force-rollups",
        action="store_true",
        help="With --mode daily, generate weekly and monthly rollups even if not due.",
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
        kwargs["base_url"] = config.OPENAI_BASE_URL
        logger.info("Using OpenAI-compatible base URL: %s", config.OPENAI_BASE_URL)
    return OpenAI(**kwargs)


def _daily_archive_path(digest_date) -> Path:
    return config.DAILY_ARCHIVE_DIR / f"{digest_date.isoformat()}.md"


def _weekly_archive_path(start_date, end_date) -> Path:
    return (
        config.WEEKLY_ARCHIVE_DIR
        / f"{start_date.isoformat()}_to_{end_date.isoformat()}.md"
    )


def _monthly_archive_path(start_date) -> Path:
    return config.MONTHLY_ARCHIVE_DIR / f"{start_date.strftime('%Y-%m')}.md"


def _run_daily_digest(now: datetime, client) -> int:
    from src.fetcher import fetch_recent_papers
    from src.models import Digest
    from src.summariser import summarise_papers

    fetched = fetch_recent_papers(
        categories=config.CATEGORIES,
        topic_keywords=config.TOPIC_KEYWORDS,
        page_size=config.ARXIV_PAGE_SIZE,
        api_url=config.ARXIV_API_URL,
    )

    if not fetched:
        logger.info(
            "ArXiv returned no parsable papers for categories %s, exiting "
            "cleanly without writing.",
            config.CATEGORIES,
        )
        return 0

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

    papers = fresh[: config.MAX_PAPERS]
    logger.info("Summarising %d papers with model %s", len(papers), config.OPENAI_MODEL)

    entries = summarise_papers(
        papers,
        client=client,
        model=config.OPENAI_MODEL,
        max_tokens=config.OPENAI_MAX_TOKENS,
    )

    if not entries:
        logger.warning(
            "All %d papers failed to summarise, exiting without writing.",
            len(papers),
        )
        return 0

    digest = Digest(digest_date=now.date(), entries=entries)
    rendered = render_digest(digest)

    append_to_digest(config.DIGEST_FILE, rendered)
    write_latest(config.LATEST_FILE, rendered)
    append_archive_file(
        _daily_archive_path(digest.digest_date),
        rendered,
        f"ArXiv 每日论文摘要 {digest.digest_date.isoformat()}",
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


def _run_period_summary(kind: str, now: datetime, client) -> bool:
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
            model=config.OPENAI_MODEL,
            max_tokens=config.ROLLUP_MAX_TOKENS,
        )
    except (OpenAIError, RuntimeError, ValueError) as exc:
        logger.error("Failed to generate %s summary for %s: %s", kind, period_label, exc)
        return False

    rendered = render_period_summary(period_label, summary, len(records))
    append_period_summary(output_file, rendered, title)
    write_latest(latest_file, rendered)
    write_archive_file(archive_file, rendered, f"{title} {period_label}")
    return True


def _run_due_rollups(now: datetime, client, *, force: bool = False) -> None:
    if config.ENABLE_WEEKLY_SUMMARY and (force or now.weekday() == 0):
        _run_period_summary("weekly", now, client)
    if config.ENABLE_MONTHLY_SUMMARY and (force or now.day == 1):
        _run_period_summary("monthly", now, client)


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


def run(argv: Sequence[str] | None = None) -> int:
    """Main entry point. Returns the desired process exit code."""
    args = _parse_args(argv)
    load_dotenv()
    _configure_logging()

    if args.mode == "archive":
        return _run_archive_backfill()

    api_key = _require_api_key()
    client = _build_openai_client(api_key)

    now = datetime.now(timezone.utc)
    logger.info("Starting %s digest run at %s", args.mode, now.isoformat())

    if args.mode == "weekly":
        _run_period_summary("weekly", now, client)
        return 0
    if args.mode == "monthly":
        _run_period_summary("monthly", now, client)
        return 0

    exit_code = _run_daily_digest(now, client)
    _run_due_rollups(now, client, force=args.force_rollups)
    return exit_code


def main() -> None:
    try:
        sys.exit(run())
    except Exception:
        logger.exception("Fatal error during digest run")
        sys.exit(1)


if __name__ == "__main__":
    main()
