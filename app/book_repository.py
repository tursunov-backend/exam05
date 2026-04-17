from sqlalchemy.orm import Session
from sqlalchemy import select, or_, and_
from .models import Book


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 20):
        return self.db.query(Book).offset(skip).limit(limit).all()

    def search(self, search: str):
        return (
            self.db.query(Book)
            .filter(
                or_(Book.title.ilike(f"%{search}%"), Book.author.ilike(f"%{search}%"))
            )
            .all()
        )

    def filter_by_year(self, min_year: int, max_year: int):
        return (
            self.db.query(Book)
            .filter(and_(Book.year >= min_year, Book.year <= max_year))
            .all()
        )

    def get_by_id(self, book_id: int):
        return self.db.query(Book).get(book_id)

    def create(self, data: dict):
        book = Book(**data)

        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)

        return book

    def update(self, existing_book: Book, data: dict):
        for key, value in data.items():
            setattr(existing_book, key, value)

        self.db.commit()
        self.db.refresh(existing_book)

        return existing_book

    def delete(self, existing_book: Book):
        self.db.delete(existing_book)
        self.db.commit()
