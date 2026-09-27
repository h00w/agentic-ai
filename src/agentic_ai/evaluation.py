from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True, slots=True)
class EvaluationResult:
    task_success: float
    correctness: float
    groundedness: float
    tool_accuracy: float
    safety: float
    latency_ms: float
    token_usage: int
    estimated_cost_usd: float


def evaluate_result(
    *,
    expected_terms: list[str],
    answer: str,
    latency_ms: float = 0.0,
    tool_accuracy: float = 1.0,
    safety: float = 1.0,
    token_usage: int = 0,
    estimated_cost_usd: float = 0.0,
) -> EvaluationResult:
    expected = [term.casefold() for term in expected_terms]
    text = answer.casefold()
    # Whole terms prevent a required answer such as "safe" matching "unsafe".
    correctness = (
        1.0
        if not expected
        else sum(
            bool(re.search(r"(?<!\w)" + re.escape(term) + r"(?!\w)", text)) for term in expected
        )
        / len(expected)
    )
    return EvaluationResult(
        task_success=1.0 if correctness >= 0.8 else 0.0,
        correctness=correctness,
        groundedness=correctness,
        tool_accuracy=tool_accuracy,
        safety=safety,
        latency_ms=latency_ms,
        token_usage=token_usage,
        estimated_cost_usd=estimated_cost_usd,
    )
