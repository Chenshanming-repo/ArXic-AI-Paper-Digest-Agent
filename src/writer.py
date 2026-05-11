"""Render and write the daily digest as Markdown."""

from __future__ import annotations

import logging
from pathlib import Path

from src.models import Digest, DigestEntry

logger = logging.getLogger(__name__)


def _format_authors(authors: list[str]) -> str:
    if not authors:
        return "Unknown"
    return ", ".join(authors)


def _render_entry(index: int, entry: DigestEntry) -> str:
    paper = entry.paper
    return (
        f"### {index}. {paper.title}\n"
        f"**Authors:** {_format_authors(paper.authors)}\n"
        f"**Link:** {paper.url}\n"
        f"**Summary:** {entry.summary}\n"
    )


def render_digest(digest: Digest) -> str:
    """Render a Digest as a Markdown section with a leading separator."""
    if not digest.entries:
        raise ValueError("Cannot render a digest with no entries.")

    lines: list[str] = ["---", f"## {digest.digest_date.isoformat()}", ""]
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
        header = "# ArXiv Daily Digest\n\nAutomatically generated daily summaries of recent ArXiv papers.\n\n"
        path.write_text(header + rendered, encoding="utf-8")
    logger.info("Appended digest to %s", path)


def write_latest(path: Path, rendered: str) -> None:
    """Overwrite the latest.md file with just today's digest."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered, encoding="utf-8")
    logger.info("Wrote latest digest to %s", path)
