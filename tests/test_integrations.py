"""Tests for the integrations module.

Tests config loading and LLM client initialization (without actual API calls).
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import patch

from daep.integrations.config import (
    AIConfig,
    PlatformConfig,
    load_config,
)
from daep.integrations.llm import LLMClient, LLMResponse, reset_client


# ---------------------------------------------------------------------------
# Config Tests
# ---------------------------------------------------------------------------


class TestAIConfig:
    def test_defaults(self):
        config = AIConfig()
        assert config.api_type == "azure"
        assert config.chat_model == "aim-gpt-4o-mini-lab"
        assert config.api_key == ""

    def test_custom_values(self):
        config = AIConfig(
            api_key="test-key",
            api_base="https://test.openai.azure.com/",
        )
        assert config.api_key == "test-key"
        assert config.api_base == "https://test.openai.azure.com/"


class TestPlatformConfig:
    def test_defaults(self):
        config = PlatformConfig()
        assert config.workspace == Path(".kiro")
        assert config.output_dir == Path("outputs")
        assert config.log_level == "INFO"


class TestLoadConfig:
    def test_loads_from_ini(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            ini_path = Path(tmpdir) / "config.ini"
            ini_path.write_text(
                "[aim]\n"
                "url = https://my-endpoint.openai.azure.com/\n"
                "api_version = 2024-06-01\n"
                "type = azure\n"
                "models = gpt-4o-mini\n"
            )
            config = load_config(config_path=ini_path)
            assert config.ai.api_base == "https://my-endpoint.openai.azure.com/"
            assert config.ai.api_version == "2024-06-01"
            assert config.ai.chat_model == "gpt-4o-mini"

    def test_env_var_override(self):
        with patch.dict(os.environ, {"AIM_API_KEY": "env-key-123"}):
            config = load_config(config_path=Path("/nonexistent/config.ini"))
            assert config.ai.api_key == "env-key-123"

    def test_loads_from_dotenv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            env_path = Path(tmpdir) / ".env"
            env_path.write_text("AIM_API_KEY=dotenv-key-456\n")

            # Clear existing env var if present
            with patch.dict(os.environ, {}, clear=True):
                os.environ.pop("AIM_API_KEY", None)
                config = load_config(
                    config_path=Path("/nonexistent"),
                    env_file=env_path,
                )
                assert config.ai.api_key == "dotenv-key-456"

    def test_missing_files_returns_defaults(self):
        config = load_config(
            config_path=Path("/nonexistent/config.ini"),
            env_file=Path("/nonexistent/.env"),
        )
        assert config.ai.api_type == "azure"
        assert config.workspace == Path(".kiro")


# ---------------------------------------------------------------------------
# LLM Client Tests (no actual API calls)
# ---------------------------------------------------------------------------


class TestLLMClient:
    def test_not_configured_without_key(self):
        config = AIConfig(api_key="", api_base="")
        client = LLMClient(config)
        assert not client.is_configured

    def test_is_configured_with_key_and_base(self):
        config = AIConfig(
            api_key="test-key",
            api_base="https://test.openai.azure.com/",
        )
        client = LLMClient(config)
        assert client.is_configured

    def test_raises_without_api_key(self):
        config = AIConfig(api_key="", api_base="https://x.com")
        client = LLMClient(config)
        try:
            client.generate("test")
            assert False, "Should have raised"
        except RuntimeError as e:
            assert "No API key" in str(e)

    def test_response_dataclass(self):
        response = LLMResponse(
            content="Hello world",
            model="gpt-4o-mini",
            usage={"prompt_tokens": 10, "completion_tokens": 5},
        )
        assert response.content == "Hello world"
        assert response.usage["prompt_tokens"] == 10

    def test_reset_client(self):
        reset_client()
        # Should not raise
        assert True
