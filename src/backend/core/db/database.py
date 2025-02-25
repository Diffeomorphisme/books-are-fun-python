from sqlalchemy.exc import ArgumentError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


try:

    db_string = "postgresql://testuser:testpwd@db:5432/testdb"

    engine = create_engine(
        db_string,
        pool_pre_ping=True,
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
