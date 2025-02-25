import uuid

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.backend.core.db.database import get_db
from src.backend.books.schema import BookModel, BookToUpdate, Book
from src.backend.books.crud import (
    get_books,
    get_book_from_id,
    update_book_with_id,
    create_book,
    delete_book_with_id
)

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get("/")
def get_all_books(db: Session = Depends(get_db)) -> list[Book]:
    return [
        Book(**book.as_dict()) for book in get_books(db)
    ]


@router.get("/{book_id}")
def get_book(book_id: uuid.UUID, db: Session = Depends(get_db)) -> Book:
    book = get_book_from_id(book_id, db)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return Book(**book.as_dict())


@router.put("/{book_id}")
def update_book(
        book_id: uuid.UUID, book: BookToUpdate, db: Session = Depends(get_db)
) -> Book:
    if not get_book_from_id(book_id, db):
        raise HTTPException(status_code=404, detail="Book not found")
    updated_book = update_book_with_id(
        BookModel(**book.model_dump(), id=book_id),
        db
    )
    return Book(**updated_book.as_dict())


@router.post("/")
def add_book(boot_title: str, db: Session = Depends(get_db)) -> Book:
    created_book = create_book(boot_title, db)
    return Book(**created_book.as_dict())


@router.delete("/{book_id}")
def remove_book(book_id: uuid.UUID, db: Session = Depends(get_db)) -> None:
    if not get_book_from_id(book_id, db):
        raise HTTPException(status_code=404, detail="Book not found")
    return delete_book_with_id(book_id, db)
