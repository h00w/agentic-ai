---
title: Agentic AI Playground
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: true
license: mit
short_description: Transparent playground for trustworthy AI agent engineering
---

# Agentic AI Playground

![Agentic AI Academy](https://raw.githubusercontent.com/h00w/agentic-ai/refs/heads/main/agenticai-banner.png)

A public interactive companion to the **Agentic AI Academy** by **Hendar Mawan, PhD**.

This Space is an engineering playground rather than a generic chatbot. It exposes planning, tool routing, policy decisions, evidence, retrieval, security controls and evaluation so learners, engineers and reviewers can inspect how trustworthy agent behavior is constructed.

## Explore the playground

- **Agent Playground** — bounded agent execution, scenario selection, tool routing, policy gates, approval requirements, latency and trace inspection
- **RAG Lab** — transparent retrieval over Academy knowledge with ranked evidence, match scores and provenance
- **Security / Prompt Injection** — inspect obvious instruction-override, secret-extraction, data-exfiltration and unsafe-tool indicators, then review the recommended control path
- **Evaluation Lab** — inspect task completeness, groundedness, tool accuracy, safety, traceability and response-efficiency gates
- **Architecture** — study the enterprise execution path from user goal through policy, tools, retrieval, evaluation, approval and audit

## Why this design

Trustworthy Agentic AI requires more than model capability. Production systems need explicit control over tools, permissions, evidence, retrieval, evaluation, observability and human responsibility.

The playground therefore makes these controls visible instead of hiding them behind an opaque conversational interface. The first public version is intentionally deterministic, framework-neutral and side-effect free so the control flow remains inspectable.

## Architecture

```text
User Goal
   ↓
Agent Controller
   ↓
Planner
   ↓
Policy Engine
   ↓
Tool Gateway
   ↓
Research Tools + Knowledge / RAG
   ↓
Evaluation
   ↓
Human Approval when required
   ↓
Final Response
   ↓
Audit / Observability
```

## Production principles demonstrated

- least-privilege tool access
- explicit policy decisions before high-impact actions
- human approval for sensitive or irreversible operations
- prompt-injection-aware handling of untrusted content
- retrieval provenance and evidence visibility
- transparent release-gate evaluation
- execution traces and latency visibility
- bounded arithmetic rather than arbitrary code execution
- no external side effects in the public demo

## Source

- Academy repository: https://github.com/h00w/agentic-ai
- Academy website: https://hendarmawan.se/agentic-ai/
- Author website: https://hendarmawan.se/
- LinkedIn: https://www.linkedin.com/in/hender/

## Deployment

This directory is the curated public Space package for `h0000w/hendar-agentic-ai`. GitHub Actions publishes it using the repository secret `HF_TOKEN`, keeping the Space synchronized with the Academy source while preserving GitHub as the canonical curriculum and engineering repository.

## Next iterations

The next iterations can add optional Hugging Face inference, richer document-backed RAG, benchmark datasets, scenario-based regression evaluation, and production observability integrations while retaining explicit policy and approval boundaries.

## License

MIT License. See the canonical repository for the complete license, curriculum and engineering assets.


## Five-level production-AI proof

The Academy now uses the shared proof model:

`L1 Runnable → L2 Reproducible → L3 Capability-Validated → L4 Production-Candidate → L5 Production-Validated`.

The public Playground and benchmark Dataset support the independently inspectable capability layer. The canonical GitHub source computes the current level with `make proof`; this project deliberately caps its claim at **L3 — Capability-Validated** and does not infer production deployment from a demo.

Specification: https://github.com/h00w/agentic-ai/blob/main/PROOF_MODEL.md
