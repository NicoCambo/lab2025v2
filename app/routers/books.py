from fastapi import APIRouter, HTTPException, Path
from pydantic import ValidationError
from models.book import Book
from models.review import Review
from data.books import books
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

@router.post("/{id}/review")
def add_review(
        id: Annotated[int, Path(description="The ID of the book to which add the review")],
        review: Review
):
    """Adds a review to the book with the given ID."""
    try:
        books[id].review = review.review
        return "Review successfully added"
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")
    except ValidationError:
        raise HTTPException(status_code=400, detail="Not a valid review")



