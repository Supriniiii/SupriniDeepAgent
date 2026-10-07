"""Requirements Engineering Engine.

Transforms developer requests into structured engineering requirements.
Produces requirements.md with functional, non-functional, constraints, and acceptance criteria.
"""

from __future__ import annotations

from daep.engines.base import BaseEngine
from daep.orchestration.context import GenerationContext
from daep.shared.enums import ArtifactType, EngineType
from daep.shared.models import EngineeringArtifact


class RequirementsEngine(BaseEngine):
    """Transforms business intent into engineering requirements."""

    @property
    def engine_type(self) -> EngineType:
        return EngineType.REQUIREMENTS

    def validate_inputs(self, context: GenerationContext) -> list[str]:
        issues: list[str] = []
        if not context.request.description:
            issues.append("Request description is empty")
        return issues

    def _run(self, context: GenerationContext) -> list[EngineeringArtifact]:
        request = context.request
        knowledge = self.get_knowledge(context, "decision_rules")

        content = self._generate_requirements(request.name, request.description)

        return [
            EngineeringArtifact(
                name="requirements.md",
                artifact_type=ArtifactType.SPECIFICATION,
                engine=EngineType.REQUIREMENTS,
                content=content,
                metadata={
                    "agent_name": request.name,
                    "agent_type": request.agent_type,
                },
            )
        ]

    def _generate_requirements(self, name: str, description: str) -> str:
        """Generate requirements specification content."""
        return f"""# Requirements Specification: {name}

## Business Objective

{description}

## Functional Requirements

### FR-1: Core Capability
- **Description:** The agent shall perform its primary function as described.
- **Acceptance Criteria:** Agent produces correct outputs for standard inputs.
- **Priority:** High

### FR-2: Error Handling
- **Description:** The agent shall handle errors gracefully without data loss.
- **Acceptance Criteria:** Errors are logged, reported, and do not crash the agent.
- **Priority:** High

### FR-3: Output Generation
- **Description:** The agent shall produce structured, validated outputs.
- **Acceptance Criteria:** Outputs conform to expected formats.
- **Priority:** High

## Non-Functional Requirements

### NFR-1: Performance
- Response time under 30 seconds for standard operations.

### NFR-2: Reliability
- Agent recovers from transient failures without manual intervention.

### NFR-3: Maintainability
- Code follows DAEP engineering standards and is modular.

## Constraints

- Must integrate with approved technology stack.
- Must follow organizational security policies.
- Must not hardcode credentials.

## Acceptance Criteria

- All functional requirements are testable.
- All non-functional requirements are measurable.
- Requirements are traceable to architecture.
"""
