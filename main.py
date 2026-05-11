"""Daily ArXiv digest orchestrator.

Run from the GitHub Action (or locally) to:
  1. Fetch recent papers from configured ArXiv categories.
  2. Summarise each one with OpenAI.
  3. Append the result to digest/digest.md and overwrite digest/latest.md.

Exits with code 0 on success (including the "no papers today" case) and
code 1 on a fatal error so the Action shows as failed.
"""

from __future__ import annotations

import logging
import os
import sys
from datetime import datetime, timezone

from dotenv import load_dotenv
from openai import OpenAI

import config
from src.fetcher import fetch_recent_papers
from src.models import Digest
from src.summariser import summarise_papers
from src.writer import append_to_digest, render_digest, write_latest

logger = logging.getLogger("arxiv_digest")


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )


def _require_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it as a GitHub Actions secret "
            "or to your local .env file."
        )
    return api_key


def run() -> int:
    """Main entry point. Returns the desired process exit code."""
    load_dotenv()
    _configure_logging()

    api_key = _require_api_key()

    now = datetime.now(timezone.utc)
    logger.info("Starting digest run at %s", now.isoformat())

    papers = fetch_recent_papers(
        categories=config.CATEGORIES,
        lookback_hours=config.LOOKBACK_HOURS,
        max_results=config.MAX_PAPERS,
        page_size=config.ARXIV_PAGE_SIZE,
        api_url=config.ARXIV_API_URL,
        now=now,
    )

    if not papers:
        logger.info(
            "No papers found in the last %dh for categories %s — exiting "
            "cleanly without writing.",
            config.LOOKBACK_HOURS,
            config.CATEGORIES,
        )
        return 0

    logger.info("Summarising %d papers with model %s", len(papers), config.OPENAI_MODEL)

    client = OpenAI(api_key=api_key)
    entries = summarise_papers(
        papers,
        client=client,
        model=config.OPENAI_MODEL,
        max_tokens=config.OPENAI_MAX_TOKENS,
    )

    if not entries:
        logger.warning(
            "All %d papers failed to summarise — exiting without writing.",
            len(papers),
        )
        return 0

    digest = Digest(digest_date=now.date(), entries=entries)
    rendered = render_digest(digest)

    append_to_digest(config.DIGEST_FILE, rendered)
    write_latest(config.LATEST_FILE, rendered)

    logger.info(
        "Digest complete: %d/%d papers summarised for %s",
        len(entries),
        len(papers),
        digest.digest_date.isoformat(),
    )
    return 0


def main() -> None:
    try:
        sys.exit(run())
    except Exception:
        logger.exception("Fatal error during digest run")
        sys.exit(1)


if __name__ == "__main__":
    main()
