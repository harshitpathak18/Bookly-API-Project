# user.py
import uuid
from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, Column
import sqlalchemy.dialects.postgresql as pg

# from app.models.book import Book  # for reverse relationship
# from app.models.review import Review  # for reverse relationship


class User(SQLModel, table=True):
    __tablename__ = "users"  # Table name in the DB

    # Unique user ID (UUID type)
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, nullable=False, default=uuid.uuid4)
    )

    # Basic user info
    username: str
    email: str
    first_name: str
    last_name: str

    # Role field with default "user"
    role: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False, server_default="user")
    )

    is_verified: bool = Field(default=False)  # Whether user email is verified

    # Password hash field (excluded from API responses)
    password_hash: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False), exclude=True
    )

    # Timestamps
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    # Relationships: one-to-many (User -> Books, Reviews)
    books: List["Book"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    )
    reviews: List["Review"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    )

    def __repr__(self):
        return f"<User {self.username}>"
