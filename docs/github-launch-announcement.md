# GitHub Launch Announcement — Agentic AI Academy

## Suggested release title

**Agentic AI Academy — Public Engineering Stack Launch**

## Suggested release summary

Agentic AI Academy is now live as a complete public engineering stack for trustworthy AI agents — from curriculum and reference implementation through evaluation, security, interactive demos and operational release evidence.

This milestone moves the project beyond a learning repository into a production-oriented proof system.

### What is live

- **Academy:** https://hendarmawan.se/agentic-ai/
- **Canonical source:** https://github.com/h00w/agentic-ai
- **Hugging Face Playground:** https://huggingface.co/spaces/h0000w/hendar-agentic-ai
- **Evaluation & Security Benchmark:** https://huggingface.co/datasets/h0000w/hendar-agentic-ai-dataset
- **Streamlit Engineering Lab:** https://agentic-ai-engineering-lab.streamlit.app/
- **90-second recruiter proof:** https://hendarmawan.se/agentic-ai/proof/

### Why this release matters

The project treats Agentic AI as a systems-engineering discipline rather than a chatbot feature.

The public architecture separates model capability from the control plane required for production trust:

```text
User
  ↓
Agent Controller
  ↓
Planner
  ↓
Policy Engine
  ↓
Tool Gateway
  ↓
RAG / Tools
  ↓
Evaluation
  ↓
Human Approval when required
  ↓
Response
  ↓
Audit / Observability
```

The central design principle is:

> **The model is not the system.**

Reliable agentic systems need explicit permissions, policy enforcement, evaluation, human approval, observability, regression testing, auditability and release gates around the model.

### Engineering proof included

- 14 curriculum modules
- 6 role-based learning pathways
- 10 enterprise case studies
- 10 progressive portfolio projects
- 11 runnable examples
- framework-neutral Python reference implementation
- 48-case evaluation and security benchmark across 8 domains
- prompt-injection and unsafe-action controls
- RAG evidence inspection
- agent traces and policy decisions
- latency, token and estimated-cost metrics
- regression comparison profiles
- configurable release-gate thresholds
- downloadable evaluation reports
- CI, validation and deployment smoke tests

### Public surface responsibilities

| Surface | Responsibility |
|---|---|
| Hugging Face Playground | Experience agent behavior |
| Hugging Face Dataset | Benchmark agent behavior |
| Streamlit Engineering Lab | Inspect, evaluate, compare and gate agent behavior |
| GitHub | Canonical source, architecture, tests and curriculum |
| Academy website | Professional navigation and learning entry point |

### Technical review shortcut

For the fastest review:

1. Open the **90-second proof page**.
2. Open the **Engineering Lab**.
3. Switch from **Reference baseline** to **Mixed production regression**.
4. Inspect failed benchmark cases and the release-gate decision.
5. Follow through to the canonical GitHub source.

This sequence demonstrates the project's core thesis: agent capability only becomes production-ready when it can be measured, secured, observed, compared and governed.

---

**By Hendar Mawan, PhD**  
AI Engineering · AI Architecture · Agentic AI · Secure AI · Edge AI · AI Governance
