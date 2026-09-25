from __future__ import annotations

import json
import re
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
LESSON_HEADINGS = (
    "## UNDERSTAND",
    "## BUILD",
    "## BREAK",
    "## MEASURE",
    "## SECURE",
    "## SHIP",
    "## OPERATE",
    "## GOVERN",
)


def main() -> None:
    errors: list[str] = []
    for path in (
        ROOT / "LESSON_TEMPLATE.md",
        ROOT / "lesson-schema.json",
        ROOT / "artifact-schema.json",
        ROOT / "docs" / "academy-learning-contract.md",
    ):
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    modules = sorted(path.parent for path in CURRICULUM.glob("[0-9][0-9]-*/README.md"))
    if len(modules) < 16:
        errors.append(f"expected at least 16 modules, found {len(modules)}")

    lesson_ids: set[str] = set()
    module_lesson_counts: dict[str, int] = {
        module.name.split("-", 1)[0]: 0 for module in modules
    }
    artifact_count = 0

    for meta_path in sorted(CURRICULUM.glob("[0-9][0-9]-*/*/lesson.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        missing = LESSON_FIELDS - meta.keys()
        if missing:
            errors.append(f"{meta_path.relative_to(ROOT)} missing: {sorted(missing)}")
            continue

        module_id = meta_path.parents[1].name.split("-", 1)[0]
        module_lesson_counts[module_id] = module_lesson_counts.get(module_id, 0) + 1

        if meta["id"] in lesson_ids:
            errors.append(f"duplicate lesson id: {meta['id']}")
        lesson_ids.add(meta["id"])

        if not re.fullmatch(r"[0-9]{2}\.[0-9]{2}", meta["id"]):
            errors.append(f"{meta_path.relative_to(ROOT)} invalid lesson id")
        if meta["module"] != module_id or not meta["id"].startswith(f"{module_id}."):
            errors.append(f"{meta_path.relative_to(ROOT)} module mismatch")
        if not isinstance(meta["duration_minutes"], int) or meta["duration_minutes"] < 15:
            errors.append(f"{meta_path.relative_to(ROOT)} invalid duration")
        if not isinstance(meta["outcomes"], list) or not meta["outcomes"]:
            errors.append(f"{meta_path.relative_to(ROOT)} outcomes must be non-empty")
        if not isinstance(meta["artifacts"], list) or not meta["artifacts"]:
            errors.append(f"{meta_path.relative_to(ROOT)} artifacts must be non-empty")

        readme_path = meta_path.parent / "README.md"
        if not readme_path.exists():
            errors.append(f"{meta_path.relative_to(ROOT)} missing README.md")
        else:
            readme = readme_path.read_text(encoding="utf-8")
            for heading in LESSON_HEADINGS:
                if heading not in readme:
                    errors.append(f"{readme_path.relative_to(ROOT)} missing {heading}")

        for ref in meta["artifacts"]:
            artifact_path = ROOT / ref
            if not artifact_path.exists():
                errors.append(f"missing artifact: {ref}")
                continue
            artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
            if artifact.get("source_lesson") != meta["id"]:
                errors.append(f"{ref} source_lesson does not match {meta['id']}")

    uncovered = [module_id for module_id, count in module_lesson_counts.items() if count < 1]
    if uncovered:
        errors.append(f"modules without metadata-backed lessons: {uncovered}")

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
        f"Curriculum audit passed: {len(modules)}/{len(modules)} modules covered, "
        f"{len(lesson_ids)} metadata-backed lessons, "
        f"{artifact_count} artifact manifests, {skill_count} skills"
    )


if __name__ == "__main__":
    main()
