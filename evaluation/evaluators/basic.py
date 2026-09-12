from agentic_ai.evaluation import evaluate_result


def keyword_evaluator(answer: str, expected_terms: list[str]):
    return evaluate_result(expected_terms=expected_terms, answer=answer)
