# Leadership and Strategy

Leaders should build a portfolio of bounded opportunities, not a single “AI agent strategy.” Prioritize by value, feasibility, risk, data readiness, integration effort, operating cost and organizational change.

## Architecture

```mermaid
flowchart LR
  Opportunities --> Score[Value / feasibility / risk] --> Portfolio --> Pilot --> Evidence --> Scale
  Portfolio --> Buy[Build vs buy]
  Portfolio --> TCO[TCO]
  Portfolio --> Gov[Governance]
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
