from datetime import datetime
from pathlib import Path
from google import genai
from dotenv import load_dotenv
import os
from tracker import save_topic, show_progress
from weakness_tracker import log_topic, show_weaknesses
from readiness_score import show_score
from visual_engine import (
    animate_binary_search,
    animate_bubble_sort,
    compare_search,
    animate_tree,
)

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM = "You are a strict DSA coach. Never give direct answers. Use Socratic method."

history = [
    {"role": "user", "parts": [{"text": SYSTEM}]},
    {"role": "model", "parts": [{"text": "Understood. I will coach using Socratic method."}]}
]

current_topic = None
topic_turn_count = 0
STRUGGLE_THRESHOLD = 3

print("DSA Coach Agent — type 'quit' to exit\n")

session_file = f"sessions/session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
Path("sessions").mkdir(exist_ok=True)

while True:
    user = input("You: ")
    if user == "quit":
        break

    # Topic setter
    if user.startswith("topic:"):
        current_topic = user.replace("topic:", "").strip()
        topic_turn_count = 0
        print(f"Topic set: {current_topic}\n")
        continue

    # Help command
    if user == "help":
        print("""
Commands
─────────────────────────────
topic: <name>     Set current topic
struggled: <name> Log struggle manually  
mastered: <name>  Log mastery manually
weaknesses        Show weak areas
progress          Show studied topics
score             Show readiness score
visual: <number>  Binary search animation
sort: <numbers>   Bubble sort animation
compare: <number> Linear vs binary search
tree              Binary tree traversal
help              Show this menu
quit              Exit
─────────────────────────────
""")
        continue

    # Commands
    if user.startswith("studied:"):
        save_topic(user.replace("studied:", "").strip())
        print("Saved.\n")
        continue

    if user.startswith("struggled:"):
        topic = user.replace("struggled:", "").strip()
        log_topic(topic, struggled=True)
        print("Logged as struggle.\n")
        continue

    if user.startswith("mastered:"):
        topic = user.replace("mastered:", "").strip()
        log_topic(topic, struggled=False)
        print("Logged as mastered.\n")
        continue

    if user == "progress":
        show_progress()
        continue

    if user == "weaknesses":
        show_weaknesses()
        continue

    if user == "score":
        show_score()
        continue

    # Visuals
    if user.startswith("visual:"):
        parts = user.replace("visual:", "").strip().split()
        target = int(parts[-1])
        arr = list(range(2, 22, 2))
        animate_binary_search(arr, target)
        continue

    if user.startswith("sort:"):
        nums = list(map(int, user.replace("sort:", "").strip().split()))
        animate_bubble_sort(nums)
        continue

    if user.startswith("compare:"):
        target = int(user.replace("compare:", "").strip())
        compare_search(target)
        continue

    if user == "tree":
        animate_tree()
        continue

    # Auto-detect
    if current_topic:
        topic_turn_count += 1
        if topic_turn_count >= STRUGGLE_THRESHOLD:
            log_topic(current_topic, struggled=True)
            print(f"[Auto-detected struggle: {current_topic}]\n")
            topic_turn_count = 0

    # Gemini call
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