"""Tests for the DAEP CLI.

Verifies CLI commands work end-to-end using Typer's test runner.
"""

import tempfile
from pathlib import Path

from typer.testing import CliRunner

from daep.cli.main import app

runner = CliRunner()


class TestVersion:
    def test_shows_version(self):
        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert "0.1.0" in result.output


class TestStatus:
    def test_shows_status(self):
        result = runner.invoke(app, ["status"])
        assert result.exit_code == 0
        assert "Engineering Engines" in result.output


class TestEngines:
    def test_lists_engines(self):
        result = runner.invoke(app, ["engines"])
        assert result.exit_code == 0
        assert "Architecture" in result.output


class TestGenerate:
    def test_generates_project(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = runner.invoke(app, [
                "generate",
                "Test Agent",
                "--type", "coding",
                "--output", tmpdir,
                "--workspace", str(Path(".kiro")),
            ])
            assert result.exit_code == 0
            assert "Generation Complete" in result.output

            # Verify project was created
            project_dir = Path(tmpdir) / "test_agent"
            assert (project_dir / "pyproject.toml").exists()
            assert (project_dir / "src" / "test_agent" / "agent.py").exists()

    def test_research_agent(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = runner.invoke(app, [
                "generate",
                "Research Assistant",
                "--type", "research",
                "--output", tmpdir,
            ])
            assert result.exit_code == 0
            assert "Generation Complete" in result.output
