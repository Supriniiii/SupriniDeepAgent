"""Generation context.

The shared context object that flows through the entire engineering pipeline.
Carries the request, loaded framework resources, execution plan, and artifacts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from daep.orchestration.request import GenerationRequest
from daep.shared.enums import SessionStatus
from daep.shared.models import EngineeringArtifact, ExecutionPlan


@dataclass
class GenerationContext:
    """Shared context passed through every stage of the pipeline.

    Built incrementally as the GOE loads resources and executes stages.
    """

    request: GenerationRequest

    # Framework resources (populated by FrameworkLoader)
    steering: dict[str, str] = field(default_factory=dict)
    knowledge: dict[str, dict[str, str]] = field(default_factory=dict)
    standards: dict[str, str] = field(default_factory=dict)
    templates: dict[str, str] = field(default_factory=dict)
    specifications: dict[str, Any] = field(default_factory=dict)

    # Execution state
    execution_plan: ExecutionPlan = field(default_factory=ExecutionPlan)
    status: SessionStatus = SessionStatus.PENDING
    artifacts: list[EngineeringArtifact] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def add_artifact(self, artifact: EngineeringArtifact) -> None:
        """Register a generated artifact."""
        self.artifacts.append(artifact)

    def add_error(self, error: str) -> None:
        """Record an error."""
        self.errors.append(error)

    def add_warning(self, warning: str) -> None:
        """Record a warning."""
        self.warnings.append(warning)

    @property
    def is_failed(self) -> bool:
        """Check if the pipeline has failed."""
        return self.status == SessionStatus.FAILED

    @property
    def artifact_names(self) -> list[str]:
        """List names of all produced artifacts."""
        return [a.name for a in self.artifacts]
