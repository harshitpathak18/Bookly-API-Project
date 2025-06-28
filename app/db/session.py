from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Create async engine
engine = create_async_engine(url=settings.DATABASE_URL, echo=True, future=True)

# Async session factory
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
