from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SandboxPlan:
    image: str = "python:3.12-slim"
    network_enabled: bool = False
    cpu_limit: str = "0.5"
    memory_limit: str = "256m"
    timeout_seconds: int = 5
    read_only_root: bool = True


def validate_code_for_demo(code: str) -> tuple[bool, str]:
    """Static teaching gate only; not a substitute for an actual sandbox.

    The academy intentionally does not execute generated code on the host. Production systems
    should execute inside an isolated container/microVM with network, filesystem, syscall, CPU,
    memory and time limits.
    """
    blocked = ("subprocess", "os.system", "eval(", "exec(", "socket", "requests.", "urllib")
    lowered = code.lower()
    for token in blocked:
        if token in lowered:
            return False, f"blocked token: {token}"
    return True, "static checks passed; isolated execution still required"
