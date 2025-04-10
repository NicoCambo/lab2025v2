from fastapi import APIRouter
from app.models.book import Book
from app.data.books import books

router = APIRouter(prefix="/books")


@router.get("/")
def get_all_books() -> list[Book]:
    """Returns the list of available books."""
    return list(books.values())

@router.get("/{id}")
def get_book_by_id(id: int) -> Book:
    """Returns the book with the given id."""
    return books[id]