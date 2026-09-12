# Agentic AI Glossary

120 terms used throughout the academy.

## Abstention
System choice to decline or escalate when confidence/evidence is insufficient.

## Action
A tool invocation or other externally observable operation selected by an agent.

## Action limit
Maximum number of actions an agent may take during a run.

## Agent
A system that pursues goals through iterative decisions, state and actions under explicit controls.

## Agent controller
Deterministic orchestration logic that manages state, policy, tools, budgets and stopping.

## Agent loop
Repeated plan/action/observation/evaluation cycle that continues until a stop condition.

## Agent registry
Catalog of approved agents, owners, capabilities, versions and policy metadata.

## Agent trajectory
Ordered sequence of plans, tool calls, observations and decisions in one run.

## Alignment
Degree to which system behavior matches intended goals, constraints and values.

## Approval gate
Control requiring an authorized human or service to approve an action before execution.

## Async I/O
Concurrent waiting model used to handle multiple network/tool operations efficiently.

## Audit log
Tamper-resistant record of security-relevant and operationally relevant events.

## Authentication
Verification of identity.

## Authorization
Decision about which authenticated identity may perform which action on which resource.

## Autonomy
Extent to which an agent can select and execute actions without human intervention.

## Budget
Explicit bound on steps, time, tokens, cost, retries or privileged actions.

## Canary release
Limited rollout used to detect regressions before broad deployment.

## Change control
Process for reviewing and approving modifications to a production system.

## Chunk
Retrieval unit created by segmenting a source document.

## Circuit breaker
Reliability pattern that stops calls to a failing dependency for a period.

## Citation
Reference connecting an answer claim to source evidence.

## Conflict resolution
Mechanism for reconciling contradictory agent outputs or recommendations.

## Consensus
Multi-agent decision approach aggregating independent proposals or votes.

## Context manager
Python construct that safely acquires and releases resources.

## Context window
Maximum model input/output token region available for a request.

## Cost per successful task
Total run cost divided by tasks meeting the success threshold.

## Crew
Set of specialized agents coordinating around shared work.

## Data lineage
Record of where data came from and how it was transformed.

## Data residency
Requirement governing geographic storage/processing location of data.

## Dataclass
Python construct for concise typed data containers.

## Default deny
Security posture where an action is prohibited unless explicitly allowed.

## Defense in depth
Use of multiple independent security controls so one failure does not expose the system.

## Delegation
Assignment of a subtask from one agent/manager to another agent or worker.

## Deterministic workflow
Predefined control flow whose decision sequence is specified by code/rules.

## Drift
Meaningful change in inputs, behavior, model quality or environment over time.

## Embedding
Vector representation used to compare semantic similarity.

## Evaluation
Systematic measurement of task quality, safety, reliability, latency and cost.

## Evaluation drift
Change in measured performance or score distributions over time.

## Excessive agency
Risk created when an agent has broader permissions or autonomy than necessary.

## Fallback
Alternative behavior used when the preferred model, tool or dependency fails.

## Function calling
Model capability to produce structured arguments for an application-defined tool.

## Golden dataset
Versioned set of representative tasks and expected outcomes used for evaluation.

## Groundedness
Degree to which claims are supported by provided or retrieved evidence.

## Guardrail
Control that constrains, validates, detects or blocks unsafe/invalid behavior.

## Hallucination
Model output that presents unsupported or incorrect information as if reliable.

## Human evaluation
Assessment performed by qualified reviewers using defined rubrics.

## Human in the loop
Workflow where human review or decision is part of agent execution.

## Idempotency
Property that repeated execution produces no additional unintended state change.

## Indirect prompt injection
Malicious instructions embedded in external content consumed by an agent.

## Inference
Execution of a trained model to produce output from input.

## Input validation
Checking inputs against expected type, format, range, authorization and policy.

## Knowledge graph
Graph representation of entities and relationships used for structured knowledge reasoning/retrieval.

## LLM
Large language model used to generate or transform language and structured outputs.

## Least privilege
Granting only the minimum permissions necessary for the task.

## Long-term memory
Persisted information available across runs or sessions under retention rules.

## MCP
Model Context Protocol, a protocol for exposing tools and context to AI applications.

## Memory
State retained and reused by an agent within or across runs.

## Model gateway
Central service for routing, policy, credentials, telemetry and model/provider access.

## Model routing
Selection of a model based on task, quality, latency, policy or cost needs.

## Model selection
Choice of model based on capability, latency, cost, safety, context and governance needs.

## Multi-agent system
System of multiple agent roles coordinating to complete a task.

## Network restriction
Sandbox or service rule limiting outbound/inbound connectivity.

## Observability
Ability to understand internal system behavior from traces, metrics and logs.

## Observation
Information returned from the environment or tool after an action.

## OpenTelemetry
Vendor-neutral telemetry standard for traces, metrics and logs.

## Orchestration
Coordination of models, tools, state, retries, policies and workflows.

## Output validation
Checking generated/tool output before it is trusted, stored or acted upon.

## PII
Personally identifiable information requiring privacy-aware processing and access control.

## Planner
Component that decomposes a goal into steps or selects the next action.

## Policy engine
Deterministic component that decides whether an action is allowed, denied or needs approval.

## Privilege escalation
Acquisition or use of permissions beyond those intended for an identity or task.

## Prompt
Instruction and context supplied to a model.

## Prompt injection
Adversarial instruction intended to override or redirect system behavior.

## Pydantic
Python library for typed data validation and structured models.

## RAG
Retrieval-Augmented Generation: retrieving external evidence to ground generation.

## Rate limit
Bound on requests/actions per unit of time.

## ReAct
Agent pattern combining reasoning-oriented planning with actions and observations.

## Red teaming
Adversarial testing intended to uncover abuse paths, failure modes and control gaps.

## Regression test
Test ensuring previously correct behavior remains correct after change.

## Release gate
Evidence-based decision point that must pass before deployment or increased autonomy.

## Reranking
Second-stage ordering of retrieved items by relevance or quality.

## Resilience
Ability to continue or degrade safely under failures.

## Resource limit
Bound on CPU, memory, storage, network, time or concurrency.

## Retry
Reattempt of a failed operation under bounded rules.

## Risk appetite
Amount and type of risk an organization is willing to accept.

## Risk register
Structured record of risks, controls, owners, evidence and residual risk.

## Rollback
Reversion to a prior safe version or configuration.

## SLO
Service level objective defining an expected reliability/performance target.

## Safety evaluation
Tests designed to identify harmful, policy-violating or unsafe behavior.

## Sandbox
Isolated execution environment that limits effects of untrusted code or tools.

## Secret
Credential or sensitive key that must not be exposed in code, prompts or logs.

## Semantic search
Retrieval using vector meaning similarity rather than only lexical match.

## Short-term memory
State retained within a current session or task.

## State
Data representing current task context and progress.

## State store
Persistent system used to save agent/workflow state.

## Stopping condition
Rule that terminates an agent loop safely.

## Structured output
Model output constrained to a schema usable by deterministic code.

## Supervisor agent
Agent or controller that delegates work and reviews subordinate outputs.

## System instruction
High-priority behavioral instruction supplied by the application/system layer.

## TCO
Total cost of ownership across models, infrastructure, integration, operations, governance and people.

## Task success
Measure of whether the user/business task met predefined acceptance criteria.

## Temperature
Model sampling parameter affecting output variability.

## Threat model
Structured analysis of assets, adversaries, attack paths, controls and residual risk.

## Timeout
Maximum allowed duration for an operation before it is terminated or treated as failed.

## Token
Discrete model text unit used for context and cost accounting.

## Token budget
Maximum token consumption allowed for a run or workflow.

## Tool
Application-defined capability an agent can invoke.

## Tool accuracy
Fraction of tool choices/calls that are correct and properly parameterized.

## Tool discovery
Mechanism for enumerating available tools and their capabilities under policy.

## Tool gateway
Controlled service boundary mediating agent access to external tools/APIs.

## Tool schema
Machine-readable specification of tool name, arguments and constraints.

## Tool use
Agent selection and invocation of external functions or services.

## Trace
Structured record of a request's execution path across components.

## Trajectory evaluation
Assessment of the sequence of agent decisions and actions, not only final output.

## Transparency
Ability to communicate system purpose, limitations, evidence and decision processes appropriately.

## Untrusted input
Data that must be validated before use because its integrity or intent is not guaranteed.

## Vector database
Store optimized for similarity search over vector embeddings.

## Verification
Process of checking whether an output/action satisfies requirements or evidence.

## Versioning
Tracking controlled revisions of prompts, models, tools, datasets, policies and code.

## Workflow
Defined sequence of steps transforming inputs into outputs.
