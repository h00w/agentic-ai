# Reproducibility

This repository implements **Production AI Evidence Contract v1** and the **Production AI Five-Level Proof Model v1**.

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

The command runs the deterministic Academy verification chain (`pytest`, example validation, benchmark validation), records Git/runtime identity, hashes relevant source, benchmark, policy and dependency files, retains stdout/stderr, and writes the Evidence Contract bundle under `evidence/out/current/`.

A reproduction `PASS` is **L2 — Reproducible**. It is not a claim that every model/provider configuration is production-ready, safe, or approved for autonomous operation.

## Assess the five-level proof

```bash
make proof
```

The proof assessor verifies the public Hugging Face Playground and benchmark Dataset in addition to the Level-2 evidence and emits `proof.json` plus `proof-summary.md`.

The Academy's configured ceiling is **L3 — Capability-Validated**. Levels 4-5 are intentionally not inferred from a public educational/research engineering environment.

For a network-independent run:

```bash
make proof-offline
```

Offline assessment can establish at most L2.

See [PROOF_MODEL.md](PROOF_MODEL.md) for the cumulative level definitions.

## Clean-room check

```bash
git clone https://github.com/h00w/agentic-ai.git
cd agentic-ai
git checkout <commit>
python -m pip install -e ".[dev]"
make proof
cat evidence/out/current/proof-summary.md
```


## Portable proof artifact and signed provenance

Step 3 packages the proof state with `make proof-package` and verifies internal integrity with `make proof-verify`.

The archive contains the Evidence Contract, proof assessment, proof manifest, direct-dependency SPDX SBOM, provenance linkage, schemas, proof model and checksums. Trusted GitHub Actions runs additionally attach SLSA provenance, SBOM and custom proof-manifest attestations to the completed bundle.

Verify the external signature with:

```bash
gh attestation verify --owner h00w evidence/out/current/production-ai-proof-bundle.tar.gz
```

See [PROVENANCE.md](PROVENANCE.md). A valid signature proves provenance and integrity; it does not raise the five-level proof state by itself.
