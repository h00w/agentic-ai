from agentic_ai.sandbox import validate_code_for_demo


def test_static_sandbox_gate_blocks_exec():
    allowed, _ = validate_code_for_demo("exec('print(1)')")
    assert not allowed


def test_static_sandbox_gate_allows_simple_math():
    allowed, _ = validate_code_for_demo("print(1 + 1)")
    assert allowed
