"""Render and write the daily digest as Markdown."""

from __future__ import annotations

import logging
import re
from pathlib import Path

from src.models import Digest, DigestEntry

logger = logging.getLogger(__name__)

# Match the arxiv id portion of any abs URL we have ever written into the
# digest. We intentionally include the version suffix so reposted versions
# (vN+1) of an already-digested paper would be treated as new.
_ARXIV_URL_RE = re.compile(r"https?://arxiv\.org/abs/(\S+)")


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
