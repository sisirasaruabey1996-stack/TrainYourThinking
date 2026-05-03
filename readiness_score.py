import json
from pathlib import Path

def calculate_score() -> int:
    file = Path("weakness.json")
    if not file.exists():
        return 100

    data = json.loads(file.read_text())
    if not data:
        return 100

    total_rate = 0
    for topic, stats in data.items():
        if stats["attempts"] > 0:
            struggle_rate = stats["struggles"] / stats["attempts"]
            total_rate += struggle_rate

    avg_struggle = total_rate / len(data)
    score = round((1 - avg_struggle) * 100)
    return max(0, min(100, score))

def show_score():
    score = calculate_score()
    bar = "█" * (score // 5) + "░" * (20 - score // 5)
    print(f"\n--- Google Readiness Score ---")
    print(f"  [{bar}] {score}/100")
    if score >= 80:
        print("  Status: Interview ready")
    elif score >= 50:
        print("  Status: Keep practicing")
    else:
        print("  Status: Focus on weak areas")
    print()