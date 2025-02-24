from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.backend.core.db.database import get_db
from src.backend.books.schema import BookModel, BookToUpdate
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
def get_all_books(db: Session = Depends(get_db)) -> [BookModel]:
    return get_books(db)


@router.get("/{book_id}")
def get_book(book_id, db: Session = Depends(get_db)) -> [BookModel]:
    if not get_book_from_id(book_id, db):
        raise HTTPException(status_code=404, detail="Book not found")
    return get_book_from_id(book_id, db)


@router.put("/{book_id}")
def update_book(
        book_id, book: BookToUpdate, db: Session = Depends(get_db)
) -> BookModel:
    if not get_book_from_id(book_id, db):
        raise HTTPException(status_code=404, detail="Book not found")
    return update_book_with_id(
        BookModel(**book.model_dump(), id=book_id),
        db
    )


@router.post("/")
def add_book(boot_title: str, db: Session = Depends(get_db)) -> BookModel:
    return create_book(boot_title, db)


@router.delete("/{book_id}")
def remove_book(book_id, db: Session = Depends(get_db)) -> None:
    if not get_book_from_id(book_id, db):
        raise HTTPException(status_code=404, detail="Book not found")
    return delete_book_with_id(book_id, db)
