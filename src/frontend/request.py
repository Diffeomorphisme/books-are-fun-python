from http.client import HTTPException
import requests
import pandas as pd

from model import Book


def get_all_books() -> pd.DataFrame | None:
    response = requests.get("http://backend:3000/api/books")
    if response.status_code != 200:
        return
    results = response.json()

    books = [
        Book(**result) for result in results
    ]
    return pd.DataFrame([book.model_dump() for book in books])
