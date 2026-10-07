"""Execution planner.

Analyzes the GenerationContext and produces an ExecutionPlan
that defines which engines to run, in what order, and with what inputs.
"""

from __future__ import annotations

import logging

from daep.orchestration.context import GenerationContext
from daep.shared.enums import EngineType
from daep.shared.models import ExecutionPlan, ExecutionStep

logger = logging.getLogger(__name__)


class Planner:
    """Creates an execution plan from the generation context.

    For v0.1 this is deterministic — always produces the same
    pipeline order. Future versions will adapt based on request type.
    """

    def plan(self, context: GenerationContext) -> ExecutionPlan:
        """Produce an execution plan for the generation request."""
        logger.info("Creating execution plan for: %s", context.request.name)

        steps = self._build_steps(context)
        knowledge_domains = self._determine_knowledge_domains(context)
        templates = self._determine_templates(context)
        engines = self._determine_engines(context)

        plan = ExecutionPlan(
            steps=steps,
            knowledge_domains=knowledge_domains,
            templates_required=templates,
            estimated_engines=engines,
        )

        logger.info(
            "Plan created: %d steps, %d engines, %d knowledge domains",
            plan.total_steps,
            len(engines),
            len(knowledge_domains),
        )
        return plan

    def _build_steps(self, context: GenerationContext) -> list[ExecutionStep]:
        """Build the ordered execution steps."""
        return [
            ExecutionStep(
                order=1,
                name="Load Knowledge",
                engine=EngineType.REQUIREMENTS,
                description="Load relevant knowledge for this request",
                inputs=["request", "knowledge_base"],
                outputs=["loaded_knowledge"],
            ),
            ExecutionStep(
                order=2,
                name="Load Standards",
                engine=EngineType.REQUIREMENTS,
                description="Load organization standards",
                inputs=["request", "standards"],
                outputs=["loaded_standards"],
            ),
            ExecutionStep(
                order=3,
                name="Run Architecture Engine",
                engine=EngineType.ARCHITECTURE,
                description="Design the solution architecture",
                inputs=["request", "knowledge", "standards"],
                outputs=["architecture.md", "adr.md"],
            ),
            ExecutionStep(
                order=4,
                name="Run Component Engine",
                engine=EngineType.COMPONENT,
                description="Identify and define required components",
                inputs=["architecture.md"],
                outputs=["component-plan.md"],
            ),
            ExecutionStep(
                order=5,
                name="Run Workflow Engine",
                engine=EngineType.WORKFLOW,
                description="Design execution workflows",
                inputs=["architecture.md", "component-plan.md"],
                outputs=["workflow-specification.md"],
            ),
            ExecutionStep(
                order=6,
                name="Run Prompt Engine",
                engine=EngineType.PROMPT,
                description="Design the reasoning layer",
                inputs=["architecture.md", "workflow-specification.md"],
                outputs=["prompt-package.md"],
            ),
            ExecutionStep(
                order=7,
                name="Run Memory Engine",
                engine=EngineType.MEMORY,
                description="Design memory strategy",
                inputs=["workflow-specification.md"],
                outputs=["memory-strategy.md"],
            ),
            ExecutionStep(
                order=8,
                name="Validate",
                engine=EngineType.VALIDATION,
                description="Validate all generated artifacts",
                inputs=["all_artifacts"],
                outputs=["validation-report.md"],
            ),
            ExecutionStep(
                order=9,
                name="Write Files",
                engine=EngineType.EVALUATION,
                description="Write artifacts to output directory",
                inputs=["all_artifacts", "output_directory"],
                outputs=["generated_files"],
            ),
        ]

    def _determine_knowledge_domains(
        self, context: GenerationContext
    ) -> list[str]:
        """Determine which knowledge domains to consult."""
        domains = [
            "architectures",
            "components",
            "workflows",
            "harnesses",
            "memory",
            "prompts",
        ]

        agent_type = context.request.agent_type
        if agent_type == "coding":
            domains.extend(["tools", "testing"])
        elif agent_type == "research":
            domains.extend(["tools", "capabilities"])
        elif agent_type == "data":
            domains.extend(["tools", "deployment"])

        return domains

    def _determine_templates(self, context: GenerationContext) -> list[str]:
        """Determine which templates are needed."""
        templates = ["agents/generic-agent"]
        agent_type = context.request.agent_type
        if agent_type:
            templates.append(f"agents/{agent_type}-agent")
        return templates

    def _determine_engines(self, context: GenerationContext) -> list[EngineType]:
        """Determine which engines to invoke."""
        return [
            EngineType.ARCHITECTURE,
            EngineType.COMPONENT,
            EngineType.WORKFLOW,
            EngineType.PROMPT,
            EngineType.MEMORY,
            EngineType.VALIDATION,
        ]
