# Retrieval-Augmented Generation

RAG should improve evidence quality rather than merely add context. Preserve authorization filtering, source provenance, chunk metadata, retrieval scores, citations and evaluation.

## Architecture

```mermaid
flowchart LR
  Docs --> Chunk --> Index[Vector / hybrid index]
  Query --> Retrieve --> Rerank --> Context --> Agent --> Answer
  Index --> Retrieve
  Answer --> Cite[Citations]
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
