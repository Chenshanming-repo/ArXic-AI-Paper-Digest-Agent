"""Pydantic models for the ArXiv digest bot."""

from __future__ import annotations

from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class Paper(BaseModel):
    """A single ArXiv paper as fetched from the API."""

    arxiv_id: str = Field(..., description="ArXiv identifier, e.g. '2401.12345v1'.")
    url: HttpUrl = Field(..., description="Canonical abs URL on arxiv.org.")
    title: str = Field(..., description="Paper title with whitespace normalised.")
    authors: list[str] = Field(..., description="Ordered list of author names.")
    abstract: str = Field(..., description="Paper abstract with whitespace normalised.")
    published: datetime = Field(..., description="UTC submission timestamp.")
    updated: Optional[datetime] = Field(
        default=None, description="UTC updated timestamp from arXiv."
    )
    primary_category: Optional[str] = Field(
        default=None, description="Primary ArXiv category, e.g. 'cs.AI'."
    )
    categories: list[str] = Field(
        default_factory=list, description="All arXiv categories listed on the entry."
    )
    pdf_url: Optional[str] = Field(default=None, description="Canonical PDF URL.")


class DigestEntry(BaseModel):
    """A paper paired with its LLM-generated summary, ready to render."""

    paper: Paper
    summary: str = Field(..., description="2-3 sentence Chinese summary.")


class Digest(BaseModel):
    """A full daily digest: a date plus the entries to render."""

    digest_date: date
    entries: list[DigestEntry]

    @property
    def paper_count(self) -> int:
        return len(self.entries)
