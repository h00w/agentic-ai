# Academy Lesson Template

Deep lessons follow **UNDERSTAND → BUILD → BREAK → MEASURE → SECURE → SHIP → OPERATE → GOVERN**.

Create a sibling `lesson.json` with `id`, `title`, `module`, `level`, `duration_minutes`, `prerequisites`, `outcomes`, and `artifacts`.

## UNDERSTAND
Define the engineering problem, system boundary, deterministic controls and why probabilistic behavior is justified.

## BUILD
Implement the smallest useful mechanism before introducing a high-level framework.

## BREAK
Demonstrate a controlled failure in a system you own or are authorized to test.

## MEASURE
Define success and failure criteria and reuse Academy benchmark cases where useful.

## SECURE
Name trust boundaries, permissions, validation, approval and fail-closed behavior.

## SHIP
Create an artifact manifest conforming to `artifact-schema.json`.

## OPERATE
Specify traces, metrics, budgets, timeout/retry behavior and incident signals.

## GOVERN
State ownership, review requirements, retained evidence and release blockers.

A lesson is complete only when the mechanism is explainable, testable, failure-aware and leaves reusable engineering evidence.
