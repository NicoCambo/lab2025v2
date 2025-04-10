from fastapi import APIRouter, HTTPException, Path
from app.models.book import Book
from app.data.books import books
from typing import Annotated

router = APIRouter(prefix="/books")


@router.get("/")
def get_all_books() -> list[Book]:
    """Returns the list of available books."""
    return list(books.values())

@router.get("/{id}")
def get_book_by_id(id: Annotated[int, Path(description="The ID of the book to get")]) -> Book:
    """Returns the book with the given id."""
    try:
        return books[id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")
