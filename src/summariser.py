"""Summarise ArXiv papers using the OpenAI API."""

from __future__ import annotations

import logging
import json
import re
from collections.abc import Mapping, Sequence
from typing import Any

from openai import OpenAI, OpenAIError

from src.models import DigestEntry, Paper

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "你是一名技术能力强的 AI 研究员。请为技术读者简洁总结 ArXiv 论文。"
    "所有回答都使用简体中文；必要的模型名、算法名和英文缩写可以保留。"
)

USER_PROMPT_TEMPLATE = (
    "论文标题：{title}\n\n"
    "摘要：{abstract}\n\n"
    "请用 2-3 句简体中文总结这篇论文，必须覆盖：它解决的问题、采用的方法、"
    "以及关键结果或主要贡献。不要输出英文段落。"
)

ROLLUP_PROMPT_TEMPLATE = (
    "下面是 {period_name} 的 ArXiv 论文条目，每条包含标题、链接和每日摘要。\n\n"
    "{records}\n\n"
    "请用简体中文写一份面向技术读者的阶段性综述，结构包括：\n"
    "1. 本周期总体趋势；\n"
    "2. AI/深度学习/生物信息学方向的主要主题；\n"
    "3. 最值得继续跟踪的论文及原因，保留对应链接；\n"
    "4. 可能的后续研究或应用机会。\n"
    "内容要具体，不要泛泛而谈。"
)

_WS_RE = re.compile(r"\s+")
_HTML_RESPONSE_RE = re.compile(r"^\s*(?:<!doctype\s+html|<html[\s>])", re.IGNORECASE)
_ROLLUP_SUMMARY_LIMIT = 420


def _build_user_prompt(paper: Paper) -> str:
    return USER_PROMPT_TEMPLATE.format(title=paper.title, abstract=paper.abstract)


def _normalise(text: str) -> str:
    return _WS_RE.sub(" ", text).strip()


def _reject_html_response(content: str) -> str:
    if _HTML_RESPONSE_RE.search(content):
        raise RuntimeError(
            "AI provider returned an HTML page instead of a chat completion. "
            "Check BASE_URL; OpenAI-compatible endpoints usually end with /v1."
        )
    return content


def _extract_response_content(response: Any) -> str:
    """Extract message content from OpenAI SDK or OpenAI-compatible responses."""
    if isinstance(response, str):
        try:
            return _extract_response_content(json.loads(response))
        except json.JSONDecodeError:
            return _reject_html_response(response)

    if isinstance(response, Mapping):
        choices = response.get("choices")
        if choices:
            first_choice = choices[0]
            if isinstance(first_choice, Mapping):
                message = first_choice.get("message")
                if isinstance(message, Mapping):
                    return _reject_html_response(str(message.get("content") or ""))
                return _reject_html_response(str(first_choice.get("text") or ""))
        return _reject_html_response(
            str(response.get("content") or response.get("text") or "")
        )

    choices = getattr(response, "choices", None)
    if choices:
        first_choice = choices[0]
        message = getattr(first_choice, "message", None)
        if message is not None:
            return _reject_html_response(str(getattr(message, "content", "") or ""))
        return _reject_html_response(str(getattr(first_choice, "text", "") or ""))

    return _reject_html_response(str(getattr(response, "content", "") or ""))


def _truncate(text: str, limit: int) -> str:
    text = _normalise(text)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def _build_rollup_prompt(
    records: Sequence[Mapping[str, str]], period_name: str
) -> str:
    lines: list[str] = []
    for index, record in enumerate(records, start=1):
        lines.append(
            "\n".join(
                [
                    f"{index}. 标题：{record['title']}",
                    f"   日期：{record['date']}",
                    f"   链接：{record['link']}",
                    f"   每日摘要：{_truncate(record['summary'], _ROLLUP_SUMMARY_LIMIT)}",
                ]
            )
        )
    return ROLLUP_PROMPT_TEMPLATE.format(
        period_name=period_name,
        records="\n\n".join(lines),
    )


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

    content = _extract_response_content(response)
    summary = _normalise(content)
    if not summary:
        raise RuntimeError(f"Empty summary returned for paper {paper.arxiv_id}")
    return summary


def summarise_period(
    records: Sequence[Mapping[str, str]],
    *,
    period_name: str,
    client: OpenAI,
    model: str,
    max_tokens: int,
) -> str:
    """Generate a Chinese weekly/monthly rollup from daily digest records."""
    if not records:
        raise ValueError("Cannot summarise an empty period.")

    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _build_rollup_prompt(records, period_name)},
        ],
    )

    content = _extract_response_content(response)
    summary = _normalise(content)
    if not summary:
        raise RuntimeError(f"Empty summary returned for period {period_name}")
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
