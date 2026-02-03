from dotenv import load_dotenv
import os
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: GEMINI_API_KEY not found in .env file")
    exit(1)

try:
    # Initialize client
    client = genai.Client(api_key=api_key)
    
    # List available models
    print("Available models:\n")
    models = client.models.list()
    
    for model in models:
        print(f"- {model.name}")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
