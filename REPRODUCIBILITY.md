# Reproducibility

This repository implements **Production AI Evidence Contract v1** so another engineer can rerun the declared verification chain and receive a machine-readable evidence bundle bound to the exact Git commit, benchmark inputs, environment and logs.

## One-command reproduction

```bash
git clone https://github.com/h00w/agentic-ai.git
cd agentic-ai
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
make reproduce
```

The default reproduction path is intentionally offline with respect to model providers and does not require an API key.

## What `make reproduce` verifies

The plan in `evidence/reproduction-plan.json` executes:

1. `pytest -q`;
2. runnable-example validation;
3. documentation link checks;
4. benchmark schema/content validation;
5. generation of a Production AI Evidence Contract v1 bundle.

The declared evidence inputs include the benchmark source, evaluation engine, framework-neutral reference implementation, security policy and dependency manifest.

## Evidence output

```text
artifacts/reproduction/<UTC timestamp>-<git sha>/
├── evidence.json
├── summary.md
├── checksums.sha256
└── logs/
```

`evidence.json` records repository identity, commit, tracked dirty state, environment, SHA-256 identities for declared inputs, every verification step and the resulting reproduction status.

Statuses are:

- `REPRODUCED` — all declared checks passed from a clean tracked working tree;
- `PARTIAL` — checks passed but tracked local modifications were present;
- `FAILED` — a declared input or verification step failed.

These are **reproduction statuses**, not deployment-authority decisions.

## Why this matters for the Academy

The Academy's 48-case benchmark and engineering examples are useful only if their evidence can be reconstructed. The contract therefore binds the result to the exact source revision and benchmark definition instead of relying on screenshots or a mutable live demo.

Reproduction does not prove that the synthetic benchmark covers all real production failures. It proves that the declared tests, benchmark structure and controls can be rerun for the identified revision.

## Verify the bundle

On a system with GNU `sha256sum`:

```bash
cd artifacts/reproduction/$(cat artifacts/reproduction/LATEST)
sha256sum --check checksums.sha256
```

For publication-quality evidence, reproduce from an immutable tag or full commit SHA with a clean working tree and retain the complete evidence directory.

## Custom evidence location

```bash
REPRO_OUT=/tmp/agentic-ai-evidence make reproduce
```

## Contract source

The canonical schema is maintained in `h00w/model-quality-release-gate` and vendored locally at:

`evidence/production-ai-evidence-contract-v1.schema.json`

The local schema is hashed into every generated evidence bundle so a result can identify the contract definition used to generate it.

## Updating the plan

When the benchmark, evaluation engine, critical security controls or dependency contract changes, update `evidence/reproduction-plan.json` in the same pull request. Do not remove failing checks merely to obtain a green reproduction status; failures are part of the evidence.
