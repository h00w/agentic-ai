# Architecture Diagram Index

## 1. Agent loop
```mermaid
flowchart LR
Goal --> Plan --> Act --> Observe --> Evaluate --> Done{Done?}
Done -->|No| Plan
```

## 2. Tool calling
```mermaid
flowchart LR
Agent --> Schema --> Policy --> Gateway --> Tool --> Validate --> Agent
```

## 3. RAG
```mermaid
flowchart LR
Sources --> Index --> Retrieve --> Rerank --> Context --> Agent --> CitedAnswer
```

## 4. Memory
```mermaid
flowchart TD
Agent --> WorkingState
Agent --> ShortTerm
Agent --> LongTerm
LongTerm --> RetentionPolicy
```

## 5. Multi-agent
```mermaid
flowchart TD
Supervisor --> Researcher
Supervisor --> Developer
Supervisor --> Tester
Supervisor --> Reviewer
```

## 6. Evaluation
```mermaid
flowchart LR
Dataset --> Agent --> Outputs --> Metrics --> ReleaseGate
Agent --> Trajectory --> Metrics
```

## 7. Security
```mermaid
flowchart LR
Input --> Validate --> Agent --> Policy --> ToolGateway --> Sandbox --> Tool --> Audit
```

## 8. Production
```mermaid
flowchart LR
Client --> API --> Queue --> Worker --> ModelGateway
Worker --> ToolGateway
Worker --> StateStore
Worker --> Telemetry
```

## 9. Observability
```mermaid
flowchart LR
Agent --> OTel
Tools --> OTel
Policy --> OTel
OTel --> Traces
OTel --> Metrics
OTel --> Logs
```

## 10. Enterprise
```mermaid
flowchart TD
Channels --> AgentPlatform
AgentPlatform --> Identity
AgentPlatform --> Policy
AgentPlatform --> ModelGateway
AgentPlatform --> ToolGateway
AgentPlatform --> Knowledge
AgentPlatform --> Evaluation
AgentPlatform --> Audit
```

## 11. Capstone
```mermaid
flowchart TD
User --> Controller --> Planner --> Policy --> ToolGateway --> ResearchTools --> Knowledge --> Evaluation --> Approval --> Report --> Audit
```

## 12. Learning pathway
```mermaid
flowchart LR
Beginner --> Python --> Foundations --> Agent --> Tools --> Memory --> RAG --> MultiAgent --> Evaluation --> Security --> Production --> Observability --> Governance --> Enterprise --> Leadership --> Capstone
```
