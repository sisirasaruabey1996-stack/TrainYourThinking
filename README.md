# TrainYourThinking 🧠
> An AI-powered, full-stack interview preparation system built to crack 
> MAANG-level interviews — designed, built, and used by a DevOps engineer 
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