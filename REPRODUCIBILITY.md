# Reproducibility

This repository implements the **Production AI Evidence Contract v1**.

## Prerequisites

- Git
- Python 3.12+

Install the project in an isolated environment:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Reproduce

```bash
make reproduce
```

The command runs the deterministic Academy verification chain (`pytest`, example validation, benchmark validation), records Git/runtime identity, hashes relevant source, benchmark, policy and dependency files, retains stdout/stderr, and writes:

```text
evidence/out/current/
├── evidence.json
├── verification.stdout.log
├── verification.stderr.log
├── checksums.sha256
└── summary.md
```

The bundle uses `evidence/production-ai-evidence-contract-v1.schema.json`, vendored from the canonical schema maintained in `h00w/model-quality-release-gate`.

## Interpretation

A reproduction `PASS` confirms the configured repository verification chain passed for the recorded commit/environment. It is not a claim that every model/provider configuration is production-ready, safe, or approved for autonomous operation.

## Clean-room check

```bash
git clone https://github.com/h00w/agentic-ai.git
cd agentic-ai
git checkout <commit>
python -m pip install -e ".[dev]"
make reproduce
cat evidence/out/current/summary.md
```
