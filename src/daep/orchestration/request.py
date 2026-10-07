"""Generation request model.

Represents a developer's request to generate a Deep Agent.
This is the entry point to the GOE.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class GenerationRequest:
    """A developer's request to generate a Deep Agent.

    Attributes:
        name: Human-readable name for the agent.
        description: What the agent should do.
        specification: Path to the spec or .kiro workspace.
        output_directory: Where to write generated artifacts.
        options: Additional configuration (agent_type, architecture, etc).
    """

    name: str
    description: str
    specification: Path
    output_directory: Path
    options: dict[str, Any] = field(default_factory=dict)

    @property
    def agent_type(self) -> str | None:
        """Extract the agent type from options if specified."""
        return self.options.get("agent_type")

    @property
    def architecture(self) -> str | None:
        """Extract architecture preference from options."""
        return self.options.get("architecture")

    @property
    def target_environment(self) -> str:
        """Extract target environment, defaulting to development."""
        return self.options.get("target_environment", "development")
