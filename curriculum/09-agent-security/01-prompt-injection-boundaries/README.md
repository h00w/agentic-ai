# Lesson 09.01 — Prompt Injection and Trust Boundaries

## UNDERSTAND

Model prompt injection as a trust-boundary and confused-deputy problem, not a wording problem.

## BUILD

Map untrusted inputs from users, web, retrieval, memory, MCP, files and other agents to the privileged actions they could influence.

## BREAK

Place a malicious instruction in retrieved evidence or a tool description and verify it cannot directly authorize an action.

## MEASURE

Injection fixtures do not alter protected instructions, permissions or approval state.

## SECURE

Use least privilege, content/data separation, deterministic policy gates and approval for high-impact actions.

## SHIP

Complete `artifacts/worksheet.md` and retain the artifact manifest as reviewable evidence for this lesson.

## OPERATE

Monitor injection detections, denied actions, suspicious memory entries and anomalous tool requests.

## GOVERN

Retain red-team fixtures as regression tests and assign owners to material trust boundaries.
