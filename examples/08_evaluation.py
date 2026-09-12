from dataclasses import asdict

from agentic_ai.evaluation import evaluate_result

result = evaluate_result(
    expected_terms=["policy", "tools"], answer="Use policy gates around tools.", token_usage=42
)
print(asdict(result))
