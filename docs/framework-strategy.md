# Framework Strategy

Use a framework when durable graph/state orchestration, checkpointing, human interrupts, or shared team conventions reduce real engineering work. Do not use one when a few deterministic steps are sufficient, when the abstraction hides critical state/policy/retry behavior, or when dependency weight exceeds the orchestration benefit.

Prefer a deterministic workflow when the sequence is stable, risk is high, inputs are structured, acceptance criteria are clear, and adaptive planning adds little value.

Framework mappings: LangGraph for graph/state orchestration; CrewAI for role-oriented team patterns; Microsoft Agent Framework / AutoGen ecosystem for enterprise and research multi-agent/tool patterns. `src/agentic_ai/` remains framework-neutral.
