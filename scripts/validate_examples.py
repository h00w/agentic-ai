from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
examples = sorted((ROOT / "examples").glob("*.py"))
env = os.environ.copy()
env["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + env.get("PYTHONPATH", "")
for example in examples:
    completed = subprocess.run([sys.executable, str(example)], cwd=ROOT, capture_output=True, text=True, timeout=10, env=env)
    if completed.returncode != 0:
        print(completed.stdout)
        print(completed.stderr, file=sys.stderr)
        raise SystemExit(f"Example failed: {example.name}")
    print(f"PASS {example.name}")
