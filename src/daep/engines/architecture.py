"""Architecture Engineering Engine.

Transforms requirements into a complete solution architecture.
Selects patterns, defines components, interfaces, and data flow.
"""

from __future__ import annotations

from daep.engines.base import BaseEngine
from daep.orchestration.context import GenerationContext
from daep.shared.enums import ArtifactType, EngineType
from daep.shared.models import EngineeringArtifact


class ArchitectureEngine(BaseEngine):
    """Designs the solution architecture from requirements."""

    @property
    def engine_type(self) -> EngineType:
        return EngineType.ARCHITECTURE

    def validate_inputs(self, context: GenerationContext) -> list[str]:
        issues: list[str] = []
        if not context.request.name:
            issues.append("Agent name is required for architecture design")
        return issues

    def _run(self, context: GenerationContext) -> list[EngineeringArtifact]:
        request = context.request
        pattern = request.architecture or "planner-executor"

        architecture_content = self._generate_architecture(
            request.name, request.description, pattern
        )
        adr_content = self._generate_adr(request.name, pattern)

        return [
            EngineeringArtifact(
                name="architecture.md",
                artifact_type=ArtifactType.ARCHITECTURE,
                engine=EngineType.ARCHITECTURE,
                content=architecture_content,
                metadata={"pattern": pattern},
            ),
            EngineeringArtifact(
                name="adr.md",
                artifact_type=ArtifactType.ARCHITECTURE,
                engine=EngineType.ARCHITECTURE,
                content=adr_content,
            ),
        ]

    def _generate_architecture(
        self, name: str, description: str, pattern: str
    ) -> str:
        return f"""# Architecture: {name}

## Pattern

{pattern.replace('-', ' ').title()}

## Overview

{description}

## Components

| Component | Responsibility |
|-----------|---------------|
| Planner | Decomposes objectives into tasks |
| Executor | Performs planned tasks |
| Memory | Maintains execution context |
| Tool Manager | Coordinates external tools |
| Verifier | Validates outputs |

## Data Flow

Request → Planner → Execution Plan → Executor → Artifacts → Verifier → Output

## Interfaces

- Input: GenerationRequest
- Output: EngineeringArtifacts
- Internal: Context-based artifact passing

## Technology

- Runtime: Python 3.11+
- Framework: DAEP
- Pattern: {pattern}
"""

    def _generate_adr(self, name: str, pattern: str) -> str:
        return f"""# ADR: Architecture Pattern Selection for {name}

## Status

Accepted

## Context

The agent requires a structured execution model that separates planning from execution.

## Decision

Selected the {pattern} architecture pattern.

## Consequences

- Clear separation of concerns.
- Supports iterative refinement.
- Enables independent testing of planner and executor.
"""
