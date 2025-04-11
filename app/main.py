from fastapi import FastAPI
from app.data.books import books


app = FastAPI()

app.include_router(books.router, tags=["books"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)