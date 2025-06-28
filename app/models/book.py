import uuid
from datetime import datetime, date
from typing import List, Optional

from sqlalchemy.dialects import postgresql as pg
from sqlmodel import Column, Field, Relationship, SQLModel


from app.models.user import User
from app.models.review import Review
from app.models.tag import Tag, BookTag  # M2M link model


class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, nullable=False, default=uuid.uuid4)
    )

    # Book details
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int

    # Foreign Key to the user who added the book
    user_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="users.uid")

    # Timestamps
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now()))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now()))

    # Relationships
    user: Optional[User] = Relationship(back_populates="books")
    reviews: List[Review] = Relationship(
        back_populates="book", sa_relationship_kwargs={"lazy": "selectin"}
    )
    tags: List[Tag] = Relationship(
        link_model=BookTag,
        back_populates="books",
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    def _repr__(self):
        return f"<Book {self.title}>"
