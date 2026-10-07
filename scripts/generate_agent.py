"""Generate the No Code Frontend Agent using the DAEP pipeline."""

from pathlib import Path

from daep.engines.registry import EngineRegistry
from daep.generation.project_generator import ProjectGenerator
from daep.orchestration.context import GenerationContext
from daep.orchestration.goe import GenerationOrchestrationEngine
from daep.orchestration.request import GenerationRequest
from daep.outputs.packager import OutputPackager


def main():
    # Build request
    request = GenerationRequest(
        name="No Code Frontend Agent",
        description=(
            "An AI agent that generates front-end UI components, layouts, "
            "and pages from natural language descriptions without requiring "
            "manual coding. Uses LangChain and Azure OpenAI to interpret "
            "design requests and produce HTML/CSS/JavaScript."
        ),
        specification=Path(".kiro"),
        output_directory=Path("my_agents/no_code_frontend_agent"),
        options={"agent_type": "coding", "architecture": "planner-executor"},
    )

    # Phase 1: Engineering Pipeline
    print("=" * 60)
    print("DAEP: Deep Agent Engineering Platform")
    print("=" * 60)
    print()
    print(f"Agent: {request.name}")
    print(f"Type: coding")
    print(f"Architecture: planner-executor")
    print()
    print("Phase 1: Engineering Pipeline")
    print("-" * 40)

    registry = EngineRegistry()
    registry.register_defaults()

    goe = GenerationOrchestrationEngine(workspace=Path(".kiro"))
    registry.register_all_with_dispatcher(goe.dispatcher)

    report = goe.generate(request)

    status = "SUCCESS" if report.success else "FAILED"
    print(f"  Status: {status}")
    print(f"  Duration: {report.duration:.2f}s")
    print(f"  Steps: {report.steps_completed}/{report.steps_total}")
    print(f"  Artifacts: {report.artifacts_produced}")
    print(f"  Files: {len(report.generated_files)}")
    print()

    if not report.success:
        print("FAILED - errors:")
        for e in report.errors:
            print(f"  - {e}")
        return

    # Phase 2: Code Generation
    print("Phase 2: Code Generation")
    print("-" * 40)

    context = GenerationContext(request=request)
    generator = ProjectGenerator(output_dir=Path("my_agents"))
    project_dir = generator.generate(context)

    print(f"  Project: {project_dir}")
    file_count = sum(1 for _ in project_dir.rglob("*") if _.is_file())
    print(f"  Files generated: {file_count}")
    print()

    # Phase 3: Package Delivery
    print("Phase 3: Package Delivery")
    print("-" * 40)

    delivery_dir = Path("my_agents/no_code_frontend_agent_delivery")
    packager = OutputPackager()
    package = packager.package(
        delivery_dir=delivery_dir,
        context=context,
        report=report,
        project_dir=project_dir,
    )

    print(f"  Delivery: {package.path}")
    print(f"  Manifest: {delivery_dir / 'manifest.json'}")
    print(f"  Summary: {delivery_dir / 'summary.md'}")
    print()

    # Done
    print("=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)
    print()
    print("Next steps:")
    print(f"  cd {project_dir}")
    print("  pip install -e .")
    print("  export AIM_API_KEY=your-key")
    print("  # Edit config.ini with your Azure endpoint")
    print("  pytest")
    print()


if __name__ == "__main__":
    main()
