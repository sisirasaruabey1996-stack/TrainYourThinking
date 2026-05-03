from interview_engine import load_questions
from evaluation_engine import evaluate_answer
from session import Session, QuestionResult
from knowledge_model import update, increment_sessions
import json
import random

def run_interview():

    print("\n=== Mock Interview Session ===\n")

    all_questions = load_questions()
    selected = random.sample(all_questions, 3)

    session = Session(
        questions=[q["id"] for q in selected]
    )

    for q in selected:

        print(f"\n--- Question {session.current_index + 1} ---")
        print(f"{q['title']} ({q['difficulty']})")
        print(f"{q['link']}\n")

        attempts = 0

        while True:
            user_answer = input("Your answer (type 'quit' to exit): ")

            if user_answer.lower() == "quit":
                return

            attempts += 1

            print("\nEvaluating...\n")
            raw_result = evaluate_answer(q, user_answer)

            cleaned = raw_result.replace("```json", "").replace("```", "").strip()

            try:
                result = json.loads(cleaned)
            except:
                print("Parse error. Raw output:\n", raw_result)
                continue

            score = (
                result["correctness"] +
                result["complexity_awareness"] +
                result["key_insight_found"] +
                result["clarity"] +
                result["edge_cases"]
            )

            print(f"\nScore: {score}/10")
            print(f"Verdict: {result['verdict']}")
            print(f"Feedback: {result['feedback']}\n")

            if result["verdict"] == "pass":

                # ✅ SAVE RESULT IN SESSION
                session.add_result(
                    QuestionResult(
                        question_id=q["id"],
                        attempts=attempts,
                        final_score=score,
                        verdict="pass",
                        missed=result["missed"]
                    )
                )

                # 🔥 UPDATE KNOWLEDGE MODEL
                update(
                    topic=q["topic"],
                    score=score,
                    difficulty=q["difficulty"]
                )

                print("✅ Moving to next question...\n")
                session.advance()
                break

            else:
                print("Try again. Improve your answer.\n")

    # 🔥 SESSION COMPLETE
    print("\n=== Interview Complete ===")
    print(f"Session ID: {session.session_id}")

    final_score = session.session_score()

    print(f"Final Score: {final_score}/10")

    if final_score >= 7:
        print("Verdict: READY")
    elif final_score >= 5:
        print("Verdict: BORDERLINE")
    else:
        print("Verdict: NOT READY")

    # 🔥 INCREMENT SESSION COUNT
    increment_sessions()

    print("\nDetailed Results:")
    for r in session.results:
        print(f"{r.question_id} → {r.final_score}/10 in {r.attempts} attempts")


if __name__ == "__main__":
    run_interview()