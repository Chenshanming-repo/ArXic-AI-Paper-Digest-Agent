"""Polite, rate-limited arXiv API client."""

from __future__ import annotations

import email.utils
import logging
import random
import time
from collections.abc import Callable
from datetime import datetime, timezone

import httpx

logger = logging.getLogger(__name__)

RETRY_STATUSES = {429, 500, 502, 503, 504}
DEFAULT_USER_AGENT = "LongReadPaperBot/0.1 (mailto:YOUR_EMAIL@example.com)"


class ArxivRateLimiter:
    """Single-process rate limiter for polite arXiv API access."""

    def __init__(
        self,
        *,
        min_interval_seconds: float = 3.5,
        jitter_seconds: float = 1.5,
        clock: Callable[[], float] = time.monotonic,
        sleeper: Callable[[float], None] = time.sleep,
        jitter_fn: Callable[[], float] | None = None,
    ) -> None:
        self.min_interval_seconds = min_interval_seconds
        self.jitter_seconds = jitter_seconds
        self._clock = clock
        self._sleeper = sleeper
        self._jitter_fn = jitter_fn or (lambda: random.uniform(0, jitter_seconds))
        self._last_request_at: float | None = None

    def wait(self) -> float:
        """Sleep until the next request is allowed and return slept seconds."""
        now = self._clock()
        if self._last_request_at is None:
            self._last_request_at = now
            return 0.0

        target_interval = self.min_interval_seconds + self._jitter_fn()
        elapsed = now - self._last_request_at
        wait_seconds = max(0.0, target_interval - elapsed)
        if wait_seconds > 0:
            logger.info("Rate limiting arXiv request for %.1fs", wait_seconds)
            self._sleeper(wait_seconds)
        self._last_request_at = self._clock()
        return wait_seconds


def _retry_after_seconds(response: httpx.Response) -> float | None:
    """Parse Retry-After as seconds or HTTP date."""
    header = response.headers.get("Retry-After")
    if not header:
        return None
    try:
        return max(0.0, float(header))
    except ValueError:
        try:
            parsed = email.utils.parsedate_to_datetime(header)
        except (TypeError, ValueError, IndexError, OverflowError):
            return None
        if parsed is None:
            return None
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return max(0.0, (parsed - datetime.now(timezone.utc)).total_seconds())


class ArxivApiClient:
    """HTTP client for arXiv Atom API with retry, backoff, and rate limiting."""

    def __init__(
        self,
        *,
        api_url: str,
        user_agent: str = DEFAULT_USER_AGENT,
        timeout_seconds: float = 60.0,
        max_retries: int = 5,
        backoff_base_seconds: float = 30.0,
        backoff_max_seconds: float = 600.0,
        backoff_jitter_seconds: float = 10.0,
        rate_limiter: ArxivRateLimiter | None = None,
        http_client: httpx.Client | None = None,
        sleeper: Callable[[float], None] = time.sleep,
        jitter_fn: Callable[[], float] | None = None,
    ) -> None:
        self.api_url = api_url
        self.max_retries = max_retries
        self.backoff_base_seconds = backoff_base_seconds
        self.backoff_max_seconds = backoff_max_seconds
        self.backoff_jitter_seconds = backoff_jitter_seconds
        self.rate_limiter = rate_limiter or ArxivRateLimiter()
        self._sleeper = sleeper
        self._jitter_fn = jitter_fn or (
            lambda: random.uniform(0, backoff_jitter_seconds)
        )
        self._owns_client = http_client is None
        self._client = http_client or httpx.Client(
            timeout=timeout_seconds,
            follow_redirects=True,
            headers={"User-Agent": user_agent},
            limits=httpx.Limits(max_connections=1, max_keepalive_connections=1),
        )

    def close(self) -> None:
        """Close the underlying HTTP client when owned by this instance."""
        if self._owns_client:
            self._client.close()

    def __enter__(self) -> "ArxivApiClient":
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def _backoff_seconds(self, retry_index: int) -> float:
        base = min(
            self.backoff_base_seconds * (2 ** max(0, retry_index - 1)),
            self.backoff_max_seconds,
        )
        return min(self.backoff_max_seconds, base + self._jitter_fn())

    def _retry_wait_seconds(self, response: httpx.Response, retry_index: int) -> float:
        retry_after = _retry_after_seconds(response)
        if retry_after is not None:
            return retry_after
        return self._backoff_seconds(retry_index)

    def get(self, params: dict[str, str]) -> str:
        """GET arXiv API with bounded retries and return response text."""
        last_error: Exception | None = None
        total_attempts = self.max_retries + 1

        for attempt in range(1, total_attempts + 1):
            self.rate_limiter.wait()
            logger.info(
                "arXiv request attempt %d/%d params=%s",
                attempt,
                total_attempts,
                params,
            )
            try:
                response = self._client.get(self.api_url, params=params)
            except httpx.RequestError as exc:
                last_error = exc
                if attempt >= total_attempts:
                    logger.error(
                        "arXiv request failed permanently after %d attempts: %s",
                        attempt,
                        exc,
                    )
                    raise
                wait_seconds = self._backoff_seconds(attempt)
                logger.warning(
                    "arXiv request network error on attempt %d/%d (%s); "
                    "retrying in %.1fs",
                    attempt,
                    total_attempts,
                    exc,
                    wait_seconds,
                )
                self._sleeper(wait_seconds)
                continue

            if response.status_code in RETRY_STATUSES and attempt < total_attempts:
                wait_seconds = self._retry_wait_seconds(response, attempt)
                logger.warning(
                    "arXiv returned HTTP %d on attempt %d/%d; retrying in %.1fs",
                    response.status_code,
                    attempt,
                    total_attempts,
                    wait_seconds,
                )
                self._sleeper(wait_seconds)
                continue

            try:
                response.raise_for_status()
            except httpx.HTTPStatusError as exc:
                last_error = exc
                logger.error(
                    "arXiv request failed permanently with HTTP %d after %d attempts",
                    response.status_code,
                    attempt,
                )
                raise

            logger.info("arXiv request succeeded on attempt %d/%d", attempt, total_attempts)
            return response.text

        assert last_error is not None
        raise last_error
