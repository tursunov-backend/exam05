from fastapi import HTTPException
from sqlalchemy.orm import Session

from .book_repository import BookRepository
from .schemas import CreateBook, UpdateBook


class BookService:
    def __init__(self, db: Session):
        self.repo = BookRepository(db)

    def get_all_books(self, skip: int = 0, limit: int = 20):
        return self.repo.get_all(skip, limit)

    def search_books(self, search: str):
        return self.repo.search(search)

    def filter_books(self, min_year: int, max_year: int):
        if min_year > max_year:
            raise HTTPException(status_code=400, detail="Invalid year")
        return self.repo.filter_by_year(min_year, max_year)

    def get_one_book(self, book_id: int):
        book = self.repo.get_by_id(book_id)

        if not book:
            raise HTTPException(status_code=404, detail="book not fount.")

        return book

    def create_book(self, book: CreateBook):
        data = book.model_dump()
        return self.repo.create(data)

    def update_book(self, book_id: int, book: UpdateBook):
        existing_book = self.repo.get_by_id(book_id)

        if not existing_book:
            raise HTTPException(status_code=404, detail="book not fount.")

        data = book.model_dump()
        return self.repo.update(existing_book, data)

    def delete_book(self, book_id: int):
        existing_book = self.repo.get_by_id(book_id)

        if not existing_book:
            raise HTTPException(status_code=404, detail="book not fount.")
        
        self.repo.delete(existing_book)
