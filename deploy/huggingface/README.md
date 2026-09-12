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

A public interactive companion to the **Agentic AI Academy** by **Hendar Mawan, PhD**.

This Space is designed as an engineering playground rather than a generic chatbot. It exposes the execution path so learners and reviewers can inspect how an agent selects tools, passes policy gates, produces evidence and is evaluated.

## What you can explore

- bounded agent execution
- deterministic tool routing
- human approval gates
- policy decisions
- safe arithmetic execution
- grounded Academy knowledge retrieval
- execution traces
- transparent evaluation metrics
- enterprise-oriented agent architecture

## Why this design

Trustworthy Agentic AI requires more than model capability. Production systems need explicit control over tools, permissions, evidence, evaluation, observability and human responsibility.

The playground therefore makes those controls visible instead of hiding them behind an opaque conversational interface.

## Architecture

```text
User Goal
   ↓
Controller
   ↓
Planner / Tool Selection
   ↓
Policy Engine
   ↓
Tool Gateway
   ↓
Knowledge / Bounded Tools
   ↓
Evidence + Evaluation
   ↓
Human Approval when required
   ↓
Response + Audit Trace
```

## Source

- Academy repository: https://github.com/h00w/agentic-ai
- Academy website: https://hendarmawan.se/agentic-ai/
- Author: https://hendarmawan.se/

## Deployment

This directory is the curated public Space package for `h0000w/hendar-agentic-ai`. GitHub Actions publishes it using the repository secret `HF_TOKEN`, so the Hugging Face Space stays synchronized with the Academy source while remaining intentionally smaller than the canonical repository.

## Planned next iterations

The first public release is intentionally framework-neutral and side-effect free. Future iterations can add optional Hugging Face inference, richer RAG, scenario-based evaluation and production observability while keeping policy and approval boundaries explicit.

## License

MIT License. See the canonical repository for the full license and curriculum.
