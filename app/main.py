from fastapi import FastAPI
from app.routers import books, frontend, users
from starlette.staticfiles import StaticFiles
from app.data.db import init_database
from contextlib import contextmanager, asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    # an start
    init_database()
    yield
    # an close


app = FastAPI(lifespan=lifespan)
app.include_router(books.router, tags=["books"])
app.include_router(frontend.router)
app.include_router(users.router, tags=["users"])
app.mount("/static", StaticFiles(directory="app/static"), name='static')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)