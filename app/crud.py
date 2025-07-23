"""
Operations with bookmarks.
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Bookmark
from app.schemas import BookmarkCreate


async def get_bookmark(db: AsyncSession, bookmark_id: int):
    """
    Get a bookmark by id.
    """

    result = await db.execute(select(Bookmark).filter(Bookmark.id == bookmark_id))
    return result.scalars().first()


async def get_bookmarks(db: AsyncSession, skip: int = 0, limit: int = 100):
    """
    Get bookmarks.
    """

    result = await db.execute(select(Bookmark).offset(skip).limit(limit))
    return result.scalars().all()


async def create_bookmark(db: AsyncSession, bookmark: BookmarkCreate):
    """
    Create a new bookmark.
    """

    db_bookmark = Bookmark(**bookmark.model_dump())
    db.add(db_bookmark)
    await db.commit()
    await db.refresh(db_bookmark)
    return db_bookmark
