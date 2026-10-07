"""Project Scaffolder.

Creates the directory structure for a generated Python project.
"""

from __future__ import annotations

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class ProjectScaffolder:
    """Creates the skeleton directory structure for a generated agent project."""

    def create_structure(self, project_dir: Path, package_name: str) -> None:
        """Create the complete project directory structure.

        Structure:
            project_dir/
            ├── src/
            │   └── {package_name}/
            │       └── __init__.py
            ├── tests/
            │   └── __init__.py
            ├── prompts/
            ├── docs/
            └── config.ini
        """
        dirs = [
            project_dir / "src" / package_name,
            project_dir / "tests",
            project_dir / "prompts",
            project_dir / "docs",
        ]

        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)

        # Create __init__.py files
        init_content = f'"""Generated agent: {package_name}."""\n'
        (project_dir / "src" / package_name / "__init__.py").write_text(
            init_content, encoding="utf-8"
        )
        (project_dir / "tests" / "__init__.py").write_text("", encoding="utf-8")

        logger.info("Project structure created: %s", project_dir)
