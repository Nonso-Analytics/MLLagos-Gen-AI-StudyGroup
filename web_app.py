from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
import markdown
from app import GeminiCLI

# Setup templates folder
templates = Jinja2Templates(directory="templates")
app = FastAPI()

# Initialize Gemini CLI (reads API key from .env)
cli = GeminiCLI()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "answer": None})

@app.post("/", response_class=HTMLResponse)
async def ask_gemini(request: Request, question: str = Form(...)):
    # Get Gemini response
    raw_answer = cli.ask(question)

    # Convert Markdown to HTML
    html_answer = markdown.markdown(
        raw_answer,
        extensions=["extra", "nl2br"]  # preserves line breaks and extra formatting
    )

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "answer": html_answer, "question": question}
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("web_app:app", host="0.0.0.0", port=port)
