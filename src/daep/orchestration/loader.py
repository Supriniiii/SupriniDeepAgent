"""Framework loader.

Reads the .kiro directory structure and populates the GenerationContext
with steering, knowledge, standards, templates, and specifications.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import yaml

from daep.orchestration.context import GenerationContext

logger = logging.getLogger(__name__)


class FrameworkLoader:
    """Loads the DAEP framework resources from .kiro/.

    Reads steering documents, knowledge base, standards,
    templates, and specifications into the GenerationContext.
    """

    def __init__(self, workspace: Path | None = None) -> None:
        self._workspace = workspace or Path(".kiro")

    def load(self, context: GenerationContext) -> GenerationContext:
        """Load all framework resources into the context."""
        logger.info("Loading framework from: %s", self._workspace)

        context.steering = self._load_steering()
        context.knowledge = self._load_knowledge()
        context.standards = self._load_standards()
        context.templates = self._load_templates()
        context.specifications = self._load_specifications()

        logger.info(
            "Framework loaded: steering=%d, knowledge=%d, standards=%d, "
            "templates=%d, specs=%d",
            len(context.steering),
            len(context.knowledge),
            len(context.standards),
            len(context.templates),
            len(context.specifications),
        )
        return context

    def _load_steering(self) -> dict[str, str]:
        """Load all steering documents."""
        path = self._workspace / "steering"
        if not path.exists():
            logger.warning("Steering path not found: %s", path)
            return {}

        documents: dict[str, str] = {}
        for file in sorted(path.glob("*.md")):
            documents[file.stem] = file.read_text(encoding="utf-8")
        return documents

    def _load_knowledge(self) -> dict[str, dict[str, str]]:
        """Load knowledge base organized by domain."""
        path = self._workspace / "knowledge"
        if not path.exists():
            logger.warning("Knowledge path not found: %s", path)
            return {}

        domains: dict[str, dict[str, str]] = {}
        for domain_dir in sorted(path.iterdir()):
            if domain_dir.is_dir():
                docs: dict[str, str] = {}
                for file in domain_dir.rglob("*.md"):
                    relative = file.relative_to(domain_dir)
                    docs[str(relative)] = file.read_text(encoding="utf-8")
                if docs:
                    domains[domain_dir.name] = docs
        return domains

    def _load_standards(self) -> dict[str, str]:
        """Load organization standards (code and docs)."""
        path = self._workspace / "standards"
        if not path.exists():
            return {}

        documents: dict[str, str] = {}
        for ext in ("*.py", "*.md"):
            for file in path.rglob(ext):
                relative = file.relative_to(path)
                documents[str(relative)] = file.read_text(encoding="utf-8")
        return documents

    def _load_templates(self) -> dict[str, str]:
        """Load template catalog (paths only for efficiency)."""
        path = self._workspace / "templates"
        if not path.exists():
            return {}

        templates: dict[str, str] = {}
        for file in path.rglob("*.md"):
            if file.name != "README.md":
                relative = file.relative_to(path)
                templates[str(relative)] = file.name
        return templates

    def _load_specifications(self) -> dict[str, Any]:
        """Load engine contract YAML specifications."""
        path = self._workspace / "engines"
        if not path.exists():
            return {}

        specs: dict[str, Any] = {}
        for engine_dir in sorted(path.iterdir()):
            if engine_dir.is_dir():
                contract = engine_dir / "engine-contract.yaml"
                if contract.exists():
                    with open(contract, encoding="utf-8") as f:
                        specs[engine_dir.name] = yaml.safe_load(f) or {}
        return specs

    def load_template_content(self, category: str, name: str) -> str | None:
        """Load the full content of a specific template."""
        path = self._workspace / "templates" / category / name
        if path.exists():
            return path.read_text(encoding="utf-8")
        return None
