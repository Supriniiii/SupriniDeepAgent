"""Tool management for the agent."""

from __future__ import annotations

from pathlib import Path


class ToolManager:
    """Manages external tool integrations."""

    def __init__(self) -> None:
        self._tools: dict[str, callable] = {}
        self._register_defaults()

    def _register_defaults(self) -> None:
        """Register default tools."""
        pass

    def read_file(self, path: str) -> str:
        """Read a file from the project."""
        file_path = Path(path)
        if file_path.exists():
            return file_path.read_text(encoding="utf-8")
        return f"File not found: {path}"

    def write_file(self, path: str, content: str) -> str:
        """Write content to a file."""
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")
        return f"Written: {path}"

    def list_tools(self) -> list[str]:
        """List available tools."""
        return list(self._tools.keys())
