from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from app.query import ask_question
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("API_KEY")

class QueryRequest(BaseModel):
    question: str

def verify_key(x_api_key: str):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.post("/query")
def query(req: QueryRequest, x_api_key: str = Header(...)):
    verify_key(x_api_key)

    answer = ask_question(req.question)

    return {
        "question": req.question,
        "answer": answer
    }