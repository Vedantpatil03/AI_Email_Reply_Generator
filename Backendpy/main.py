from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

# Configure Gemini API
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

app = FastAPI()

# Allow Chrome extension to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    emailText: str
    tone: str

@app.post("/generate-reply")
def generate_reply(data: EmailRequest):
    prompt = f"You are an assistant that writes professional email replies.\n\nWrite a {data.tone} email reply to this message:\n\n{data.emailText}"

    response = client.models.generate_content(
        model=DEFAULT_MODEL,
        contents=prompt
    )
    reply = response.text
    return {"reply": reply}
