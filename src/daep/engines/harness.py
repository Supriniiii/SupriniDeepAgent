"""Harness Engineering Engine.

Designs the runtime execution environment including lifecycle,
state management, checkpointing, recovery, and observability.
"""

from __future__ import annotations

from daep.engines.base import BaseEngine
from daep.orchestration.context import GenerationContext
from daep.shared.enums import ArtifactType, EngineType
from daep.shared.models import EngineeringArtifact


class HarnessEngine(BaseEngine):
    """Designs the agent runtime harness."""

    @property
    def engine_type(self) -> EngineType:
        return EngineType.HARNESS

    def _run(self, context: GenerationContext) -> list[EngineeringArtifact]:
        request = context.request
        harness_type = self._select_harness(context)

        content = self._generate_harness_spec(request.name, harness_type)

        return [
            EngineeringArtifact(
                name="harness-specification.md",
                artifact_type=ArtifactType.SPECIFICATION,
                engine=EngineType.HARNESS,
                content=content,
                metadata={"harness_type": harness_type},
            )
        ]

    def _select_harness(self, context: GenerationContext) -> str:
        """Select the appropriate harness type."""
        agent_type = context.request.agent_type
        mapping = {
            "coding": "coding",
            "research": "research",
            "workflow": "workflow",
            "data": "workflow",
        }
        return mapping.get(agent_type or "", "enterprise")

    def _generate_harness_spec(self, name: str, harness_type: str) -> str:
        return f"""# Harness Specification: {name}

## Harness Type

{harness_type.title()} Harness

## Lifecycle

Initialize → Register → Configure → Execute → Monitor → Shutdown

## State Management

- Checkpointing: enabled
- Recovery: checkpoint-based
- Persistence: session duration

## Observability

- Logging: structured (JSON)
- Metrics: execution duration, step counts
- Health checks: liveness endpoint

## Runtime Configuration

- Timeout: 300s
- Max retries: 3
- Parallel execution: false
"""
