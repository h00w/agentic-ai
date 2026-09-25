# Lesson Authoring Guide

The Academy scales through **curriculum-as-code**, not by copying prose into folders.

## Contract

Every deep lesson contains:

```text
<lesson>/
├── README.md
├── lesson.json
└── artifacts/
    ├── artifact.json
    └── worksheet.md
```

The README follows:

`UNDERSTAND → BUILD → BREAK → MEASURE → SECURE → SHIP → OPERATE → GOVERN`.

The metadata conforms to `lesson-schema.json`, and reusable evidence conforms to `artifact-schema.json`.

## Scaffold a lesson

Preview without writing:

```bash
python scripts/scaffold_lesson.py \
  --module 06 \
  --lesson 02 \
  --slug retrieval-quality \
  --title "Retrieval Quality and Source Authority" \
  --artifact-type evaluation \
  --dry-run
```

Create the files by removing `--dry-run`.

The scaffolder refuses to overwrite an existing lesson directory.

## Authoring rules

1. Mechanism before framework.
2. At least one controlled failure.
3. At least one measurable acceptance criterion.
4. Explicit trust/permission boundary.
5. Reusable evidence, not just explanatory prose.
6. Operational signal and change-control implication.
7. Benchmark or regression cases when a meaningful failure class is discovered.

## Quality gate

`python scripts/audit_curriculum.py` fails when a module has no metadata-backed deep lesson, lesson metadata is structurally invalid, required lifecycle sections are absent, or artifact/evidence paths are broken.

`python scripts/build_catalog.py --check` ensures the committed catalog matches the filesystem.
