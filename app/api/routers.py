"""
Bookmark router.
"""

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, schemas
from app.database import get_db


bookmark_router = APIRouter(prefix='/bookmark')

@bookmark_router.post("", response_model=schemas.Bookmark)
async def create_bookmark( bookmark: schemas.BookmarkCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new bookmark.
    """

    return await create_bookmark(bookmark, db)


@bookmark_router.get("/bookmarks/", response_model=list[schemas.Bookmark])
async def read_bookmarks(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """
    Return bookmarks.
    """

    bookmarks = await crud.get_bookmarks(db, skip=skip, limit=limit)
    return bookmarks


@bookmark_router.get("/bookmarks/{bookmark_id}", response_model=schemas.Bookmark)
async def read_bookmark(bookmark_id: int, db: AsyncSession = Depends(get_db)):
    """
    Get bookmark by id.
    """

    db_bookmark = await crud.get_bookmark(db, bookmark_id=bookmark_id)
    if db_bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return db_bookmark
