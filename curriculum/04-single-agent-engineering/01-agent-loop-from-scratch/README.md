# Lesson 04.01 — Agent Loop From Scratch

## UNDERSTAND

An agent loop receives a goal, obtains a decision, optionally executes an allowed tool, observes the result and stops at a terminal answer or deterministic stopping condition. The host—not the model—owns tool registration and step budgets.

## BUILD

Inspect `src/agentic_ai/from_scratch.py` and run `pytest tests/test_from_scratch.py`.

## BREAK

Unknown tool requests fail closed and repeated calls stop at the host-owned step budget.

## MEASURE

Acceptance requires direct completion, valid tool observation, unknown-tool blocking and bounded termination.

## SECURE

A decision function may propose actions but cannot create new tool authority. Production extensions should add argument validation, policy, approval and timeout controls.

## SHIP

The artifact manifest points to the implementation and tests as reusable evidence.

## OPERATE

Track step count, tool calls, unknown-tool attempts, terminal reason, latency and cost.

## GOVERN

Changes to tool authority, stopping logic and budgets require review and regression evidence.
