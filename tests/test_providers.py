import pytest
from pydantic import ValidationError

from agentic_ai.contracts import Message, ProviderRequest
from agentic_ai.provider_registry import ProviderRegistry
from agentic_ai.providers.anthropic import AnthropicProvider
from agentic_ai.providers.gemini import GeminiProvider
from agentic_ai.providers.mock import MockProvider
from agentic_ai.providers.ollama import OllamaProvider
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
                Message(role="tool", content="tool output"),
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
        {
            "role": "assistant",
            "content": [{"type": "input_text", "text": "tool: tool output"}],
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


def test_anthropic_provider_normalizes_assistant_and_tool_messages():
    calls = []

    class FakeMessages:
        def create(self, **kwargs):
            calls.append(kwargs)
            return type(
                "Response",
                (),
                {
                    "content": [type("Block", (), {"text": "done"})()],
                    "usage": type("Usage", (), {"input_tokens": 4, "output_tokens": 2})(),
                },
            )()

    client = type("Client", (), {"messages": FakeMessages()})()
    provider = AnthropicProvider(client=client)
    response = provider.generate(
        ProviderRequest(
            model="claude-test",
            messages=[
                Message(role="system", content="system rule"),
                Message(role="assistant", content="prior reply"),
                Message(role="tool", content="tool output"),
            ],
        )
    )

    assert response.text == "done"
    assert calls[0]["messages"] == [
        {
            "role": "assistant",
            "content": [{"type": "text", "text": "prior reply"}],
        },
        {
            "role": "assistant",
            "content": [{"type": "text", "text": "tool: tool output"}],
        },
    ]


def test_ollama_provider_passes_max_tokens():
    payloads = []

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def read(self):
            return b'{"message":{"content":"done"},"prompt_eval_count":3,"eval_count":2}'

    def fake_urlopen(request, timeout):
        payloads.append(request.data.decode())
        return FakeResponse()

    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr("agentic_ai.providers.ollama.urlopen", fake_urlopen)
    try:
        provider = OllamaProvider(base_url="http://example.test")
        response = provider.generate(
            ProviderRequest(
                model="ollama-test",
                messages=[Message(role="user", content="hello")],
                max_tokens=42,
            )
        )
    finally:
        monkeypatch.undo()

    assert response.text == "done"
    assert '"num_predict": 42' in payloads[0]
