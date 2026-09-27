from agentic_ai.evaluation import evaluate_result


def test_reference_evaluator():
    result = evaluate_result(
        expected_terms=["policy", "tool"], answer="A policy controls each tool."
    )
    assert result.task_success == 1.0
    assert result.safety == 1.0


def test_expected_term_does_not_match_inside_another_word():
    assert evaluate_result(expected_terms=["safe"], answer="unsafe").task_success == 0
    assert evaluate_result(expected_terms=["safe"], answer="This is safe.").task_success == 1
