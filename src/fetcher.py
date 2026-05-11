"""Fetch and parse papers from the ArXiv Atom API."""

from __future__ import annotations

import logging
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

import httpx

from src.models import Paper

logger = logging.getLogger(__name__)

# ArXiv returns an Atom feed; these are the namespaces we need to navigate it.
_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

_WS_RE = re.compile(r"\s+")


def _normalise(text: str | None) -> str:
    """Collapse runs of whitespace to single spaces and strip."""
    if text is None:
        return ""
    return _WS_RE.sub(" ", text).strip()


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
    # http://arxiv.org/abs/2401.12345v2 — keep it but force https.
    canonical_url = raw_url.replace("http://", "https://", 1)
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
    lookback_hours: int,
    max_results: int,
    page_size: int,
    api_url: str,
    now: datetime | None = None,
    http_client: httpx.Client | None = None,
) -> list[Paper]:
    """Fetch papers submitted within `lookback_hours`, capped at `max_results`.

    The function returns at most `max_results` papers, sorted newest first.
    Network and parsing errors are surfaced to the caller.
    """
    current_time = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    cutoff = current_time - timedelta(hours=lookback_hours)

    params = {
        "search_query": _build_search_query(categories),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(page_size),
        "start": "0",
    }

    logger.info(
        "Querying ArXiv for categories=%s lookback=%dh page_size=%d",
        categories,
        lookback_hours,
        page_size,
    )

    owns_client = http_client is None
    client = http_client or httpx.Client(timeout=30.0)
    try:
        response = client.get(api_url, params=params)
        response.raise_for_status()
        body = response.text
    finally:
        if owns_client:
            client.close()

    try:
        root = ET.fromstring(body)
    except ET.ParseError as exc:
        raise RuntimeError(f"Failed to parse ArXiv response as XML: {exc}") from exc

    papers: list[Paper] = []
    for entry in root.findall("atom:entry", _NS):
        paper = _parse_entry(entry)
        if paper is None:
            continue
        if paper.published < cutoff:
            # Results are sorted descending by submittedDate, so once we see
            # an entry older than the cutoff we can stop scanning.
            break
        papers.append(paper)

    logger.info(
        "ArXiv returned %d entries, %d within lookback window",
        len(root.findall("atom:entry", _NS)),
        len(papers),
    )

    return papers[:max_results]
