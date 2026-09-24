import pytest
from pydantic import ValidationError

from agentic_ai.contracts import Message, ProviderRequest
from agentic_ai.provider_registry import ProviderRegistry
from agentic_ai.providers.mock import MockProvider


def test_mock_provider_round_trip():
    provider = MockProvider()
    response = provider.generate(
        ProviderRequest(
            model="mock-1",
            messages=[Message(role="user", content="hello provider layer")],
        )
    )
    assert response.provider == "mock"
    assert response.model == "mock-1"
    assert response.text == "hello provider layer"
    assert response.usage.total_tokens >= 3


def test_provider_request_validates_temperature():
    with pytest.raises(ValidationError):
        ProviderRequest(
            model="mock-1",
            messages=[Message(role="user", content="hello")],
            temperature=3.0,
        )


def test_registry_exposes_mock_provider():
    registry = ProviderRegistry()
    assert "mock" in registry.names()
    assert isinstance(registry.create("mock"), MockProvider)


def test_registry_rejects_unknown_provider():
    with pytest.raises(KeyError):
        ProviderRegistry().create("missing")
