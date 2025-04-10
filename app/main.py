from fastapi import FastAPI
from app.data.books import books


app = FastAPI()

app.include_router(books.router, tags=["books"])



if __name__ == "__main__":
    import unicorn
    unicorn.run("main:app1", reload=True)