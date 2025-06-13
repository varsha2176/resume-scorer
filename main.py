from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/score", response_class=HTMLResponse)
def score_resume(request: Request, resume_text: str = Form(...)):
    text = resume_text.lower()
    score = 0
    suggestions = []

    if "python" in text:
        score += 20
    else:
        suggestions.append("Mention Python if you know it.")
    
    if "project" in text:
        score += 20
    else:
        suggestions.append("Include your projects.")

    if "experience" in text:
        score += 30
    else:
        suggestions.append("Highlight your experience.")

    if "education" in text:
        score += 30
    else:
        suggestions.append("Add your education details.")

    return templates.TemplateResponse("result.html", {
        "request": request,
        "score": min(score, 100),
        "suggestions": suggestions
    })
