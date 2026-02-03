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

print("✓ API key found")

try:
    # Initialize client
    client = genai.Client(api_key=api_key)
    print("✓ Client initialized")
    
    # Test API call
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say 'Hello, API is working!' in one sentence"
    )
    
    print("✓ API call successful")
    print(f"\nResponse: {response.text}")
    print("\n✅ Your Gemini API key is working perfectly!")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    print("Your API key might be invalid or you might not have internet connection")
