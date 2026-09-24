from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class Message(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: str


class ToolSpec(BaseModel):
    name: str
    description: str
    input_schema: dict[str, Any] = Field(default_factory=dict)


class ProviderRequest(BaseModel):
    messages: list[Message]
    model: str
    temperature: float = Field(default=0.0, ge=0.0, le=2.0)
    max_tokens: int = Field(default=512, ge=1)
    tools: list[ToolSpec] = Field(default_factory=list)
    response_schema: dict[str, Any] | None = None


class ProviderUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class ProviderResponse(BaseModel):
    provider: str
    model: str
    text: str
    structured: dict[str, Any] | None = None
    tool_calls: list[dict[str, Any]] = Field(default_factory=list)
    usage: ProviderUsage = Field(default_factory=ProviderUsage)
    latency_ms: float = 0.0
