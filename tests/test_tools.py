import pytest

from agentic_ai.tools import Tool, ToolRegistry


def tool(name="search", response="original"):
    return Tool(name, "Read evidence", lambda arguments: response)


def test_constructor_rejects_duplicate_tool_handlers():
    with pytest.raises(ValueError, match="already registered"):
        ToolRegistry([tool(), tool(response="replacement")])


def test_later_registration_cannot_replace_a_handler():
    registry = ToolRegistry([tool()])
    with pytest.raises(ValueError, match="already registered"):
        registry.register(tool(response="replacement"))
    assert registry.execute("search", {}) == "original"


def test_distinct_tools_remain_available_in_stable_order():
    registry = ToolRegistry([tool("search"), tool("calculator", "42")])
    assert registry.names() == ["calculator", "search"]
    assert registry.execute("calculator", {}) == "42"


@pytest.mark.parametrize(
    "candidate,field",
    [
        (Tool("", "description", lambda arguments: "ok"), "name"),
        (Tool("search", " ", lambda arguments: "ok"), "description"),
        (Tool("search", "description", None), "handler"),
        (Tool("search", "description", lambda arguments: "ok", read_only="true"), "read_only"),
    ],
)
def test_registry_rejects_malformed_tool_contracts(candidate, field):
    with pytest.raises(ValueError, match=field):
        ToolRegistry([candidate])
