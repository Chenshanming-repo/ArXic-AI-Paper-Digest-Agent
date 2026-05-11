"""Tuneable configuration for the ArXiv digest bot.

Anything a user might reasonably want to change without touching application
logic lives in this module. Values can also be overridden via environment
variables for ad-hoc local runs.
"""

from __future__ import annotations

import os
from pathlib import Path


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _env_list(name: str, default: list[str]) -> list[str]:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    return [item.strip() for item in raw.split(",") if item.strip()]


# ArXiv categories to monitor. See https://arxiv.org/category_taxonomy
CATEGORIES: list[str] = _env_list(
    "ARXIV_CATEGORIES", ["cs.AI", "cs.LG", "cs.CL"]
)

# Cap papers per day to keep summarisation costs predictable.
MAX_PAPERS: int = _env_int("MAX_PAPERS", 10)

# Only include papers published within this many hours of the run.
LOOKBACK_HOURS: int = _env_int("LOOKBACK_HOURS", 24)

# How many results to ask ArXiv for before applying the lookback filter.
# 50 is plenty when monitoring a handful of categories.
ARXIV_PAGE_SIZE: int = _env_int("ARXIV_PAGE_SIZE", 50)

# ArXiv API endpoint. Use https; the http endpoint redirects.
ARXIV_API_URL: str = "https://export.arxiv.org/api/query"

# OpenAI model used for summarisation. gpt-4o-mini is cheap and fast and
# perfectly adequate for 2-3 sentence summaries.
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Max output tokens for a single summary.
OPENAI_MAX_TOKENS: int = _env_int("OPENAI_MAX_TOKENS", 300)

# Filesystem layout.
PROJECT_ROOT: Path = Path(__file__).resolve().parent
DIGEST_DIR: Path = PROJECT_ROOT / "digest"
DIGEST_FILE: Path = DIGEST_DIR / "digest.md"
LATEST_FILE: Path = DIGEST_DIR / "latest.md"
