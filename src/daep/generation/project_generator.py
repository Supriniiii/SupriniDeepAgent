"""Project Generator.

Produces a complete, installable Python project from engineering artifacts.
Generates:
  - Project structure (pyproject.toml, README, etc.)
  - Agent implementation (main agent class)
  - Prompts (externalized prompt files)
  - Tools (tool wrappers)
  - Memory (memory configuration)
  - Configuration (config files)
  - Tests (basic test suite)
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from daep.generation.renderer import TemplateRenderer
from daep.generation.scaffolder import ProjectScaffolder
from daep.orchestration.context import GenerationContext

logger = logging.getLogger(__name__)


class ProjectGenerator:
    """Generates a complete Python project from engineering artifacts.

    This is the final stage of the DAEP pipeline — it takes all the
    engineering work (architecture, components, prompts, memory, workflow)
    and produces a working codebase.
    """

    def __init__(self, output_dir: Path | None = None) -> None:
        self._output_dir = output_dir or Path("outputs")
        self._renderer = TemplateRenderer()
        self._scaffolder = ProjectScaffolder()

    def generate(self, context: GenerationContext) -> Path:
        """Generate the complete project.

        Returns the path to the generated project root.
        """
        request = context.request
        project_name = self._normalize_name(request.name)
        project_dir = self._output_dir / project_name

        logger.info("Generating project: %s → %s", request.name, project_dir)

        # 1. Create project structure
        self._scaffolder.create_structure(project_dir, project_name)

        # 2. Generate pyproject.toml
        self._generate_pyproject(project_dir, project_name, request.description)

        # 3. Generate agent code
        self._generate_agent(project_dir, project_name, context)

        # 4. Generate prompts
        self._generate_prompts(project_dir, project_name, context)

        # 5. Generate configuration
        self._generate_config(project_dir, project_name, context)

        # 6. Generate tests
        self._generate_tests(project_dir, project_name, context)

        # 7. Generate README
        self._generate_readme(project_dir, request.name, request.description)

        logger.info("Project generated: %s", project_dir)
        return project_dir

    def _normalize_name(self, name: str) -> str:
        """Convert agent name to a valid Python package name."""
        return name.lower().replace(" ", "_").replace("-", "_")

    def _generate_pyproject(
        self, project_dir: Path, package_name: str, description: str
    ) -> None:
        """Generate pyproject.toml."""
        content = self._renderer.render_pyproject(package_name, description)
        (project_dir / "pyproject.toml").write_text(content, encoding="utf-8")

    def _generate_agent(
        self, project_dir: Path, package_name: str, context: GenerationContext
    ) -> None:
        """Generate the main agent module."""
        src_dir = project_dir / "src" / package_name

        # Main agent class
        agent_code = self._renderer.render_agent(
            package_name=package_name,
            agent_name=context.request.name,
            description=context.request.description,
            architecture=context.request.architecture or "planner-executor",
        )
        (src_dir / "agent.py").write_text(agent_code, encoding="utf-8")

        # Prompts module
        prompts_code = self._renderer.render_prompts_module(
            package_name=package_name,
            agent_name=context.request.name,
            description=context.request.description,
        )
        (src_dir / "prompts.py").write_text(prompts_code, encoding="utf-8")

        # Tools module
        tools_code = self._renderer.render_tools_module(
            package_name=package_name,
            agent_type=context.request.agent_type,
        )
        (src_dir / "tools.py").write_text(tools_code, encoding="utf-8")

        # Memory module
        memory_code = self._renderer.render_memory_module(package_name)
        (src_dir / "memory.py").write_text(memory_code, encoding="utf-8")

        # Config module
        config_code = self._renderer.render_config_module(package_name)
        (src_dir / "config.py").write_text(config_code, encoding="utf-8")

    def _generate_prompts(
        self, project_dir: Path, package_name: str, context: GenerationContext
    ) -> None:
        """Generate externalized prompt files."""
        prompts_dir = project_dir / "prompts"

        system_prompt = self._renderer.render_system_prompt(
            context.request.name, context.request.description
        )
        (prompts_dir / "system.md").write_text(system_prompt, encoding="utf-8")

        planning_prompt = self._renderer.render_planning_prompt()
        (prompts_dir / "planning.md").write_text(planning_prompt, encoding="utf-8")

        execution_prompt = self._renderer.render_execution_prompt()
        (prompts_dir / "execution.md").write_text(execution_prompt, encoding="utf-8")

    def _generate_config(
        self, project_dir: Path, package_name: str, context: GenerationContext
    ) -> None:
        """Generate configuration files."""
        config_content = self._renderer.render_agent_config(
            package_name, context.request.name
        )
        (project_dir / "config.ini").write_text(config_content, encoding="utf-8")

    def _generate_tests(
        self, project_dir: Path, package_name: str, context: GenerationContext
    ) -> None:
        """Generate test files."""
        tests_dir = project_dir / "tests"
        test_code = self._renderer.render_tests(package_name, context.request.name)
        (tests_dir / f"test_{package_name}.py").write_text(test_code, encoding="utf-8")

    def _generate_readme(
        self, project_dir: Path, name: str, description: str
    ) -> None:
        """Generate project README."""
        content = self._renderer.render_readme(name, description)
        (project_dir / "README.md").write_text(content, encoding="utf-8")
