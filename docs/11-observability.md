# Observability

Record traces that answer what the agent intended, which policy decision applied, which tool was called, what evidence returned, what it cost, how long it took, and why the run stopped.

## Architecture

```mermaid
flowchart LR
  Agent --> Trace
  Tools --> Trace
  Policy --> Trace
  Eval --> Trace
  Trace --> OTel[OpenTelemetry]
  OTel --> Metrics
  OTel --> Logs
  OTel --> Traces
  Metrics --> Alerts
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
