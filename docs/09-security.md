# Agent Security

Threat-model the complete action path: prompt/input, model, retrieval, tools, network, sandbox, secrets, identity, approvals, output and audit. Assume model-generated content is untrusted.

## Architecture

```mermaid
flowchart TD
  Input --> Validate --> Agent
  Agent --> Policy
  Policy -->|Allow| Gateway
  Policy -->|Approve| Human
  Policy -->|Deny| Block
  Human --> Gateway
  Gateway --> Sandbox
  Sandbox --> Tool
  Tool --> OutputCheck[Output validation]
  OutputCheck --> Agent
  Policy --> Audit
  Gateway --> Audit
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
