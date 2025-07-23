"""
Main
"""

from fastapi import FastAPI

from app.api.routers import bookmark_router


app = FastAPI(title='Bookmarks')

app.include_router(bookmark_router)
