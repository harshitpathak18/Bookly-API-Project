# review.py
import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Column, Relationship
import sqlalchemy.dialects.postgresql as pg

# from app.models.user import User
# from app.models.book import Book


class Review(SQLModel, table=True):
    __tablename__ = "reviews"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, nullable=False, default=uuid.uuid4)
    )

    rating: int = Field(lt=5)  # Rating must be less than 5
    review_text: str = Field(sa_column=Column(pg.VARCHAR, nullable=False))

    # Foreign keys
    user_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="users.uid")
    book_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="books.uid")

    # Timestamps
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    # Relationships
    user: Optional['User'] = Relationship(back_populates="reviews")
    book: Optional['Book'] = Relationship(back_populates="reviews")

    def __repr__(self):
        return f"<Review for book {self.book_uid} by user {self.user_uid}>"
