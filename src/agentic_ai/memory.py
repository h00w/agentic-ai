from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class MemoryStore:
    """Simple in-memory learning reference; replace with durable storage in production."""

    items: list[str] = field(default_factory=list)

    def add(self, item: str) -> None:
        self.items.append(item)

    def recent(self, limit: int = 5) -> list[str]:
        if limit <= 0:
            return []
        return self.items[-limit:]

    def search(self, query: str, limit: int = 5) -> list[str]:
        terms = {term.lower() for term in query.split() if term}
        scored: list[tuple[int, str]] = []
        for item in self.items:
            score = sum(term in item.lower() for term in terms)
            if score:
                scored.append((score, item))
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [item for _, item in scored[:limit]]
