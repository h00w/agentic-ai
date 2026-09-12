# Agent Evaluation

Build evaluations around real tasks and risk. Golden datasets, trajectory checks, tool correctness, groundedness, safety, latency, cost and human review should be versioned with the system.

## Architecture

```mermaid
flowchart LR
  Dataset --> Runner --> Agent --> Trace
  Trace --> Metrics
  Agent --> Output --> Metrics
  Metrics --> Gate{Release gate}
  Gate -->|Pass| Deploy
  Gate -->|Fail| Fix
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
