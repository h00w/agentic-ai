# Lesson 02.01 — Typed Tool Contracts in Python

## UNDERSTAND

Define tool inputs, outputs, errors and side effects before connecting a model.

## BUILD

Design a typed contract for a read-only tool and a side-effecting tool, including validation and error semantics.

## BREAK

Try malformed, missing and extra arguments and define the fail-closed result before execution.

## MEASURE

All accepted inputs satisfy the declared contract; invalid inputs never reach the executor.

## SECURE

Schemas validate structure but do not grant authority. Keep permission and approval checks outside the model.

## SHIP

Complete `artifacts/worksheet.md` and retain the artifact manifest as reviewable evidence for this lesson.

## OPERATE

Track validation failures, tool latency, error classes and schema-version mismatches.

## GOVERN

Version breaking contract changes and require review when side-effect classification or permissions expand.
