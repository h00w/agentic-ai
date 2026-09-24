# Agentic AI Academy

## Engineering trustworthy AI agents from learning to production.

**EXPLORE • IMPLEMENT • SCALE**

<p align="center">
  <a href="https://hendarmawan.se/agentic-ai/"><strong>Academy Website</strong></a> ·
  <a href="https://huggingface.co/spaces/h0000w/hendar-agentic-ai"><strong>Playground</strong></a> ·
  <a href="https://huggingface.co/datasets/h0000w/hendar-agentic-ai-dataset"><strong>Benchmark Dataset</strong></a> ·
  <a href="https://agentic-ai-engineering-lab.streamlit.app/"><strong>Engineering Lab</strong></a> ·
  <a href="#getting-started-in-5-minutes"><strong>Start Learning</strong></a>
</p>

<p align="center">
  <a href="https://github.com/h00w/agentic-ai/actions/workflows/ci.yml"><img src="https://github.com/h00w/agentic-ai/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12%2B-3776AB" alt="Python 3.12+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
  <a href="curriculum/"><img src="https://img.shields.io/badge/Curriculum-16%20Modules-0B3D91" alt="16 modules"></a>
  <a href="evaluation/"><img src="https://img.shields.io/badge/Evaluation-Reproducible-6A5ACD" alt="Evaluation"></a>
  <a href="docs/security.md"><img src="https://img.shields.io/badge/Security-Defense--in--Depth-2E8B57" alt="Security"></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/Release-v0.1.0-1f6feb" alt="v0.1.0"></a>
</p>

<p align="center">
  <a href="https://hendarmawan.se/agentic-ai/">
    <img src="https://raw.githubusercontent.com/h00w/agentic-ai/refs/heads/main/agenticai-banner.png" alt="Agentic AI — From Learning to Implementation to Scale" width="100%">
  </a>
</p>

**Agentic AI Academy** is an open-source curriculum, engineering laboratory, reference architecture, evaluation benchmark and professional portfolio for learning how to design, build, evaluate, secure, operate, govern and scale AI agents.

This is not a collection of chatbot tutorials. The Academy treats agentic AI as a **systems-engineering discipline**: capability must be paired with measurable reliability, bounded autonomy, explicit permissions, evaluation, observability, governance and safe failure behavior.

**Canonical source:** this repository  
**Professional Academy page:** https://hendarmawan.se/agentic-ai/  
**Agentic AI Playground:** https://huggingface.co/spaces/h0000w/hendar-agentic-ai  
**Evaluation & Security Benchmark:** https://huggingface.co/datasets/h0000w/hendar-agentic-ai-dataset  
**Agentic AI Engineering Lab:** https://agentic-ai-engineering-lab.streamlit.app/

**By Hendar Mawan, PhD**

> **Hendar Mawan : AI Engineering Leader**  
> AI Engineering · AI Architecture · Agentic AI · Secure AI · Edge AI · AI Governance

---

## Phase 1 — Provider Runtime & Structured Contracts

The Academy now includes a provider-neutral LLM runtime foundation designed for reproducible AI engineering rather than one-off SDK examples.

**Phase 1 engineering proof**

- Provider-neutral `ProviderRequest` / `ProviderResponse` contracts validated with Pydantic.
- Deterministic `MockProvider` for local development, CI and benchmark reproducibility.
- Optional adapters for OpenAI, Anthropic, Gemini and Ollama.
- Provider registry for runtime selection and extension.
- Provider benchmark hook that records pass/fail, model, latency and token usage.
- Secret-free CI tests for contracts, registry behavior and benchmark integration.
- Existing deterministic agent, policy and safety paths remain unchanged.

```text
application / benchmark
        ↓
provider-neutral contracts
        ↓
provider registry
   ┌────┼────────┬────────┬────────┐
   ↓    ↓        ↓        ↓        ↓
 mock  OpenAI  Anthropic Gemini   Ollama
        ↓
normalized response + usage + latency
        ↓
evaluation / release-gate pipeline
```

Install the core only:

```bash
pip install -e ".[dev]"
```

Install optional hosted-provider SDKs:

```bash
pip install -e ".[dev,providers]"
```

The mock provider is the default reference path for tests and does not require credentials. Hosted providers are opt-in.

---

## Public Engineering Stack

The public stack is intentionally separated by function rather than duplicated across platforms:

| Surface | Purpose | What it proves |
|---|---|---|
| [Hugging Face Playground](https://huggingface.co/spaces/h0000w/hendar-agentic-ai) | **Experience the agent** | bounded agent behavior, RAG, prompt-injection controls, policy decisions and evaluation signals |
| [Hugging Face Dataset](https://huggingface.co/datasets/h0000w/hendar-agentic-ai-dataset) | **Benchmark the agent** | task success, tool routing, groundedness, prompt injection, unsafe actions, policy, multi-agent and regression cases |
| [Streamlit Engineering Lab](https://agentic-ai-engineering-lab.streamlit.app/) | **Inspect, evaluate and operate the agent** | benchmark runner, traces, RAG evidence, security failures, regression comparison, latency/cost metrics, release gates and downloadable reports |

```text
curriculum → implementation → dataset → evaluation → interactive demo → production engineering
```

The benchmark currently contains **104 expert-authored synthetic cases across 8 domains** (13 per domain), with deterministic validation and automated Hugging Face publishing. The Engineering Lab consumes the same benchmark structure to demonstrate operational evaluation and release-gate behavior.

---

## Why Agentic AI?

Generative models can produce useful outputs, but production agents must do more. They maintain state, choose tools, interact with external systems, recover from failure, operate under permissions, generate evidence and stop safely.

The central engineering question is not simply:

> *Can the model act?*

It is:

> *Can the complete system act reliably, safely, observably, economically and accountably?*

That distinction drives the architecture of this Academy.

## What You Will Learn

```mermaid
flowchart LR
    A[Explore] --> B[Implement]
    B --> C[Scale]
    A --> A1[Foundations & Value]
    B --> B1[Agents · Tools · RAG · Multi-Agent · Evaluation]
    C --> C1[Security · Production · Observability · Governance · Leadership]
    C1 --> D[Responsible Enterprise Research Agent]
```

A learner completing the full pathway should be able to move through:

**AI foundations → agent fundamentals → Python implementation → single-agent systems → tools → memory → RAG → multi-agent systems → evaluation → security → production → observability → governance → enterprise architecture → AI leadership.**

## Who This Is For

The Academy supports multiple entry points: complete beginners, Python developers, AI/ML engineers, software engineers, researchers, students, technical professionals, AI product managers, enterprise architects and technology leaders.

Choose the relevant path in [`learning-paths/`](learning-paths/).

## Learning Philosophy

The default learning mix is **30% theory · 50% implementation · 20% reflection and evaluation**.

Every module is designed to answer:

- Why does this matter?
- What should I learn?
- How do I implement it?
- What can go wrong?
- How do professionals solve it?
- How does this appear in interviews?
- How does this appear in production?
- What should I build next?

Concepts come before frameworks. Use a deterministic workflow when a task is stable and fully specifiable. Use an agent when uncertainty, planning, tool selection, adaptive sequencing or iterative recovery create material value. Use multi-agent systems only when specialization or parallel decomposition produces measurable benefit.

The Academy learning contract is **UNDERSTAND → BUILD → BREAK → MEASURE → SECURE → SHIP → OPERATE → GOVERN**. Each deep lesson keeps reusable engineering evidence rather than ending with a notebook or prompt. See [`docs/academy-learning-contract.md`](docs/academy-learning-contract.md), [`LESSON_TEMPLATE.md`](LESSON_TEMPLATE.md), the machine-readable [`catalog.json`](catalog.json), and [Agent Loop From Scratch](curriculum/04-single-agent-engineering/01-agent-loop-from-scratch/README.md).

## Curriculum

| # | Module | Core outcome |
|---|---|---|
| 01 | [Exploring Agentic AI](curriculum/01-exploring-agentic-ai/README.md) | Evaluate opportunity, autonomy, constraints and organizational value. |
| 02 | [Python for Agentic AI](curriculum/02-python-for-agentic-ai/README.md) | Build the Python skills used directly in agent engineering. |
| 03 | [LLM & Agent Foundations](curriculum/03-llm-agent-foundations/README.md) | Understand structured outputs, planning, verification and model choice. |
| 04 | [Single-Agent Engineering](curriculum/04-single-agent-engineering/README.md) | Implement bounded, stateful, tool-using agent loops. |
| 05 | [Tools, APIs & MCP](curriculum/05-tools-apis-mcp/README.md) | Design tool schemas, API integrations, permissions and boundaries. |
| 06 | [RAG, Knowledge & Memory](curriculum/06-rag-memory-knowledge/README.md) | Build grounded retrieval and durable state. |
| 07 | [Multi-Agent Systems](curriculum/07-multi-agent-systems/README.md) | Design delegation, routing, supervision and shared state. |
| 08 | [Agent Evaluation](curriculum/08-agent-evaluation/README.md) | Measure success, correctness, groundedness, safety, latency and cost. |
| 09 | [Security & Safety](curriculum/09-agent-security/README.md) | Apply least privilege, sandboxing, policy enforcement, approval and audit controls. |
| 10 | [Production Agent Engineering](curriculum/10-production-engineering/README.md) | Package, deploy, recover, rate-limit, route and operate agents. |
| 11 | [Observability & Operations](curriculum/11-observability/README.md) | Trace trajectories, tool calls, token usage, cost, failures and drift. |
| 12 | [Governance, Risk & Scaling](curriculum/12-governance-scaling/README.md) | Build risk registers, deployment gates, incident processes and scaling playbooks. |
| 13 | [Enterprise Agentic AI Architecture](curriculum/13-enterprise-architecture/README.md) | Architect model/tool gateways, policy, identity, knowledge, evaluation and audit. |
| 14 | [Agentic AI Leadership & Strategy](curriculum/14-agentic-ai-leadership/README.md) | Prioritize portfolios, quantify ROI/TCO and lead responsible transformation. |
| 15 | [MCP Engineering](curriculum/15-mcp-engineering/README.md) | Engineer MCP contracts, trust boundaries, authorization, reliability and conformance evidence. |
| 16 | [Agent Skills Engineering](curriculum/16-agent-skills-engineering/README.md) | Package portable, testable capabilities with explicit permissions, failure behavior and evidence. |

## Learning Pathways

- [Complete Beginner](learning-paths/beginner.md) — 12–16 weeks
- [Python Developer](learning-paths/python-developer.md) — 8–10 weeks
- [AI/ML Engineer](learning-paths/ai-engineer.md) — 8 weeks
- [AI Product Manager](learning-paths/product-manager.md) — 6 weeks
- [AI Architect / Technical Leader](learning-paths/architect.md) — 8 weeks
- [Researcher](learning-paths/researcher.md) — architecture, planning, memory, evaluation, multi-agent systems and trustworthy AI

## Engineering Proof

The Academy includes:

- **16 curriculum modules** with coaching, exercises, assessments, production framing and portfolio evidence.
- **10 enterprise case studies** across research, support, software engineering, cybersecurity, finance, HR, sales, healthcare administration, manufacturing and public-sector knowledge work.
- **10 progressive portfolio projects** from a Python tool chest to the enterprise capstone.
- **11 runnable examples** covering agent loops, function calling, tools, memory, RAG, guardrails, evaluation, multi-agent patterns, observability and secure agents.
- **104-case evaluation and security benchmark** across eight balanced domains with a common schema and automated validation.
- **Reusable evaluation infrastructure** for task success, correctness, groundedness, tool accuracy, safety, latency, token usage and estimated cost.
- **Security architecture** based on least privilege, explicit tool permissions, validation, policy gates, human approval, sandbox boundaries, timeouts, budgets, network restrictions and audit logging.
- **Production engineering** with tests, Docker, CI, configuration, health checks, logging, reliability patterns and operational controls.
- **Live operational Engineering Lab** with regression profiles, release thresholds, trace inspection and downloadable evaluation reports.
- **Curriculum-as-code controls** with a lesson contract, artifact manifests, generated catalog, structural audit and CI freshness checks.
- **Portable Agent Skills library** for evaluation, threat modeling and production-readiness evidence review.

## Flagship Capstone

### Responsible Enterprise Research Agent

The flagship capstone integrates planning, policy enforcement, bounded tool use, retrieval, memory, evaluation, human approval, cost controls, failure recovery and auditability.

```mermaid
flowchart TD
    U[User] --> C[Agent Controller]
    C --> P[Planner]
    P --> PE[Policy Engine]
    PE --> TG[Tool Gateway]
    TG --> RT[Research Tools]
    RT --> K[Knowledge / RAG]
    K --> E[Evaluation]
    E --> H{Human approval required?}
    H -->|Yes| A[Human Approval]
    H -->|No| F[Final Report]
    A --> F
    F --> O[Audit / Observability]
```

[View the capstone →](projects/10-enterprise-agentic-ai-capstone/README.md)

## Technology Stack

- **Core:** Python 3.12+, type hints, dataclasses, Pydantic, pytest, asyncio, pathlib, logging
- **Agent strategy:** framework-neutral first; optional LangGraph, CrewAI and Microsoft agent ecosystem patterns
- **Knowledge:** in-memory learning references; optional Chroma and PostgreSQL + pgvector extensions
- **Evaluation:** pytest + custom deterministic evaluation harness + public JSONL benchmark
- **Operations:** Docker, GitHub Actions, OpenTelemetry-compatible tracing, Prometheus-style metrics
- **Security:** explicit permissions, policy gates, approval points, resource budgets, execution isolation, audit logging
- **Interfaces:** Gradio on Hugging Face for the public Playground; Hugging Face Datasets for benchmark publication; Streamlit for the Engineering Lab

## Getting Started in 5 Minutes

### 1. Clone

```bash
git clone https://github.com/h00w/agentic-ai.git
cd agentic-ai
```

### 2. Create an isolated Python environment

**macOS / Linux**

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

### 4. Verify the repository

```bash
pytest
python scripts/validate_examples.py
python scripts/check_links.py
python scripts/validate_benchmark_dataset.py
```

### 5. Run your first agent example

```bash
python examples/01_hello_agent.py
python examples/02_agent_loop.py
python examples/04_tool_agent.py
```

### 6. Run the Engineering Lab locally

```bash
pip install -r deploy/streamlit/requirements.txt
streamlit run deploy/streamlit/app.py
```

**No API key is required** for the core curriculum, deterministic examples, benchmark, tests or Engineering Lab. External model providers are optional extensions.

### Recommended first learning route

1. [Module 01 — Exploring Agentic AI](curriculum/01-exploring-agentic-ai/README.md)
2. [Module 02 — Python for Agentic AI](curriculum/02-python-for-agentic-ai/README.md)
3. Run [`examples/01_hello_agent.py`](examples/01_hello_agent.py)
4. Run [`examples/02_agent_loop.py`](examples/02_agent_loop.py)
5. Continue with the [Complete Beginner pathway](learning-paths/beginner.md)

## Production Readiness

Production-ready agents need explicit owners, measurable task success, bounded autonomy, deterministic safety controls, retries and timeouts, fallback behavior, cost and token budgets, observability, incident response, rollback, regression tests and change-control evidence.

Use the [Production Readiness Checklist](docs/production-readiness-checklist.md).

## Security

Security is a throughline, not a single chapter. Privileged actions should pass through authentication/authorization, policy evaluation, input/output validation, bounded tool permissions, execution isolation, resource limits, approval rules and audit logging.

Start with [docs/security.md](docs/security.md) and [SECURITY.md](SECURITY.md).

## Governance

The repository includes an [Agent Risk Register](docs/agent-risk-register.md), [Governance Checklist](docs/agent-governance-checklist.md), [Deployment Playbook](docs/deployment-playbook.md) and enterprise architecture guidance.

## Career Outcomes

Completion is designed to produce portfolio evidence for roles such as:

**Agentic AI Engineer · AI Engineer · Production AI Engineer · AI Architect · Applied AI Lead · AI Platform Engineer · Trustworthy AI Engineer · AI Security Engineer · AI Product Manager · AI Engineering Leader**

## Repository Structure

```text
agentic-ai/
├── curriculum/          # 16 modules + metadata-backed deep lessons
├── learning-paths/      # role-based self-study sequences
├── case-studies/        # 10 enterprise scenarios
├── projects/            # 10 progressive portfolio builds
├── labs/                # guided implementation exercises
├── examples/            # safe runnable examples
├── evaluation/          # evaluators, metrics and regression tests
├── skills/              # portable, evidence-oriented Agent Skills
├── dataset/             # public 104-case evaluation & security benchmark source
├── catalog.json         # filesystem-derived curriculum and skills catalog
├── deploy/
│   ├── huggingface/     # Agentic AI Playground
│   └── streamlit/       # Agentic AI Engineering Lab
├── src/agentic_ai/      # framework-neutral reference implementation
├── tests/               # unit/integration tests
├── docs/                # handbook, governance and architecture guidance
└── .github/workflows/   # CI + publishing + smoke tests
```

## Release & Roadmap

- Current public milestone: **v0.1.0 — Initial Academy Release**
- Next development milestone: **v0.2.0 — Curriculum-as-Code Foundation**
- Release notes: [`RELEASE_NOTES_v0.1.0.md`](RELEASE_NOTES_v0.1.0.md)
- Changelog: [`CHANGELOG.md`](CHANGELOG.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- Citation metadata: [`CITATION.cff`](CITATION.cff)

The current public proof stack is live across GitHub, Hugging Face and Streamlit. Next iterations focus on stronger framework/model comparison, richer observability, larger regression suites and deeper enterprise reference-platform patterns.

## Contribution

Contributions are welcome when they preserve the Academy's principles: concept-first teaching, safe runnable examples, production credibility, explicit security boundaries, reproducible evaluation and vendor neutrality.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Author

**Hendar Mawan, PhD**  
**Hendar Mawan : AI Engineering Leader**  
AI Engineering · AI Architecture · Agentic AI · Secure AI · Edge AI · AI Governance

- Academy: https://hendarmawan.se/agentic-ai/
- Playground: https://huggingface.co/spaces/h0000w/hendar-agentic-ai
- Benchmark: https://huggingface.co/datasets/h0000w/hendar-agentic-ai-dataset
- Engineering Lab: https://agentic-ai-engineering-lab.streamlit.app/
- Website: https://hendarmawan.se
- GitHub: https://github.com/h00w
- LinkedIn: https://www.linkedin.com/in/hender
- Email: hendar@hendarmawan.se

---

**Agentic AI Academy — Engineering trustworthy AI agents from learning to production.**
