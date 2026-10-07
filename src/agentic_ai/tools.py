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
        self._tools: dict[str, Tool] = {}
        for tool in tools or []:
            self.register(tool)

    def register(self, tool: Tool) -> None:
        if not isinstance(tool.name, str) or not tool.name.strip():
            raise ValueError("Tool name must be a non-empty string")
        if not isinstance(tool.description, str) or not tool.description.strip():
            raise ValueError("Tool description must be a non-empty string")
        if not callable(tool.handler):
            raise ValueError("Tool handler must be callable")
        if not isinstance(tool.read_only, bool):
            raise ValueError("Tool read_only must be a boolean")
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
