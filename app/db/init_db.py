from sqlmodel import SQLModel
from app.db.session import engine

# Import models to register tables
from app.models.book import Book
from app.models.review import Review
from app.models.tag import Tag, BookTag
from app.models.user import User


async def init_db() -> None:
    print("Creating async database tables...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    print("✅ Database initialized successfully.")
