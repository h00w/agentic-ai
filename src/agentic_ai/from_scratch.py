from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass

Tool = Callable[[dict[str, str]], str]


class StepBudgetExceeded(RuntimeError):
    """Raised when an agent cannot reach a terminal answer within its step budget."""


class UnknownToolError(RuntimeError):
    """Raised when a decision requests a tool outside the explicit registry."""


@dataclass(frozen=True, slots=True)
class ToolCall:
    name: str
    arguments: dict[str, str]


@dataclass(frozen=True, slots=True)
class Decision:
    final: str | None = None
    tool_call: ToolCall | None = None

    def __post_init__(self) -> None:
        choices = int(self.final is not None) + int(self.tool_call is not None)
        if choices != 1:
            raise ValueError("Decision must contain exactly one of final or tool_call")


@dataclass(frozen=True, slots=True)
class Observation:
    tool: str
    output: str


@dataclass(frozen=True, slots=True)
class AgentRun:
    answer: str
    steps: int
    observations: tuple[Observation, ...]
    trace: tuple[str, ...]


type Decide = Callable[[str, tuple[Observation, ...]], Decision]


def run_bounded_agent(
    goal: str,
    decide: Decide,
    tools: Mapping[str, Tool],
    *,
    max_steps: int = 4,
) -> AgentRun:
    """Run the smallest useful framework-neutral agent loop."""
    if max_steps < 1:
        raise ValueError("max_steps must be >= 1")

    observations: list[Observation] = []
    trace: list[str] = [f"goal:{goal}"]
    for step in range(1, max_steps + 1):
        decision = decide(goal, tuple(observations))
        if decision.final is not None:
            trace.append(f"step:{step}:final")
            return AgentRun(
                answer=decision.final,
                steps=step,
                observations=tuple(observations),
                trace=tuple(trace),
            )
        call = decision.tool_call
        if call is None:
            raise RuntimeError("Decision invariant violated")
        tool = tools.get(call.name)
        if tool is None:
            raise UnknownToolError(call.name)
        trace.append(f"step:{step}:tool:{call.name}")
        observations.append(Observation(tool=call.name, output=tool(dict(call.arguments))))

    raise StepBudgetExceeded("Agent stopped after reaching max_steps")
