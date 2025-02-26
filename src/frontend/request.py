import requests
import pandas as pd

from model import Book


BACKEND_URL = "http://backend:3000/api/books"

def get_all_books() -> pd.DataFrame | None:
    """Fetch the books from the backend"""
    try:
        response = requests.get(BACKEND_URL)
        if response.status_code != 200:
            return

        results = response.json()
        books = [
            Book(**result) for result in results
        ]
        return pd.DataFrame([book.model_dump() for book in books])
    except Exception as e:
        print(f"Error fetching books: {e}")
        return
