from google import genai
from dotenv import load_dotenv
import os
from tracker import save_topic, show_progress

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM = "You are a strict DSA coach. Never give direct answers. Use Socratic method."

history = [
    {"role": "user", "parts": [{"text": SYSTEM}]},
    {"role": "model", "parts": [{"text": "Understood. I will coach using Socratic method."}]}
]

print("DSA Coach Agent — type 'quit' to exit\n")

while True:
    user = input("You: ")
    if user == "quit":
        break

    if user.startswith("studied:"):
        save_topic(user.replace("studied:", "").strip())
        print("Saved.\n")
        continue

    if user == "progress":
        show_progress()
        continue

    history.append({"role": "user", "parts": [{"text": user}]})

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history
    )

    reply = response.text
    history.append({"role": "model", "parts": [{"text": reply}]})

    print(f"\nCoach: {reply}\n")