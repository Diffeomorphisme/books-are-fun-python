from sqlalchemy.exc import ArgumentError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote

from src.backend.core import settings

try:
    if 'QUOTE_PW' in settings.DB_CONNECTION_STRING:
        db_string = settings.DB_CONNECTION_STRING.format_map(
            {'QUOTE_PW': quote(settings.QUOTE_PW)}
        )
    else:
        db_string = settings.DB_CONNECTION_STRING

    engine = create_engine(
        db_string,
        pool_pre_ping=True,
        # connect_args={"check_same_thread": False},  # only for sqlite
        echo=False
    )
except ArgumentError:
    engine = None

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Database dependencies."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
