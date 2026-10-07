"""Engine dispatcher.

Selects and routes execution to the appropriate Engineering Engines
based on the execution plan.
"""

from __future__ import annotations

import logging
from typing import Protocol

from daep.orchestration.context import GenerationContext
from daep.shared.enums import EngineType
from daep.shared.models import EngineeringArtifact

logger = logging.getLogger(__name__)


class EngineeringEngine(Protocol):
    """Protocol that all Engineering Engines must implement."""

    @property
    def engine_type(self) -> EngineType: ...

    def execute(self, context: GenerationContext) -> list[EngineeringArtifact]: ...


class Dispatcher:
    """Routes execution to registered Engineering Engines.

    Holds a registry of available engines and selects the
    appropriate engine for each execution step.
    """

    def __init__(self) -> None:
        self._engines: dict[EngineType, EngineeringEngine] = {}

    def register_engine(self, engine: EngineeringEngine) -> None:
        """Register an engineering engine."""
        self._engines[engine.engine_type] = engine
        logger.info("Engine registered: %s", engine.engine_type.value)

    def dispatch(
        self, engine_type: EngineType, context: GenerationContext
    ) -> list[EngineeringArtifact]:
        """Dispatch work to a registered engine.

        Returns the artifacts produced by the engine.
        Returns empty list if no engine is registered for the type.
        """
        engine = self._engines.get(engine_type)

        if engine is None:
            logger.debug("No engine registered for: %s", engine_type.value)
            return []

        logger.info("Dispatching to engine: %s", engine_type.value)
        artifacts = engine.execute(context)

        logger.info(
            "Engine completed: %s produced %d artifacts",
            engine_type.value,
            len(artifacts),
        )
        return artifacts

    @property
    def available_engines(self) -> list[EngineType]:
        """List all registered engine types."""
        return list(self._engines.keys())

    @property
    def engine_count(self) -> int:
        """Count of registered engines."""
        return len(self._engines)
