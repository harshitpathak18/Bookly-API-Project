FastAPI_Project/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── books.py
│   │   │   │   ├── users.py
│   │   │   │   ├── reviews.py
│   │   │   │   ├── tags.py
│   │   │   │   ├── auth.py
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   │
│   ├── models/
│   │   ├── book.py
│   │   ├── user.py
│   │   ├── review.py
│   │   ├── tag.py
│   │   ├── __init__.py
│   │
│   ├── schemas/
│   │   ├── book.py
│   │   ├── user.py
│   │   ├── review.py
│   │   ├── tag.py
│   │   └── auth.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── book_service.py
│   │   ├── user_service.py
│   │   ├── review_service.py
│   │   ├── tag_service.py
│   │   └── auth_service.py
│   │   └── __init__.py
│   │
│   ├── db/
│   │   ├── session.py          # DB connection
│   │   ├── init_db.py          # DB creation logic
│   │   └── __init__.py
│   │
│   ├── core/
│   │   ├── config.py           # Pydantic settings
│   │   ├── security.py         # Password hashing, JWT handling
│   │   └── __init__.py
│   │
│   ├── main.py                 # FastAPI app instance
│   └── __init__.py
│
├── .env
├── pyproject.toml
├── requirements.txt
├── README.md
└── uvicorn.config.py (optional)
