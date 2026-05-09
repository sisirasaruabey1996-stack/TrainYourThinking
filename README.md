# TrainYourThinking 🧠
> An AI-powered, full-stack interview preparation system built to crack 
> Designed, built, and used by a DevOps engineer 
> transitioning into AI/ML with zero prior ML experience.

---

## Why this exists

Most DSA prep tools give you answers.
This one never does.

TrainYourThinking uses the **Socratic method** — the same technique used by 
the world's best teachers and interviewers. It asks questions back. It makes 
you think. It detects when you're struggling before you even admit it.

It was built to solve a real problem: how do you prepare for a Google interview 
when you're starting from scratch, working full-time, and have no one to 
coach you?

The answer: build the coach yourself.

---

## What's inside

### 🎯 Mock Interview Engine
- Real LeetCode-style questions (curated, not generated)
- Structured evaluation using Gemini 2.5 Flash
- Scores every answer across 4 dimensions:
  - **Correctness** (0–4)
  - **Complexity awareness** (0–2)
  - **Edge case handling** (0–2)
  - **Clarity** (0–2)
- Verdict: Pass / Borderline / Fail
- Attempt penalty system (mirrors real interview pressure)
- Learning mode triggered automatically on failure

### 💬 Socratic DSA Coach (CLI + GUI)
- Never gives direct answers
- Multi-turn memory across the entire conversation
- Auto-detects struggle after 3 consecutive turns on same topic
- Manual logging: `struggled:` and `mastered:` commands
- Session logger saves every conversation to file

### 📊 Persistent Knowledge Model
- Tracks every topic attempted across all sessions
- Stores: attempts, scores, trend, can_solve_easy/medium/hard
- Answers: "Can this user solve a medium binary search problem?"
- Updates after every question automatically

### 🔄 Adaptive Decision Engine
- After every answer, decides:
  - Score ≥ 8 → advance to harder question
  - Score 4–7 → reinforce same topic
  - Score ≤ 3 → trigger learning mode + drop difficulty
  - 2 consecutive fails → switch topic entirely
  - 3 consecutive passes → skip to hard

### 📈 Readiness Score (0–100)
- Calculated from struggle rate across all tracked topics
- Weighted by topic difficulty and attempt count
- Visual progress bar in terminal
- Updates automatically after every session

### 🎬 Visual Algorithm Engine
- Binary search — animated step-by-step narrowing
- Bubble sort — visual swap animation
- Linear vs binary comparison — side by side
- Binary tree traversal — node-by-node with diagram

### 🖥️ Streamlit Web GUI
- Chat interface as main screen (like Claude/ChatGPT)
- Mock Interview mode via sidebar
- Evaluation screen with score breakdown
- Learning mode with visual animations
- Session complete screen with final verdict

---

## Tech stack

| Layer | Technology |
|---|---|
| Language | Python 3.14 |
| LLM | Gemini 2.5 Flash (google-genai) |
| GUI | Streamlit |
| Storage | JSON + SQLite |
| CLI | Rich terminal interface |
| Testing | pytest |

---

## Project structure

    TrainYourThinking/
    │
    ├── main.py                  # CLI DSA coach (Socratic)
    ├── app.py                   # Streamlit GUI
    ├── interview_cli.py         # Mock interview engine
    ├── visual_engine.py         # Algorithm animations
    ├── tracker.py               # Progress tracker
    ├── weakness_tracker.py      # Weakness detection
    ├── weakness.json            # Persisted weakness data
    ├── knowledge_model.py       # Cross-session knowledge
    ├── knowledge.json           # Persisted knowledge data
    ├── decision_engine.py       # Adaptive difficulty routing
    ├── readiness_score.py       # 0-100 score calculator
    ├── session.py               # Session state management
    ├── questions.json           # Curated question bank
    ├── requirements.txt
    ├── .env.example
    └── sessions/                # Auto-saved conversations

---

## Run locally

    git clone https://github.com/sisirasaruabey1996-stack/TrainYourThinking
    cd TrainYourThinking
    pip install -r requirements.txt
    cp .env.example .env
    # Add your Gemini API key to .env

**CLI Coach (Socratic mode):**

    python main.py

**Web GUI:**

    streamlit run app.py

**Mock Interview (CLI):**

    python interview_cli.py

---

## CLI commands

| Command | Action |
|---|---|
| `topic: binary search` | Set current topic |
| `struggled: arrays` | Log struggle manually |
| `mastered: arrays` | Log mastery manually |
| `weaknesses` | Show weak areas + struggle rate |
| `progress` | Show all studied topics |
| `score` | Show readiness score (0–100) |
| `visual: 14` | Animate binary search |
| `sort: 5 3 8 1 4` | Animate bubble sort |
| `compare: 14` | Linear vs binary comparison |
| `tree` | Binary tree traversal animation |
| `knowledge` | Full topic knowledge model |
| `help` | Show all commands |
| `quit` | Exit |

---

## How evaluation works

Every answer is scored by Gemini 2.5 Flash acting as a Google L5 interviewer:

    Correctness  → Is the core approach right?          (0–4)
    Complexity   → Did you state time AND space?         (0–2)
    Edge Cases   → Did you name specific edge cases?     (0–2)
    Clarity      → Was the explanation well structured?  (0–2)

Pre-checks run before the LLM call — regex detection of complexity
terms and edge case keywords — used as signals to improve accuracy.

**Verdict thresholds:**
- Pass = total ≥ 8
- Borderline = total 5–7
- Fail = total ≤ 4

---

## Get your API key

1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Create a free API key
3. Add to `.env`:

        GEMINI_API_KEY=your_key_here

---

## Built by

**Sisira Saru Abey**  
DevOps Engineer at Siemens Advanta → transitioning to AI/ML

This project was built from scratch during Week 1 of learning Python.  
No ML background. No formal AI training. Just a clear goal and daily commits.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/sisira-saru-abey-b918b6241)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/sisirasaruabey1996-stack)

---

## Roadmap

- [ ] Voice input (SpeechRecognition)
- [ ] Spaced repetition scheduler (SM-2 algorithm)
- [ ] ML curriculum track (Python → Deep Learning → System Design)
- [ ] Google readiness prediction chart (improvement over time)
- [ ] Deploy to Streamlit Cloud (public demo)

---

> *"I built a system to prepare for the interview.*  
> *Then I used the system to prepare for the interview.*  
> *That's the project."*
