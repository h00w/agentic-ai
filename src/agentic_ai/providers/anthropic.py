from __future__ import annotations

from time import perf_counter

from agentic_ai.contracts import ProviderRequest, ProviderResponse, ProviderUsage

from .base import LLMProvider


class AnthropicProvider(LLMProvider):
    name = "anthropic"

    def __init__(self, client=None) -> None:
        if client is None:
            try:
                from anthropic import Anthropic
            except ImportError as exc:
                raise RuntimeError(
                    "Anthropic support requires the optional 'providers' dependency group."
                ) from exc
            client = Anthropic()
        self.client = client

    def generate(self, request: ProviderRequest) -> ProviderResponse:
        started = perf_counter()
        system = "\n".join(m.content for m in request.messages if m.role == "system")
        messages = [m.model_dump() for m in request.messages if m.role != "system"]
        response = self.client.messages.create(
            model=request.model,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            system=system or None,
            messages=messages,
        )
        text = "".join(getattr(block, "text", "") for block in response.content)
        usage_obj = getattr(response, "usage", None)
        prompt_tokens = int(getattr(usage_obj, "input_tokens", 0) or 0)
        completion_tokens = int(getattr(usage_obj, "output_tokens", 0) or 0)
        return ProviderResponse(
            provider=self.name,
            model=request.model,
            text=text,
            usage=ProviderUsage(
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=prompt_tokens + completion_tokens,
            ),
            latency_ms=(perf_counter() - started) * 1000,
        )
