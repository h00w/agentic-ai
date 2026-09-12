# Agentic AI Engineering Lab

Operational Streamlit companion to the **Agentic AI Academy**.

The Hugging Face Space is the public agent experience. The Hugging Face dataset is the benchmark. This Streamlit application is the engineering and operations layer for inspecting evaluation evidence, regressions and release decisions.

## Capabilities

- run the eight-domain Agentic AI benchmark
- inspect per-domain pass rates and case-level evidence
- inspect execution traces and policy decisions
- review RAG context and grounding expectations
- surface prompt-injection and unsafe-action failures
- compare a current run against a reference baseline
- inspect latency, token and estimated cost signals
- enforce configurable release-gate thresholds
- download a Markdown evaluation report

The initial lab deliberately uses deterministic synthetic outcomes. That keeps the reference behavior inspectable and makes regression demonstrations reproducible. A later adapter can replace the deterministic evaluator with live models or agent endpoints while preserving the same benchmark and release-gate contract.

## Run locally

```bash
pip install -r deploy/streamlit/requirements.txt
streamlit run deploy/streamlit/app.py
```

Run from the repository root because the app reads the canonical benchmark files under `dataset/data/`.

## Deploy on Streamlit Community Cloud

Create a new app from `h00w/agentic-ai` and use:

- branch: `main`
- main file path: `deploy/streamlit/app.py`
- suggested app URL: `agentic-ai-engineering-lab.streamlit.app`
- Python: 3.12

No application secrets are required for the deterministic public version.

## Source-of-truth chain

```text
Agentic AI Academy
        ↓
Canonical GitHub engineering source
        ↓
Hugging Face evaluation & security benchmark
        ↓
Hugging Face interactive playground
        ↓
Streamlit engineering / operations lab
```

## Related resources

- Academy: https://hendarmawan.se/agentic-ai/
- GitHub: https://github.com/h00w/agentic-ai
- Hugging Face Playground: https://huggingface.co/spaces/h0000w/hendar-agentic-ai
- Benchmark Dataset: https://huggingface.co/datasets/h0000w/hendar-agentic-ai-dataset
- Author: https://hendarmawan.se/

## Scope

This is an educational and portfolio-grade engineering reference. Benchmark passes are evidence about the included synthetic scenarios, not certification of complete safety, security or regulatory compliance.
