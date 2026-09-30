import pytest

from agentic_ai.providers.mock import MockProvider
from evaluation.provider_benchmark import (
    ProviderBenchmarkCase,
    ProviderBenchmarkResult,
    compare_provider_runs,
    run_provider_case,
)


def test_provider_benchmark_case_passes_for_expected_term():
    result = run_provider_case(
        MockProvider(),
        model="mock-1",
        case=ProviderBenchmarkCase(
            case_id="provider-001",
            prompt="grounded evidence",
            expected_terms=("evidence",),
        ),
    )
    assert result.passed
    assert result.provider == "mock"


@pytest.mark.parametrize(
    "case",
    [
        ProviderBenchmarkCase("", "prompt", ("term",)),
        ProviderBenchmarkCase("a", "  ", ("term",)),
        ProviderBenchmarkCase("a", "prompt", ()),
        ProviderBenchmarkCase("a", "prompt", (" ",)),
    ],
)
def test_empty_benchmark_case_cannot_pass(case):
    with pytest.raises(ValueError, match="benchmark case requires"):
        run_provider_case(MockProvider(), model="mock-1", case=case)


def _result(case_id: str, passed: bool) -> ProviderBenchmarkResult:
    return ProviderBenchmarkResult(case_id, "mock", "mock-1", passed, 10.0, 5)


def test_comparison_exposes_missing_cases_and_regressions():
    comparison = compare_provider_runs(
        [_result("a", True), _result("b", True)],
        [_result("a", False), _result("c", True)],
    )
    assert not comparison.aligned
    assert comparison.regressed_case_ids == ("a",)
    assert comparison.missing_case_ids == ("b",)
    assert comparison.unexpected_case_ids == ("c",)


def test_comparison_rejects_duplicate_cases():
    try:
        compare_provider_runs([_result("a", True), _result("a", False)], [_result("a", True)])
    except ValueError as exc:
        assert "duplicate" in str(exc)
    else:
        raise AssertionError("duplicate cases must be rejected")


def test_comparison_rejects_mixed_provider_identity():
    import pytest

    with pytest.raises(ValueError, match="mixes provider/model"):
        compare_provider_runs(
            [_result("a", True), ProviderBenchmarkResult("b", "other", "model-2", True, 10.0, 5)],
            [_result("a", True)],
        )


def test_comparison_rejects_invalid_latency_and_token_evidence():
    import pytest

    for invalid in (
        ProviderBenchmarkResult("a", "mock", "mock-1", True, float("nan"), 5),
        ProviderBenchmarkResult("a", "mock", "mock-1", True, 10.0, -1),
    ):
        with pytest.raises(ValueError, match="invalid benchmark result"):
            compare_provider_runs([invalid], [_result("a", True)])
