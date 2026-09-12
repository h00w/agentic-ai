from __future__ import annotations

from dataclasses import asdict, dataclass, field
from time import perf_counter


@dataclass(slots=True)
class TraceEvent:
    name: str
    detail: str
    elapsed_ms: float


@dataclass(slots=True)
class TraceRecorder:
    events: list[TraceEvent] = field(default_factory=list)
    _started: float = field(default_factory=perf_counter)

    def record(self, name: str, detail: str) -> None:
        self.events.append(TraceEvent(name, detail, (perf_counter() - self._started) * 1000))

    def as_dicts(self) -> list[dict[str, object]]:
        return [asdict(event) for event in self.events]
