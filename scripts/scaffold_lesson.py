from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum"
ARTIFACT_TYPES = {
    "code",
    "skill",
    "agent",
    "mcp",
    "schema",
    "policy",
    "evaluation",
    "trace",
    "threat_model",
    "runbook",
    "architecture",
    "release_evidence",
}


def find_module(module_id: str) -> Path:
    matches = sorted(CURRICULUM.glob(f"{module_id}-*"))
    if len(matches) != 1:
        raise SystemExit(f"Expected exactly one module for {module_id}; found {len(matches)}")
    return matches[0]


def build_files(
    *,
    module_id: str,
    lesson_no: str,
    slug: str,
    title: str,
    level: str,
    duration: int,
    artifact_type: str,
) -> dict[Path, str]:
    if not re.fullmatch(r"[0-9]{2}", module_id):
        raise SystemExit("--module must be two digits, for example 06")
    if not re.fullmatch(r"[0-9]{2}", lesson_no):
        raise SystemExit("--lesson must be two digits, for example 02")
    if artifact_type not in ARTIFACT_TYPES:
        raise SystemExit(f"Unsupported artifact type: {artifact_type}")

    module_dir = find_module(module_id)
    target = module_dir / f"{lesson_no}-{slug}"
    lesson_id = f"{module_id}.{lesson_no}"
    artifact_path = target / "artifacts" / "artifact.json"
    worksheet_path = target / "artifacts" / "worksheet.md"

    readme = f"""# Lesson {lesson_id} — {title}

## UNDERSTAND

Define the mechanism, system boundary, deterministic controls and uncertainty.

## BUILD

Implement or complete the reusable worksheet for this lesson.

## BREAK

Exercise one bounded failure in an environment you own or are authorized to test.

## MEASURE

Define success and failure criteria.

## SECURE

Document trust boundaries, permissions, validation and approval behavior.

## SHIP

Retain the artifact manifest and worksheet as reviewable evidence.

## OPERATE

Define traces, metrics, budgets and incident signals.

## GOVERN

State ownership, review requirements and release blockers.
"""

    metadata = {
        "id": lesson_id,
        "title": title,
        "module": module_id,
        "level": level,
        "duration_minutes": duration,
        "prerequisites": [],
        "outcomes": [
            f"Explain the core mechanism of {title}",
            "Demonstrate a controlled failure and measurable acceptance criterion",
            "Produce a reusable evidence artifact",
        ],
        "artifacts": [artifact_path.relative_to(ROOT).as_posix()],
    }
    artifact = {
        "id": f"artifact-{module_id}-{lesson_no}-{slug}",
        "type": artifact_type,
        "source_lesson": lesson_id,
        "summary": f"Reusable worksheet produced by {title}.",
        "paths": [worksheet_path.relative_to(ROOT).as_posix()],
        "evidence": [
            {
                "kind": "worksheet",
                "path": worksheet_path.relative_to(ROOT).as_posix(),
                "claim": "The worksheet records the lesson's bounded engineering evidence.",
            }
        ],
        "maturity": "learning",
    }
    worksheet = f"""# {title} — Engineering Worksheet

## Problem
- Goal:
- System boundary:
- Deterministic controls:
- Uncertainty:

## Failure
- Failure condition:
- Expected safe behavior:

## Measurement
- Metric:
- Threshold:
- Evidence:

## Security
- Trust boundary:
- Permission:
- Approval condition:

## Operations
- Trace or metric:
- Recovery:
- Owner:
"""

    return {
        target / "README.md": readme,
        target / "lesson.json": json.dumps(metadata, indent=2) + "\n",
        artifact_path: json.dumps(artifact, indent=2) + "\n",
        worksheet_path: worksheet,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold an Academy deep lesson.")
    parser.add_argument("--module", required=True)
    parser.add_argument("--lesson", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument(
        "--level",
        default="intermediate",
        choices=("beginner", "intermediate", "advanced", "leadership"),
    )
    parser.add_argument("--duration", type=int, default=75)
    parser.add_argument("--artifact-type", required=True, choices=sorted(ARTIFACT_TYPES))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    files = build_files(
        module_id=args.module,
        lesson_no=args.lesson,
        slug=args.slug,
        title=args.title,
        level=args.level,
        duration=args.duration,
        artifact_type=args.artifact_type,
    )
    target = next(iter(files)).parent
    if target.exists():
        raise SystemExit(f"Refusing to overwrite existing lesson directory: {target}")

    if args.dry_run:
        for path in files:
            print(path.relative_to(ROOT))
        return

    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Created {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
