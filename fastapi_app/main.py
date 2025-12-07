from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process", response_class=HTMLResponse)
def process(request: Request, username: str = Form(...)):
    message = f"Hello {username}, FastAPI ne aapka data receive kar liya!"
    return templates.TemplateResponse("index.html", {
        "request": request,
        "message": message
    })

