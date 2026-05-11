"""Pydantic models for the ArXiv digest bot."""

from __future__ import annotations

from datetime import datetime, date

from pydantic import BaseModel, Field, HttpUrl


class Paper(BaseModel):
    """A single ArXiv paper as fetched from the API."""

    arxiv_id: str = Field(..., description="ArXiv identifier, e.g. '2401.12345v1'.")
    url: HttpUrl = Field(..., description="Canonical abs URL on arxiv.org.")
    title: str = Field(..., description="Paper title with whitespace normalised.")
    authors: list[str] = Field(..., description="Ordered list of author names.")
    abstract: str = Field(..., description="Paper abstract with whitespace normalised.")
    published: datetime = Field(..., description="UTC submission timestamp.")
    primary_category: str | None = Field(
        default=None, description="Primary ArXiv category, e.g. 'cs.AI'."
    )


class DigestEntry(BaseModel):
    """A paper paired with its LLM-generated summary, ready to render."""

    paper: Paper
    summary: str = Field(..., description="2-3 sentence plain-English summary.")


class Digest(BaseModel):
    """A full daily digest: a date plus the entries to render."""

    digest_date: date
    entries: list[DigestEntry]

    @property
    def paper_count(self) -> int:
        return len(self.entries)
