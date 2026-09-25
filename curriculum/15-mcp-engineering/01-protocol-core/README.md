# Lesson 15.01 — MCP Protocol Core and Tool Contract

## UNDERSTAND

MCP capability discovery describes what a server can expose; it does not decide what a client is authorized to execute.

## BUILD

Inspect `artifacts/tool-contract.example.json` and identify schema, side effects, requested scope, trust level and reliability metadata.

## BREAK

Review schema drift, malicious descriptions, silent side-effect changes and out-of-scope capabilities.

## MEASURE

Conformance checks should validate schema, stable identity, declared side effects, timeout behavior and authorization metadata.

## SECURE

Treat external MCP descriptions, resources and outputs as untrusted data. Protocol discovery must never become privilege discovery.

## SHIP

Retain the tool contract and artifact manifest as reusable protocol evidence.

## OPERATE

Track server availability, capability changes, timeouts, retries, policy denials and approval waits.

## GOVERN

Review server admission, scope expansion, schema incompatibility and side-effect changes before production use.
