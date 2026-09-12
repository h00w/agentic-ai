# RAG Knowledge Agent

## Learning objectives
- convert a business goal into explicit agent state and control flow
- define tool contracts and permissions
- add tests, evaluation criteria, failure handling and observability
- document security assumptions and extension points

## Architecture
```mermaid
flowchart LR
    U[User] --> C[Controller]
    C --> P[Plan]
    P --> G[Policy]
    G --> T[Tool Gateway]
    T --> S[State / Knowledge]
    S --> E[Evaluation]
    E --> O[Output]
    O --> A[Audit]
```

## Requirements
Python 3.12+. Core exercises use the local framework-neutral package and deterministic tools. External model APIs are optional.

## Installation
```bash
pip install -e .[dev]
pytest
```

## Source code
Reuse and extend `src/agentic_ai/` plus the closest numbered example under `examples/`.

## Tests
Write at least one happy-path test, one policy-denial test, one malformed-input test, and one recovery/timeout test where relevant.

## Expected output
A reproducible result with visible plan/control decisions, bounded tool use, evaluation evidence and a trace.

## Failure modes
Wrong tool selection, unavailable tool, malformed arguments, stale retrieval, policy denial, timeout, partial execution, runaway retry, excessive cost, unsafe output and missing evidence.

## Security considerations
Never expose credentials in prompts or source control. Apply least privilege, validation, policy gates, approval for high-impact actions, resource budgets, network restrictions and audit logging. Generated code belongs in an isolated sandbox, not the host.

## Extension exercises
1. Add strict-schema retrieval filters.
2. Create a ten-case golden dataset.
3. Add groundedness and citation checks.
4. Add authorization-aware retrieval.
5. Write a production-readiness review.
