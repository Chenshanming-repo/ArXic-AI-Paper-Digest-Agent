"""Summarise ArXiv papers using the OpenAI API."""

from __future__ import annotations

import logging
import re

from openai import OpenAI, OpenAIError

from src.models import DigestEntry, Paper

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a technical AI researcher. Summarise ArXiv papers concisely "
    "for a technical audience."
)

USER_PROMPT_TEMPLATE = (
    "Paper title: {title}\n\n"
    "Abstract: {abstract}\n\n"
    "Write a 2-3 sentence plain-English summary that captures: what problem "
    "is being solved, what approach was used, and what the key result or "
    "contribution is."
)

_WS_RE = re.compile(r"\s+")


def _build_user_prompt(paper: Paper) -> str:
    return USER_PROMPT_TEMPLATE.format(title=paper.title, abstract=paper.abstract)


def _normalise(text: str) -> str:
    return _WS_RE.sub(" ", text).strip()


def summarise_paper(
    paper: Paper,
    *,
    client: OpenAI,
    model: str,
    max_tokens: int,
) -> str:
    """Generate a summary for a single paper.

    Raises the underlying OpenAI exception on failure so the caller can
    decide whether to skip or abort.
    """
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _build_user_prompt(paper)},
        ],
    )

    if not response.choices:
        raise RuntimeError(f"No choices returned for paper {paper.arxiv_id}")

    content = response.choices[0].message.content or ""
    summary = _normalise(content)
    if not summary:
        raise RuntimeError(f"Empty summary returned for paper {paper.arxiv_id}")
    return summary


def summarise_papers(
    papers: list[Paper],
    *,
    client: OpenAI,
    model: str,
    max_tokens: int,
) -> list[DigestEntry]:
    """Summarise a list of papers, skipping any that fail individually."""
    entries: list[DigestEntry] = []
    for paper in papers:
        try:
            summary = summarise_paper(
                paper, client=client, model=model, max_tokens=max_tokens
            )
        except (OpenAIError, RuntimeError) as exc:
            logger.error(
                "Failed to summarise paper %s (%s): %s",
                paper.arxiv_id,
                paper.title,
                exc,
            )
            continue
        entries.append(DigestEntry(paper=paper, summary=summary))
    return entries
