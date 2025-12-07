"""
This module defines FastAPI routes for rendering HTML templates
and processing form input using FastAPI and Jinja2.
"""

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Render the homepage."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/process", response_class=HTMLResponse)
def process(request: Request, username: str = Form(...)):
    """Process the submitted form and display a message."""
    message = f"Hello {username}, FastAPI ne aapka data receive kar liya!"
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": message}
    )

