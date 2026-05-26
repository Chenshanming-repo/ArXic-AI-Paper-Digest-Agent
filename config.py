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

# Cap on summaries written per run; set to 0 to summarise every fresh paper
# that matches the configured categories and topic keywords.
MAX_PAPERS: int = _env_int("MAX_PAPERS", 0)

# How many newest ArXiv results to inspect before deduplication/topic filtering.
# Increase this when tracking broad topics and using MAX_PAPERS=0.
ARXIV_PAGE_SIZE: int = _env_int("ARXIV_PAGE_SIZE", 200)

# ArXiv API endpoint. Use https; the http endpoint redirects.
ARXIV_API_URL: str = "https://export.arxiv.org/api/query"
ARXIV_USER_AGENT: str = os.getenv(
    "ARXIV_USER_AGENT",
    "ArxivDigestBot/0.1 (+https://github.com/Kiraaa1/ArXic-AI-Paper-Digest-Agent)",
)
ARXIV_RATE_LIMIT_SECONDS: float = float(os.getenv("ARXIV_RATE_LIMIT_SECONDS", "3.5"))
ARXIV_RATE_LIMIT_JITTER_SECONDS: float = float(
    os.getenv("ARXIV_RATE_LIMIT_JITTER_SECONDS", "1.5")
)
ARXIV_MAX_RETRIES: int = _env_int("ARXIV_MAX_RETRIES", 3)

# OpenAI-compatible model used for summarisation. Use "auto" to query the
# provider's /models endpoint and pick a suitable text model.
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "auto")

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

# Email delivery. If EMAIL_RECIPIENTS is empty, email sending is disabled.
EMAIL_RECIPIENTS: list[str] = _env_list("EMAIL_RECIPIENTS", [])
EMAIL_SEND_DAILY: bool = _env_bool("EMAIL_SEND_DAILY", True)
EMAIL_SEND_WEEKLY: bool = _env_bool("EMAIL_SEND_WEEKLY", True)
EMAIL_SEND_MONTHLY: bool = _env_bool("EMAIL_SEND_MONTHLY", True)

SMTP_HOST: str = os.getenv("SMTP_HOST", "")
SMTP_USE_SSL: bool = _env_bool("SMTP_USE_SSL", False)
SMTP_USE_TLS: bool = _env_bool("SMTP_USE_TLS", True)
SMTP_PORT: int = _env_int("SMTP_PORT", 465 if SMTP_USE_SSL else 587)
SMTP_USERNAME: str = os.getenv("SMTP_USERNAME", "")
SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
EMAIL_FROM: str = os.getenv("EMAIL_FROM") or SMTP_USERNAME

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
METADATA_DB_FILE: Path = DIGEST_DIR / "arxiv_metadata.sqlite3"
