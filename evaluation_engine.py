import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

EVAL_PROMPT = """
You are a Google L5 interviewer. Be strict.

Question: {question}
Key insight the candidate must find: {key_insight}
Optimal time complexity: {optimal_tc}
Optimal space complexity: {optimal_sc}
Common mistakes: {common_mistakes}

Candidate's answer: {user_answer}

Return ONLY this JSON, no other text:
{{
  "correctness": <0-3>,
  "complexity_awareness": <0-2>,
  "key_insight_found": <0-2>,
  "clarity": <0-1>,
  "edge_cases": <0-2>,
  "verdict": "<pass|borderline|fail>",
  "feedback": "<2 sentences max>",
  "missed": ["<gap1>", "<gap2>"]
}}
"""

def evaluate_answer(question, user_answer):
    prompt = EVAL_PROMPT.format(
        question=question["title"],
        key_insight=question["key_insight"],
        optimal_tc=question["optimal_tc"],
        optimal_sc=question["optimal_sc"],
        common_mistakes=", ".join(question["common_mistakes"]),
        user_answer=user_answer
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text