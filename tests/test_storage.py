from __future__ import annotations

import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from src.models import Paper
from src.storage import PaperMetadataStore


def _paper(arxiv_id: str = "2605.00001v1", title: str = "Test Paper") -> Paper:
    return Paper(
        arxiv_id=arxiv_id,
        url=f"https://arxiv.org/abs/{arxiv_id}",
        title=title,
        authors=["Ada Lovelace", "Alan Turing"],
        abstract="A test abstract.",
        published=datetime(2026, 5, 26, tzinfo=timezone.utc),
        updated=datetime(2026, 5, 26, tzinfo=timezone.utc),
        primary_category="cs.AI",
        categories=["cs.AI", "cs.LG"],
        pdf_url=f"https://arxiv.org/pdf/{arxiv_id}",
    )


class PaperMetadataStoreTest(unittest.TestCase):
    def test_upsert_deduplicates_by_arxiv_id(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = Path(tmp_dir) / "papers.sqlite3"
            with PaperMetadataStore(db_path) as store:
                self.assertTrue(store.upsert_paper(_paper(title="First")))
                self.assertFalse(store.upsert_paper(_paper(title="Updated")))

                self.assertEqual(store.count(), 1)
                row = store.get_paper_row("2605.00001v1")
                self.assertIsNotNone(row)
                assert row is not None
                self.assertEqual(row["title"], "Updated")
                self.assertIn("cs.AI", row["categories_json"])

    def test_upsert_many_counts_new_and_existing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = Path(tmp_dir) / "papers.sqlite3"
            with PaperMetadataStore(db_path) as store:
                store.upsert_paper(_paper("2605.00001v1"))
                new_count, updated_count = store.upsert_papers(
                    [_paper("2605.00001v1"), _paper("2605.00002v1")]
                )

                self.assertEqual((new_count, updated_count), (1, 1))
                self.assertEqual(store.count(), 2)


if __name__ == "__main__":
    unittest.main()
