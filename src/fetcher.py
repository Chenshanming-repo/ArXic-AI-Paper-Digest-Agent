"""Fetch and parse papers from the ArXiv Atom API."""

from __future__ import annotations

import logging
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

import httpx

from src.models import Paper

logger = logging.getLogger(__name__)

# ArXiv returns an Atom feed; these are the namespaces we need to navigate it.
_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

_WS_RE = re.compile(r"\s+")

# ArXiv asks API clients to identify themselves with a descriptive
# User-Agent. Generic library UAs (e.g. python-httpx/x.y.z) get throttled
# aggressively, especially from shared egress IPs like GitHub Actions runners.
USER_AGENT = (
    "ArxivDigestBot/0.1 "
    "(+https://github.com/Kiraaa1/ArXic-AI-Paper-Digest-Agent)"
)

# Retry policy for transient ArXiv errors (429, 5xx).
_RETRY_STATUSES = {429, 500, 502, 503, 504}
_MAX_ATTEMPTS = 4
_BACKOFF_BASE_SECONDS = 5.0
_BACKOFF_CAP_SECONDS = 60.0


def _normalise(text: str | None) -> str:
    """Collapse runs of whitespace to single spaces and strip."""
    if text is None:
        return ""
    return _WS_RE.sub(" ", text).strip()


def _retry_after_seconds(response: httpx.Response, attempt: int) -> float:
    """Pick a wait time for the next retry.

    Honours the server's `Retry-After` header when present, otherwise uses
    exponential backoff: 5s, 10s, 20s, ... capped at 60s.
    """
    header = response.headers.get("Retry-After")
    if header:
        try:
            return max(0.0, float(header))
        except ValueError:
            pass
    return min(_BACKOFF_BASE_SECONDS * (2 ** (attempt - 1)), _BACKOFF_CAP_SECONDS)


def _request_with_retry(
    client: httpx.Client, api_url: str, params: dict[str, str]
) -> str:
    """GET the ArXiv API with retry/backoff on 429 and 5xx responses."""
    last_response: httpx.Response | None = None
    for attempt in range(1, _MAX_ATTEMPTS + 1):
        response = client.get(api_url, params=params)
        last_response = response
        if response.status_code in _RETRY_STATUSES and attempt < _MAX_ATTEMPTS:
            wait = _retry_after_seconds(response, attempt)
            logger.warning(
                "ArXiv returned %d on attempt %d/%d; sleeping %.1fs before retry",
                response.status_code,
                attempt,
                _MAX_ATTEMPTS,
                wait,
            )
            time.sleep(wait)
            continue
        response.raise_for_status()
        return response.text
    # Exhausted retries while still on a retryable status.
    assert last_response is not None
    last_response.raise_for_status()
    return last_response.text  # pragma: no cover - unreachable


def _build_search_query(categories: list[str]) -> str:
    """Build the ArXiv `search_query` value from a list of category strings.

    Example: ['cs.AI', 'cs.LG'] -> 'cat:cs.AI OR cat:cs.LG'
    httpx will URL-encode the spaces; ArXiv treats '+' and ' ' equivalently
    in this context.
    """
    if not categories:
        raise ValueError("At least one ArXiv category must be configured.")
    return " OR ".join(f"cat:{cat}" for cat in categories)


def _parse_entry(entry: ET.Element) -> Paper | None:
    """Parse a single <entry> element into a Paper, or None if malformed."""
    id_el = entry.find("atom:id", _NS)
    title_el = entry.find("atom:title", _NS)
    summary_el = entry.find("atom:summary", _NS)
    published_el = entry.find("atom:published", _NS)

    if id_el is None or title_el is None or summary_el is None or published_el is None:
        return None

    raw_url = (id_el.text or "").strip()
    if not raw_url:
        return None

    # ArXiv's <id> is the abs URL with a version suffix, e.g.
    # http://arxiv.org/abs/2401.12345v2 (or, for old-format papers,
    # http://arxiv.org/abs/cs.LG/0301001v1). Force https and keep
    # everything after /abs/ so the id round-trips through the digest file.
    canonical_url = raw_url.replace("http://", "https://", 1)
    if "/abs/" in canonical_url:
        arxiv_id = canonical_url.split("/abs/", 1)[1]
    else:
        arxiv_id = canonical_url.rsplit("/", 1)[-1]

    try:
        published = datetime.fromisoformat(
            (published_el.text or "").replace("Z", "+00:00")
        )
    except ValueError:
        return None
    if published.tzinfo is None:
        published = published.replace(tzinfo=timezone.utc)
    else:
        published = published.astimezone(timezone.utc)

    authors: list[str] = []
    for author_el in entry.findall("atom:author", _NS):
        name_el = author_el.find("atom:name", _NS)
        if name_el is not None and name_el.text:
            name = _normalise(name_el.text)
            if name:
                authors.append(name)

    primary_el = entry.find("arxiv:primary_category", _NS)
    primary_category = (
        primary_el.attrib.get("term") if primary_el is not None else None
    )

    try:
        return Paper(
            arxiv_id=arxiv_id,
            url=canonical_url,
            title=_normalise(title_el.text),
            authors=authors,
            abstract=_normalise(summary_el.text),
            published=published,
            primary_category=primary_category,
        )
    except Exception as exc:  # pydantic ValidationError or similar
        logger.warning("Skipping malformed entry %s: %s", arxiv_id, exc)
        return None


def fetch_recent_papers(
    *,
    categories: list[str],
    page_size: int,
    api_url: str,
    http_client: httpx.Client | None = None,
) -> list[Paper]:
    """Fetch the most recent ArXiv submissions for the given categories.

    Returns up to `page_size` papers sorted by submission date, newest first.
    No time-window filtering is applied here: the caller is responsible for
    deduplication and capping the final list. Network and parsing errors
    are surfaced to the caller.
    """
    params = {
        "search_query": _build_search_query(categories),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(page_size),
        "start": "0",
    }

    logger.info(
        "Querying ArXiv for categories=%s page_size=%d",
        categories,
        page_size,
    )

    owns_client = http_client is None
    client = http_client or httpx.Client(
        timeout=30.0,
        follow_redirects=True,
        headers={"User-Agent": USER_AGENT},
    )
    try:
        body = _request_with_retry(client, api_url, params)
    finally:
        if owns_client:
            client.close()

    try:
        root = ET.fromstring(body)
    except ET.ParseError as exc:
        raise RuntimeError(f"Failed to parse ArXiv response as XML: {exc}") from exc

    raw_entries = root.findall("atom:entry", _NS)
    papers: list[Paper] = []
    for entry in raw_entries:
        paper = _parse_entry(entry)
        if paper is not None:
            papers.append(paper)

    logger.info(
        "ArXiv returned %d entries, %d parsed successfully",
        len(raw_entries),
        len(papers),
    )

    return papers
