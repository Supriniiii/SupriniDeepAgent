"""Tests for the generation module.

Verifies that the ProjectGenerator produces a complete, valid Python project.
"""

import tempfile
from pathlib import Path

from daep.generation.project_generator import ProjectGenerator
from daep.generation.renderer import TemplateRenderer
from daep.generation.scaffolder import ProjectScaffolder
from daep.orchestration.context import GenerationContext
from daep.orchestration.request import GenerationRequest


def _make_context(
    name: str = "Code Review Agent",
    description: str = "Reviews pull requests for code quality",
    agent_type: str = "coding",
) -> GenerationContext:
    return GenerationContext(
        request=GenerationRequest(
            name=name,
            description=description,
            specification=Path("."),
            output_directory=Path("out"),
            options={"agent_type": agent_type},
        )
    )


# ---------------------------------------------------------------------------
# Scaffolder Tests
# ---------------------------------------------------------------------------


class TestScaffolder:
    def test_creates_structure(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            project_dir = Path(tmpdir) / "test_project"
            scaffolder = ProjectScaffolder()
            scaffolder.create_structure(project_dir, "test_agent")

            assert (project_dir / "src" / "test_agent" / "__init__.py").exists()
            assert (project_dir / "tests" / "__init__.py").exists()
            assert (project_dir / "prompts").is_dir()
            assert (project_dir / "docs").is_dir()


# ---------------------------------------------------------------------------
# Renderer Tests
# ---------------------------------------------------------------------------


class TestRenderer:
    def test_render_pyproject(self):
        r = TemplateRenderer()
        content = r.render_pyproject("my_agent", "A test agent")
        assert 'name = "my_agent"' in content
        assert "langchain" in content

    def test_render_agent(self):
        r = TemplateRenderer()
        content = r.render_agent("my_agent", "My Agent", "Does stuff", "planner-executor")
        assert "class MyAgent:" in content
        assert "def run(" in content

    def test_render_system_prompt(self):
        r = TemplateRenderer()
        content = r.render_system_prompt("Test Agent", "Does testing")
        assert "Test Agent" in content
        assert "Does testing" in content

    def test_render_readme(self):
        r = TemplateRenderer()
        content = r.render_readme("Test Agent", "A test agent")
        assert "# Test Agent" in content
        assert "Quick Start" in content


# ---------------------------------------------------------------------------
# ProjectGenerator Integration Tests
# ---------------------------------------------------------------------------


class TestProjectGenerator:
    def test_generates_complete_project(self):
        """ProjectGenerator creates a valid, complete Python project."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            context = _make_context()
            generator = ProjectGenerator(output_dir=output_dir)

            project_dir = generator.generate(context)

            # Verify structure
            assert project_dir.exists()
            assert (project_dir / "pyproject.toml").exists()
            assert (project_dir / "README.md").exists()
            assert (project_dir / "config.ini").exists()
            assert (project_dir / "src" / "code_review_agent" / "agent.py").exists()
            assert (project_dir / "src" / "code_review_agent" / "prompts.py").exists()
            assert (project_dir / "src" / "code_review_agent" / "tools.py").exists()
            assert (project_dir / "src" / "code_review_agent" / "memory.py").exists()
            assert (project_dir / "src" / "code_review_agent" / "config.py").exists()
            assert (project_dir / "prompts" / "system.md").exists()
            assert (project_dir / "prompts" / "planning.md").exists()
            assert (project_dir / "prompts" / "execution.md").exists()
            assert (project_dir / "tests" / "test_code_review_agent.py").exists()

    def test_generated_agent_has_run_method(self):
        """Generated agent code should have a run() method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            context = _make_context()
            generator = ProjectGenerator(output_dir=output_dir)
            project_dir = generator.generate(context)

            agent_code = (project_dir / "src" / "code_review_agent" / "agent.py").read_text()
            assert "def run(self, request: str)" in agent_code
            assert "class CodeReviewAgent:" in agent_code

    def test_coding_agent_has_file_tools(self):
        """Coding agent should have file read/write tools."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            context = _make_context(agent_type="coding")
            generator = ProjectGenerator(output_dir=output_dir)
            project_dir = generator.generate(context)

            tools_code = (project_dir / "src" / "code_review_agent" / "tools.py").read_text()
            assert "read_file" in tools_code
            assert "write_file" in tools_code

    def test_research_agent_has_search_tool(self):
        """Research agent should have search tool."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            context = _make_context(
                name="Research Agent",
                description="Researches topics",
                agent_type="research",
            )
            generator = ProjectGenerator(output_dir=output_dir)
            project_dir = generator.generate(context)

            tools_code = (project_dir / "src" / "research_agent" / "tools.py").read_text()
            assert "search" in tools_code

    def test_prompts_are_externalized(self):
        """Prompts should be in the prompts/ directory, not hardcoded."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            context = _make_context()
            generator = ProjectGenerator(output_dir=output_dir)
            project_dir = generator.generate(context)

            system = (project_dir / "prompts" / "system.md").read_text()
            assert "Code Review Agent" in system
            assert "reviews pull requests" in system.lower()
