"""Documentation Engineering Engine.

Generates project documentation including README, architecture docs,
API documentation, guides, and engineering reports.
"""

from __future__ import annotations

from daep.engines.base import BaseEngine
from daep.orchestration.context import GenerationContext
from daep.shared.enums import ArtifactType, EngineType
from daep.shared.models import EngineeringArtifact


class DocumentationEngine(BaseEngine):
    """Generates comprehensive project documentation."""

    @property
    def engine_type(self) -> EngineType:
        return EngineType.EVALUATION  # Runs in evaluation phase

    @property
    def name(self) -> str:
        return "Documentation Engineering Engine"

    def _run(self, context: GenerationContext) -> list[EngineeringArtifact]:
        request = context.request
        artifacts: list[EngineeringArtifact] = []

        # Generate README
        artifacts.append(
            EngineeringArtifact(
                name="README.md",
                artifact_type=ArtifactType.DOCUMENTATION,
                engine=EngineType.EVALUATION,
                content=self._generate_readme(request.name, request.description),
            )
        )

        # Generate architecture documentation
        artifacts.append(
            EngineeringArtifact(
                name="docs/architecture.md",
                artifact_type=ArtifactType.DOCUMENTATION,
                engine=EngineType.EVALUATION,
                content=self._generate_architecture_doc(request.name, context),
            )
        )

        return artifacts

    def _generate_readme(self, name: str, description: str) -> str:
        return f"""# {name}

## Overview

{description}

## Quick Start

```bash
pip install -e .
```

## Architecture

See `docs/architecture.md` for detailed architecture documentation.

## Usage

```python
# Initialize the agent
agent = {name.replace(' ', '')}()
result = agent.run(request)
```

## Engineering Standards

This project follows DAEP Engineering Standards.

## License

MIT
"""

    def _generate_architecture_doc(
        self, name: str, context: GenerationContext
    ) -> str:
        artifact_names = [a.name for a in context.artifacts]
        artifact_list = "\n".join(f"- {n}" for n in artifact_names) or "- (none yet)"
        return f"""# Architecture: {name}

## Engineering Artifacts

{artifact_list}

## Design Decisions

See `adr.md` for Architecture Decision Records.

## Components

See `component-plan.md` for component composition.

## Workflow

See `workflow-specification.md` for execution flow.
"""
