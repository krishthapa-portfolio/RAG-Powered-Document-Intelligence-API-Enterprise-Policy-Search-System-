from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from app.query import ask_question
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("API_KEY")

class QuestionRequest(BaseModel):
    question: str

# 🔐 SECURITY CHECK FUNCTION
def verify_key(x_api_key: str):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.post("/ask")
def ask(req: QuestionRequest, x_api_key: str = Header(None)):

    verify_key(x_api_key)

    answer = ask_question(req.question)

    return {
        "question": req.question,
        "answer": answer
    }

