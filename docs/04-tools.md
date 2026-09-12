# Tools, APIs and MCP

Treat every tool as a privileged capability. Tools need explicit schemas, authentication, authorization, policy, validation, budgets, timeouts, error semantics and auditability.

## Architecture

```mermaid
flowchart LR
  Agent --> Schema[Tool schema] --> Policy[Policy gate] --> Gateway[Tool gateway] --> API[External API]
  API --> Validate[Output validation] --> Agent
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
