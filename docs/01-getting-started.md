# Getting Started

Start with a learning pathway, install the package locally, run the tests, then execute examples in numerical order. Core learning does not require an API key.

## Architecture

```mermaid
flowchart LR
  Path[Choose pathway] --> Install[Install]
  Install --> Tests[Run tests]
  Tests --> Examples[Run examples]
  Examples --> Modules[Study modules]
  Modules --> Projects[Build projects]
  Projects --> Capstone[Capstone]
```

## Professional practice

Define ownership, interfaces, failure behavior, security boundaries, evidence, SLOs, cost limits, release criteria and rollback before increasing autonomy. Prefer small composable controls over one opaque “agent framework” abstraction.

## Review questions

- What is deterministic and what is probabilistic?
- Which action has the highest blast radius?
- What evidence proves the design works?
- Which telemetry detects silent failure?
- What is the safe fallback?
