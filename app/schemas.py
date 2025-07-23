"""
Bookmark shemas
"""

from pydantic import BaseModel, HttpUrl


class BookmarkBase(BaseModel):
    title: str
    url: HttpUrl
    description: str | None = None
    tags: str | None = None

class BookmarkCreate(BookmarkBase):
    pass

class Bookmark(BookmarkBase):
    id: int

    class Config:
        from_attributes = True
