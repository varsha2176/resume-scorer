from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def score_resume(text: str) -> int:
    keywords = {
        "python": 20,
        "machine learning": 20,
        "deep learning": 15,
        "tensorflow": 10,
        "data analysis": 10,
        "pandas": 10,
        "sql": 5,
        "scikit-learn": 10
    }

    score = 0
    text_lower = text.lower()

    for word, weight in keywords.items():
        if word in text_lower:
            score += weight

    return min(score, 100)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/score", response_class=HTMLResponse)
def score(request: Request, resume_text: str = Form(...)):
    result = score_resume(resume_text)
    return templates.TemplateResponse("result.html", {"request": request, "score": result})
