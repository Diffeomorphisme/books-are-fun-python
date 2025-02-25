import uuid

from sqlalchemy.orm import Session
from src.backend.books.schema import BookModel
from src.backend.core.utils import logger


def get_book_from_id(book_id: uuid.UUID, db: Session) -> BookModel | None:
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def get_books(db: Session) -> [BookModel]:
    return db.query(BookModel).all()


def create_book(book_title: str, db: Session) -> BookModel:
    book_to_create = BookModel(title=book_title)
    db.add(book_to_create)
    db.commit()
    db.refresh(book_to_create)
    return book_to_create


def update_book_with_id(
        book_to_update: BookModel, db: Session
) -> BookModel | None:
    existing_book = get_book_from_id(book_to_update.id, db)
    if existing_book:
        book_to_update.id = existing_book.id
        db.merge(book_to_update)
        db.commit()
        return book_to_update
    else:
        logger.error("Book not found")


def delete_book_with_id(book_id: uuid.UUID, db: Session):
    existing_book = get_book_from_id(book_id, db)
    if existing_book:
        db.delete(existing_book)
        db.commit()
    else:
        logger.error("Book not found")
