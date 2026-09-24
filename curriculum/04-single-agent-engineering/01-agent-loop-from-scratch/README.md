# Lesson 04.01 — Agent Loop From Scratch

Implement the smallest useful bounded agent loop before introducing an orchestration framework.

## BUILD

Inspect `src/agentic_ai/from_scratch.py` and run `pytest tests/test_from_scratch.py`.

## BREAK

Unknown tool requests fail closed and repeated calls stop at the host-owned step budget.

## MEASURE

Acceptance requires direct completion, valid tool observation, unknown-tool blocking and bounded termination.

## SECURE

A decision function may propose actions but cannot create new tool authority.

## SHIP

The artifact manifest points to the implementation and tests.

## OPERATE

Track step count, tool calls, terminal reason, latency and cost.

## GOVERN

Changes to tool authority and budgets require review and regression evidence.
