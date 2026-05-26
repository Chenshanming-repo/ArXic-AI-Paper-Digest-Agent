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


def _env_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _env_list(name: str, default: list[str]) -> list[str]:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    return [item.strip() for item in raw.split(",") if item.strip()]


# ArXiv categories to monitor. See https://arxiv.org/category_taxonomy
CATEGORIES: list[str] = _env_list(
    "ARXIV_CATEGORIES", ["cs.AI", "cs.LG", "stat.ML", "q-bio.QM", "q-bio.GN"]
)

# Topic terms used as a second-stage filter after the ArXiv category query.
# Keep this broad enough to catch AI/deep-learning/bioinformatics papers, but
# narrow enough to avoid unrelated papers from broad categories.
TOPIC_KEYWORDS: list[str] = _env_list(
    "ARXIV_TOPIC_KEYWORDS",
    [
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "neural",
        "transformer",
        "large language model",
        "llm",
        "foundation model",
        "diffusion model",
        "reinforcement learning",
        "representation learning",
        "bioinformatics",
        "computational biology",
        "genomics",
        "proteomics",
        "single-cell",
        "protein",
        "dna",
        "rna",
    ],
)

# Cap on summaries written per run; controls cost and noise.
MAX_PAPERS: int = _env_int("MAX_PAPERS", 10)

# How many results to ask ArXiv for. We pull more than MAX_PAPERS so that,
# after deduplication against papers we have already digested, we still
# have a healthy pool to choose from.
ARXIV_PAGE_SIZE: int = _env_int("ARXIV_PAGE_SIZE", 50)

# ArXiv API endpoint. Use https; the http endpoint redirects.
ARXIV_API_URL: str = "https://export.arxiv.org/api/query"

# OpenAI model used for summarisation. gpt-4o-mini is cheap and fast and
# perfectly adequate for 2-3 sentence summaries.
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Optional OpenAI-compatible endpoint for third-party providers.
OPENAI_BASE_URL: str | None = (
    os.getenv("BASE_URL") or os.getenv("OPENAI_BASE_URL") or None
)

# Max output tokens for a single summary.
OPENAI_MAX_TOKENS: int = _env_int("OPENAI_MAX_TOKENS", 300)

# Max output tokens for weekly/monthly rollup summaries.
ROLLUP_MAX_TOKENS: int = _env_int("ROLLUP_MAX_TOKENS", 1200)

# Automatic rollups. The default daily run writes the previous completed ISO
# week on Mondays and the previous completed calendar month on the first day.
ENABLE_WEEKLY_SUMMARY: bool = _env_bool("ENABLE_WEEKLY_SUMMARY", True)
ENABLE_MONTHLY_SUMMARY: bool = _env_bool("ENABLE_MONTHLY_SUMMARY", True)

# Filesystem layout.
PROJECT_ROOT: Path = Path(__file__).resolve().parent
DIGEST_DIR: Path = PROJECT_ROOT / "digest"
DIGEST_FILE: Path = DIGEST_DIR / "digest.md"
LATEST_FILE: Path = DIGEST_DIR / "latest.md"
WEEKLY_DIGEST_FILE: Path = DIGEST_DIR / "weekly.md"
LATEST_WEEKLY_FILE: Path = DIGEST_DIR / "latest_weekly.md"
MONTHLY_DIGEST_FILE: Path = DIGEST_DIR / "monthly.md"
LATEST_MONTHLY_FILE: Path = DIGEST_DIR / "latest_monthly.md"
ARCHIVE_DIR: Path = DIGEST_DIR / "archive"
DAILY_ARCHIVE_DIR: Path = ARCHIVE_DIR / "daily"
WEEKLY_ARCHIVE_DIR: Path = ARCHIVE_DIR / "weekly"
MONTHLY_ARCHIVE_DIR: Path = ARCHIVE_DIR / "monthly"
