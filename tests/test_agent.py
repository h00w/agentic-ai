from agentic_ai import AgentController, PolicyEngine, Tool, ToolRegistry


def test_agent_executes_allowed_search():
    registry = ToolRegistry([Tool("search", "mock", lambda args: "grounded evidence")])
    result = AgentController(registry, PolicyEngine({"search"})).run("Research agent security")
    assert result.answer == "grounded evidence"
    assert result.state.completed
    assert result.policy_decisions == ("search:allow",)


def test_agent_blocks_unapproved_tool():
    registry = ToolRegistry([Tool("search", "mock", lambda args: "should not run")])
    result = AgentController(registry, PolicyEngine(set())).run("Research anything")
    assert "blocked" in result.answer.lower()


def test_write_tool_requires_approval_even_when_allowlisted():
    calls = []
    registry = ToolRegistry(
        [
            Tool(
                "write",
                "Change a record",
                lambda args: calls.append(args) or "updated",
                read_only=False,
            )
        ]
    )
    result = AgentController(registry, PolicyEngine({"write"})).run("Update a record")
    assert calls == []
    assert not result.state.completed
    assert result.policy_decisions == ("write:require_approval",)
    assert "approval required" in result.answer.lower()
