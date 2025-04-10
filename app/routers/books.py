from fastapi import APIRouter
from models.book import Book
from data.books import books

router = APIRouter(prefix="/books")


@router.get("/")
def get_all_books() -> list[Book]:
    """Returns the list of available books."""
    return list(books.values())