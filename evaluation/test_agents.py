from agentic_ai.evaluation import evaluate_result


def test_reference_evaluator():
    result = evaluate_result(
        expected_terms=["policy", "tool"], answer="A policy controls each tool."
    )
    assert result.task_success == 1.0
    assert result.safety == 1.0
