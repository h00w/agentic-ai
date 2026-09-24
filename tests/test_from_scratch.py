import pytest

from agentic_ai.from_scratch import (
    Decision,
    Observation,
    StepBudgetExceeded,
    ToolCall,
    UnknownToolError,
    run_bounded_agent,
)


def test_direct_answer_stops_without_tool() -> None:
    result = run_bounded_agent(
        "Say hello",
        lambda _goal, _observations: Decision(final="hello"),
        {},
    )
    assert result.answer == "hello"
    assert result.steps == 1


def test_tool_observation_can_lead_to_final_answer() -> None:
    def decide(_goal: str, observations: tuple[Observation, ...]) -> Decision:
        if not observations:
            return Decision(tool_call=ToolCall("lookup", {"query": "release gate"}))
        return Decision(final=f"observed:{observations[-1].output}")

    result = run_bounded_agent(
        "Check the release gate",
        decide,
        {"lookup": lambda args: f"found:{args['query']}"},
        max_steps=3,
    )
    assert result.answer == "observed:found:release gate"
    assert result.steps == 2


def test_unknown_tool_fails_closed() -> None:
    with pytest.raises(UnknownToolError):
        run_bounded_agent(
            "Use a tool",
            lambda _goal, _observations: Decision(
                tool_call=ToolCall("not_registered", {})
            ),
            {},
        )


def test_step_budget_stops_runaway_loop() -> None:
    with pytest.raises(StepBudgetExceeded):
        run_bounded_agent(
            "Keep searching",
            lambda _goal, _observations: Decision(
                tool_call=ToolCall("search", {"query": "same"})
            ),
            {"search": lambda _args: "no terminal answer"},
            max_steps=2,
        )
