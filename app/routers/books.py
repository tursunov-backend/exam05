from typing import Annotated

from fastapi import APIRouter, Depends, Query, Path, Body
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import BookCreate, BookUpdate, BookResponse
from app.book_service import BookService

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def get_all_books(
    db: Annotated[Session, Depends(get_db)],
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(gt=0)] = 10,
):
    service = BookService(db)
    return service.get_all_books(skip, limit)


@router.get("/search", response_model=list[BookResponse])
def search_books(
    search: Annotated[str, Query(min_length=2)], db: Annotated[Session, Depends(get_db)]
):
    service = BookService(db)
    return service.search_books(search)


@router.get("/filter", response_model=list[BookResponse])
def filter_books(
    min_year: Annotated[int, Query(ge=0)],
    max_year: Annotated[int, Query(ge=0)],
    db: Annotated[Session, Depends(get_db)],
):
    service = BookService(db)
    return service.filter_books(min_year, max_year)


@router.get("/{book_id}", response_model=BookResponse)
def get_one_book(
    book_id: Annotated[int, Path(gt=0)], db: Annotated[Session, Depends(get_db)]
):
    book = BookService(db)
    return book.get_one_book(book_id)


@router.post("/", response_model=BookResponse)
def create_book(
    book: Annotated[BookCreate, Body()], db: Annotated[Session, Depends(get_db)]
):
    books = BookService(db)
    return books.create_book(book)


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: Annotated[int, Path(gt=0)],
    book: Annotated[BookUpdate, Body()],
    db: Annotated[Session, Depends(get_db)],
):
    books = BookService(db)
    return books.update_book(book_id, book)


@router.delete("/{book_id}")
def delete_book(
    book_id: Annotated[int, Path(gt=0)], db: Annotated[Session, Depends(get_db)]
):
    service = BookService(db)
    service.delete_book(book_id)
    db.commit()
    return {"message": "Book deleted"}
