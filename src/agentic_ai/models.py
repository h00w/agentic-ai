from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ToolCall(BaseModel):
    name: str
    arguments: dict[str, Any] = Field(default_factory=dict)


class Observation(BaseModel):
    tool: str
    success: bool
    output: str


class AgentState(BaseModel):
    goal: str
    steps: int = 0
    observations: list[Observation] = Field(default_factory=list)
    completed: bool = False
