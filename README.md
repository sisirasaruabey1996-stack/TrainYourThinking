# TrainYourThinking 🧠
> AI-powered DSA coach built to crack Google interviews.

## What it does
- Socratic DSA coaching (never gives direct answers)
- Auto-detects topics you struggle with
- Tracks progress across sessions
- Calculates Google interview readiness score (0–100)

## Tech stack
- Python 3.14
- Gemini 2.5 Flash API
- Local JSON + session file storage

## Commands
| Command | Action |
|---|---|
| `topic: binary search` | Set current topic |
| `struggled: arrays` | Manual struggle log |
| `mastered: arrays` | Manual mastery log |
| `weaknesses` | Show weak areas |
| `progress` | Show studied topics |
| `score` | Show readiness score |
| `quit` | Exit |

## Readiness Score
Calculated from struggle rate across all topics.
Updates automatically after every session.

## Run locally
```bash
git clone https://github.com/sisirasaruabey1996-stack/TrainYourThinking
cd TrainYourThinking
pip install -r requirements.txt
cp .env.example .env  # add your Gemini API key
python main.py
```

## Built by
Sisira Saru Abey — DevOps Engineer transitioning to AI/ML