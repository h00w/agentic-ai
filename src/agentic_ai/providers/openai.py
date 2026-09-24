from __future__ import annotations

from time import perf_counter

from agentic_ai.contracts import ProviderRequest, ProviderResponse, ProviderUsage

from .base import LLMProvider


class OpenAIProvider(LLMProvider):
    name = "openai"

    def __init__(self, client=None) -> None:
        if client is None:
            try:
                from openai import OpenAI
            except ImportError as exc:
                raise RuntimeError(
                    "OpenAI support requires the optional 'providers' dependency group."
                ) from exc
            client = OpenAI()
        self.client = client

    def generate(self, request: ProviderRequest) -> ProviderResponse:
        started = perf_counter()
        response = self.client.responses.create(
            model=request.model,
            input=[
                {
                    "role": message.role if message.role != "tool" else "assistant",
                    "content": [
                        {
                            "type": "input_text",
                            "text": (
                                message.content
                                if message.role != "tool"
                                else f"tool: {message.content}"
                            ),
                        }
                    ],
                }
                for message in request.messages
            ],
            temperature=request.temperature,
            max_output_tokens=request.max_tokens,
        )
        text = getattr(response, "output_text", "") or ""
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
