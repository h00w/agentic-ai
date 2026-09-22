from __future__ import annotations

from time import perf_counter

from agentic_ai.contracts import ProviderRequest, ProviderResponse, ProviderUsage

from .base import LLMProvider


class MockProvider(LLMProvider):
    name = "mock"

    def generate(self, request: ProviderRequest) -> ProviderResponse:
        started = perf_counter()
        user_messages = [m.content for m in request.messages if m.role == "user"]
        text = user_messages[-1] if user_messages else ""
        structured = None
        if request.response_schema is not None:
            structured = {"answer": text}
        elapsed_ms = (perf_counter() - started) * 1000
        prompt_tokens = sum(len(m.content.split()) for m in request.messages)
        completion_tokens = len(text.split())
        return ProviderResponse(
            provider=self.name,
            model=request.model,
            text=text,
            structured=structured,
            usage=ProviderUsage(
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=prompt_tokens + completion_tokens,
            ),
            latency_ms=elapsed_ms,
        )
