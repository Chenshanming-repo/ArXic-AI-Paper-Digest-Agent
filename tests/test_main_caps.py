from __future__ import annotations

import unittest
from datetime import datetime, timezone

import main
from src.models import Paper


def _paper(arxiv_id: str, *, primary: str = "cs.AI") -> Paper:
    return Paper(
        arxiv_id=arxiv_id,
        url=f"https://arxiv.org/abs/{arxiv_id}",
        title=f"Title {arxiv_id}",
        authors=["A"],
        abstract="abstract",
        published=datetime(2026, 5, 26, 10, tzinfo=timezone.utc),
        primary_category=primary,
    )


class CapPapersPerCategoryTest(unittest.TestCase):
    def test_zero_cap_returns_input_unchanged(self) -> None:
        papers = [_paper("a"), _paper("b")]
        capped = main._cap_papers_per_category(
            papers,
            found_in_category={"a": "cs.AI", "b": "cs.LG"},
            categories=["cs.AI", "cs.LG"],
            max_per_category=0,
        )
        self.assertEqual([p.arxiv_id for p in capped], ["a", "b"])

    def test_each_category_capped_independently(self) -> None:
        papers = [
            _paper("ai1"),
            _paper("ai2"),
            _paper("ai3"),
            _paper("lg1"),
            _paper("lg2"),
        ]
        found = {
            "ai1": "cs.AI",
            "ai2": "cs.AI",
            "ai3": "cs.AI",
            "lg1": "cs.LG",
            "lg2": "cs.LG",
        }
        capped = main._cap_papers_per_category(
            papers,
            found_in_category=found,
            categories=["cs.AI", "cs.LG"],
            max_per_category=2,
        )
        self.assertEqual(
            [p.arxiv_id for p in capped],
            ["ai1", "ai2", "lg1", "lg2"],
        )

    def test_input_order_within_category_is_preserved(self) -> None:
        papers = [
            _paper("ai1"),
            _paper("lg1"),
            _paper("ai2"),
            _paper("lg2"),
            _paper("ai3"),
        ]
        found = {p.arxiv_id: ("cs.AI" if "ai" in p.arxiv_id else "cs.LG") for p in papers}
        capped = main._cap_papers_per_category(
            papers,
            found_in_category=found,
            categories=["cs.AI", "cs.LG"],
            max_per_category=2,
        )
        # cs.AI bucket first, in the order encountered: ai1, ai2.
        # cs.LG bucket next: lg1, lg2.
        self.assertEqual([p.arxiv_id for p in capped], ["ai1", "ai2", "lg1", "lg2"])

    def test_empty_category_buckets_are_skipped(self) -> None:
        papers = [_paper("ai1"), _paper("ai2")]
        found = {"ai1": "cs.AI", "ai2": "cs.AI"}
        capped = main._cap_papers_per_category(
            papers,
            found_in_category=found,
            categories=["cs.AI", "stat.ML"],
            max_per_category=10,
        )
        self.assertEqual([p.arxiv_id for p in capped], ["ai1", "ai2"])

    def test_papers_not_in_mapping_are_dropped(self) -> None:
        papers = [_paper("ai1"), _paper("orphan")]
        found = {"ai1": "cs.AI"}  # "orphan" missing
        capped = main._cap_papers_per_category(
            papers,
            found_in_category=found,
            categories=["cs.AI"],
            max_per_category=10,
        )
        self.assertEqual([p.arxiv_id for p in capped], ["ai1"])


if __name__ == "__main__":
    unittest.main()
