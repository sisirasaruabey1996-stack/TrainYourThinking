import json
from pathlib import Path

FILE = "weakness.json"

def load():
    if Path(FILE).exists():
        return json.loads(Path(FILE).read_text())
    return {}

def log_topic(topic: str, struggled: bool):
    data = load()
    if topic not in data:
        data[topic] = {"attempts": 0, "struggles": 0}
    data[topic]["attempts"] += 1
    if struggled:
        data[topic]["struggles"] += 1
    Path(FILE).write_text(json.dumps(data, indent=2))

def show_weaknesses():
    data = load()
    if not data:
        print("\nNo data yet.\n")
        return
    print("\n--- Weak areas ---")
    for topic, stats in sorted(
        data.items(),
        key=lambda x: x[1]["struggles"],
        reverse=True
    ):
        rate = round(stats["struggles"] / stats["attempts"] * 100)
        print(f"  {topic}: {rate}% struggle rate")
    print()