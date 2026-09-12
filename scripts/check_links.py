from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
errors = []
for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    for target in pattern.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        path = (md.parent / clean).resolve()
        if not path.exists():
            errors.append(f"{md.relative_to(ROOT)} -> {target}")
if errors:
    raise SystemExit("Broken relative links:\n" + "\n".join(errors))
print("Relative links: OK")
