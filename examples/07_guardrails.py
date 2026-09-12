from agentic_ai.models import RiskLevel
from agentic_ai.policy import PolicyEngine

policy = PolicyEngine(allowed_tools={"search", "calculator"}, approval_tools={"email"})
for tool in ["search", "email", "export_database"]:
    print(tool, policy.evaluate(tool, RiskLevel.LOW).value)
