---
name: threat-model-agent
version: 0.1.0
permissions:
  network: false
  filesystem: read-only
---

# Objective

Create a defensive threat model for an agentic system.

# Inputs

Architecture, roles, autonomy, tools, integrations, data classes and policy boundaries.

# Procedure

Identify assets and trust boundaries, enumerate plausible failure or misuse classes, map controls, identify deterministic enforcement points and record residual risk.

# Failure conditions

Architecture is too incomplete, unauthorized exploitation is requested, or required topology and permissions are unknown.

# Evidence produced

A threat model with assets, boundaries, threats, controls, residual risk, owners and recommended regression tests.
