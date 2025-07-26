from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None

@app.post("/api/chat")
async def chat(request: ChatRequest):
    return {"response": "This will be replaced with LLM integration"}
