
"""Generation Orchestration Engine (GOE).

The central coordinator for the DAEP engineering lifecycle.
Accepts generation requests and orchestrates the complete pipeline:
  Create Context → Load Framework → Plan → Dispatch → Execute →
  Validate → Write Outputs → Report
"""

from __future__ import annotations

import logging
import time
from pathlib import Path

from daep.orchestration.context import GenerationContext
from daep.orchestration.dispatcher import Dispatcher
from daep.orchestration.executor import Executor
from daep.orchestration.loader import FrameworkLoader
from daep.orchestration.planner import Planner
from daep.orchestration.report import GenerationReport, ReportBuilder
from daep.orchestration.request import GenerationRequest
from daep.shared.enums import SessionStatus

logger = logging.getLogger(__name__)


class GenerationOrchestrationEngine:
    """Orchestrates the complete Deep Agent generation lifecycle.

    The GOE does not perform engineering work itself.
    It coordinates the framework loader, planner, dispatcher,
    executor, and report builder to transform a developer request
    into a production-ready solution.

    Usage:
        goe = GenerationOrchestrationEngine()
        report = goe.generate(request)
    """

    def __init__(
        self,
        workspace: Path | None = None,
        dispatcher: Dispatcher | None = None,
    ) -> None:
        self._workspace = workspace or Path(".kiro")
        self._loader = FrameworkLoader(self._workspace)
        self._planner = Planner()
        self._dispatcher = dispatcher or Dispatcher()
        self._executor = Executor(self._dispatcher)
        self._report_builder = ReportBuilder()

    def generate(self, request: GenerationRequest) -> GenerationReport:
        """Execute the complete engineering pipeline.

        This is the primary entry point for the platform.

        Flow:
            1. Create Context
            2. Load Framework
            3. Plan
            4. Execute (dispatch to engines)
            5. Validate
            6. Write Outputs
            7. Report
        """
        start_time = time.time()
        logger.info("GOE: Starting generation for '%s'", request.name)

        # 1. Create Context
        context = GenerationContext(request=request)
        context.status = SessionStatus.LOADING

        # 2. Load Framework
        context = self._load_framework(context)
        if context.is_failed:
            return self._build_report(context, start_time)

        # 3. Plan
        context.status = SessionStatus.PLANNING
        context.execution_plan = self._planner.plan(context)

        # 4. Execute (dispatches to engines)
        context = self._executor.execute(context)
        if context.is_failed:
            return self._build_report(context, start_time)

        # 5. Validate
        context.status = SessionStatus.VALIDATING
        context = self._validate(context)
        if context.is_failed:
            return self._build_report(context, start_time)

        # 6. Write Outputs
        context.status = SessionStatus.WRITING
        written_files = self._write_outputs(context)

        # 7. Complete
        context.status = SessionStatus.COMPLETED
        logger.info(
            "GOE: Generation complete for '%s' (%d artifacts, %d files)",
            request.name,
            len(context.artifacts),
            len(written_files),
        )

        return self._build_report(context, start_time, written_files)

    def _load_framework(self, context: GenerationContext) -> GenerationContext:
        """Load the DAEP framework resources."""
        try:
            return self._loader.load(context)
        except Exception as e:
            context.status = SessionStatus.FAILED
            context.add_error(f"Framework loading failed: {e}")
            logger.error("Framework loading failed: %s", e)
            return context

    def _validate(self, context: GenerationContext) -> GenerationContext:
        """Validate generated artifacts.

        For v0.1 this is a simple completeness check.
        Future versions will invoke the Validation Engine.
        """
        plan = context.execution_plan

        if plan.completed_steps < plan.total_steps:
            context.add_warning(
                f"Only {plan.completed_steps}/{plan.total_steps} steps completed"
            )

        if not context.artifacts:
            context.add_warning("No artifacts were produced")

        return context

    def _write_outputs(self, context: GenerationContext) -> list[Path]:
        """Write generated artifacts to the output directory."""
        output_dir = context.request.output_directory
        output_dir.mkdir(parents=True, exist_ok=True)

        written: list[Path] = []
        for artifact in context.artifacts:
            file_path = output_dir / artifact.name
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(artifact.content, encoding="utf-8")
            artifact.path = file_path
            written.append(file_path)
            logger.debug("Wrote artifact: %s", file_path)

        return written

    def _build_report(
        self,
        context: GenerationContext,
        start_time: float,
        written_files: list[Path] | None = None,
    ) -> GenerationReport:
        """Build the final generation report."""
        duration = time.time() - start_time
        return self._report_builder.build(context, duration, written_files)

    @property
    def dispatcher(self) -> Dispatcher:
        """Access the dispatcher for engine registration."""
        return self._dispatcher
