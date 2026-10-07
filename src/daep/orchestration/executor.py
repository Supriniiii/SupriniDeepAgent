"""Pipeline executor.

Runs every step in the execution plan sequentially,
dispatching to the appropriate Engineering Engine for each step.
"""

from __future__ import annotations

import logging
import time

from daep.orchestration.context import GenerationContext
from daep.orchestration.dispatcher import Dispatcher
from daep.shared.enums import SessionStatus
from daep.shared.models import ExecutionStep

logger = logging.getLogger(__name__)


class Executor:
    """Executes the engineering pipeline step by step.

    Iterates through the execution plan, dispatches each step
    to the appropriate engine, and tracks progress and timing.
    """

    def __init__(self, dispatcher: Dispatcher) -> None:
        self._dispatcher = dispatcher

    def execute(self, context: GenerationContext) -> GenerationContext:
        """Execute all steps in the execution plan.

        Each step is dispatched to the appropriate engine.
        If a step fails, the pipeline stops and the context
        is marked as failed.
        """
        context.status = SessionStatus.EXECUTING
        plan = context.execution_plan

        logger.info(
            "Executing pipeline: %d steps for '%s'",
            plan.total_steps,
            context.request.name,
        )

        for step in plan.steps:
            try:
                self._execute_step(context, step)
            except Exception as e:
                context.status = SessionStatus.FAILED
                context.add_error(f"Step {step.order} ({step.name}) failed: {e}")
                logger.error("Step failed: %s - %s", step.name, str(e))
                break

        if context.status != SessionStatus.FAILED:
            logger.info(
                "Pipeline complete: %d/%d steps",
                plan.completed_steps,
                plan.total_steps,
            )

        return context

    def _execute_step(
        self, context: GenerationContext, step: ExecutionStep
    ) -> None:
        """Execute a single step by dispatching to its engine."""
        logger.info(
            "Step %d: %s [engine=%s]",
            step.order,
            step.name,
            step.engine.value,
        )

        start_time = time.time()

        # Dispatch to the engine
        artifacts = self._dispatcher.dispatch(step.engine, context)

        # Register artifacts in context
        for artifact in artifacts:
            context.add_artifact(artifact)

        # Mark step complete
        step.duration = time.time() - start_time
        step.completed = True

        logger.info(
            "Step %d complete: %s (%.2fs, %d artifacts)",
            step.order,
            step.name,
            step.duration,
            len(artifacts),
        )
