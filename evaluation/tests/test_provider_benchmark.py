from agentic_ai.providers.mock import MockProvider
from evaluation.provider_benchmark import ProviderBenchmarkCase, run_provider_case


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
