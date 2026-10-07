"""Generation report.

Produces a summary report of the generation session including
success/failure, artifacts produced, timing, and issues.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from daep.orchestration.context import GenerationContext
from daep.shared.enums import SessionStatus

logger = logging.getLogger(__name__)


@dataclass
class GenerationReport:
    """Summary of a completed generation session."""

    success: bool
    duration: float
    generated_files: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    steps_completed: int = 0
    steps_total: int = 0
    artifacts_produced: int = 0
    timestamp: datetime = field(default_factory=datetime.now)

    def summary(self) -> str:
        """Produce a human-readable summary."""
        status = "SUCCESS" if self.success else "FAILED"
        lines = [
            f"Generation Report ({status})",
            f"{'=' * 40}",
            f"Duration: {self.duration:.2f}s",
            f"Steps: {self.steps_completed}/{self.steps_total}",
            f"Artifacts: {self.artifacts_produced}",
            f"Files: {len(self.generated_files)}",
        ]

        if self.warnings:
            lines.append(f"Warnings: {len(self.warnings)}")
            for w in self.warnings:
                lines.append(f"  ⚠ {w}")

        if self.errors:
            lines.append(f"Errors: {len(self.errors)}")
            for e in self.errors:
                lines.append(f"  ✗ {e}")

        if self.generated_files:
            lines.append("Generated Files:")
            for f in self.generated_files:
                lines.append(f"  → {f}")

        return "\n".join(lines)


class ReportBuilder:
    """Builds a GenerationReport from a completed GenerationContext."""

    def build(
        self,
        context: GenerationContext,
        duration: float,
        written_files: list[Path] | None = None,
    ) -> GenerationReport:
        """Create a report from the generation context."""
        plan = context.execution_plan

        report = GenerationReport(
            success=context.status == SessionStatus.COMPLETED,
            duration=duration,
            generated_files=[str(f) for f in (written_files or [])],
            warnings=list(context.warnings),
            errors=list(context.errors),
            steps_completed=plan.completed_steps,
            steps_total=plan.total_steps,
            artifacts_produced=len(context.artifacts),
        )

        logger.info(
            "Report built: success=%s, artifacts=%d, duration=%.2fs",
            report.success,
            report.artifacts_produced,
            report.duration,
        )
        return report
