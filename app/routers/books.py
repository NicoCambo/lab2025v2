from fastapi import APIRouter, HTTPException, Path, Form
from app.models.review import Review
from typing import Annotated
from app.models.book import Book, BookPublic, BookCreate
from app.data.db import SessionDep
from sqlmodel import select

router = APIRouter(prefix="/books")


@router.get("/")
def get_all_books(
        session: SessionDep,
        sort: bool = False
) -> list[BookPublic]:
    """Returns the list of available books."""
    statement = select(Book)
    books = session.exec(statement).all()
    if sort:
        return sorted(books, key=lambda book: book.review)
    return books

@router.post("/")
def add_book(book: BookCreate, session: SessionDep):
    """Adds a new book."""
    validate_book=Book.model_validate(book)
    session.add(validate_book)
    session.commit()
    return "Book successfully added."

@router.post(" form/")
def add_book_from_form(
        book: Annotated[BookCreate, Form()],
        session: SessionDep
):
    """Adds a new book"""
    validate_book = Book.model_validate(book)
    session.add(validate_book)
    session.commit()
    return "Book successfully added."


@router.delete("/")
def delete_all_books(session: SessionDep):
    """Deletes all books."""
    statement = select(Book)
    session.execute(statement).delete()
    session.commit()
    return "All books successfully deleted."

@router.delete("/{id}")
def delete_book(
        session: SessionDep,
        id: Annotated[int, Path(description="The ID of the book to delete")]
):
    """Deletes the book with the given ID."""
    book = session.get(Book,id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()
    return "Book successfully deleted"

@router.get("/{id}")
def get_book_by_id(
        session: SessionDep,
        id: Annotated[int, Path(description="The ID of the book to get")]
) -> BookPublic:
    """Returns the book with the given id."""
    book = session.get(Book,id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/{id}/review")
def add_review(
        session: SessionDep,
        id: Annotated[int, Path(description="The ID of the book to which add the review")],
        review: Review
):
    """Adds a review to the book with the given ID."""
    book = session.get(Book,id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.review = review.review
    session.commit()
    return "Review successfully added"

@router.put("/{id}")
def update_book(
        session: SessionDep,
        id: Annotated[int, Path(description="The ID of the book to update")],
        new_book: BookCreate
):
    """Updates the book with the given ID."""
    book = session.get(Book,id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = new_book.title
    book.author = new_book.author
    book.review = new_book.review
    session.add(book)
    session.commit()
    return "Book successfully updated."







