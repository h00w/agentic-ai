from agentic_ai import AgentController, PolicyEngine, Tool, ToolRegistry


def echo(args: dict[str, object]) -> str:
    return f"Hello from a bounded agent. Goal: {args['query']}"


registry = ToolRegistry([Tool("echo", "Return a deterministic greeting", echo)])
agent = AgentController(registry, PolicyEngine({"echo"}))
print(agent.run("Learn the basic agent control loop").answer)
