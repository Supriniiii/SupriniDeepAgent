"""Tests for the output packager module."""

import json
import tempfile
from pathlib import Path

from daep.orchestration.context import GenerationContext
from daep.orchestration.report import GenerationReport
from daep.orchestration.request import GenerationRequest
from daep.outputs.packager import DeliveryPackage, OutputPackager, PackageManifest
from daep.shared.enums import ArtifactType, EngineType
from daep.shared.models import EngineeringArtifact


def _make_context_with_artifacts() -> GenerationContext:
    """Create a context with some artifacts for testing."""
    request = GenerationRequest(
        name="Test Agent",
        description="A test agent",
        specification=Path("."),
        output_directory=Path("out"),
        options={"agent_type": "coding", "architecture": "planner-executor"},
    )
    context = GenerationContext(request=request)
    context.add_artifact(EngineeringArtifact(
        name="requirements.md",
        artifact_type=ArtifactType.SPECIFICATION,
        engine=EngineType.REQUIREMENTS,
        content="# Requirements\n\nTest requirements.",
    ))
    context.add_artifact(EngineeringArtifact(
        name="architecture.md",
        artifact_type=ArtifactType.ARCHITECTURE,
        engine=EngineType.ARCHITECTURE,
        content="# Architecture\n\nPlanner-Executor.",
    ))
    return context


def _make_report(success: bool = True) -> GenerationReport:
    return GenerationReport(
        success=success,
        duration=2.5,
        generated_files=["requirements.md", "architecture.md"],
        steps_completed=9,
        steps_total=9,
        artifacts_produced=2,
        warnings=["No long-term memory configured"] if not success else [],
    )


# ---------------------------------------------------------------------------
# Manifest Tests
# ---------------------------------------------------------------------------


class TestPackageManifest:
    def test_to_json(self):
        manifest = PackageManifest(
            name="Test Agent",
            agent_type="coding",
            engineering_artifacts=["requirements.md"],
        )
        data = json.loads(manifest.to_json())
        assert data["name"] == "Test Agent"
        assert data["agent_type"] == "coding"
        assert "requirements.md" in data["engineering_artifacts"]

    def test_defaults(self):
        manifest = PackageManifest(name="X")
        assert manifest.generator == "Deep Agent Engineering Platform"
        assert manifest.validation_passed is True


# ---------------------------------------------------------------------------
# Packager Tests
# ---------------------------------------------------------------------------


class TestOutputPackager:
    def test_creates_delivery_structure(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            delivery_dir = Path(tmpdir) / "delivery"
            context = _make_context_with_artifacts()
            report = _make_report()

            packager = OutputPackager()
            package = packager.package(delivery_dir, context, report)

            assert package.path == delivery_dir
            assert (delivery_dir / "manifest.json").exists()
            assert (delivery_dir / "summary.md").exists()
            assert (delivery_dir / "engineering").is_dir()

    def test_writes_engineering_artifacts(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            delivery_dir = Path(tmpdir) / "delivery"
            context = _make_context_with_artifacts()
            report = _make_report()

            packager = OutputPackager()
            package = packager.package(delivery_dir, context, report)

            assert (delivery_dir / "engineering" / "requirements.md").exists()
            assert (delivery_dir / "engineering" / "architecture.md").exists()
            assert len(package.manifest.engineering_artifacts) == 2

    def test_copies_project_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a mock project directory
            project_dir = Path(tmpdir) / "project"
            project_dir.mkdir()
            (project_dir / "pyproject.toml").write_text("[project]\nname='test'\n")
            (project_dir / "src").mkdir()
            (project_dir / "src" / "agent.py").write_text("# agent code\n")

            delivery_dir = Path(tmpdir) / "delivery"
            context = _make_context_with_artifacts()
            report = _make_report()

            packager = OutputPackager()
            package = packager.package(
                delivery_dir, context, report, project_dir=project_dir
            )

            assert (delivery_dir / "project" / "pyproject.toml").exists()
            assert (delivery_dir / "project" / "src" / "agent.py").exists()
            assert len(package.manifest.project_files) == 2

    def test_manifest_records_validation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            delivery_dir = Path(tmpdir) / "delivery"
            context = _make_context_with_artifacts()
            report = _make_report(success=False)

            packager = OutputPackager()
            package = packager.package(delivery_dir, context, report)

            assert package.manifest.validation_passed is False
            assert len(package.manifest.warnings) == 1

    def test_summary_includes_agent_name(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            delivery_dir = Path(tmpdir) / "delivery"
            context = _make_context_with_artifacts()
            report = _make_report()

            packager = OutputPackager()
            packager.package(delivery_dir, context, report)

            summary = (delivery_dir / "summary.md").read_text()
            assert "Test Agent" in summary
            assert "PASSED" in summary

    def test_manifest_json_is_valid(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            delivery_dir = Path(tmpdir) / "delivery"
            context = _make_context_with_artifacts()
            report = _make_report()

            packager = OutputPackager()
            packager.package(delivery_dir, context, report)

            manifest_content = (delivery_dir / "manifest.json").read_text()
            data = json.loads(manifest_content)
            assert data["name"] == "Test Agent"
            assert data["agent_type"] == "coding"
            assert data["architecture"] == "planner-executor"
