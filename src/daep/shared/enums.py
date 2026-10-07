"""Shared enumerations used across DAEP modules."""

from enum import Enum


class SessionStatus(str, Enum):
    """Execution states for a generation session."""

    PENDING = "pending"
    LOADING = "loading"
    PLANNING = "planning"
    DISPATCHING = "dispatching"
    EXECUTING = "executing"
    VALIDATING = "validating"
    WRITING = "writing"
    COMPLETED = "completed"
    FAILED = "failed"


class EngineType(str, Enum):
    """Available Engineering Engine types."""

    REQUIREMENTS = "requirements"
    ARCHITECTURE = "architecture"
    CAPABILITY = "capability"
    COMPONENT = "component"
    HARNESS = "harness"
    WORKFLOW = "workflow"
    MEMORY = "memory"
    PROMPT = "prompt"
    VALIDATION = "validation"
    EVALUATION = "evaluation"


class ArtifactType(str, Enum):
    """Types of engineering artifacts produced."""

    SPECIFICATION = "specification"
    ARCHITECTURE = "architecture"
    COMPONENT = "component"
    WORKFLOW = "workflow"
    PROMPT = "prompt"
    MEMORY = "memory"
    CODE = "code"
    CONFIGURATION = "configuration"
    DOCUMENTATION = "documentation"
    TEST = "test"
    DEPLOYMENT = "deployment"
    REPORT = "report"


# Ordered pipeline stages (single source of truth)
PIPELINE_STAGES: list[str] = [
    "intake",
    "requirements",
    "architecture",
    "capability_discovery",
    "component_selection",
    "harness",
    "workflow",
    "memory",
    "prompts",
    "generation",
    "testing",
    "documentation",
    "deployment",
    "validation",
    "post_generation",
]
