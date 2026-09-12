from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from .models import AgentState, Observation, RiskLevel
from .observability import TraceRecorder
from .policy import PolicyDecision, PolicyEngine
from .tools import ToolRegistry


@dataclass(frozen=True, slots=True)
class AgentResult:
    answer: str
    state: AgentState
    elapsed_ms: float
    policy_decisions: tuple[str, ...]


class AgentController:
    """Deterministic teaching agent with explicit planning and policy gates."""

    def __init__(
        self,
        tools: ToolRegistry,
        policy: PolicyEngine,
        max_steps: int = 6,
        trace: TraceRecorder | None = None,
    ) -> None:
        if max_steps < 1:
            raise ValueError("max_steps must be >= 1")
        self.tools = tools
        self.policy = policy
        self.max_steps = max_steps
        self.trace = trace or TraceRecorder()

    def run(self, goal: str) -> AgentResult:
        started = perf_counter()
        state = AgentState(goal=goal)
        decisions: list[str] = []
        self.trace.record("goal", goal)
        tool_name = self._select_tool(goal)
        if tool_name is None:
            answer = f"No tool required. Goal acknowledged: {goal}"
            state.completed = True
            self.trace.record("complete", "direct response")
            return AgentResult(answer, state, (perf_counter() - started) * 1000, tuple(decisions))
        while not state.completed and state.steps < self.max_steps:
            state.steps += 1
            decision = self.policy.evaluate(tool_name, RiskLevel.LOW)
            decisions.append(f"{tool_name}:{decision.value}")
            self.trace.record("policy", decisions[-1])
            if decision is PolicyDecision.DENY:
                return AgentResult(
                    f"Action blocked by policy: {tool_name}",
                    state,
                    (perf_counter() - started) * 1000,
                    tuple(decisions),
                )
            if decision is PolicyDecision.REQUIRE_APPROVAL:
                return AgentResult(
                    f"Human approval required before tool execution: {tool_name}",
                    state,
                    (perf_counter() - started) * 1000,
                    tuple(decisions),
                )
            output = self.tools.execute(tool_name, {"query": goal})
            state.observations.append(Observation(tool=tool_name, success=True, output=output))
            self.trace.record("tool", f"{tool_name} -> {output}")
            state.completed = True
        answer = state.observations[-1].output if state.observations else "No result produced."
        self.trace.record("complete", answer)
        return AgentResult(answer, state, (perf_counter() - started) * 1000, tuple(decisions))

    def _select_tool(self, goal: str) -> str | None:
        lowered = goal.lower()
        names = self.tools.names()
        if ("calculate" in lowered or any(ch.isdigit() for ch in goal)) and "calculator" in names:
            return "calculator"
        if (
            any(word in lowered for word in ("search", "research", "find", "evidence"))
            and "search" in names
        ):
            return "search"
        return names[0] if names else None
