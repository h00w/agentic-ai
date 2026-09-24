from __future__ import annotations

from collections.abc import Callable

from agentic_ai.providers.base import LLMProvider
from agentic_ai.providers.mock import MockProvider


ProviderFactory = Callable[[], LLMProvider]


class ProviderRegistry:
    def __init__(self) -> None:
        self._factories: dict[str, ProviderFactory] = {"mock": MockProvider}

    def register(self, name: str, factory: ProviderFactory) -> None:
        self._factories[name] = factory

    def create(self, name: str) -> LLMProvider:
        try:
            return self._factories[name]()
        except KeyError as exc:
            available = ", ".join(sorted(self._factories))
            raise KeyError(f"Unknown provider '{name}'. Available: {available}") from exc

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._factories))
