from typing import Generator

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.settings import settings


url = URL.create(
    drivername="postgresql",
    username=settings.DB_USER,
    password=settings.DB_PASS,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)
engine = create_engine(url)
SessionLocal = sessionmaker(engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
