"""Tests for No Code Frontend Agent."""

from pathlib import Path

from no_code_frontend_agent.prompts import PromptManager
from no_code_frontend_agent.memory import MemoryManager
from no_code_frontend_agent.config import load_agent_config


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
            mm.store(request=f"req {i}", response=f"resp {i}")
        assert len(mm._history) == 3


class TestConfig:
    def test_loads_defaults_when_no_file(self):
        config = load_agent_config(Path("/nonexistent/config.ini"))
        assert config["ai"]["model"] == "aim-gpt-4o-mini-lab"
        assert config["ai"]["api_version"] == "2024-06-01"
