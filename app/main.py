from fastapi import FastAPI
from app.api.v1.endpoints import books
from app.db.init_db import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()  
    yield

def create_app() -> FastAPI:
    app = FastAPI(
        title="Bookly API",
        version="1.0.0",
        description="A simple API for managing books and users with authentication and reviews.",
        lifespan=lifespan,
    )
    app.include_router(books.router, prefix="/books", tags=["books"])
    return app



if __name__ == "__main__":
    # uvicorn app.main:create_app --reload
    pass
                


