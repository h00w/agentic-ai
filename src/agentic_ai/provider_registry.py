from __future__ import annotations

from collections.abc import Callable
from importlib import import_module

from agentic_ai.providers.base import LLMProvider

ProviderFactory = Callable[[], LLMProvider]


def provider_factory(module_name: str, class_name: str) -> ProviderFactory:
    def factory() -> LLMProvider:
        module = import_module(module_name)
        provider_class = getattr(module, class_name)
        return provider_class()

    return factory


class ProviderRegistry:
    def __init__(self) -> None:
        self._factories: dict[str, ProviderFactory] = {
            "anthropic": provider_factory("agentic_ai.providers.anthropic", "AnthropicProvider"),
            "gemini": provider_factory("agentic_ai.providers.gemini", "GeminiProvider"),
            "mock": provider_factory("agentic_ai.providers.mock", "MockProvider"),
            "ollama": provider_factory("agentic_ai.providers.ollama", "OllamaProvider"),
            "openai": provider_factory("agentic_ai.providers.openai", "OpenAIProvider"),
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
