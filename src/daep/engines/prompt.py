"""Prompt Engineering Engine.

Designs the complete reasoning layer including system prompts,
planning prompts, context assembly, model routing, and output specs.
"""

from __future__ import annotations

from daep.engines.base import BaseEngine
from daep.orchestration.context import GenerationContext
from daep.shared.enums import ArtifactType, EngineType
from daep.shared.models import EngineeringArtifact


class PromptEngine(BaseEngine):
    """Designs the agent prompt architecture."""

    @property
    def engine_type(self) -> EngineType:
        return EngineType.PROMPT

    def _run(self, context: GenerationContext) -> list[EngineeringArtifact]:
        request = context.request
        content = self._generate_prompt_package(request.name, request.description)

        return [
            EngineeringArtifact(
                name="prompt-package.md",
                artifact_type=ArtifactType.PROMPT,
                engine=EngineType.PROMPT,
                content=content,
            )
        ]

    def _generate_prompt_package(self, name: str, description: str) -> str:
        return f"""# Prompt Package: {name}

## System Prompt

You are {name}, an AI engineering agent.
Your purpose: {description}
Follow DAEP engineering standards. Produce deterministic, traceable outputs.

## Planning Prompt

Analyze the objective and decompose it into actionable steps.
Consider dependencies, priorities, and available resources.
Output: Numbered execution plan.

## Execution Prompt

Execute the current task according to the plan.
Use available tools. Follow coding standards.
Output: Task result with metadata.

## Reflection Prompt

Review the completed execution.
Identify improvements, gaps, and lessons learned.
Output: Reflection report with recommendations.

## Verification Prompt

Verify outputs against requirements.
Check completeness, correctness, and quality.
Output: Pass/fail with evidence.

## Context Assembly

Order: system → task → memory → tools → constraints
Max size: 8000 tokens
Overflow: Summarize older context

## Model Routing

- Planning: Primary model
- Execution: Primary model
- Reflection: Primary model
- Verification: Primary model
"""
