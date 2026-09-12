# Multi-Agent Systems

Use multi-agent systems only when specialization, parallel work, independent verification, or governance separation outweigh coordination overhead and new failure modes.

## Architecture

```mermaid
flowchart TD
  Supervisor --> Researcher
  Supervisor --> Developer
  Supervisor --> Tester
  Supervisor --> Reviewer
  Researcher --> Shared[Shared state]
  Developer --> Shared
  Tester --> Shared
  Reviewer --> Shared
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
