"""Template Renderer.

Generates Python source code for agent projects.
Each method renders a specific file type with proper imports,
structure, and documentation.
"""

from __future__ import annotations


class TemplateRenderer:
    """Renders Python source code templates for generated agents."""

    def render_pyproject(self, package_name: str, description: str) -> str:
        """Render pyproject.toml."""
        return f'''[project]
name = "{package_name}"
version = "0.1.0"
description = "{description}"
requires-python = ">=3.11"
dependencies = [
    "langchain>=0.3.0",
    "langchain-openai>=0.2.0",
    "pydantic>=2.0",
    "pyyaml>=6.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "ruff>=0.5",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/{package_name}"]
'''

    def render_agent(
        self,
        package_name: str,
        agent_name: str,
        description: str,
        architecture: str,
    ) -> str:
        """Render the main agent class."""
        class_name = agent_name.replace(" ", "").replace("-", "")
        return f'''"""
{agent_name}

{description}
Architecture: {architecture}
"""

from __future__ import annotations

import logging
from pathlib import Path

from {package_name}.config import load_agent_config
from {package_name}.prompts import PromptManager
from {package_name}.tools import ToolManager
from {package_name}.memory import MemoryManager

logger = logging.getLogger(__name__)


class {class_name}:
    """Main agent class.

    Implements the {architecture} pattern:
      Plan → Execute → Reflect → Verify
    """

    def __init__(self, config_path: Path | None = None) -> None:
        self.config = load_agent_config(config_path)
        self.prompts = PromptManager()
        self.tools = ToolManager()
        self.memory = MemoryManager()
        self._llm = None

    def _get_llm(self):
        """Lazy-initialize the LLM client."""
        if self._llm is None:
            from langchain_openai.chat_models import AzureChatOpenAI

            self._llm = AzureChatOpenAI(
                deployment_name=self.config["ai"]["model"],
                azure_endpoint=self.config["ai"]["endpoint"],
                openai_api_key=self.config["ai"]["api_key"],
                openai_api_version=self.config["ai"]["api_version"],
                temperature=0.3,
            )
        return self._llm

    def run(self, request: str) -> str:
        """Execute the agent on a request.

        Args:
            request: Natural language description of what to do.

        Returns:
            The agent's response/output.
        """
        logger.info("Agent executing: %s", request[:80])

        # 1. Build context
        context = self.memory.get_context()
        system_prompt = self.prompts.get_system_prompt()

        # 2. Plan
        plan = self._plan(request, context, system_prompt)

        # 3. Execute
        result = self._execute(plan, context)

        # 4. Update memory
        self.memory.store(request=request, response=result)

        return result

    def _plan(self, request: str, context: str, system_prompt: str) -> str:
        """Create an execution plan."""
        from langchain.schema import HumanMessage, SystemMessage

        llm = self._get_llm()
        planning_prompt = self.prompts.get_planning_prompt()

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"{{planning_prompt}}\\n\\nRequest: {{request}}\\n\\nContext: {{context}}"),
        ]
        result = llm.invoke(messages)
        return result.content

    def _execute(self, plan: str, context: str) -> str:
        """Execute the plan."""
        from langchain.schema import HumanMessage, SystemMessage

        llm = self._get_llm()
        execution_prompt = self.prompts.get_execution_prompt()

        messages = [
            SystemMessage(content=self.prompts.get_system_prompt()),
            HumanMessage(content=f"{{execution_prompt}}\\n\\nPlan: {{plan}}\\n\\nContext: {{context}}"),
        ]
        result = llm.invoke(messages)
        return result.content
'''

    def render_prompts_module(
        self, package_name: str, agent_name: str, description: str
    ) -> str:
        """Render the prompts management module."""
        return f'''"""Prompt management for {agent_name}."""

from __future__ import annotations

from pathlib import Path


class PromptManager:
    """Loads and manages externalized prompts."""

    def __init__(self, prompts_dir: Path | None = None) -> None:
        self._dir = prompts_dir or Path(__file__).parent.parent.parent / "prompts"

    def get_system_prompt(self) -> str:
        """Load the system prompt."""
        path = self._dir / "system.md"
        if path.exists():
            return path.read_text(encoding="utf-8")
        return "You are {agent_name}. {description}"

    def get_planning_prompt(self) -> str:
        """Load the planning prompt."""
        path = self._dir / "planning.md"
        if path.exists():
            return path.read_text(encoding="utf-8")
        return "Analyze the request and create a step-by-step plan."

    def get_execution_prompt(self) -> str:
        """Load the execution prompt."""
        path = self._dir / "execution.md"
        if path.exists():
            return path.read_text(encoding="utf-8")
        return "Execute the plan step by step. Produce the final output."
'''

    def render_tools_module(
        self, package_name: str, agent_type: str | None
    ) -> str:
        """Render the tools module."""
        tools_section = ""
        if agent_type == "coding":
            tools_section = '''
    def read_file(self, path: str) -> str:
        """Read a file from the project."""
        file_path = Path(path)
        if file_path.exists():
            return file_path.read_text(encoding="utf-8")
        return f"File not found: {path}"

    def write_file(self, path: str, content: str) -> str:
        """Write content to a file."""
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")
        return f"Written: {path}"
'''
        elif agent_type == "research":
            tools_section = '''
    def search(self, query: str) -> str:
        """Search for information."""
        # Placeholder — integrate with your search service
        return f"Search results for: {query}"
'''

        return f'''"""Tool management for the agent."""

from __future__ import annotations

from pathlib import Path


class ToolManager:
    """Manages external tool integrations."""

    def __init__(self) -> None:
        self._tools: dict[str, callable] = {{}}
        self._register_defaults()

    def _register_defaults(self) -> None:
        """Register default tools."""
        pass
{tools_section}
    def list_tools(self) -> list[str]:
        """List available tools."""
        return list(self._tools.keys())
'''

    def render_memory_module(self, package_name: str) -> str:
        """Render the memory management module."""
        return f'''"""Memory management for the agent."""

from __future__ import annotations


class MemoryManager:
    """Manages agent memory (working + session)."""

    def __init__(self, max_history: int = 20) -> None:
        self._history: list[dict[str, str]] = []
        self._max_history = max_history

    def store(self, request: str, response: str) -> None:
        """Store an interaction in memory."""
        self._history.append({{"request": request, "response": response[:500]}})
        if len(self._history) > self._max_history:
            self._history = self._history[-self._max_history:]

    def get_context(self) -> str:
        """Get recent context for the agent."""
        if not self._history:
            return "No previous context."
        recent = self._history[-5:]
        lines = []
        for entry in recent:
            lines.append(f"Request: {{entry['request'][:100]}}")
            lines.append(f"Response: {{entry['response'][:200]}}")
            lines.append("")
        return "\\n".join(lines)

    def clear(self) -> None:
        """Clear all memory."""
        self._history.clear()
'''

    def render_config_module(self, package_name: str) -> str:
        """Render the configuration module."""
        return f'''"""Configuration loading for the agent."""

from __future__ import annotations

import os
from configparser import ConfigParser
from pathlib import Path
from typing import Any


def load_agent_config(config_path: Path | None = None) -> dict[str, Any]:
    """Load agent configuration.

    Reads from config.ini and environment variables.
    """
    path = config_path or Path("config.ini")
    config: dict[str, Any] = {{
        "ai": {{
            "model": "aim-gpt-4o-mini-lab",
            "endpoint": "",
            "api_key": "",
            "api_version": "2024-06-01",
        }}
    }}

    # Load from config.ini
    if path.exists():
        parser = ConfigParser()
        with open(path) as f:
            parser.read_file(f)

        if parser.has_section("aim"):
            config["ai"]["endpoint"] = parser.get("aim", "url", fallback="")
            config["ai"]["api_version"] = parser.get("aim", "api_version", fallback="2024-06-01")
            models = parser.get("aim", "models", fallback="")
            if models:
                config["ai"]["model"] = models.split(",")[0].strip()

    # Override from environment
    config["ai"]["api_key"] = os.environ.get("AIM_API_KEY", "")
    endpoint = os.environ.get("AIM_API_BASE")
    if endpoint:
        config["ai"]["endpoint"] = endpoint

    return config
'''

    def render_system_prompt(self, name: str, description: str) -> str:
        """Render the system prompt file."""
        return f"""You are {name}.

## Purpose

{description}

## Behavior

- Follow engineering standards.
- Produce structured, deterministic outputs.
- Validate your work before responding.
- Be concise and precise.
- Cite sources when applicable.

## Constraints

- Do not hallucinate information.
- If unsure, say so clearly.
- Follow the plan step by step.
- Produce actionable outputs.
"""

    def render_planning_prompt(self) -> str:
        """Render the planning prompt file."""
        return """Analyze the following request and create a step-by-step execution plan.

## Instructions

1. Identify the core objective.
2. Break the objective into discrete tasks.
3. Identify dependencies between tasks.
4. Order tasks by dependency and priority.
5. Note any tools or information needed.

## Output Format

Produce a numbered plan:
1. [Task description]
2. [Task description]
...
"""

    def render_execution_prompt(self) -> str:
        """Render the execution prompt file."""
        return """Execute the following plan step by step.

## Instructions

- Complete each step in order.
- Use available tools when needed.
- Validate outputs before proceeding.
- Report any issues encountered.
- Produce the final result.

## Output

Provide the complete result of executing the plan.
"""

    def render_agent_config(self, package_name: str, agent_name: str) -> str:
        """Render the config.ini file."""
        return f"""[aim]
url = 
api_version = 2024-06-01
type = azure
models = aim-gpt-4o-mini-lab

[agent]
name = {agent_name}
package = {package_name}
log_level = INFO
"""

    def render_tests(self, package_name: str, agent_name: str) -> str:
        """Render the test file."""
        class_name = agent_name.replace(" ", "").replace("-", "")
        return f'''"""Tests for {agent_name}."""

from pathlib import Path

from {package_name}.prompts import PromptManager
from {package_name}.memory import MemoryManager
from {package_name}.config import load_agent_config


class TestPromptManager:
    def test_loads_defaults(self):
        pm = PromptManager(prompts_dir=Path("/nonexistent"))
        system = pm.get_system_prompt()
        assert len(system) > 0

    def test_loads_planning(self):
        pm = PromptManager(prompts_dir=Path("/nonexistent"))
        planning = pm.get_planning_prompt()
        assert "plan" in planning.lower()


class TestMemoryManager:
    def test_store_and_retrieve(self):
        mm = MemoryManager()
        mm.store(request="test request", response="test response")
        context = mm.get_context()
        assert "test request" in context

    def test_clear(self):
        mm = MemoryManager()
        mm.store(request="x", response="y")
        mm.clear()
        context = mm.get_context()
        assert "No previous context" in context

    def test_max_history(self):
        mm = MemoryManager(max_history=3)
        for i in range(10):
            mm.store(request=f"req {{i}}", response=f"resp {{i}}")
        assert len(mm._history) == 3


class TestConfig:
    def test_loads_defaults_when_no_file(self):
        config = load_agent_config(Path("/nonexistent/config.ini"))
        assert config["ai"]["model"] == "aim-gpt-4o-mini-lab"
        assert config["ai"]["api_version"] == "2024-06-01"
'''

    def render_readme(self, name: str, description: str) -> str:
        """Render the project README."""
        package_name = name.lower().replace(" ", "_").replace("-", "_")
        return f"""# {name}

{description}

## Quick Start

```bash
# Install
pip install -e .

# Set your API key
export AIM_API_KEY=your-key-here

# Run
python -c "from {package_name}.agent import {name.replace(' ', '')}; agent = {name.replace(' ', '')}(); print(agent.run('Hello'))"
```

## Architecture

- Pattern: Planner-Executor
- LLM: Azure OpenAI
- Memory: Session-based
- Prompts: Externalized in `prompts/`

## Configuration

Edit `config.ini` with your Azure OpenAI endpoint:

```ini
[aim]
url = https://your-endpoint.openai.azure.com/
api_version = 2024-06-01
type = azure
models = aim-gpt-4o-mini-lab
```

Set your API key as an environment variable:

```bash
export AIM_API_KEY=your-key
```

## Project Structure

```
{package_name}/
├── src/{package_name}/
│   ├── agent.py      ← Main agent class
│   ├── prompts.py    ← Prompt management
│   ├── tools.py      ← Tool integrations
│   ├── memory.py     ← Memory management
│   └── config.py     ← Configuration
├── prompts/           ← Externalized prompt files
├── tests/             ← Test suite
├── config.ini         ← Configuration
└── pyproject.toml     ← Package definition
```

## Testing

```bash
pip install -e ".[dev]"
pytest
```

## Generated by DAEP

This agent was generated by the Deep Agent Engineering Platform.
"""
