from __future__ import annotations

import unittest
from datetime import date, datetime, timezone

from src.models import Digest, DigestEntry, Paper
from src.writer import render_digest


def _paper(arxiv_id: str, *, primary: str = "cs.AI") -> Paper:
    return Paper(
        arxiv_id=arxiv_id,
        url=f"https://arxiv.org/abs/{arxiv_id}",
        title=f"Title {arxiv_id}",
        authors=["A"],
        abstract="abstract",
        published=datetime(2026, 5, 26, 10, 0, tzinfo=timezone.utc),
        primary_category=primary,
    )


def _entry(arxiv_id: str, *, primary: str = "cs.AI") -> DigestEntry:
    return DigestEntry(paper=_paper(arxiv_id, primary=primary), summary="s")


class RenderDigestCategoryGroupingTest(unittest.TestCase):
    def test_groups_entries_by_category_in_specified_order(self) -> None:
        digest = Digest(
            digest_date=date(2026, 5, 26),
            entries=[
                _entry("2605.0001"),
                _entry("2605.0002"),
                _entry("2605.0003"),
            ],
        )
        category_by_id = {
            "2605.0001": "cs.LG",
            "2605.0002": "cs.AI",
            "2605.0003": "cs.AI",
        }

        rendered = render_digest(
            digest,
            category_by_id=category_by_id,
            category_order=["cs.AI", "cs.LG"],
        )

        ai_pos = rendered.find("### cs.AI")
        lg_pos = rendered.find("### cs.LG")
        self.assertGreater(ai_pos, 0)
        self.assertGreater(lg_pos, ai_pos)

        # Each paper appears under exactly one category subsection.
        self.assertEqual(rendered.count("Title 2605.0001"), 1)
        self.assertEqual(rendered.count("Title 2605.0002"), 1)
        self.assertEqual(rendered.count("Title 2605.0003"), 1)

        # 0002 and 0003 are both cs.AI and should appear before the cs.LG header.
        self.assertLess(rendered.find("Title 2605.0002"), lg_pos)
        self.assertLess(rendered.find("Title 2605.0003"), lg_pos)
        self.assertGreater(rendered.find("Title 2605.0001"), lg_pos)

    def test_papers_without_known_category_fall_into_other_section(self) -> None:
        digest = Digest(
            digest_date=date(2026, 5, 26),
            entries=[_entry("2605.0001"), _entry("2605.0099")],
        )
        category_by_id = {"2605.0001": "cs.AI"}

        rendered = render_digest(
            digest,
            category_by_id=category_by_id,
            category_order=["cs.AI"],
        )

        self.assertIn("### cs.AI", rendered)
        self.assertIn("### 其他", rendered)
        self.assertIn("Title 2605.0099", rendered)

    def test_render_without_category_args_keeps_flat_layout(self) -> None:
        digest = Digest(
            digest_date=date(2026, 5, 26),
            entries=[_entry("2605.0001")],
        )

        rendered = render_digest(digest)

        self.assertIn("Title 2605.0001", rendered)
        self.assertNotIn("### cs.AI", rendered)


if __name__ == "__main__":
    unittest.main()
