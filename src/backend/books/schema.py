import uuid
from sqlalchemy import Column, String, UUID

from src.backend.core.db.database import Base
from pydantic import BaseModel


class BookModel(Base):
    __tablename__ = 'book'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)


class BookToUpdate(BaseModel):
    title: str