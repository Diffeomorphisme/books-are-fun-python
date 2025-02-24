from fastapi import APIRouter
from src.backend.books.endpoints import router as books_router

api_router = APIRouter(prefix="/api")

api_router.include_router(books_router)
