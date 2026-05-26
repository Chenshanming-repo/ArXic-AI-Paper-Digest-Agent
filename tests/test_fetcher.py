from __future__ import annotations

import unittest
from datetime import datetime, timezone
from unittest import mock

from src import fetcher
from src.models import Paper


_EMPTY_FEED = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<feed xmlns="http://www.w3.org/2005/Atom"></feed>'
)


class _StubArxivClient:
    def __init__(self, **kwargs: object) -> None:
        _StubArxivClient.last_kwargs = kwargs

    def __enter__(self) -> "_StubArxivClient":
        return self

    def __exit__(self, *_exc: object) -> None:
        return None

    def get(self, _params: dict[str, str]) -> str:
        return _EMPTY_FEED


class FetchPapersByQueryUserAgentTest(unittest.TestCase):
    def test_fallback_branch_uses_caller_supplied_user_agent(self) -> None:
        _StubArxivClient.last_kwargs = {}

        with mock.patch.object(fetcher, "ArxivApiClient", _StubArxivClient):
            fetcher.fetch_papers_by_query(
                query="cat:cs.AI",
                max_results=1,
                api_url="https://export.arxiv.org/api/query",
                user_agent="PassedThroughBot/9.9 (+example.com)",
            )

        self.assertEqual(
            _StubArxivClient.last_kwargs.get("user_agent"),
            "PassedThroughBot/9.9 (+example.com)",
        )


def _paper(arxiv_id: str, *, published: datetime, primary: str) -> Paper:
    return Paper(
        arxiv_id=arxiv_id,
        url=f"https://arxiv.org/abs/{arxiv_id}",
        title=f"Title {arxiv_id}",
        authors=["A"],
        abstract="abstract",
        published=published,
        primary_category=primary,
    )


class FetchRecentPapersPerCategoryTest(unittest.TestCase):
    def test_queries_each_category_separately_and_dedupes(self) -> None:
        ts1 = datetime(2026, 5, 26, 10, 0, tzinfo=timezone.utc)
        ts2 = datetime(2026, 5, 26, 11, 0, tzinfo=timezone.utc)
        ts3 = datetime(2026, 5, 26, 12, 0, tzinfo=timezone.utc)

        responses = {
            "cat:cs.AI": [
                _paper("2401.0001", published=ts2, primary="cs.AI"),
                _paper("2401.0002", published=ts1, primary="cs.AI"),
            ],
            "cat:cs.LG": [
                _paper("2401.0001", published=ts2, primary="cs.LG"),
                _paper("2401.0003", published=ts3, primary="cs.LG"),
            ],
        }
        seen_queries: list[str] = []

        def fake_fetch_papers_by_query(*, query: str, **_: object):
            seen_queries.append(query)
            return responses[query]

        with mock.patch.object(
            fetcher, "fetch_papers_by_query", fake_fetch_papers_by_query
        ):
            papers, found_in = fetcher.fetch_recent_papers(
                categories=["cs.AI", "cs.LG"],
                page_size=10,
                api_url="https://export.arxiv.org/api/query",
            )

        self.assertEqual(seen_queries, ["cat:cs.AI", "cat:cs.LG"])
        self.assertEqual(
            [p.arxiv_id for p in papers],
            ["2401.0003", "2401.0001", "2401.0002"],
        )
        self.assertEqual(
            found_in,
            {
                "2401.0001": "cs.AI",
                "2401.0002": "cs.AI",
                "2401.0003": "cs.LG",
            },
        )


if __name__ == "__main__":
    unittest.main()

