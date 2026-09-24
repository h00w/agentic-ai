from __future__ import annotations

from time import perf_counter

from agentic_ai.contracts import ProviderRequest, ProviderResponse, ProviderUsage

from .base import LLMProvider


class GeminiProvider(LLMProvider):
    name = "gemini"

    def __init__(self, client=None) -> None:
        if client is None:
            try:
                from google import genai
            except ImportError as exc:
                raise RuntimeError(
                    "Gemini support requires the optional 'providers' dependency group."
                ) from exc
            client = genai.Client()
        self.client = client

    def generate(self, request: ProviderRequest) -> ProviderResponse:
        started = perf_counter()
        contents = "\n".join(f"{m.role}: {m.content}" for m in request.messages)
        response = self.client.models.generate_content(
            model=request.model,
            contents=contents,
        )
        text = getattr(response, "text", "") or ""
        return ProviderResponse(
            provider=self.name,
            model=request.model,
            text=text,
            usage=ProviderUsage(),
            latency_ms=(perf_counter() - started) * 1000,
        )
