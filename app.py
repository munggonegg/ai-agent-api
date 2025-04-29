import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@app.get("/")
async def root():
    return {"message": "Welcome to the LLM API 🚀. Use POST /ask to interact."}

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": request.question},
            ],
            model="llama3-70b-8192",
        )

        answer = chat_completion.choices[0].message.content
        return AnswerResponse(answer=answer)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))