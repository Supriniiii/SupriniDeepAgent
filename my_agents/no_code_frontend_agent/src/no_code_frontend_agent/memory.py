"""Memory management for the agent."""

from __future__ import annotations


class MemoryManager:
    """Manages agent memory (working + session)."""

    def __init__(self, max_history: int = 20) -> None:
        self._history: list[dict[str, str]] = []
        self._max_history = max_history

    def store(self, request: str, response: str) -> None:
        """Store an interaction in memory."""
        self._history.append({"request": request, "response": response[:500]})
        if len(self._history) > self._max_history:
            self._history = self._history[-self._max_history:]

    def get_context(self) -> str:
        """Get recent context for the agent."""
        if not self._history:
            return "No previous context."
        recent = self._history[-5:]
        lines = []
        for entry in recent:
            lines.append(f"Request: {entry['request'][:100]}")
            lines.append(f"Response: {entry['response'][:200]}")
            lines.append("")
        return "\n".join(lines)

    def clear(self) -> None:
        """Clear all memory."""
        self._history.clear()
