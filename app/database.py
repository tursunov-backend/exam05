# from typing import Generator

# from sqlalchemy import URL, create_engine
# from sqlalchemy.orm import sessionmaker, Session

# from app.core.settings import settings


# url = URL.create(
#     drivername="postgresql+psycopg2",
#     host=settings.db_host,
#     port=settings.db_port,
#     username=settings.db_user,
#     password=settings.db_password,
#     database=settings.db_name,
# )
# engine = create_engine(url)
# SessionLocal = sessionmaker(engine)


# def get_db() -> Generator[Session, None, None]:
#     db = SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()