"""Prompt management for Code Review Agent."""

from __future__ import annotations

from pathlib import Path


class PromptManager:
    """Loads and manages externalized prompts."""

    def __init__(self, prompts_dir: Path | None = None) -> None:
        self._dir = prompts_dir or Path(__file__).parent.parent.parent / "prompts"

    def get_system_prompt(self) -> str:
        """Load the system prompt."""
        path = self._dir / "system.md"
        if path.exists():
            return path.read_text(encoding="utf-8")
        return "You are Code Review Agent. An AI agent that reviews code for quality, best practices, security vulnerabilities, and maintainability issues. Analyzes pull requests and produces structured review feedback."

    def get_planning_prompt(self) -> str:
        """Load the planning prompt."""
        path = self._dir / "planning.md"
        if path.exists():
            return path.read_text(encoding="utf-8")
        return "Analyze the request and create a step-by-step plan."

    def get_execution_prompt(self) -> str:
        """Load the execution prompt."""
        path = self._dir / "execution.md"
        if path.exists():
            return path.read_text(encoding="utf-8")
        return "Execute the plan step by step. Produce the final output."
