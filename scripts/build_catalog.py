from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum"
SKILLS = ROOT / "skills"
OUTPUT = ROOT / "catalog.json"


def build_catalog() -> dict[str, object]:
    modules: list[dict[str, object]] = []
    for readme in sorted(CURRICULUM.glob("[0-9][0-9]-*/README.md")):
        module_dir = readme.parent
        module_id, slug = module_dir.name.split("-", 1)
        modules.append(
            {
                "id": module_id,
                "slug": slug,
                "path": module_dir.relative_to(ROOT).as_posix(),
                "lesson_count": sum(1 for _ in module_dir.glob("*/lesson.json")),
            }
        )

    lessons: list[dict[str, object]] = []
    for metadata_path in sorted(CURRICULUM.glob("[0-9][0-9]-*/*/lesson.json")):
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata["path"] = metadata_path.parent.relative_to(ROOT).as_posix()
        lessons.append(metadata)

    skills = [
        {"name": f.parent.name, "path": f.relative_to(ROOT).as_posix()}
        for f in sorted(SKILLS.glob("*/SKILL.md"))
    ]
    return {
        "schema_version": 1,
        "source": "filesystem-derived",
        "modules": modules,
        "lessons": lessons,
        "skills": skills,
        "totals": {
            "modules": len(modules),
            "lessons_with_metadata": len(lessons),
            "skills": len(skills),
        },
    }


def render_catalog(catalog: dict[str, object]) -> str:
    return json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = render_catalog(build_catalog())
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            raise SystemExit("catalog.json is stale; run python scripts/build_catalog.py")
        print("catalog.json is current")
        return
    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
