"""Read daily digest history and select records for weekly/monthly rollups."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)

_DATE_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s*$")
_ENTRY_RE = re.compile(r"^###\s+\d+\.\s+(.+?)\s*$")
_FIELD_RE = re.compile(r"^\*\*(作者|Authors|链接|Link|摘要|Summary):\*\*\s*(.*)$")

_FIELD_MAP = {
    "作者": "authors",
    "Authors": "authors",
    "链接": "link",
    "Link": "link",
    "摘要": "summary",
    "Summary": "summary",
}


@dataclass(frozen=True)
class DigestRecord:
    """A compact record parsed from digest/digest.md."""

    digest_date: date
    title: str
    authors: str
    link: str
    summary: str

    def as_prompt_record(self) -> dict[str, str]:
        return {
            "date": self.digest_date.isoformat(),
            "title": self.title,
            "authors": self.authors,
            "link": self.link,
            "summary": self.summary,
        }


@dataclass(frozen=True)
class DigestSection:
    """One rendered daily section parsed from digest/digest.md."""

    digest_date: date
    rendered: str


def _parse_date(raw: str) -> date | None:
    try:
        return date.fromisoformat(raw)
    except ValueError:
        return None


def parse_digest_records(path: Path) -> list[DigestRecord]:
    """Parse daily digest Markdown into compact records for rollup prompts."""
    if not path.exists():
        return []

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        logger.warning("Could not read %s for rollup source records: %s", path, exc)
        return []

    records: list[DigestRecord] = []
    current_date: date | None = None
    current: dict[str, str] | None = None

    def flush_current() -> None:
        nonlocal current
        if current_date is None or current is None:
            current = None
            return
        title = current.get("title", "").strip()
        summary = current.get("summary", "").strip()
        if not title or not summary:
            current = None
            return
        records.append(
            DigestRecord(
                digest_date=current_date,
                title=title,
                authors=current.get("authors", "").strip(),
                link=current.get("link", "").strip(),
                summary=summary,
            )
        )
        current = None

    for line in lines:
        date_match = _DATE_RE.match(line)
        if date_match:
            flush_current()
            current_date = _parse_date(date_match.group(1))
            continue

        entry_match = _ENTRY_RE.match(line)
        if entry_match and current_date is not None:
            flush_current()
            current = {"title": entry_match.group(1).strip()}
            continue

        field_match = _FIELD_RE.match(line)
        if field_match and current is not None:
            field_name = _FIELD_MAP[field_match.group(1)]
            current[field_name] = field_match.group(2).strip()

    flush_current()
    return records


def parse_digest_sections(path: Path) -> list[DigestSection]:
    """Parse digest/digest.md into rendered daily sections grouped by date."""
    if not path.exists():
        return []

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        logger.warning("Could not read %s for archive source sections: %s", path, exc)
        return []

    sections: list[DigestSection] = []
    for raw_section in re.split(r"(?m)^---\s*$", text):
        stripped = raw_section.strip()
        if not stripped:
            continue

        lines = stripped.splitlines()
        date_value: date | None = None
        for line in lines:
            date_match = _DATE_RE.match(line)
            if date_match:
                date_value = _parse_date(date_match.group(1))
                break

        if date_value is None:
            continue

        rendered = "---\n" + stripped + "\n"
        sections.append(DigestSection(digest_date=date_value, rendered=rendered))

    return sections


def records_between(path: Path, start: date, end: date) -> list[DigestRecord]:
    """Return records whose digest date is inside the inclusive date range."""
    return [
        record
        for record in parse_digest_records(path)
        if start <= record.digest_date <= end
    ]


def previous_iso_week(reference: datetime) -> tuple[date, date]:
    """Return the Monday-Sunday range before the reference date's ISO week."""
    today = reference.date()
    current_monday = today - timedelta(days=today.weekday())
    start = current_monday - timedelta(days=7)
    end = current_monday - timedelta(days=1)
    return start, end


def previous_calendar_month(reference: datetime) -> tuple[date, date]:
    """Return the previous completed calendar month for the reference date."""
    first_this_month = reference.date().replace(day=1)
    end = first_this_month - timedelta(days=1)
    start = end.replace(day=1)
    return start, end
