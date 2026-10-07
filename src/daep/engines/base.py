"""Base Engineering Engine.

Defines the common interface that all Engineering Engines must implement.
Provides shared lifecycle hooks: validate_inputs, execute, validate_outputs.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any

from daep.orchestration.context import GenerationContext
from daep.shared.enums import EngineType
from daep.shared.models import EngineeringArtifact

logger = logging.getLogger(__name__)


class BaseEngine(ABC):
    """Abstract base class for all Engineering Engines.

    Every engine must:
      1. Declare its engine_type.
      2. Implement _run() to produce artifacts.

    The base class provides:
      - Input validation.
      - Logging.
      - Output validation.
      - Error handling.

    Usage by the Dispatcher:
        artifacts = engine.execute(context)
    """

    @property
    @abstractmethod
    def engine_type(self) -> EngineType:
        """The engine's unique type identifier."""
        ...

    @property
    def name(self) -> str:
        """Human-readable engine name."""
        return f"{self.engine_type.value.title()} Engineering Engine"

    # ------------------------------------------------------------------
    # Public interface (called by Dispatcher)
    # ------------------------------------------------------------------

    def execute(self, context: GenerationContext) -> list[EngineeringArtifact]:
        """Execute the engine's engineering process.

        Template method that handles validation and error handling
        around the core _run() implementation.
        """
        logger.info("[%s] Starting execution", self.name)

        # Validate inputs
        issues = self.validate_inputs(context)
        if issues:
            logger.warning("[%s] Input validation issues: %s", self.name, issues)

        # Core execution
        try:
            artifacts = self._run(context)
        except Exception as e:
            logger.error("[%s] Execution failed: %s", self.name, e)
            raise

        # Validate outputs
        output_issues = self.validate_outputs(artifacts)
        if output_issues:
            logger.warning("[%s] Output validation issues: %s", self.name, output_issues)

        logger.info(
            "[%s] Completed: %d artifacts produced", self.name, len(artifacts)
        )
        return artifacts

    # ------------------------------------------------------------------
    # Hooks for subclasses
    # ------------------------------------------------------------------

    @abstractmethod
    def _run(self, context: GenerationContext) -> list[EngineeringArtifact]:
        """Core engine logic. Subclasses implement this.

        Args:
            context: The shared generation context with all loaded resources.

        Returns:
            List of engineering artifacts produced by this engine.
        """
        ...

    def validate_inputs(self, context: GenerationContext) -> list[str]:
        """Validate that required inputs are available.

        Override in subclasses for engine-specific validation.
        Returns a list of issues (empty if valid).
        """
        return []

    def validate_outputs(
        self, artifacts: list[EngineeringArtifact]
    ) -> list[str]:
        """Validate produced artifacts meet quality standards.

        Override in subclasses for engine-specific validation.
        Returns a list of issues (empty if valid).
        """
        issues: list[str] = []
        for artifact in artifacts:
            if not artifact.name:
                issues.append("Artifact missing name")
            if not artifact.content:
                issues.append(f"Artifact '{artifact.name}' has empty content")
        return issues

    def get_knowledge(self, context: GenerationContext, domain: str) -> dict[str, str]:
        """Retrieve knowledge from a specific domain."""
        return context.knowledge.get(domain, {})

    def get_template(self, context: GenerationContext, path: str) -> str:
        """Retrieve a template by path."""
        return context.templates.get(path, "")
