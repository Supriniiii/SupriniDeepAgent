"""DAEP CLI.

Developer-facing command interface for the Deep Agent Engineering Platform.

Usage:
    daep generate "Build a Code Review Agent"
    daep generate "Research Assistant" --type research
    daep status
    daep version
"""

from __future__ import annotations

import logging
import sys
import time
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from daep.engines.registry import EngineRegistry
from daep.generation.project_generator import ProjectGenerator
from daep.orchestration.context import GenerationContext
from daep.orchestration.goe import GenerationOrchestrationEngine
from daep.orchestration.request import GenerationRequest

app = typer.Typer(
    name="daep",
    help="Deep Agent Engineering Platform — Generate production-ready AI agents.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def generate(
    objective: str = typer.Argument(..., help="What agent to build"),
    agent_type: str = typer.Option("coding", "--type", "-t", help="Agent type: coding, research, data, workflow"),
    architecture: str = typer.Option("planner-executor", "--arch", "-a", help="Architecture pattern"),
    output: str = typer.Option("outputs", "--output", "-o", help="Output directory"),
    workspace: str = typer.Option(".kiro", "--workspace", "-w", help="DAEP workspace path"),
) -> None:
    """Generate a complete Deep Agent from a business objective.

    This runs the full DAEP engineering pipeline:
      1. Engineering artifacts (architecture, components, prompts, etc.)
      2. Working Python project you can install and run

    Example:
        daep generate "Code Review Agent" --type coding
        daep generate "Research Assistant" --type research
    """
    console.print()
    console.print(Panel.fit(
        f"[bold cyan]DAEP[/] Deep Agent Engineering Platform\n"
        f"Generating: [bold]{objective}[/]",
        border_style="cyan",
    ))
    console.print()

    # Build request
    request = GenerationRequest(
        name=objective,
        description=f"A {agent_type} agent: {objective}",
        specification=Path(workspace),
        output_directory=Path(output) / _normalize(objective),
        options={
            "agent_type": agent_type,
            "architecture": architecture,
        },
    )

    # Run engineering pipeline
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        # Phase 1: Engineering
        task = progress.add_task("Running engineering pipeline...", total=None)

        registry = EngineRegistry()
        registry.register_defaults()

        goe = GenerationOrchestrationEngine(workspace=Path(workspace))
        registry.register_all_with_dispatcher(goe.dispatcher)

        report = goe.generate(request)
        progress.update(task, description="Engineering complete ✓")
        progress.stop()

    console.print()

    if not report.success:
        console.print("[bold red]✗ Engineering failed[/]")
        for error in report.errors:
            console.print(f"  [red]• {error}[/]")
        raise typer.Exit(1)

    # Show engineering report
    _show_engineering_report(report)

    # Phase 2: Code generation
    console.print()
    console.print("[bold cyan]Phase 2:[/] Generating project code...")
    console.print()

    # Build context for project generation
    context = GenerationContext(request=request)
    generator = ProjectGenerator(output_dir=Path(output))
    project_dir = generator.generate(context)

    # Final summary
    console.print()
    console.print(Panel.fit(
        f"[bold green]✓ Generation Complete[/]\n\n"
        f"Project: [bold]{project_dir}[/]\n"
        f"Agent: {objective}\n"
        f"Type: {agent_type}\n"
        f"Architecture: {architecture}\n\n"
        f"[dim]Next steps:[/]\n"
        f"  cd {project_dir}\n"
        f"  pip install -e .\n"
        f"  export AIM_API_KEY=your-key\n"
        f"  # Edit config.ini with your endpoint\n"
        f"  pytest",
        border_style="green",
    ))


@app.command()
def status() -> None:
    """Show DAEP platform status."""
    table = Table(title="DAEP Platform Status", border_style="cyan")
    table.add_column("Component", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Details")

    # Check workspace
    workspace = Path(".kiro")
    ws_status = "Ready" if workspace.exists() else "Not Found"
    table.add_row("Workspace", ws_status, str(workspace.absolute()))

    # Check engines
    registry = EngineRegistry()
    registry.register_defaults()
    table.add_row("Engineering Engines", f"{registry.count} registered", ", ".join(e.value for e in registry.available))

    # Check knowledge
    knowledge_path = workspace / "knowledge"
    if knowledge_path.exists():
        domains = [d.name for d in knowledge_path.iterdir() if d.is_dir()]
        table.add_row("Knowledge Base", f"{len(domains)} domains", ", ".join(domains[:6]) + "...")
    else:
        table.add_row("Knowledge Base", "Not Found", "")

    # Check templates
    templates_path = workspace / "templates"
    if templates_path.exists():
        categories = [d.name for d in templates_path.iterdir() if d.is_dir()]
        table.add_row("Templates", f"{len(categories)} categories", ", ".join(categories))
    else:
        table.add_row("Templates", "Not Found", "")

    # Check standards
    standards_path = workspace / "standards"
    table.add_row("Standards", "Available" if standards_path.exists() else "Not Found", "")

    console.print()
    console.print(table)
    console.print()


@app.command()
def version() -> None:
    """Show DAEP version."""
    from daep import __version__
    console.print(f"[bold cyan]DAEP[/] v{__version__}")


@app.command()
def engines() -> None:
    """List available Engineering Engines."""
    registry = EngineRegistry()
    registry.register_defaults()

    table = Table(title="Engineering Engines", border_style="cyan")
    table.add_column("Engine", style="cyan")
    table.add_column("Type")

    for engine_type in registry.available:
        engine = registry.get(engine_type)
        if engine:
            table.add_row(engine.name, engine_type.value)

    console.print()
    console.print(table)
    console.print()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _normalize(name: str) -> str:
    """Normalize a name to a directory-safe string."""
    return name.lower().replace(" ", "_").replace("-", "_")


def _show_engineering_report(report) -> None:
    """Display the engineering report."""
    table = Table(title="Engineering Report", border_style="cyan")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Status", "✓ Success" if report.success else "✗ Failed")
    table.add_row("Duration", f"{report.duration:.2f}s")
    table.add_row("Steps", f"{report.steps_completed}/{report.steps_total}")
    table.add_row("Artifacts", str(report.artifacts_produced))
    table.add_row("Files Written", str(len(report.generated_files)))

    if report.warnings:
        table.add_row("Warnings", str(len(report.warnings)))

    console.print(table)

    if report.generated_files:
        console.print()
        console.print("[dim]Engineering artifacts:[/]")
        for f in report.generated_files[:10]:
            console.print(f"  [dim]→ {f}[/]")
        if len(report.generated_files) > 10:
            console.print(f"  [dim]  ... and {len(report.generated_files) - 10} more[/]")


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    app()
