from sqlmodel import SQLModel, Field
from typing import Annotated


class Book(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    author: str
    review: Annotated[int, Field(ge=1, le=5)] = None
