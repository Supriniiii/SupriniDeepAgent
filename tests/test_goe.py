"""Tests for the Generation Orchestration Engine.

Validates the end-to-end GOE flow:
  Request → Context → Load → Plan → Execute → Validate → Write → Report
"""

import tempfile
from pathlib import Path

from daep.orchestration.context import GenerationContext
from daep.orchestration.dispatcher import Dispatcher
from daep.orchestration.executor import Executor
from daep.orchestration.goe import GenerationOrchestrationEngine
from daep.orchestration.loader import FrameworkLoader
from daep.orchestration.planner import Planner
from daep.orchestration.report import GenerationReport, ReportBuilder
from daep.orchestration.request import GenerationRequest
from daep.shared.enums import ArtifactType, EngineType, SessionStatus
from daep.shared.models import EngineeringArtifact, ExecutionPlan


# ---------------------------------------------------------------------------
# Request Tests
# ---------------------------------------------------------------------------


class TestGenerationRequest:
    def test_create_basic_request(self):
        request = GenerationRequest(
            name="Test Agent",
            description="A test agent",
            specification=Path("specs/test"),
            output_directory=Path("outputs/test"),
        )
        assert request.name == "Test Agent"
        assert request.description == "A test agent"
        assert request.agent_type is None
        assert request.architecture is None
        assert request.target_environment == "development"

    def test_request_with_options(self):
        request = GenerationRequest(
            name="Coding Agent",
            description="A coding agent",
            specification=Path("specs/coding"),
            output_directory=Path("outputs/coding"),
            options={
                "agent_type": "coding",
                "architecture": "planner-executor",
                "target_environment": "production",
            },
        )
        assert request.agent_type == "coding"
        assert request.architecture == "planner-executor"
        assert request.target_environment == "production"

    def test_request_defaults(self):
        request = GenerationRequest(
            name="X",
            description="Y",
            specification=Path("."),
            output_directory=Path("out"),
        )
        assert request.options == {}
        assert request.target_environment == "development"


# ---------------------------------------------------------------------------
# Context Tests
# ---------------------------------------------------------------------------


class TestGenerationContext:
    def test_create_context(self):
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        assert context.status == SessionStatus.PENDING
        assert len(context.artifacts) == 0
        assert not context.is_failed

    def test_add_artifact(self):
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        artifact = EngineeringArtifact(
            name="architecture.md",
            artifact_type=ArtifactType.ARCHITECTURE,
            engine=EngineType.ARCHITECTURE,
            content="# Architecture",
        )
        context.add_artifact(artifact)
        assert len(context.artifacts) == 1
        assert context.artifact_names == ["architecture.md"]

    def test_error_tracking(self):
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        context.add_error("Something went wrong")
        context.status = SessionStatus.FAILED
        assert context.is_failed
        assert "Something went wrong" in context.errors

    def test_warning_tracking(self):
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        context.add_warning("Incomplete output")
        assert "Incomplete output" in context.warnings


# ---------------------------------------------------------------------------
# Planner Tests
# ---------------------------------------------------------------------------


class TestPlanner:
    def test_creates_plan(self):
        request = GenerationRequest(
            name="Test Agent",
            description="A test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        planner = Planner()
        plan = planner.plan(context)

        assert plan.total_steps == 9
        assert len(plan.estimated_engines) > 0
        assert len(plan.knowledge_domains) > 0

    def test_plan_includes_core_engines(self):
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        planner = Planner()
        plan = planner.plan(context)

        assert EngineType.ARCHITECTURE in plan.estimated_engines
        assert EngineType.COMPONENT in plan.estimated_engines
        assert EngineType.WORKFLOW in plan.estimated_engines

    def test_plan_adapts_to_coding_agent(self):
        request = GenerationRequest(
            name="Coding Agent",
            description="A coding agent",
            specification=Path("."),
            output_directory=Path("out"),
            options={"agent_type": "coding"},
        )
        context = GenerationContext(request=request)
        planner = Planner()
        plan = planner.plan(context)

        assert "tools" in plan.knowledge_domains
        assert "testing" in plan.knowledge_domains


# ---------------------------------------------------------------------------
# Dispatcher Tests
# ---------------------------------------------------------------------------


class TestDispatcher:
    def test_register_engine(self):
        class MockEngine:
            @property
            def engine_type(self) -> EngineType:
                return EngineType.ARCHITECTURE

            def execute(self, context):
                return []

        dispatcher = Dispatcher()
        dispatcher.register_engine(MockEngine())
        assert EngineType.ARCHITECTURE in dispatcher.available_engines
        assert dispatcher.engine_count == 1

    def test_dispatch_unregistered_returns_empty(self):
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        dispatcher = Dispatcher()
        result = dispatcher.dispatch(EngineType.ARCHITECTURE, context)
        assert result == []

    def test_dispatch_registered_engine(self):
        class MockEngine:
            @property
            def engine_type(self) -> EngineType:
                return EngineType.ARCHITECTURE

            def execute(self, context):
                return [
                    EngineeringArtifact(
                        name="architecture.md",
                        artifact_type=ArtifactType.ARCHITECTURE,
                        engine=EngineType.ARCHITECTURE,
                        content="# Architecture",
                    )
                ]

        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        dispatcher = Dispatcher()
        dispatcher.register_engine(MockEngine())

        result = dispatcher.dispatch(EngineType.ARCHITECTURE, context)
        assert len(result) == 1
        assert result[0].name == "architecture.md"


# ---------------------------------------------------------------------------
# Executor Tests
# ---------------------------------------------------------------------------


class TestExecutor:
    def test_execute_completes_steps(self):
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        planner = Planner()
        context.execution_plan = planner.plan(context)

        dispatcher = Dispatcher()
        executor = Executor(dispatcher)
        result = executor.execute(context)

        # All steps complete (no engines registered, so no artifacts)
        assert result.execution_plan.completed_steps == 9
        assert result.status != SessionStatus.FAILED


# ---------------------------------------------------------------------------
# Report Tests
# ---------------------------------------------------------------------------


class TestReport:
    def test_success_report(self):
        report = GenerationReport(
            success=True,
            duration=5.2,
            generated_files=["architecture.md", "component-plan.md"],
            steps_completed=9,
            steps_total=9,
            artifacts_produced=5,
        )
        assert report.success
        summary = report.summary()
        assert "SUCCESS" in summary
        assert "5.20" in summary

    def test_failed_report(self):
        report = GenerationReport(
            success=False,
            duration=1.0,
            errors=["Step 3 failed: engine not found"],
        )
        assert not report.success
        assert "FAILED" in report.summary()
        assert any("Step 3 failed" in e for e in report.errors)

    def test_report_builder(self):
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        context.status = SessionStatus.COMPLETED
        context.add_warning("No artifacts produced")

        builder = ReportBuilder()
        report = builder.build(context, duration=2.5)

        assert report.success
        assert report.duration == 2.5
        assert "No artifacts produced" in report.warnings


# ---------------------------------------------------------------------------
# Framework Loader Tests
# ---------------------------------------------------------------------------


class TestFrameworkLoader:
    def test_load_missing_workspace(self):
        loader = FrameworkLoader(Path("/nonexistent/path"))
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        result = loader.load(context)

        # Should not fail, just return empty
        assert result.steering == {}
        assert result.knowledge == {}

    def test_load_real_workspace(self):
        workspace = Path(".kiro")
        if not workspace.exists():
            return  # Skip if not in project root

        loader = FrameworkLoader(workspace)
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
        )
        context = GenerationContext(request=request)
        result = loader.load(context)

        assert len(result.steering) > 0
        assert len(result.knowledge) > 0


# ---------------------------------------------------------------------------
# GOE Integration Tests
# ---------------------------------------------------------------------------


class TestGOEIntegration:
    def test_end_to_end_no_engines(self):
        """GOE completes successfully with no engines registered."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "output"
            workspace = Path(tmpdir) / ".kiro"

            # Create minimal workspace
            (workspace / "steering").mkdir(parents=True)
            (workspace / "knowledge").mkdir(parents=True)
            (workspace / "standards").mkdir(parents=True)
            (workspace / "templates").mkdir(parents=True)
            (workspace / "engines").mkdir(parents=True)

            request = GenerationRequest(
                name="Test Agent",
                description="A test agent",
                specification=workspace,
                output_directory=output_dir,
            )

            goe = GenerationOrchestrationEngine(workspace=workspace)
            report = goe.generate(request)

            assert report.success is True
            assert report.duration >= 0
            assert report.steps_total == 9
            assert report.steps_completed == 9

    def test_end_to_end_with_engine(self):
        """GOE produces artifacts when an engine is registered."""

        class MockArchEngine:
            @property
            def engine_type(self) -> EngineType:
                return EngineType.ARCHITECTURE

            def execute(self, context):
                return [
                    EngineeringArtifact(
                        name="architecture.md",
                        artifact_type=ArtifactType.ARCHITECTURE,
                        engine=EngineType.ARCHITECTURE,
                        content="# Mock Architecture\n\nPlanner-Executor pattern.",
                    )
                ]

        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "output"
            workspace = Path(tmpdir) / ".kiro"

            (workspace / "steering").mkdir(parents=True)
            (workspace / "knowledge").mkdir(parents=True)
            (workspace / "standards").mkdir(parents=True)
            (workspace / "templates").mkdir(parents=True)
            (workspace / "engines").mkdir(parents=True)

            request = GenerationRequest(
                name="Test Agent",
                description="A test agent",
                specification=workspace,
                output_directory=output_dir,
            )

            goe = GenerationOrchestrationEngine(workspace=workspace)
            goe.dispatcher.register_engine(MockArchEngine())
            report = goe.generate(request)

            assert report.success is True
            assert report.artifacts_produced == 1
            assert len(report.generated_files) == 1
            assert (output_dir / "architecture.md").exists()

    def test_report_summary_output(self):
        """GOE report produces readable summary."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "output"
            workspace = Path(tmpdir) / ".kiro"

            (workspace / "steering").mkdir(parents=True)
            (workspace / "knowledge").mkdir(parents=True)
            (workspace / "standards").mkdir(parents=True)
            (workspace / "templates").mkdir(parents=True)
            (workspace / "engines").mkdir(parents=True)

            request = GenerationRequest(
                name="Summary Test",
                description="Testing report output",
                specification=workspace,
                output_directory=output_dir,
            )

            goe = GenerationOrchestrationEngine(workspace=workspace)
            report = goe.generate(request)

            summary = report.summary()
            assert "SUCCESS" in summary
            assert "Steps: 9/9" in summary
