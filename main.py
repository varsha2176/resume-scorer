from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Resume(BaseModel):
    resume_text: str

@app.post("/score-resume")
def score_resume(resume: Resume):
    text = resume.resume_text.lower()
    
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

    return {
        "score": min(score, 100),
        "suggestions": suggestions
    }
