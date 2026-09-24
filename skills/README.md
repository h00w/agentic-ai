# Agent Skills Architecture

A skill is a portable capability contract, not merely a prompt. Each `SKILL.md` must contain `# Objective`, `# Inputs`, `# Procedure`, `# Failure conditions`, and `# Evidence produced`.

Design rules: bounded purpose, explicit permissions, deterministic checks first, fail closed, and leave reviewable evidence.

Starter skills: `evaluate-agent`, `threat-model-agent`, and `production-readiness-review`.
