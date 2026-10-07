"""Component Engineering Engine.

Identifies, selects, and defines the software components required
to implement the approved architecture.
"""

from __future__ import annotations

from daep.engines.base import BaseEngine
from daep.orchestration.context import GenerationContext
from daep.shared.enums import ArtifactType, EngineType
from daep.shared.models import EngineeringArtifact


class ComponentEngine(BaseEngine):
    """Defines the component composition for the solution."""

    @property
    def engine_type(self) -> EngineType:
        return EngineType.COMPONENT

    def _run(self, context: GenerationContext) -> list[EngineeringArtifact]:
        request = context.request
        components = self._select_components(context)

        content = self._generate_component_plan(request.name, components)

        return [
            EngineeringArtifact(
                name="component-plan.md",
                artifact_type=ArtifactType.COMPONENT,
                engine=EngineType.COMPONENT,
                content=content,
                metadata={"component_count": len(components)},
            )
        ]

    def _select_components(self, context: GenerationContext) -> list[dict[str, str]]:
        """Select components based on architecture."""
        base_components = [
            {"name": "Planner", "responsibility": "Task decomposition and sequencing"},
            {"name": "Executor", "responsibility": "Task execution coordination"},
            {"name": "Memory Manager", "responsibility": "Context and state management"},
            {"name": "Tool Manager", "responsibility": "External tool coordination"},
            {"name": "Verifier", "responsibility": "Output verification"},
            {"name": "State Manager", "responsibility": "Execution state tracking"},
        ]

        if context.request.agent_type == "coding":
            base_components.extend([
                {"name": "Repository Analyzer", "responsibility": "Code analysis"},
                {"name": "Code Generator", "responsibility": "Source code production"},
                {"name": "Test Generator", "responsibility": "Test creation"},
            ])

        return base_components

    def _generate_component_plan(
        self, name: str, components: list[dict[str, str]]
    ) -> str:
        table_rows = "\n".join(
            f"| {c['name']} | {c['responsibility']} |" for c in components
        )
        return f"""# Component Plan: {name}

## Selected Components

| Component | Responsibility |
|-----------|---------------|
{table_rows}

## Component Dependencies

- Planner → Executor (plan consumption)
- Executor → Tool Manager (tool invocation)
- Executor → Memory Manager (context access)
- Verifier → Executor (output validation)

## New Components Required

None — all components available in DAEP component library.
"""
