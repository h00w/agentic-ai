---
name: evaluate-agent
version: 0.1.0
permissions:
  network: false
  filesystem: read-only
---

# Objective

Evaluate an agent against explicit capability, safety and regression criteria without inventing missing evidence.

# Inputs

Benchmark cases, outputs or traces, expected labels and optional release thresholds.

# Procedure

Run deterministic checks first, measure relevant rates, separate observations from interpretation and report passed, failed and unresolved gates.

# Failure conditions

Required fixtures are missing, required traces are unavailable, unauthorized access would be needed, or the requested conclusion exceeds the evidence.

# Evidence produced

A structured evaluation summary with metrics, failures, uncertainty and evidence references.
