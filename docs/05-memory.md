# Memory

Separate working state, conversation memory, durable task memory and user/profile memory. Define retention, ownership, privacy, update rules and deletion semantics explicitly.

## Architecture

```mermaid
flowchart TD
  Agent --> Working[Working state]
  Agent --> Conversation[Conversation memory]
  Agent --> Durable[Durable memory]
  Durable --> Policy[Retention & access policy]
  Conversation --> Policy
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
