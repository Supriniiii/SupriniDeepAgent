"""Tests for Engineering Engines.

Validates the base engine framework, all engine implementations,
and the engine registry.
"""

import tempfile
from pathlib import Path

from daep.engines.architecture import ArchitectureEngine
from daep.engines.base import BaseEngine
from daep.engines.capability import CapabilityEngine
from daep.engines.component import ComponentEngine
from daep.engines.evaluation import EvaluationEngine
from daep.engines.harness import HarnessEngine
from daep.engines.memory import MemoryEngine
from daep.engines.prompt import PromptEngine
from daep.engines.registry import EngineRegistry
from daep.engines.requirements import RequirementsEngine
from daep.engines.validation import ValidationEngine
from daep.engines.workflow import WorkflowEngine
from daep.orchestration.context import GenerationContext
from daep.orchestration.dispatcher import Dispatcher
from daep.orchestration.request import GenerationRequest
from daep.shared.enums import ArtifactType, EngineType


def _make_context(
    name: str = "Test Agent",
    description: str = "A test agent",
    agent_type: str | None = None,
) -> GenerationContext:
    """Helper to create a test context."""
    options = {}
    if agent_type:
        options["agent_type"] = agent_type
    request = GenerationRequest(
        name=name,
        description=description,
        specification=Path("."),
        output_directory=Path("out"),
        options=options,
    )
    return GenerationContext(request=request)


# ---------------------------------------------------------------------------
# Base Engine Tests
# ---------------------------------------------------------------------------


class TestBaseEngine:
    def test_cannot_instantiate_abstract(self):
        """BaseEngine cannot be instantiated directly."""
        try:
            BaseEngine()  # type: ignore
            assert False, "Should raise TypeError"
        except TypeError:
            pass

    def test_validate_outputs_catches_empty(self):
        """validate_outputs flags empty content."""
        engine = RequirementsEngine()
        from daep.shared.models import EngineeringArtifact

        artifact = EngineeringArtifact(
            name="test.md",
            artifact_type=ArtifactType.SPECIFICATION,
            engine=EngineType.REQUIREMENTS,
            content="",
        )
        issues = engine.validate_outputs([artifact])
        assert any("empty content" in i for i in issues)

    def test_validate_outputs_passes_valid(self):
        """validate_outputs returns no issues for valid artifacts."""
        engine = RequirementsEngine()
        from daep.shared.models import EngineeringArtifact

        artifact = EngineeringArtifact(
            name="test.md",
            artifact_type=ArtifactType.SPECIFICATION,
            engine=EngineType.REQUIREMENTS,
            content="# Valid content",
        )
        issues = engine.validate_outputs([artifact])
        assert issues == []


# ---------------------------------------------------------------------------
# Requirements Engine Tests
# ---------------------------------------------------------------------------


class TestRequirementsEngine:
    def test_engine_type(self):
        engine = RequirementsEngine()
        assert engine.engine_type == EngineType.REQUIREMENTS

    def test_produces_requirements(self):
        context = _make_context()
        engine = RequirementsEngine()
        artifacts = engine.execute(context)

        assert len(artifacts) == 1
        assert artifacts[0].name == "requirements.md"
        assert "Functional Requirements" in artifacts[0].content

    def test_validates_empty_description(self):
        context = _make_context(description="")
        engine = RequirementsEngine()
        issues = engine.validate_inputs(context)
        assert any("empty" in i for i in issues)


# ---------------------------------------------------------------------------
# Architecture Engine Tests
# ---------------------------------------------------------------------------


class TestArchitectureEngine:
    def test_engine_type(self):
        engine = ArchitectureEngine()
        assert engine.engine_type == EngineType.ARCHITECTURE

    def test_produces_architecture_and_adr(self):
        context = _make_context()
        engine = ArchitectureEngine()
        artifacts = engine.execute(context)

        assert len(artifacts) == 2
        names = [a.name for a in artifacts]
        assert "architecture.md" in names
        assert "adr.md" in names

    def test_uses_requested_pattern(self):
        request = GenerationRequest(
            name="Test",
            description="Test",
            specification=Path("."),
            output_directory=Path("out"),
            options={"architecture": "manager-worker"},
        )
        context = GenerationContext(request=request)
        engine = ArchitectureEngine()
        artifacts = engine.execute(context)

        arch = next(a for a in artifacts if a.name == "architecture.md")
        assert "Manager Worker" in arch.content


# ---------------------------------------------------------------------------
# Capability Engine Tests
# ---------------------------------------------------------------------------


class TestCapabilityEngine:
    def test_engine_type(self):
        assert CapabilityEngine().engine_type == EngineType.CAPABILITY

    def test_produces_capability_plan(self):
        context = _make_context()
        artifacts = CapabilityEngine().execute(context)
        assert artifacts[0].name == "capability-plan.md"

    def test_adapts_to_coding_agent(self):
        context = _make_context(agent_type="coding")
        artifacts = CapabilityEngine().execute(context)
        assert "code_generation" in artifacts[0].content


# ---------------------------------------------------------------------------
# Component Engine Tests
# ---------------------------------------------------------------------------


class TestComponentEngine:
    def test_engine_type(self):
        assert ComponentEngine().engine_type == EngineType.COMPONENT

    def test_produces_component_plan(self):
        context = _make_context()
        artifacts = ComponentEngine().execute(context)
        assert artifacts[0].name == "component-plan.md"
        assert "Planner" in artifacts[0].content

    def test_coding_agent_adds_components(self):
        context = _make_context(agent_type="coding")
        artifacts = ComponentEngine().execute(context)
        assert "Code Generator" in artifacts[0].content


# ---------------------------------------------------------------------------
# Harness Engine Tests
# ---------------------------------------------------------------------------


class TestHarnessEngine:
    def test_engine_type(self):
        assert HarnessEngine().engine_type == EngineType.HARNESS

    def test_produces_harness_spec(self):
        context = _make_context()
        artifacts = HarnessEngine().execute(context)
        assert artifacts[0].name == "harness-specification.md"

    def test_selects_coding_harness(self):
        context = _make_context(agent_type="coding")
        artifacts = HarnessEngine().execute(context)
        assert "Coding" in artifacts[0].content


# ---------------------------------------------------------------------------
# Workflow Engine Tests
# ---------------------------------------------------------------------------


class TestWorkflowEngine:
    def test_engine_type(self):
        assert WorkflowEngine().engine_type == EngineType.WORKFLOW

    def test_produces_workflow_spec(self):
        context = _make_context()
        artifacts = WorkflowEngine().execute(context)
        assert artifacts[0].name == "workflow-specification.md"
        assert "States" in artifacts[0].content


# ---------------------------------------------------------------------------
# Memory Engine Tests
# ---------------------------------------------------------------------------


class TestMemoryEngine:
    def test_engine_type(self):
        assert MemoryEngine().engine_type == EngineType.MEMORY

    def test_produces_memory_strategy(self):
        context = _make_context()
        artifacts = MemoryEngine().execute(context)
        assert artifacts[0].name == "memory-strategy.md"
        assert "Working Memory" in artifacts[0].content


# ---------------------------------------------------------------------------
# Prompt Engine Tests
# ---------------------------------------------------------------------------


class TestPromptEngine:
    def test_engine_type(self):
        assert PromptEngine().engine_type == EngineType.PROMPT

    def test_produces_prompt_package(self):
        context = _make_context()
        artifacts = PromptEngine().execute(context)
        assert artifacts[0].name == "prompt-package.md"
        assert "System Prompt" in artifacts[0].content


# ---------------------------------------------------------------------------
# Validation Engine Tests
# ---------------------------------------------------------------------------


class TestValidationEngine:
    def test_engine_type(self):
        assert ValidationEngine().engine_type == EngineType.VALIDATION

    def test_produces_validation_report(self):
        context = _make_context()
        artifacts = ValidationEngine().execute(context)
        assert artifacts[0].name == "validation-report.md"


# ---------------------------------------------------------------------------
# Evaluation Engine Tests
# ---------------------------------------------------------------------------


class TestEvaluationEngine:
    def test_engine_type(self):
        assert EvaluationEngine().engine_type == EngineType.EVALUATION

    def test_produces_evaluation_report(self):
        context = _make_context()
        artifacts = EvaluationEngine().execute(context)
        assert artifacts[0].name == "evaluation-report.md"
        assert "overall_score" in artifacts[0].metadata


# ---------------------------------------------------------------------------
# Engine Registry Tests
# ---------------------------------------------------------------------------


class TestEngineRegistry:
    def test_register_engine(self):
        registry = EngineRegistry()
        registry.register(RequirementsEngine())
        assert EngineType.REQUIREMENTS in registry.available
        assert registry.count == 1

    def test_register_defaults(self):
        registry = EngineRegistry()
        registry.register_defaults()
        # 10 unique EngineType slots (some engines share types as extensions)
        assert registry.count == 10
        assert EngineType.ARCHITECTURE in registry.available
        assert EngineType.EVALUATION in registry.available

    def test_get_engine(self):
        registry = EngineRegistry()
        registry.register(ArchitectureEngine())
        engine = registry.get(EngineType.ARCHITECTURE)
        assert engine is not None
        assert engine.engine_type == EngineType.ARCHITECTURE

    def test_register_all_with_dispatcher(self):
        registry = EngineRegistry()
        registry.register_defaults()
        dispatcher = Dispatcher()
        registry.register_all_with_dispatcher(dispatcher)
        assert dispatcher.engine_count == 10


# ---------------------------------------------------------------------------
# Tool Engine Tests
# ---------------------------------------------------------------------------


class TestToolEngine:
    def test_name(self):
        from daep.engines.tool import ToolEngine
        assert ToolEngine().name == "Tool Engineering Engine"

    def test_produces_tool_config(self):
        from daep.engines.tool import ToolEngine
        context = _make_context()
        artifacts = ToolEngine().execute(context)
        assert artifacts[0].name == "tool-configuration.md"

    def test_coding_agent_includes_git(self):
        from daep.engines.tool import ToolEngine
        context = _make_context(agent_type="coding")
        artifacts = ToolEngine().execute(context)
        assert "Git" in artifacts[0].content


# ---------------------------------------------------------------------------
# Documentation Engine Tests
# ---------------------------------------------------------------------------


class TestDocumentationEngine:
    def test_name(self):
        from daep.engines.documentation import DocumentationEngine
        assert DocumentationEngine().name == "Documentation Engineering Engine"

    def test_produces_readme_and_docs(self):
        from daep.engines.documentation import DocumentationEngine
        context = _make_context()
        artifacts = DocumentationEngine().execute(context)
        names = [a.name for a in artifacts]
        assert "README.md" in names
        assert "docs/architecture.md" in names


# ---------------------------------------------------------------------------
# Configuration Engine Tests
# ---------------------------------------------------------------------------


class TestConfigurationEngine:
    def test_name(self):
        from daep.engines.configuration import ConfigurationEngine
        assert ConfigurationEngine().name == "Configuration Engineering Engine"

    def test_produces_dev_and_prod_configs(self):
        from daep.engines.configuration import ConfigurationEngine
        context = _make_context()
        artifacts = ConfigurationEngine().execute(context)
        names = [a.name for a in artifacts]
        assert "config/development.yaml" in names
        assert "config/production.yaml" in names

    def test_dev_config_has_debug(self):
        from daep.engines.configuration import ConfigurationEngine
        context = _make_context()
        artifacts = ConfigurationEngine().execute(context)
        dev = next(a for a in artifacts if "development" in a.name)
        assert "DEBUG" in dev.content


# ---------------------------------------------------------------------------
# Integration: GOE with All Engines
# ---------------------------------------------------------------------------


class TestGOEWithEngines:
    def test_full_pipeline_with_all_engines(self):
        """GOE produces all expected artifacts when all engines are registered."""
        from daep.orchestration.goe import GenerationOrchestrationEngine

        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "output"
            workspace = Path(tmpdir) / ".kiro"

            (workspace / "steering").mkdir(parents=True)
            (workspace / "knowledge").mkdir(parents=True)
            (workspace / "standards").mkdir(parents=True)
            (workspace / "templates").mkdir(parents=True)
            (workspace / "engines").mkdir(parents=True)

            request = GenerationRequest(
                name="Code Review Agent",
                description="An agent that reviews pull requests for quality",
                specification=workspace,
                output_directory=output_dir,
                options={"agent_type": "coding"},
            )

            # Create GOE and register all engines
            registry = EngineRegistry()
            registry.register_defaults()

            goe = GenerationOrchestrationEngine(workspace=workspace)
            registry.register_all_with_dispatcher(goe.dispatcher)

            report = goe.generate(request)

            assert report.success is True
            assert report.artifacts_produced > 5
            assert len(report.generated_files) > 5

            # Verify key files were written
            assert (output_dir / "requirements.md").exists()
            assert (output_dir / "architecture.md").exists()
            assert (output_dir / "component-plan.md").exists()
            assert (output_dir / "workflow-specification.md").exists()
            assert (output_dir / "prompt-package.md").exists()
            assert (output_dir / "memory-strategy.md").exists()
