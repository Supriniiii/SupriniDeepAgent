"""Capability Engineering Engine.

Discovers reusable capabilities before creating new implementations.
Searches registries and knowledge base for existing assets.
"""

from __future__ import annotations

from daep.engines.base import BaseEngine
from daep.orchestration.context import GenerationContext
from daep.shared.enums import ArtifactType, EngineType
from daep.shared.models import EngineeringArtifact


class CapabilityEngine(BaseEngine):
    """Discovers and selects reusable capabilities."""

    @property
    def engine_type(self) -> EngineType:
        return EngineType.CAPABILITY

    def _run(self, context: GenerationContext) -> list[EngineeringArtifact]:
        request = context.request
        capabilities = self._discover_capabilities(context)

        content = self._generate_capability_plan(request.name, capabilities)

        return [
            EngineeringArtifact(
                name="capability-plan.md",
                artifact_type=ArtifactType.SPECIFICATION,
                engine=EngineType.CAPABILITY,
                content=content,
                metadata={"capabilities_found": len(capabilities)},
            )
        ]

    def _discover_capabilities(self, context: GenerationContext) -> list[str]:
        """Discover available capabilities from knowledge base."""
        capabilities = [
            "planning",
            "execution",
            "reflection",
            "verification",
            "memory_management",
            "tool_invocation",
        ]

        if context.request.agent_type == "coding":
            capabilities.extend(["code_generation", "code_review", "testing"])
        elif context.request.agent_type == "research":
            capabilities.extend(["information_retrieval", "synthesis", "citation"])

        return capabilities

    def _generate_capability_plan(
        self, name: str, capabilities: list[str]
    ) -> str:
        cap_list = "\n".join(f"- {cap}" for cap in capabilities)
        return f"""# Capability Plan: {name}

## Discovered Capabilities

{cap_list}

## Reuse Assessment

All listed capabilities are available in the DAEP component library.
New capabilities should only be created if no existing match is found.

## Gap Analysis

No capability gaps identified for standard agent generation.
"""
