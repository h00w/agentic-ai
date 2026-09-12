# Responsible Enterprise Research Agent — Capstone Rubric

Score 1–4 per dimension. A portfolio-ready capstone should score **3 or higher in every dimension** and have no unresolved critical security finding.

| Dimension | 1 | 2 | 3 — Professional | 4 — Exemplary |
|---|---|---|---|---|
| Goal & workflow | vague | partial | explicit workflow and acceptance criteria | measurable baseline + alternatives |
| Tool use | ad hoc | schemas only | typed allowlisted tools with failures | policy-aware gateway + contracts + quotas |
| RAG & memory | unsupported | basic retrieval | cited authorized retrieval + state lifecycle | reranking, provenance, retention, eval |
| Evaluation | demo only | few happy tests | golden set + regression + safety + cost/latency | segment analysis + confidence + release gates |
| Security | prompt-only | partial controls | least privilege, validation, approval, sandbox design, budgets | threat model + red-team evidence + kill switch |
| Observability | print logs | basic logging | trace plan/policy/tools/eval/cost | SLOs, dashboards, alerts, incident evidence |
| Reliability | none | retries | bounded retry/timeout/fallback/idempotency | failure injection + recovery evidence |
| Governance | none | checklist | owner, risk class, deployment gate, audit | change control + review cadence + retirement |
| Architecture | monolith | partial boundaries | clear controller/policy/gateways/state/eval | justified trade-offs + scaling design |
| Communication | unclear | functional | concise README, diagram, decisions, limits | executive + engineer views, demo narrative |
