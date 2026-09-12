from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

ToolHandler = Callable[[dict[str, object]], str]


@dataclass(frozen=True, slots=True)
class Tool:
    name: str
    description: str
    handler: ToolHandler
    read_only: bool = True


class ToolRegistry:
    def __init__(self, tools: list[Tool] | None = None) -> None:
        self._tools: dict[str, Tool] = {tool.name: tool for tool in tools or []}

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        try:
            return self._tools[name]
        except KeyError as exc:
            raise KeyError(f"Unknown tool: {name}") from exc

    def names(self) -> list[str]:
        return sorted(self._tools)

    def execute(self, name: str, arguments: dict[str, object]) -> str:
        return self.get(name).handler(arguments)
