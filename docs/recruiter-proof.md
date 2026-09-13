# Agentic AI Academy — 90-Second Recruiter Proof

**Engineering trustworthy AI agents from learning to production.**

This is the shortest technical-review path through the Agentic AI Academy by **Hendar Mawan, PhD**.

## Public proof chain

1. **Academy** — https://hendarmawan.se/agentic-ai/
   - 14-module curriculum from foundations through enterprise architecture and AI leadership.
2. **Canonical source** — https://github.com/h00w/agentic-ai
   - Framework-neutral reference implementation, tests, security patterns, CI and production engineering guidance.
3. **Hugging Face Playground** — https://huggingface.co/spaces/h0000w/hendar-agentic-ai
   - Experience bounded agent behavior, RAG evidence, policy gates and prompt-injection controls.
4. **Evaluation & Security Benchmark** — https://huggingface.co/datasets/h0000w/hendar-agentic-ai-dataset
   - 48 synthetic expert-authored cases across eight evaluation and security domains.
5. **Streamlit Engineering Lab** — https://agentic-ai-engineering-lab.streamlit.app/
   - Inspect per-domain pass rates, traces, policy decisions, RAG evidence, security failures, regressions, latency/cost and release-gate decisions.
6. **Recruiter proof page** — https://hendarmawan.se/agentic-ai/proof/
   - One-page architecture and 60–90 second walkthrough.

## Architecture

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

The architectural premise is simple: **the model is not the system**. Production trust comes from the control plane around the model—permissions, policy, evaluation, approval, evidence, observability and release criteria.

## 60–90 second script

> I built the Agentic AI Academy to demonstrate how I engineer trustworthy agents from first principles through production operations. The GitHub repository is the canonical source: curriculum, reference architecture, code, tests, security patterns and CI. The Hugging Face Playground lets you experience a bounded agent and inspect RAG, policy and prompt-injection behavior. The public benchmark then tests eight domains including task success, tool routing, groundedness, unsafe actions and regressions. Finally, the Streamlit Engineering Lab turns those benchmark cases into operational evidence: pass rates, traces, security failures, latency and cost, regression comparisons and a configurable release gate. The key point is that I do not treat an agent as just a model call—I design the control plane around it so capability can be evaluated, secured, observed and governed before release.

## Recording sequence

| Time | Screen | Message |
|---|---|---|
| 0–15 s | Academy page | Trustworthy agent engineering, not another chatbot demo. |
| 15–35 s | GitHub architecture | Controller, policy, tools/RAG, evaluation, approval and audit boundaries. |
| 35–55 s | Hugging Face Playground + Dataset | Live behavior plus repeatable benchmark evidence. |
| 55–80 s | Engineering Lab | Switch from Reference baseline to a regression profile and show the release gate change. |
| 80–90 s | Proof page / closing frame | Capability matters only when the full system can be measured, secured, observed and governed. |

## What this proves

- **AI engineering:** bounded agents, tool use, RAG, multi-agent patterns and reference implementations.
- **Evaluation:** task success, groundedness, routing, safety, regressions, latency, tokens and estimated cost.
- **AI security:** prompt-injection defense, unsafe-action blocking, least privilege, policy gates and approval controls.
- **Production engineering:** CI, regression qualification, release gates, operational metrics and downloadable evidence.
- **AI architecture:** separation of model capability from control, policy, tool, evaluation and audit planes.
- **Technical leadership:** a coherent public learning-to-production system rather than isolated demos.

## Recruiter shortcut

Start with the **Engineering Lab**, select **Mixed production regression**, inspect the failed cases and release gate, then open the canonical GitHub source.

**Engineering Lab:** https://agentic-ai-engineering-lab.streamlit.app/  
**Proof page:** https://hendarmawan.se/agentic-ai/proof/
