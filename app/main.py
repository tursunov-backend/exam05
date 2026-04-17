from fastapi import FastAPI
from app.routers import books

app = FastAPI(title="Book Management API")

app.include_router(books.router)
