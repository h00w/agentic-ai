from __future__ import annotations

from collections.abc import Callable

from agentic_ai.providers.anthropic import AnthropicProvider
from agentic_ai.providers.base import LLMProvider
from agentic_ai.providers.gemini import GeminiProvider
from agentic_ai.providers.mock import MockProvider
from agentic_ai.providers.ollama import OllamaProvider
from agentic_ai.providers.openai import OpenAIProvider

ProviderFactory = Callable[[], LLMProvider]


class ProviderRegistry:
    def __init__(self) -> None:
        self._factories: dict[str, ProviderFactory] = {
            "anthropic": AnthropicProvider,
            "gemini": GeminiProvider,
            "mock": MockProvider,
            "ollama": OllamaProvider,
            "openai": OpenAIProvider,
        }

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
