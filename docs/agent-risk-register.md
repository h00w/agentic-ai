# Agent Risk Register

Use this register to identify, score, own, mitigate and review risks before increasing agent autonomy or production scope. Adapt the examples to the actual business process, data classification and regulatory environment.

## Risk scoring

Use a simple **Likelihood × Impact** score from 1–5 for each dimension. Scores of 15–25 should normally block production promotion until the residual risk is explicitly accepted by an accountable owner.

| ID | Risk | Example cause | Potential impact | Baseline controls | Evidence to collect | Owner | Residual target |
|---|---|---|---|---|---|---|---|
| R-01 | Direct prompt injection | User asks the agent to ignore policy or reveal protected instructions | Unauthorized behavior or data disclosure | system policy, input classification, tool allow-list, output validation | injection test suite and blocked-action traces | AI service owner | Low |
| R-02 | Indirect prompt injection | Malicious instructions embedded in web/retrieved content | Tool abuse, exfiltration, corrupted output | treat retrieved text as data, isolate instructions, policy gate every action | poisoned-document regression tests | Security owner | Low |
| R-03 | Excessive agency | Agent receives broader permissions than needed | Irreversible or high-impact action | least privilege, read/write separation, action budgets | permission matrix and policy tests | Platform owner | Low |
| R-04 | Privilege escalation | Agent/tool assumes a more privileged identity | Unauthorized access or changes | workload identity, authorization, scoped credentials | authorization-denial tests | IAM owner | Low |
| R-05 | Sensitive-data leakage | Prompt, memory, trace or tool output contains protected data | Privacy, contractual or regulatory breach | classification, minimization, redaction, scoped retrieval, logging controls | DLP/privacy tests and trace review | Data owner | Low |
| R-06 | Secret exposure | API keys appear in source, prompts or logs | Credential compromise | secret store, scanning, redaction, short-lived credentials | secret scan and credential-rotation evidence | Security owner | Low |
| R-07 | Hallucinated action parameters | Model invents an identifier, amount or target | Wrong transaction or external action | typed schemas, deterministic validation, confirmation for high impact | invalid-parameter tests | Product owner | Low |
| R-08 | Unsafe generated code | Agent executes untrusted code on the host | Host compromise or data loss | sandboxing, disposable runtime, network/filesystem limits, timeout | isolation tests and resource-limit evidence | Platform owner | Low |
| R-09 | Malicious tool output | External tool returns adversarial or malformed content | Prompt injection, bad decisions, parser failure | schema validation, provenance, trust boundaries, sanitization | malformed/adversarial tool tests | Tool owner | Low |
| R-10 | Unbounded loops/retries | Agent repeatedly replans or calls tools | Cost spike, rate-limit exhaustion, outage | max steps, retry budget, timeout, circuit breaker | termination tests | Service owner | Low |
| R-11 | Cost escalation | Token/tool usage grows unexpectedly | Financial loss or service degradation | token/cost budgets, routing, caching, alerts | budget-exhaustion tests and cost dashboards | FinOps owner | Low |
| R-12 | Retrieval poisoning/staleness | Knowledge store contains incorrect or outdated material | Incorrect grounded answers | provenance, freshness metadata, curated sources, reranking | source-quality and freshness evaluation | Knowledge owner | Medium/Low |
| R-13 | Evaluation blind spot | Benchmark does not represent real workflows | False confidence before release | representative golden sets, safety tests, human review, drift monitoring | coverage review and regression history | Evaluation owner | Low |
| R-14 | Observability gap | Actions cannot be reconstructed | Slow incident response and weak accountability | trace IDs, tool/policy/approval logs, retention rules | incident reconstruction exercise | Operations owner | Low |
| R-15 | Human-approval bypass | High-risk path avoids intended review | Unauthorized production action | deterministic approval gate outside model, signed approval state | bypass tests | Governance owner | Low |
| R-16 | Availability/fallback failure | Model/tool dependency is unavailable | Workflow outage | timeout, fallback, queue, graceful degradation | chaos/failure tests | Operations owner | Medium/Low |
| R-17 | Model/version regression | Provider or configuration change alters behavior | Quality or safety degradation | version pinning where possible, eval gates, staged rollout, rollback | pre/post-change regression report | AI owner | Low |
| R-18 | Accountability ambiguity | No clear owner for agent decisions or incidents | Delayed response, governance failure | RACI, service ownership, approval authority, escalation path | signed ownership record | Executive sponsor | Low |

## Required fields for a project-specific register

For every material risk, record: scope, affected assets, threat/failure scenario, likelihood, impact, inherent score, controls, control owner, verification evidence, residual score, acceptance authority, review date, trigger conditions and incident/rollback linkage.

## Deployment use

Review the register at design review, before pilot, before increasing tool permissions, before increasing autonomy, before production, after model/tool/data changes, and after any significant incident. Risks should be tied to concrete test evidence rather than narrative assurances.

See [Security Reference Guide](security.md), [Governance](12-governance.md), [Production Readiness Checklist](production-readiness-checklist.md), and [Deployment Playbook](deployment-playbook.md).

---

**Hendar Mawan, PhD**  
Agentic AI Academy — Engineering trustworthy AI agents from learning to production.
