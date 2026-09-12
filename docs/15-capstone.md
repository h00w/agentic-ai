# Capstone

The Responsible Enterprise Research Agent demonstrates the full lifecycle: planning, policy, tools, knowledge/RAG, memory, evaluation, approval, final report, cost controls, recovery and audit.

## Architecture

```mermaid
flowchart TD
  User --> Controller --> Planner --> Policy --> Gateway --> ResearchTools[Research tools]
  ResearchTools --> Knowledge[Knowledge / RAG] --> Evaluation --> Approval{Human approval}
  Approval --> Report[Final report] --> Audit[Audit / observability]
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
