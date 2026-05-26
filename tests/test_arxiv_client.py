from __future__ import annotations

import unittest

import httpx

from src.arxiv_client import ArxivApiClient, ArxivRateLimiter


class FakeHttpClient:
    def __init__(self, responses: list[httpx.Response]) -> None:
        self.responses = responses
        self.calls = 0

    def get(self, _url: str, params: dict[str, str]) -> httpx.Response:
        self.calls += 1
        response = self.responses.pop(0)
        response.request = httpx.Request("GET", "https://export.arxiv.org/api/query")
        return response


class ArxivRateLimiterTest(unittest.TestCase):
    def test_waits_for_minimum_interval(self) -> None:
        now = [100.0]
        sleeps: list[float] = []

        def clock() -> float:
            return now[0]

        def sleeper(seconds: float) -> None:
            sleeps.append(seconds)
            now[0] += seconds

        limiter = ArxivRateLimiter(
            min_interval_seconds=3.5,
            jitter_seconds=0,
            clock=clock,
            sleeper=sleeper,
            jitter_fn=lambda: 0.0,
        )

        self.assertEqual(limiter.wait(), 0.0)
        self.assertAlmostEqual(limiter.wait(), 3.5)
        self.assertEqual(sleeps, [3.5])


class ArxivApiClientRetryTest(unittest.TestCase):
    def test_retries_429_then_succeeds(self) -> None:
        sleeps: list[float] = []
        fake_http = FakeHttpClient(
            [
                httpx.Response(429, text="slow down"),
                httpx.Response(200, text="<feed />"),
            ]
        )
        client = ArxivApiClient(
            api_url="https://export.arxiv.org/api/query",
            http_client=fake_http,  # type: ignore[arg-type]
            rate_limiter=ArxivRateLimiter(
                min_interval_seconds=0, jitter_seconds=0, jitter_fn=lambda: 0.0
            ),
            max_retries=5,
            backoff_base_seconds=30,
            backoff_jitter_seconds=0,
            sleeper=sleeps.append,
            jitter_fn=lambda: 0.0,
        )

        self.assertEqual(client.get({"search_query": "cat:cs.AI"}), "<feed />")
        self.assertEqual(fake_http.calls, 2)
        self.assertEqual(sleeps, [30.0])

    def test_respects_retry_after_header(self) -> None:
        sleeps: list[float] = []
        fake_http = FakeHttpClient(
            [
                httpx.Response(429, headers={"Retry-After": "7"}, text="slow down"),
                httpx.Response(200, text="<feed />"),
            ]
        )
        client = ArxivApiClient(
            api_url="https://export.arxiv.org/api/query",
            http_client=fake_http,  # type: ignore[arg-type]
            rate_limiter=ArxivRateLimiter(
                min_interval_seconds=0, jitter_seconds=0, jitter_fn=lambda: 0.0
            ),
            max_retries=5,
            sleeper=sleeps.append,
            jitter_fn=lambda: 0.0,
        )

        self.assertEqual(client.get({"search_query": "cat:cs.AI"}), "<feed />")
        self.assertEqual(sleeps, [7.0])


if __name__ == "__main__":
    unittest.main()
