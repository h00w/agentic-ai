# Governance and Scaling

Governance establishes decision rights, ownership, risk classification, human oversight, release gates, audit requirements, incident processes, change control and retirement criteria.

## Architecture

```mermaid
flowchart LR
  Idea --> Risk[Risk classification] --> Owner[Accountable owner] --> Eval[Evidence]
  Eval --> Gate{Deployment gate}
  Gate --> Pilot --> Monitor --> Scale
  Monitor --> Incident[Incident / rollback]
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
