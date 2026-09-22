from __future__ import annotations

from dataclasses import dataclass

from agentic_ai.contracts import Message, ProviderRequest
from agentic_ai.providers.base import LLMProvider


@dataclass(frozen=True, slots=True)
class ProviderBenchmarkCase:
    case_id: str
    prompt: str
    expected_terms: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ProviderBenchmarkResult:
    case_id: str
    provider: str
    model: str
    passed: bool
    latency_ms: float
    total_tokens: int


def run_provider_case(
    provider: LLMProvider,
    *,
    model: str,
    case: ProviderBenchmarkCase,
) -> ProviderBenchmarkResult:
    response = provider.generate(
        ProviderRequest(
            model=model,
            messages=[Message(role="user", content=case.prompt)],
        )
    )
    lowered = response.text.lower()
    passed = all(term.lower() in lowered for term in case.expected_terms)
    return ProviderBenchmarkResult(
        case_id=case.case_id,
        provider=response.provider,
        model=response.model,
        passed=passed,
        latency_ms=response.latency_ms,
        total_tokens=response.usage.total_tokens,
    )
