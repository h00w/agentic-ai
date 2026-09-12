from agentic_ai import AgentController, PolicyEngine, Tool, ToolRegistry


def calculator(args: dict[str, object]) -> str:
    text = str(args["query"])
    digits = [int(token) for token in text.replace("+", " ").split() if token.isdigit()]
    return str(sum(digits))


registry = ToolRegistry([Tool("calculator", "Add integers found in a query", calculator)])
print(AgentController(registry, PolicyEngine({"calculator"})).run("Calculate 20 + 22").answer)
