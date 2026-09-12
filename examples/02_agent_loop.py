from agentic_ai import AgentController, PolicyEngine, Tool, ToolRegistry


def search(args: dict[str, object]) -> str:
    return "Evidence: agents need goals, tools, policy, state, evaluation, and stopping conditions."


agent = AgentController(ToolRegistry([Tool("search", "Mock evidence search", search)]), PolicyEngine({"search"}))
result = agent.run("Research the core components of a production agent")
print(result.answer)
print("steps:", result.state.steps)
