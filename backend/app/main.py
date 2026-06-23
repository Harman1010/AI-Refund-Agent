from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import ChatRequest
from app.agents.refund_agent import process_refund


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():

    return {
        "message": "AI Refund Agent Running"
    }


@app.post("/chat")
def chat(data: ChatRequest):

    result = process_refund(data.message)

    return result