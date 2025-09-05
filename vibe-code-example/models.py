"""Data models for the Bundestag scraper."""

from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class Document(BaseModel):
    """Interface for document links found on pages."""
    title: str = Field(..., description="Title of the document")
    url: str = Field(..., description="Download URL of the document")
    file_type: str = Field(..., description="File type (PDF, DOC, etc.)")


class ScrapedDocument(BaseModel):
    """Interface for scraped document data structure."""
    topic: str = Field(..., description="Topic/category of the document")
    title: str = Field(..., description="Title of the scraped content")
    text_html: str = Field(..., description="Plain text content extracted from the scraped HTML")
    author: str = Field(..., description="Author of the content")
    documents: List[Document] = Field(default_factory=list, description="List of download links found on the page")
    scraped_at: datetime = Field(default_factory=datetime.now, description="Timestamp when the document was scraped")
    source_url: str = Field(..., description="Original URL that was scraped")