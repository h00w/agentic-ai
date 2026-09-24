---
name: production-readiness-review
version: 0.1.0
permissions:
  network: false
  filesystem: read-only
---

# Objective

Review release evidence against explicit production-readiness gates without granting deployment approval.

# Inputs

Evaluation, security, rollback, observability, risk, approval and deployment evidence.

# Procedure

Identify the claimed proof level, verify gate evidence, treat critical unresolved findings as blockers and return pass, fail or unresolved per gate.

# Failure conditions

Mandatory evidence is missing or stale, a critical issue is unresolved, or the requested proof level exceeds the evidence.

# Evidence produced

A gate-by-gate readiness review with references, blockers, unresolved items and the maximum supportable proof level.
