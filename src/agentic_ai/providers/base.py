from __future__ import annotations

from abc import ABC, abstractmethod

from agentic_ai.contracts import ProviderRequest, ProviderResponse


class LLMProvider(ABC):
    name: str

    @abstractmethod
    def generate(self, request: ProviderRequest) -> ProviderResponse:
        """Generate a response for a provider-neutral request."""
        raise NotImplementedError
