"""Shared domain models used across DAEP modules."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from daep.shared.enums import ArtifactType, EngineType


@dataclass
class EngineeringArtifact:
    """An artifact produced by an Engineering Engine."""

    name: str
    artifact_type: ArtifactType
    engine: EngineType
    content: str
    path: Path | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    validated: bool = False


@dataclass
class ExecutionStep:
    """A single step in the execution plan."""

    order: int
    name: str
    engine: EngineType
    description: str
    inputs: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    completed: bool = False
    duration: float = 0.0


@dataclass
class ExecutionPlan:
    """The complete plan for generating a Deep Agent."""

    steps: list[ExecutionStep] = field(default_factory=list)
    knowledge_domains: list[str] = field(default_factory=list)
    templates_required: list[str] = field(default_factory=list)
    estimated_engines: list[EngineType] = field(default_factory=list)

    @property
    def total_steps(self) -> int:
        return len(self.steps)

    @property
    def completed_steps(self) -> int:
        return sum(1 for s in self.steps if s.completed)

    @property
    def progress(self) -> float:
        if not self.steps:
            return 0.0
        return self.completed_steps / self.total_steps
