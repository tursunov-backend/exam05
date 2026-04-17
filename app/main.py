from fastapi import FastAPI
from .routers.books import router

from .models import *
from .database import engine

Base.metadate.create_all(bind=engine)

app = FastAPI(title="Book Management API")

app.include_router(router)
