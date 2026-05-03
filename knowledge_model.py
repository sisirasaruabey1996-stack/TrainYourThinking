import json
from pathlib import Path
from datetime import datetime

FILE = "knowledge.json"

def load() -> dict:
    if Path(FILE).exists():
        return json.loads(Path(FILE).read_text())
    return {"topics": {}, "sessions_completed": 0}

def save(data: dict):
    Path(FILE).write_text(json.dumps(data, indent=2))

def update(topic: str, score: float, difficulty: str):
    data = load()
    if topic not in data["topics"]:
        data["topics"][topic] = {
            "attempts": 0,
            "scores": [],
            "avg": 0,
            "last_3_avg": 0,
            "trend": "new",
            "can_solve_easy": False,
            "can_solve_medium": False,
            "can_solve_hard": False,
            "common_mistakes": [],
            "last_seen": ""
        }

    t = data["topics"][topic]
    t["attempts"] += 1
    t["scores"].append(round(score, 1))
    t["avg"] = round(sum(t["scores"]) / len(t["scores"]), 1)
    t["last_3_avg"] = round(sum(t["scores"][-3:]) / min(len(t["scores"]), 3), 1)
    t["last_seen"] = datetime.now().strftime("%Y-%m-%d")

    if len(t["scores"]) >= 2:
        t["trend"] = "improving" if t["scores"][-1] > t["scores"][0] else "declining"

    if t["last_3_avg"] >= 7:
        if difficulty == "easy":   t["can_solve_easy"] = True
        if difficulty == "medium": t["can_solve_medium"] = True
        if difficulty == "hard":   t["can_solve_hard"] = True

    save(data)

def can_solve(topic: str, difficulty: str) -> str:
    data = load()
    if topic not in data["topics"]:
        return "insufficient data"
    t = data["topics"][topic]
    if t["attempts"] < 3:
        return "insufficient data"
    key = f"can_solve_{difficulty}"
    return "yes" if t.get(key) else "no"

def show_knowledge():
    data = load()
    if not data["topics"]:
        print("\nNo knowledge data yet.\n")
        return
    print("\n--- Knowledge Model ---")
    for topic, t in data["topics"].items():
        print(f"\n  {topic}")
        print(f"    attempts : {t['attempts']}")
        print(f"    avg score: {t['avg']}/10")
        print(f"    trend    : {t['trend']}")
        print(f"    easy     : {'✅' if t['can_solve_easy'] else '❌'}")
        print(f"    medium   : {'✅' if t['can_solve_medium'] else '❌'}")
        print(f"    hard     : {'✅' if t['can_solve_hard'] else '❌'}")
    print()

def increment_sessions():
    data = load()
    data["sessions_completed"] += 1
    save(data)