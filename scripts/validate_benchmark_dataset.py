from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

DATA_DIR = Path("dataset/data")
REQUIRED = {
    "id",
    "domain",
    "input",
    "context",
    "expected",
    "expected_label",
    "risk_level",
    "tags",
    "rationale",
}
VALID_RISK = {"low", "medium", "high", "critical"}


def main() -> None:
    files = sorted(DATA_DIR.glob("*.jsonl"))
    if not files:
        raise SystemExit("No benchmark JSONL files found")

    seen: set[str] = set()
    domains: Counter[str] = Counter()
    total = 0

    for path in files:
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            missing = REQUIRED - record.keys()
            if missing:
                raise SystemExit(f"{path}:{line_no} missing fields: {sorted(missing)}")
            if record["id"] in seen:
                raise SystemExit(f"Duplicate id: {record['id']}")
            if record["risk_level"] not in VALID_RISK:
                raise SystemExit(f"{path}:{line_no} invalid risk_level")
            if not isinstance(record["tags"], list) or not record["tags"]:
                raise SystemExit(f"{path}:{line_no} tags must be a non-empty list")
            seen.add(record["id"])
            domains[record["domain"]] += 1
            total += 1

    expected_domains = {
        "task_success",
        "tool_routing",
        "rag_groundedness",
        "prompt_injection",
        "unsafe_tool_requests",
        "policy_decisions",
        "multi_agent_tasks",
        "regression_cases",
    }
    if set(domains) != expected_domains:
        raise SystemExit(f"Domain mismatch: {sorted(domains)}")
    if any(count < 6 for count in domains.values()):
        raise SystemExit(f"Each domain needs at least 6 cases: {dict(domains)}")

    print(f"Validated {total} benchmark cases across {len(domains)} domains")
    for domain, count in sorted(domains.items()):
        print(f"- {domain}: {count}")


if __name__ == "__main__":
    main()
