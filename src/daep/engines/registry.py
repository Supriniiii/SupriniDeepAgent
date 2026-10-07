"""Engine Registry.

Manages registration, discovery, and retrieval of Engineering Engines.
Integrates with the GOE Dispatcher to make engines available at runtime.
"""

from __future__ import annotations

import logging

from daep.engines.base import BaseEngine
from daep.orchestration.dispatcher import Dispatcher
from daep.shared.enums import EngineType

logger = logging.getLogger(__name__)


class EngineRegistry:
    """Central registry for all Engineering Engines.

    Maintains a catalog of available engines and provides
    methods to register them with the GOE dispatcher.
    """

    def __init__(self) -> None:
        self._engines: dict[EngineType, BaseEngine] = {}

    def register(self, engine: BaseEngine) -> None:
        """Register an engine in the registry."""
        self._engines[engine.engine_type] = engine
        logger.info("Registered engine: %s", engine.name)

    def get(self, engine_type: EngineType) -> BaseEngine | None:
        """Retrieve a registered engine by type."""
        return self._engines.get(engine_type)

    def register_all_with_dispatcher(self, dispatcher: Dispatcher) -> None:
        """Register all engines with the GOE dispatcher."""
        for engine in self._engines.values():
            dispatcher.register_engine(engine)
        logger.info(
            "Registered %d engines with dispatcher", len(self._engines)
        )

    @property
    def available(self) -> list[EngineType]:
        """List all registered engine types."""
        return list(self._engines.keys())

    @property
    def count(self) -> int:
        """Number of registered engines."""
        return len(self._engines)

    def register_defaults(self) -> None:
        """Register all default DAEP engines.

        Imports and registers one instance of each primary engine.
        Extension engines (Tool, Documentation, Configuration) are available
        for direct invocation but share dispatch slots with their parent types.
        """
        from daep.engines.architecture import ArchitectureEngine
        from daep.engines.capability import CapabilityEngine
        from daep.engines.component import ComponentEngine
        from daep.engines.evaluation import EvaluationEngine
        from daep.engines.harness import HarnessEngine
        from daep.engines.memory import MemoryEngine
        from daep.engines.prompt import PromptEngine
        from daep.engines.requirements import RequirementsEngine
        from daep.engines.validation import ValidationEngine
        from daep.engines.workflow import WorkflowEngine

        # Primary engines (one per EngineType slot)
        self.register(RequirementsEngine())
        self.register(ArchitectureEngine())
        self.register(CapabilityEngine())
        self.register(ComponentEngine())
        self.register(HarnessEngine())
        self.register(WorkflowEngine())
        self.register(MemoryEngine())
        self.register(PromptEngine())
        self.register(ValidationEngine())
        self.register(EvaluationEngine())

        logger.info("All default engines registered (%d)", self.count)
