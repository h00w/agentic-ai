# Enterprise Agentic AI Architecture

Centralize shared controls without forcing every business workflow into one agent framework. The platform should provide identity, policy, model routing, tool gateways, knowledge access, evaluation, telemetry, approvals and audit.

## Architecture

```mermaid
flowchart TD
  Channels --> AgentPlatform[Agent platform]
  AgentPlatform --> Identity
  AgentPlatform --> Policy
  AgentPlatform --> ModelGW[Model gateway]
  AgentPlatform --> ToolGW[Tool gateway]
  AgentPlatform --> Knowledge[Knowledge platform]
  AgentPlatform --> Eval[Evaluation platform]
  AgentPlatform --> HITL[Human approval]
  AgentPlatform --> Obs[Observability / audit]
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
