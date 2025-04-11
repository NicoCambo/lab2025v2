from fastapi import FastAPI
from app.routers import books
from fastapi.responses import HTMLResponse



app = FastAPI()

app.include_router(books.router, tags=["books"])


@app.get("/",response_class=HTMLResponse)
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    """
    return html

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)