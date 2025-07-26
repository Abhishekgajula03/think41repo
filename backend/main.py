from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm_response(prompt: str) -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="mixtral-8x7b-32768",
    )
    return response.choices[0].message.content

@app.post("/api/chat")
async def chat(request: ChatRequest):
    # ... existing conversation logic ...
    
    # Get LLM response
    llm_response = get_llm_response(request.message)
    
    return {
        "response": llm_response,
        "conversation_id": conv.id
    }
