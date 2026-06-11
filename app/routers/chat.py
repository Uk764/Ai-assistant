from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
from groq import Groq

router = APIRouter()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]
    system: Optional[str] = "You are a helpful, friendly AI assistant."
    max_tokens: Optional[int] = 1024

class ChatResponse(BaseModel):
    reply: str

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        all_messages = [{"role": "system", "content": req.system}] + \
                       [m.model_dump() for m in req.messages]
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=all_messages,
            max_tokens=req.max_tokens,
        )
        return ChatResponse(reply=response.choices[0].message.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))