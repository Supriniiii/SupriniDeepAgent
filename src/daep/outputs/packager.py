"""Output Packager.

Assembles engineering artifacts and generated project into a single
delivery package with a manifest, summary, and validation status.
"""

from __future__ import annotations

import json
import logging
import shutil
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from daep.orchestration.context import GenerationContext
from daep.orchestration.report import GenerationReport

logger = logging.getLogger(__name__)


@dataclass
class PackageManifest:
    """Describes the contents of a delivery package."""

    name: str
    version: str = "0.1.0"
    generated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    generator: str = "Deep Agent Engineering Platform"
    agent_type: str = ""
    architecture: str = ""
    engineering_artifacts: list[str] = field(default_factory=list)
    project_files: list[str] = field(default_factory=list)
    validation_passed: bool = True
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


@dataclass
class DeliveryPackage:
    """The final output of a DAEP generation run."""

    path: Path
    manifest: PackageManifest
    engineering_dir: Path | None = None
    project_dir: Path | None = None


class OutputPackager:
    """Packages all outputs into a single delivery.

    Creates:
        delivery_root/
        ├── manifest.json          ← Package descriptor
        ├── summary.md             ← Human-readable summary
        ├── engineering/           ← Engineering artifacts
        │   ├── requirements.md
        │   ├── architecture.md
        │   ├── ...
        └── project/               ← Generated runnable project
            ├── pyproject.toml
            ├── src/
            ├── ...
    """

    def package(
        self,
        delivery_dir: Path,
        context: GenerationContext,
        report: GenerationReport,
        project_dir: Path | None = None,
    ) -> DeliveryPackage:
        """Create the delivery package.

        Args:
            delivery_dir: Root directory for the delivery.
            context: Generation context with artifacts.
            report: Engineering report.
            project_dir: Path to the generated project (if separate).

        Returns:
            DeliveryPackage with paths and manifest.
        """
        delivery_dir.mkdir(parents=True, exist_ok=True)

        # 1. Write engineering artifacts
        eng_dir = delivery_dir / "engineering"
        eng_dir.mkdir(exist_ok=True)
        artifact_files = self._write_engineering_artifacts(eng_dir, context)

        # 2. Copy or reference generated project
        proj_dir: Path | None = None
        project_files: list[str] = []
        if project_dir and project_dir.exists():
            proj_dir = delivery_dir / "project"
            project_files = self._copy_project(project_dir, proj_dir)

        # 3. Build manifest
        manifest = PackageManifest(
            name=context.request.name,
            agent_type=context.request.agent_type or "generic",
            architecture=context.request.architecture or "planner-executor",
            engineering_artifacts=artifact_files,
            project_files=project_files,
            validation_passed=report.success,
            warnings=report.warnings,
            errors=report.errors,
        )

        # 4. Write manifest
        manifest_path = delivery_dir / "manifest.json"
        manifest_path.write_text(manifest.to_json(), encoding="utf-8")

        # 5. Write summary
        summary_path = delivery_dir / "summary.md"
        summary_path.write_text(
            self._generate_summary(context, report, manifest),
            encoding="utf-8",
        )

        logger.info(
            "Package created: %s (%d engineering, %d project files)",
            delivery_dir,
            len(artifact_files),
            len(project_files),
        )

        return DeliveryPackage(
            path=delivery_dir,
            manifest=manifest,
            engineering_dir=eng_dir,
            project_dir=proj_dir,
        )

    def _write_engineering_artifacts(
        self, eng_dir: Path, context: GenerationContext
    ) -> list[str]:
        """Write engineering artifacts to the engineering/ directory."""
        files: list[str] = []
        for artifact in context.artifacts:
            file_path = eng_dir / artifact.name
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(artifact.content, encoding="utf-8")
            files.append(artifact.name)
        return files

    def _copy_project(self, source: Path, dest: Path) -> list[str]:
        """Copy the generated project to the delivery."""
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(source, dest)

        files: list[str] = []
        for file in dest.rglob("*"):
            if file.is_file():
                files.append(str(file.relative_to(dest)))
        return files

    def _generate_summary(
        self,
        context: GenerationContext,
        report: GenerationReport,
        manifest: PackageManifest,
    ) -> str:
        """Generate a human-readable delivery summary."""
        status = "✓ PASSED" if report.success else "✗ FAILED"
        eng_list = "\n".join(f"- {f}" for f in manifest.engineering_artifacts)
        proj_count = len(manifest.project_files)

        warnings_section = ""
        if manifest.warnings:
            w_list = "\n".join(f"- {w}" for w in manifest.warnings)
            warnings_section = f"\n## Warnings\n\n{w_list}\n"

        return f"""# Delivery Summary: {manifest.name}

## Status: {status}

## Package Details

| Property | Value |
|----------|-------|
| Agent | {manifest.name} |
| Type | {manifest.agent_type} |
| Architecture | {manifest.architecture} |
| Generated | {manifest.generated_at} |
| Generator | {manifest.generator} |

## Engineering Artifacts ({len(manifest.engineering_artifacts)} files)

{eng_list}

## Generated Project ({proj_count} files)

A complete, installable Python project is included in the `project/` directory.

To use:
```bash
cd project/
pip install -e .
export AIM_API_KEY=your-key
# Edit config.ini with your endpoint
pytest
```

## Engineering Report

- Duration: {report.duration:.2f}s
- Steps: {report.steps_completed}/{report.steps_total}
- Artifacts: {report.artifacts_produced}
{warnings_section}
## Validation

Validation: {status}
"""
