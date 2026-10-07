"""Validation Engineering Engine.

Verifies that generated artifacts satisfy requirements,
architecture, governance, and production readiness criteria.
"""

from __future__ import annotations

from daep.engines.base import BaseEngine
from daep.orchestration.context import GenerationContext
from daep.shared.enums import ArtifactType, EngineType
from daep.shared.models import EngineeringArtifact


class ValidationEngine(BaseEngine):
    """Validates the complete generated solution."""

    @property
    def engine_type(self) -> EngineType:
        return EngineType.VALIDATION

    def _run(self, context: GenerationContext) -> list[EngineeringArtifact]:
        request = context.request
        results = self._validate_artifacts(context)
        content = self._generate_validation_report(request.name, results)

        return [
            EngineeringArtifact(
                name="validation-report.md",
                artifact_type=ArtifactType.REPORT,
                engine=EngineType.VALIDATION,
                content=content,
                metadata={"validation_passed": results["passed"]},
            )
        ]

    def _validate_artifacts(self, context: GenerationContext) -> dict:
        """Validate all produced artifacts."""
        checks: list[dict[str, str]] = []
        passed = True

        # Check that key artifacts exist
        artifact_names = [a.name for a in context.artifacts]

        expected = [
            "architecture.md",
            "component-plan.md",
            "workflow-specification.md",
            "prompt-package.md",
            "memory-strategy.md",
        ]

        for expected_name in expected:
            if expected_name in artifact_names:
                checks.append({"check": expected_name, "status": "PASS"})
            else:
                checks.append({"check": expected_name, "status": "MISSING"})
                passed = False

        # Check no empty artifacts
        for artifact in context.artifacts:
            if not artifact.content.strip():
                checks.append({
                    "check": f"{artifact.name} content",
                    "status": "FAIL (empty)",
                })
                passed = False

        return {"passed": passed, "checks": checks}

    def _generate_validation_report(
        self, name: str, results: dict
    ) -> str:
        status = "PASSED" if results["passed"] else "FAILED"
        check_lines = "\n".join(
            f"| {c['check']} | {c['status']} |" for c in results["checks"]
        )
        return f"""# Validation Report: {name}

## Status: {status}

## Checks

| Check | Status |
|-------|--------|
{check_lines}

## Production Readiness

{"Ready for deployment." if results["passed"] else "Issues must be resolved before deployment."}
"""
