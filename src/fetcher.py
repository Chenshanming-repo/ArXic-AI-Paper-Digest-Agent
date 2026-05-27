"""Fetch and parse papers from the ArXiv Atom API."""

from __future__ import annotations

import logging
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

import httpx

from src.arxiv_client import ArxivApiClient, DEFAULT_USER_AGENT
from src.models import Paper

logger = logging.getLogger(__name__)

# ArXiv returns an Atom feed; these are the namespaces we need to navigate it.
_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

_WS_RE = re.compile(r"\s+")

USER_AGENT = DEFAULT_USER_AGENT
ARXIV_MAX_RESULTS_PER_REQUEST = 5


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


def build_category_query(categories: list[str]) -> str:
    """Build an arXiv category query for CLI/config callers."""
    return _build_search_query(categories)


def build_recent_date_query(base_query: str, *, days: int, now: datetime | None = None) -> str:
    """Build an arXiv query for recently submitted or updated papers."""
    reference = now or datetime.now(timezone.utc)
    if reference.tzinfo is None:
        reference = reference.replace(tzinfo=timezone.utc)
    else:
        reference = reference.astimezone(timezone.utc)
    start = reference - timedelta(days=days)
    start_raw = start.strftime("%Y%m%d%H%M")
    end_raw = reference.strftime("%Y%m%d%H%M")
    date_query = (
        f"(submittedDate:[{start_raw} TO {end_raw}] "
        f"OR lastUpdatedDate:[{start_raw} TO {end_raw}])"
    )
    return f"({base_query}) AND {date_query}"


def _paper_matches_topic(paper: Paper, topic_keywords: list[str]) -> bool:
    if not topic_keywords:
        return True

    haystack = " ".join(
        [
            paper.title,
            paper.abstract,
            paper.primary_category or "",
            " ".join(paper.categories),
        ]
    ).casefold()
    return any(keyword.casefold() in haystack for keyword in topic_keywords)


def _parse_entry(entry: ET.Element) -> Paper | None:
    """Parse a single <entry> element into a Paper, or None if malformed."""
    id_el = entry.find("atom:id", _NS)
    title_el = entry.find("atom:title", _NS)
    summary_el = entry.find("atom:summary", _NS)
    published_el = entry.find("atom:published", _NS)
    updated_el = entry.find("atom:updated", _NS)

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

    updated = None
    if updated_el is not None and updated_el.text:
        try:
            updated = datetime.fromisoformat(updated_el.text.replace("Z", "+00:00"))
            if updated.tzinfo is None:
                updated = updated.replace(tzinfo=timezone.utc)
            else:
                updated = updated.astimezone(timezone.utc)
        except ValueError:
            updated = None

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
    categories = [
        category_el.attrib["term"]
        for category_el in entry.findall("atom:category", _NS)
        if category_el.attrib.get("term")
    ]
    if primary_category and primary_category not in categories:
        categories.insert(0, primary_category)

    pdf_url = None
    for link_el in entry.findall("atom:link", _NS):
        title = link_el.attrib.get("title", "")
        href = link_el.attrib.get("href", "")
        if title == "pdf" and href:
            pdf_url = href.replace("http://", "https://", 1)
            break
    if pdf_url is None:
        pdf_url = canonical_url.replace("/abs/", "/pdf/", 1)

    try:
        return Paper(
            arxiv_id=arxiv_id,
            url=canonical_url,
            title=_normalise(title_el.text),
            authors=authors,
            abstract=_normalise(summary_el.text),
            published=published,
            updated=updated,
            primary_category=primary_category,
            categories=categories,
            pdf_url=pdf_url,
        )
    except Exception as exc:  # pydantic ValidationError or similar
        logger.warning("Skipping malformed entry %s: %s", arxiv_id, exc)
        return None


def fetch_recent_papers(
    *,
    categories: list[str],
    topic_keywords: list[str] | None = None,
    page_size: int,
    api_url: str,
    http_client: httpx.Client | None = None,
    arxiv_client: ArxivApiClient | None = None,
) -> tuple[list[Paper], dict[str, str]]:
    """Fetch the most recent ArXiv submissions for the given categories.

    Issues one query per category, then dedupes by arxiv_id and re-sorts by
    `published` descending so the result resembles a single combined feed.
    Long ``cat:a OR cat:b OR ...`` queries are routed by arXiv's API as a
    single "long search" and are sometimes rejected on shared egress IPs;
    splitting per-category sidesteps that limit and still respects the
    polite rate limit through the shared ``ArxivApiClient``.

    Returns a `(papers, found_in_category)` tuple where `found_in_category`
    maps each emitted `arxiv_id` to the configured category that first
    surfaced it. Callers can use this to group rendered output by category.

    `page_size` is applied per category. The caller is responsible for
    further capping (`MAX_PAPERS`) and deduplication against prior runs.
    Network and parsing errors are surfaced to the caller. If
    `topic_keywords` is provided, parsed papers are filtered by
    title/abstract text after the per-category fan-out.
    """
    if not categories:
        raise ValueError("At least one ArXiv category must be configured.")

    logger.info(
        "Querying ArXiv for categories=%s page_size=%d",
        categories,
        page_size,
    )

    found_in_category: dict[str, str] = {}
    collected: list[Paper] = []
    for category in categories:
        chunk = fetch_papers_by_query(
            query=f"cat:{category}",
            max_results=page_size,
            api_url=api_url,
            http_client=http_client,
            arxiv_client=arxiv_client,
        )
        for paper in chunk:
            if paper.arxiv_id in found_in_category:
                continue
            found_in_category[paper.arxiv_id] = category
            collected.append(paper)

    collected.sort(key=lambda p: p.published, reverse=True)
    papers = collected

    if topic_keywords:
        before_count = len(papers)
        papers = [
            paper for paper in papers if _paper_matches_topic(paper, topic_keywords)
        ]
        kept_ids = {paper.arxiv_id for paper in papers}
        found_in_category = {
            arxiv_id: category
            for arxiv_id, category in found_in_category.items()
            if arxiv_id in kept_ids
        }
        logger.info(
            "Topic filter kept %d/%d papers using keywords=%s",
            len(papers),
            before_count,
            topic_keywords,
        )

    logger.info(
        "ArXiv returned %d papers available after parsing/filtering",
        len(papers),
    )

    return papers, found_in_category


def parse_atom_feed(body: str) -> list[Paper]:
    """Parse an arXiv Atom XML response into paper metadata."""
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


def fetch_papers_by_query(
    *,
    query: str,
    max_results: int,
    api_url: str,
    sort_by: str = "submittedDate",
    sort_order: str = "descending",
    start: int = 0,
    http_client: httpx.Client | None = None,
    arxiv_client: ArxivApiClient | None = None,
    user_agent: str = USER_AGENT,
) -> list[Paper]:
    """Fetch paper metadata for a raw arXiv search query."""
    if max_results <= 0:
        logger.info(
            "Skipping ArXiv query=%s because max_results=%d",
            query,
            max_results,
        )
        return []

    def fetch_with_client(client: ArxivApiClient) -> list[Paper]:
        papers: list[Paper] = []
        remaining = max_results
        current_start = start

        while remaining > 0:
            request_size = min(ARXIV_MAX_RESULTS_PER_REQUEST, remaining)
            params = {
                "search_query": query,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "max_results": str(request_size),
                "start": str(current_start),
            }

            logger.info(
                "Querying ArXiv query=%s max_results=%d start=%d",
                query,
                request_size,
                current_start,
            )
            body = client.get(params)
            chunk = parse_atom_feed(body)
            if not chunk:
                break
            papers.extend(chunk)
            remaining -= request_size
            current_start += request_size

        return papers

    logger.info("Querying ArXiv query=%s total_max_results=%d", query, max_results)
    if arxiv_client is not None:
        return fetch_with_client(arxiv_client)

    with ArxivApiClient(
        api_url=api_url,
        user_agent=user_agent,
        http_client=http_client,
    ) as client:
        return fetch_with_client(client)
