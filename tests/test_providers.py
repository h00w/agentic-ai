import pytest
from pydantic import ValidationError

from agentic_ai.contracts import Message, ProviderRequest
from agentic_ai.provider_registry import ProviderRegistry
from agentic_ai.providers.gemini import GeminiProvider
from agentic_ai.providers.mock import MockProvider
from agentic_ai.providers.openai import OpenAIProvider


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
    assert registry.names() == ("anthropic", "gemini", "mock", "ollama", "openai")
    assert isinstance(registry.create("mock"), MockProvider)


def test_registry_rejects_unknown_provider():
    with pytest.raises(KeyError):
        ProviderRegistry().create("missing")


def test_registry_supports_custom_registration():
    registry = ProviderRegistry()
    registry.register("custom", MockProvider)

    assert "custom" in registry.names()
    assert isinstance(registry.create("custom"), MockProvider)


def test_openai_provider_uses_structured_responses_input():
    calls = []

    class FakeResponses:
        def create(self, **kwargs):
            calls.append(kwargs)
            return type(
                "Response",
                (),
                {
                    "output_text": "done",
                    "usage": type("Usage", (), {"input_tokens": 3, "output_tokens": 2})(),
                },
            )()

    client = type("Client", (), {"responses": FakeResponses()})()
    provider = OpenAIProvider(client=client)
    response = provider.generate(
        ProviderRequest(
            model="gpt-test",
            messages=[
                Message(role="system", content="system rule"),
                Message(role="user", content="hello"),
                Message(role="assistant", content="prior reply"),
            ],
        )
    )

    assert response.text == "done"
    assert calls[0]["input"] == [
        {"role": "system", "content": [{"type": "input_text", "text": "system rule"}]},
        {"role": "user", "content": [{"type": "input_text", "text": "hello"}]},
        {
            "role": "assistant",
            "content": [{"type": "input_text", "text": "prior reply"}],
        },
    ]


def test_gemini_provider_preserves_turn_structure():
    calls = []

    class FakeModels:
        def generate_content(self, **kwargs):
            calls.append(kwargs)
            return type("Response", (), {"text": "done"})()

    client = type("Client", (), {"models": FakeModels()})()
    provider = GeminiProvider(client=client)
    response = provider.generate(
        ProviderRequest(
            model="gemini-test",
            messages=[
                Message(role="system", content="system rule"),
                Message(role="user", content="hello"),
                Message(role="assistant", content="prior reply"),
                Message(role="tool", content="tool output"),
            ],
        )
    )

    assert response.text == "done"
    assert calls[0] == {
        "model": "gemini-test",
        "contents": [
            {"role": "user", "parts": [{"text": "hello"}]},
            {"role": "model", "parts": [{"text": "prior reply"}]},
            {"role": "user", "parts": [{"text": "tool: tool output"}]},
        ],
        "config": {"system_instruction": "system rule"},
    }
