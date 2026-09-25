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
        system_messages = [
            message.content for message in request.messages if message.role == "system"
        ]
        contents = [
            {
                "role": "model" if message.role == "assistant" else "user",
                "parts": [
                    {
                        "text": (
                            message.content
                            if message.role in {"user", "assistant"}
                            else f"{message.role}: {message.content}"
                        )
                    }
                ],
            }
            for message in request.messages
            if message.role != "system"
        ]
        if not contents:
            contents = [{"role": "user", "parts": [{"text": ""}]}]

        kwargs = {"model": request.model, "contents": contents}
        if system_messages:
            kwargs["config"] = {"system_instruction": "\n".join(system_messages)}
        response = self.client.models.generate_content(**kwargs)
        text = getattr(response, "text", "") or ""
        return ProviderResponse(
            provider=self.name,
            model=request.model,
            text=text,
            usage=ProviderUsage(),
            latency_ms=(perf_counter() - started) * 1000,
        )
