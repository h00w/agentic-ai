from agentic_ai.models import RiskLevel
from agentic_ai.policy import PolicyDecision, PolicyEngine


def test_unknown_tool_is_denied():
    engine = PolicyEngine({"search"})
    assert engine.evaluate("database_write", RiskLevel.LOW) is PolicyDecision.DENY


def test_high_risk_requires_approval():
    engine = PolicyEngine({"search"})
    assert engine.evaluate("search", RiskLevel.HIGH) is PolicyDecision.REQUIRE_APPROVAL
