from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal, get_db


router = APIRouter(prefix="/books", tags=["Books"],)


@router.get("/", response_model=list[schemas.BookRead])
async def get_all_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books

@router.get("/{book_id}", response_model=schemas.BookRead)
async def get_one_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=schemas.BookRead)
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.put("/{book_id}", response_model=schemas.BookRead)
async def update_book(book_id: int, updated: schemas.BookUpdate, db: Session = Depends(get_db)):
    existing_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    for key, value in updated.dict(exclude_unset=True).items():
        setattr(existing_book, key, value)
    
    db.commit()
    db.refresh(existing_book)
    return existing_book

@router.delete("/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return {"message": "Book deleted "}

@router.get("/search", response_model=list[schemas.BookRead])
async def search_books(search: str, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(
        (models.Book.title.ilike(f"%{search}%")) |
        (models.Book.author.ilike(f"%{search}%"))
    ).all()

@router.get("/filter", response_model=list[schemas.BookRead])
async def filter_books(min: int, max: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(
        models.Book.year >= min,
        models.Book.year <= max
    ).all()