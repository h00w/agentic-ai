from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from agentic_ai.contracts import Message, ProviderRequest
from agentic_ai.evaluation import evaluate_result
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


@dataclass(frozen=True, slots=True)
class ProviderComparison:
    aligned: bool
    baseline_pass_rate: float
    candidate_pass_rate: float
    regressed_case_ids: tuple[str, ...]
    missing_case_ids: tuple[str, ...]
    unexpected_case_ids: tuple[str, ...]


def compare_provider_runs(
    baseline: Iterable[ProviderBenchmarkResult],
    candidate: Iterable[ProviderBenchmarkResult],
) -> ProviderComparison:
    def indexed(rows: Iterable[ProviderBenchmarkResult]) -> dict[str, ProviderBenchmarkResult]:
        result: dict[str, ProviderBenchmarkResult] = {}
        identity: tuple[str, str] | None = None
        for row in rows:
            if not row.case_id.strip() or not row.provider.strip() or not row.model.strip():
                raise ValueError("benchmark case and provider/model identity must be non-empty")
            if identity is None:
                identity = (row.provider, row.model)
            elif identity != (row.provider, row.model):
                raise ValueError("benchmark run mixes provider/model identities")
            if row.case_id in result:
                raise ValueError(f"duplicate benchmark case_id: {row.case_id}")
            result[row.case_id] = row
        if not result:
            raise ValueError("benchmark run must contain cases")
        return result

    base = indexed(baseline)
    cand = indexed(candidate)
    missing = tuple(sorted(base.keys() - cand.keys()))
    unexpected = tuple(sorted(cand.keys() - base.keys()))
    regressions = tuple(
        sorted(
            case_id
            for case_id in base.keys() & cand.keys()
            if base[case_id].passed and not cand[case_id].passed
        )
    )
    return ProviderComparison(
        aligned=not missing and not unexpected,
        baseline_pass_rate=sum(row.passed for row in base.values()) / len(base),
        candidate_pass_rate=sum(row.passed for row in cand.values()) / len(cand),
        regressed_case_ids=regressions,
        missing_case_ids=missing,
        unexpected_case_ids=unexpected,
    )


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
    passed = (
        evaluate_result(expected_terms=list(case.expected_terms), answer=response.text).task_success
        == 1.0
    )
    return ProviderBenchmarkResult(
        case_id=case.case_id,
        provider=response.provider,
        model=response.model,
        passed=passed,
        latency_ms=response.latency_ms,
        total_tokens=response.usage.total_tokens,
    )
