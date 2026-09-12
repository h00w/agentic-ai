# Production Engineering

Production agents require service boundaries, state stores, queues, idempotency, timeouts, retries, circuit breakers, model routing, rate limits, cost budgets, deployment automation, health checks and rollback.

## Architecture

```mermaid
flowchart LR
  Client --> API --> Queue --> Worker[Agent worker]
  Worker --> ModelGW[Model gateway]
  Worker --> ToolGW[Tool gateway]
  Worker --> State[State store]
  Worker --> Eval[Evaluation]
  Worker --> Telemetry[Telemetry]
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
