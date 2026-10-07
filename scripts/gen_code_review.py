"""Generate a Code Review Agent using the DAEP pipeline."""

from pathlib import Path

from daep.engines.registry import EngineRegistry
from daep.generation.project_generator import ProjectGenerator
from daep.orchestration.context import GenerationContext
from daep.orchestration.goe import GenerationOrchestrationEngine
from daep.orchestration.request import GenerationRequest
from daep.outputs.packager import OutputPackager


def main():
    request = GenerationRequest(
        name="Code Review Agent",
        description=(
            "An AI agent that reviews code for quality, best practices, "
            "security vulnerabilities, and maintainability issues. "
            "Analyzes pull requests and produces structured review feedback."
        ),
        specification=Path(".kiro"),
        output_directory=Path("my_agents/code_review_agent"),
        options={"agent_type": "coding", "architecture": "planner-executor"},
    )

    print("=" * 60)
    print("DAEP: Generating Code Review Agent")
    print("=" * 60)

    # Phase 1: Engineering
    print("\nPhase 1: Engineering Pipeline")
    registry = EngineRegistry()
    registry.register_defaults()
    goe = GenerationOrchestrationEngine(workspace=Path(".kiro"))
    registry.register_all_with_dispatcher(goe.dispatcher)
    report = goe.generate(request)

    print(f"  Status: {'SUCCESS' if report.success else 'FAILED'}")
    print(f"  Artifacts: {report.artifacts_produced}")

    # Phase 2: Code Generation
    print("\nPhase 2: Code Generation")
    context = GenerationContext(request=request)
    generator = ProjectGenerator(output_dir=Path("my_agents"))
    project_dir = generator.generate(context)
    print(f"  Project: {project_dir}")

    # Phase 3: Package
    print("\nPhase 3: Packaging")
    packager = OutputPackager()
    package = packager.package(
        delivery_dir=Path("my_agents/code_review_agent_delivery"),
        context=context,
        report=report,
        project_dir=project_dir,
    )
    print(f"  Delivery: {package.path}")
    print("\nDONE")


if __name__ == "__main__":
    main()
