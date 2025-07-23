"""
Models for database.
"""

from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Bookmark(Base):
    """
    Class of bookmark table.
    """

    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    url = Column(String(255), unique=True, index=True)
    description = Column(Text, nullable=True)
    tags = Column(String(255), nullable=True)
