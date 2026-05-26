"""Local SQLite cache for arXiv paper metadata."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from src.models import Paper


def _dt_to_str(value: datetime | None) -> str | None:
    if value is None:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    else:
        value = value.astimezone(timezone.utc)
    return value.isoformat()


class PaperMetadataStore:
    """SQLite-backed cache keyed by arXiv id."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self.path)
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._ensure_schema()

    def close(self) -> None:
        """Close the SQLite connection."""
        self._conn.close()

    def __enter__(self) -> "PaperMetadataStore":
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def _ensure_schema(self) -> None:
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS papers (
                arxiv_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                authors_json TEXT NOT NULL,
                abstract TEXT NOT NULL,
                categories_json TEXT NOT NULL,
                primary_category TEXT,
                published_date TEXT NOT NULL,
                updated_date TEXT,
                pdf_url TEXT,
                abs_url TEXT NOT NULL,
                fetched_at TEXT NOT NULL
            )
            """
        )
        self._conn.commit()

    def has_paper(self, arxiv_id: str) -> bool:
        """Return True when a paper is already cached."""
        row = self._conn.execute(
            "SELECT 1 FROM papers WHERE arxiv_id = ?",
            (arxiv_id,),
        ).fetchone()
        return row is not None

    def upsert_paper(self, paper: Paper, *, fetched_at: datetime | None = None) -> bool:
        """Insert/update one paper and return True if it was new."""
        was_new = not self.has_paper(paper.arxiv_id)
        fetched_at = fetched_at or datetime.now(timezone.utc)
        self._conn.execute(
            """
            INSERT INTO papers (
                arxiv_id, title, authors_json, abstract, categories_json,
                primary_category, published_date, updated_date, pdf_url, abs_url,
                fetched_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(arxiv_id) DO UPDATE SET
                title = excluded.title,
                authors_json = excluded.authors_json,
                abstract = excluded.abstract,
                categories_json = excluded.categories_json,
                primary_category = excluded.primary_category,
                published_date = excluded.published_date,
                updated_date = excluded.updated_date,
                pdf_url = excluded.pdf_url,
                abs_url = excluded.abs_url,
                fetched_at = excluded.fetched_at
            """,
            (
                paper.arxiv_id,
                paper.title,
                json.dumps(paper.authors, ensure_ascii=False),
                paper.abstract,
                json.dumps(paper.categories, ensure_ascii=False),
                paper.primary_category,
                _dt_to_str(paper.published),
                _dt_to_str(paper.updated),
                paper.pdf_url,
                str(paper.url),
                _dt_to_str(fetched_at),
            ),
        )
        self._conn.commit()
        return was_new

    def upsert_papers(self, papers: Iterable[Paper]) -> tuple[int, int]:
        """Upsert papers and return (new_count, updated_count)."""
        new_count = 0
        updated_count = 0
        for paper in papers:
            if self.upsert_paper(paper):
                new_count += 1
            else:
                updated_count += 1
        return new_count, updated_count

    def count(self) -> int:
        """Return number of cached papers."""
        row = self._conn.execute("SELECT COUNT(*) FROM papers").fetchone()
        return int(row[0])

    def get_paper_row(self, arxiv_id: str) -> sqlite3.Row | None:
        """Fetch one raw SQLite row by arXiv id."""
        self._conn.row_factory = sqlite3.Row
        return self._conn.execute(
            "SELECT * FROM papers WHERE arxiv_id = ?",
            (arxiv_id,),
        ).fetchone()
