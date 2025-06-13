from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/result", response_class=HTMLResponse)
def get_result(request: Request, resume_text: str = Form(...)):
    keywords = ["python", "machine learning", "deep learning", "tensorflow", "data analysis", "pandas", "sql", "scikit-learn"]
    resume_text = resume_text.lower()
    score = sum(10 for word in keywords if word in resume_text)
    return templates.TemplateResponse("result.html", {"request": request, "score": score})