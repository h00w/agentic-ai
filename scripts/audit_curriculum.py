from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum"
SKILLS = ROOT / "skills"
LESSON_FIELDS = {
    "id",
    "title",
    "module",
    "level",
    "duration_minutes",
    "prerequisites",
    "outcomes",
    "artifacts",
}
ARTIFACT_FIELDS = {"id", "type", "source_lesson", "summary", "paths", "evidence", "maturity"}
SKILL_HEADINGS = (
    "# Objective",
    "# Inputs",
    "# Procedure",
    "# Failure conditions",
    "# Evidence produced",
)


def main() -> None:
    errors: list[str] = []
    for path in (
        ROOT / "LESSON_TEMPLATE.md",
        ROOT / "artifact-schema.json",
        ROOT / "docs" / "academy-learning-contract.md",
    ):
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    modules = sorted(p.parent for p in CURRICULUM.glob("[0-9][0-9]-*/README.md"))
    if len(modules) < 16:
        errors.append(f"expected at least 16 modules, found {len(modules)}")

    lesson_count = 0
    artifact_count = 0
    for meta_path in sorted(CURRICULUM.glob("[0-9][0-9]-*/*/lesson.json")):
        lesson_count += 1
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        missing = LESSON_FIELDS - meta.keys()
        if missing:
            errors.append(f"{meta_path.relative_to(ROOT)} missing: {sorted(missing)}")
            continue
        if meta["module"] != meta_path.parents[1].name.split("-", 1)[0]:
            errors.append(f"{meta_path.relative_to(ROOT)} module mismatch")
        if not (meta_path.parent / "README.md").exists():
            errors.append(f"{meta_path.relative_to(ROOT)} missing README.md")
        for ref in meta["artifacts"]:
            if not (ROOT / ref).exists():
                errors.append(f"missing artifact: {ref}")

    for path in sorted(CURRICULUM.glob("[0-9][0-9]-*/*/artifacts/artifact.json")):
        artifact_count += 1
        artifact = json.loads(path.read_text(encoding="utf-8"))
        missing = ARTIFACT_FIELDS - artifact.keys()
        if missing:
            errors.append(f"{path.relative_to(ROOT)} missing: {sorted(missing)}")
            continue
        for ref in artifact["paths"]:
            if not (ROOT / ref).exists():
                errors.append(f"{path.relative_to(ROOT)} missing path: {ref}")
        for evidence in artifact["evidence"]:
            if not (ROOT / evidence["path"]).exists():
                errors.append(f"{path.relative_to(ROOT)} missing evidence: {evidence['path']}")

    skill_count = 0
    for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
        skill_count += 1
        content = skill_file.read_text(encoding="utf-8")
        for heading in SKILL_HEADINGS:
            if heading not in content:
                errors.append(f"{skill_file.relative_to(ROOT)} missing {heading}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(f"Curriculum audit failed with {len(errors)} error(s)")

    print(
        f"Curriculum audit passed: {len(modules)} modules, "
        f"{lesson_count} metadata-backed lessons, "
        f"{artifact_count} artifact manifests, {skill_count} skills"
    )


if __name__ == "__main__":
    main()
