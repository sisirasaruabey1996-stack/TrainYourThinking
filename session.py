# session.py
from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class QuestionResult:
    question_id: str
    attempts: int
    final_score: float
    verdict: str
    missed: list[str]

@dataclass
class Session:
    session_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    questions: list[str] = field(default_factory=list)
    current_index: int = 0
    results: list[QuestionResult] = field(default_factory=list)
    difficulty_track: str = "easy"
    mode: str = "interview"
    started_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def current_question_id(self) -> str:
        return self.questions[self.current_index]

    def is_complete(self) -> bool:
        return self.current_index >= len(self.questions)

    def advance(self):
        self.current_index += 1

    def add_result(self, result: QuestionResult):
        self.results.append(result)

    def session_score(self) -> float:
        if not self.results:
            return 0.0

        # dynamic weights (later questions matter more)
        weights = [i + 1 for i in range(len(self.results))]
        total_weight = sum(weights)

        total = sum(
            r.final_score * w
            for r, w in zip(self.results, weights)
        )

        return round(total / total_weight, 1)