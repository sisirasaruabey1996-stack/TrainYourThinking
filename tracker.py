import json
from pathlib import Path

HISTORY_FILE = "progress.json"

def load_progress():
    if Path(HISTORY_FILE).exists():
        return json.loads(Path(HISTORY_FILE).read_text())
    return {"topics": []}

def save_topic(topic: str):
    data = load_progress()
    data["topics"].append(topic)
    Path(HISTORY_FILE).write_text(json.dumps(data, indent=2))

def show_progress():
    data = load_progress()
    print("\n--- Topics studied ---")
    for t in data["topics"]:
        print(f"  - {t}")
    print()