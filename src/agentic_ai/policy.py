from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from .models import RiskLevel


class PolicyDecision(StrEnum):
    ALLOW = "allow"
    REQUIRE_APPROVAL = "require_approval"
    DENY = "deny"


@dataclass(slots=True)
class PolicyEngine:
    allowed_tools: set[str]
    approval_tools: set[str] | None = None

    def evaluate(self, tool_name: str, risk: RiskLevel = RiskLevel.LOW) -> PolicyDecision:
        if tool_name not in self.allowed_tools:
            return PolicyDecision.DENY
        if risk in {RiskLevel.HIGH, RiskLevel.CRITICAL}:
            return PolicyDecision.REQUIRE_APPROVAL
        if self.approval_tools and tool_name in self.approval_tools:
            return PolicyDecision.REQUIRE_APPROVAL
        return PolicyDecision.ALLOW
