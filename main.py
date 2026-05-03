from datetime import datetime
from pathlib import Path
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

session_file = f"sessions/session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
Path("sessions").mkdir(exist_ok=True)

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

    try:
        reply = response.text
        if not reply or not reply.strip():
            reply = "I need you to elaborate further. What are your thoughts?"
    except Exception:
        reply = "I need you to elaborate further. What are your thoughts?"

    if reply.strip():
        history.append({"role": "model", "parts": [{"text": reply}]})

    print(f"\nCoach: {reply}\n")

    with open(session_file, "a") as f:
        f.write(f"You: {user}\nCoach: {reply}\n\n")