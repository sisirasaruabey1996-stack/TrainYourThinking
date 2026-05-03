from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Initialize client
client = genai.Client(api_key=api_key)

print("DSA Coach Agent — type 'quit' to exit\n")

while True:
    user = input("You: ")
    if user == "quit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"You are a strict DSA coach. Never give direct answers. Use Socratic method.\n\nStudent: {user}"
    )

    print(f"\nCoach: {response.text}\n")