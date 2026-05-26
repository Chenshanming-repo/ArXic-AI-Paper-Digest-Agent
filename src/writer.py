"""Render and write digest Markdown files."""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import Digest, DigestEntry

logger = logging.getLogger(__name__)

# Match the arxiv id portion of any abs URL we have ever written into the
# digest. We intentionally include the version suffix so reposted versions
# (vN+1) of an already-digested paper would be treated as new.
_ARXIV_URL_RE = re.compile(r"https?://arxiv\.org/abs/(\S+)")


def _format_authors(authors: list[str]) -> str:
    if not authors:
        return "未知"
    return ", ".join(authors)


def _render_entry(index: int, entry: DigestEntry, *, heading: str = "###") -> str:
    paper = entry.paper
    return (
        f"{heading} {index}. {paper.title}\n"
        f"**作者:** {_format_authors(paper.authors)}\n"
        f"**链接:** {paper.url}\n"
        f"**摘要:** {entry.summary}\n"
    )


def render_digest(
    digest: Digest,
    *,
    category_by_id: dict[str, str] | None = None,
    category_order: list[str] | None = None,
) -> str:
    """Render a Digest as a Markdown section with a leading separator.

    When `category_by_id` and `category_order` are both supplied, entries
    are grouped under one ``### <category>`` heading per category, in the
    order given. Entries whose arxiv_id is missing from `category_by_id`
    fall into a trailing ``### 其他`` section. When either argument is
    omitted the original flat layout is preserved.
    """
    if not digest.entries:
        raise ValueError("Cannot render a digest with no entries.")

    lines: list[str] = ["---", f"## {digest.digest_date.isoformat()}", ""]

    if category_by_id is not None and category_order:
        grouped: dict[str, list[DigestEntry]] = {cat: [] for cat in category_order}
        leftovers: list[DigestEntry] = []
        for entry in digest.entries:
            category = category_by_id.get(entry.paper.arxiv_id)
            if category in grouped:
                grouped[category].append(entry)
            else:
                leftovers.append(entry)

        def emit_section(header: str, entries: list[DigestEntry]) -> None:
            lines.append(f"### {header}")
            lines.append("")
            for index, entry in enumerate(entries, start=1):
                lines.append(_render_entry(index, entry, heading="####"))

        for category in category_order:
            entries = grouped[category]
            if entries:
                emit_section(category, entries)
        if leftovers:
            emit_section("其他", leftovers)
    else:
        for index, entry in enumerate(digest.entries, start=1):
            lines.append(_render_entry(index, entry))

    return "\n".join(lines).rstrip() + "\n"


def append_to_digest(path: Path, rendered: str) -> None:
    """Append rendered Markdown to the running digest file, creating it if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size > 0:
        existing = path.read_text(encoding="utf-8")
        separator = "" if existing.endswith("\n") else "\n"
        path.write_text(existing + separator + "\n" + rendered, encoding="utf-8")
    else:
        header = "# ArXiv 每日论文摘要\n\n自动生成的近期 ArXiv 论文中文摘要。\n\n"
        path.write_text(header + rendered, encoding="utf-8")
    logger.info("Appended digest to %s", path)


def write_latest(path: Path, rendered: str) -> None:
    """Overwrite the latest.md file with just today's digest."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered, encoding="utf-8")
    logger.info("Wrote latest digest to %s", path)


def append_archive_file(path: Path, rendered: str, title: str) -> None:
    """Append a rendered section to one archive file, creating it if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size > 0:
        existing = path.read_text(encoding="utf-8")
        separator = "" if existing.endswith("\n") else "\n"
        path.write_text(existing + separator + "\n" + rendered, encoding="utf-8")
    else:
        path.write_text(f"# {title}\n\n" + rendered, encoding="utf-8")
    logger.info("Archived digest section to %s", path)


def write_archive_file(path: Path, rendered: str, title: str) -> None:
    """Overwrite one archive file with a complete rendered digest."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n" + rendered, encoding="utf-8")
    logger.info("Wrote archive file to %s", path)


def render_period_summary(period_label: str, summary: str, paper_count: int) -> str:
    """Render a weekly/monthly rollup section."""
    if not summary.strip():
        raise ValueError("Cannot render an empty period summary.")
    lines = [
        "---",
        f"## {period_label}",
        "",
        f"**论文数量:** {paper_count}",
        "",
        summary.strip(),
    ]
    return "\n".join(lines).rstrip() + "\n"


def period_summary_exists(path: Path, period_label: str) -> bool:
    """Return whether a weekly/monthly summary already has this heading."""
    if not path.exists():
        return False
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        logger.warning("Could not read %s for rollup dedup: %s", path, exc)
        return False
    return f"## {period_label}" in text


def append_period_summary(path: Path, rendered: str, title: str) -> None:
    """Append a rendered weekly/monthly summary, creating the file if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size > 0:
        existing = path.read_text(encoding="utf-8")
        separator = "" if existing.endswith("\n") else "\n"
        path.write_text(existing + separator + "\n" + rendered, encoding="utf-8")
    else:
        header = f"# {title}\n\n自动生成的 ArXiv 论文阶段性中文综述。\n\n"
        path.write_text(header + rendered, encoding="utf-8")
    logger.info("Appended period summary to %s", path)


def read_seen_arxiv_ids(path: Path) -> set[str]:
    """Return the set of arxiv ids already present in the running digest.

    Returns an empty set if the file does not exist yet (first run) or
    cannot be read. Used to suppress re-emitting papers we have already
    summarised on a previous day.
    """
    if not path.exists():
        return set()
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        logger.warning("Could not read %s for dedup: %s", path, exc)
        return set()
    return {match.rstrip(".,);]") for match in _ARXIV_URL_RE.findall(text)}
