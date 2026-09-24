from __future__ import annotations

import json
from time import perf_counter
from urllib.request import Request, urlopen

from agentic_ai.contracts import ProviderRequest, ProviderResponse, ProviderUsage

from .base import LLMProvider


class OllamaProvider(LLMProvider):
    name = "ollama"

    def __init__(self, base_url: str = "http://localhost:11434") -> None:
        self.base_url = base_url.rstrip("/")

    def generate(self, request: ProviderRequest) -> ProviderResponse:
        started = perf_counter()
        payload = json.dumps(
            {
                "model": request.model,
                "messages": [m.model_dump() for m in request.messages],
                "stream": False,
                "options": {"temperature": request.temperature},
            }
        ).encode()
        req = Request(
            f"{self.base_url}/api/chat",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(req, timeout=60) as response:
            body = json.loads(response.read().decode())
        text = body.get("message", {}).get("content", "")
        prompt_tokens = int(body.get("prompt_eval_count", 0) or 0)
        completion_tokens = int(body.get("eval_count", 0) or 0)
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
