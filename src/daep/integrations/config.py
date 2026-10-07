"""Configuration management.

Loads platform configuration from multiple sources:
  1. config.ini (lab standard)
  2. .env file (local development)
  3. Environment variables (runtime override)

Priority: env vars > .env > config.ini
"""

from __future__ import annotations

import os
from configparser import ConfigParser
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class AIConfig:
    """Azure OpenAI configuration."""

    api_key: str = ""
    api_base: str = ""
    api_version: str = "2024-06-01"
    api_type: str = "azure"
    chat_model: str = "aim-gpt-4o-mini-lab"
    embedding_model: str = "aim-text-embedding-3-large-lab"


@dataclass
class PlatformConfig:
    """Complete DAEP platform configuration."""

    ai: AIConfig = field(default_factory=AIConfig)
    workspace: Path = field(default_factory=lambda: Path(".kiro"))
    output_dir: Path = field(default_factory=lambda: Path("outputs"))
    log_level: str = "INFO"


def load_config(
    config_path: Path | None = None,
    env_file: Path | None = None,
) -> PlatformConfig:
    """Load configuration from all available sources.

    Priority order (later overrides earlier):
      1. config.ini
      2. .env file
      3. Environment variables
    """
    config = PlatformConfig()

    # 1. Load config.ini (lab standard)
    ini_path = config_path or Path("config.ini")
    if ini_path.exists():
        _load_from_ini(config, ini_path)

    # 2. Load .env file (local dev)
    dotenv_path = env_file or Path(".env")
    if dotenv_path.exists():
        _load_dotenv(config, dotenv_path)

    # 3. Override from environment variables
    _load_from_env(config)

    return config


def _load_from_ini(config: PlatformConfig, path: Path) -> None:
    """Load settings from config.ini."""
    parser = ConfigParser()
    with open(path) as f:
        parser.read_file(f)

    if parser.has_section("aim"):
        config.ai.api_base = parser.get("aim", "url", fallback="")
        config.ai.api_version = parser.get("aim", "api_version", fallback="2024-06-01")
        config.ai.api_type = parser.get("aim", "type", fallback="azure")

        # Model from config if available
        models = parser.get("aim", "models", fallback="")
        if models:
            config.ai.chat_model = models.split(",")[0].strip()


def _load_dotenv(config: PlatformConfig, path: Path) -> None:
    """Load settings from .env file."""
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

    # Apply to config
    _load_from_env(config)


def _load_from_env(config: PlatformConfig) -> None:
    """Load settings from environment variables."""
    # API Key (primary: AIM_API_KEY, fallback: OPENAI_API_KEY)
    config.ai.api_key = os.environ.get(
        "AIM_API_KEY", os.environ.get("OPENAI_API_KEY", config.ai.api_key)
    )

    # Override endpoint if set
    api_base = os.environ.get("AIM_API_BASE", os.environ.get("OPENAI_API_BASE"))
    if api_base:
        config.ai.api_base = api_base

    # Override model if set
    chat_model = os.environ.get("AIM_CHAT_MODEL")
    if chat_model:
        config.ai.chat_model = chat_model

    embedding_model = os.environ.get("AIM_EMBEDDING_MODEL")
    if embedding_model:
        config.ai.embedding_model = embedding_model

    # Platform settings
    log_level = os.environ.get("DAEP_LOG_LEVEL")
    if log_level:
        config.log_level = log_level

    workspace = os.environ.get("DAEP_WORKSPACE")
    if workspace:
        config.workspace = Path(workspace)

    output_dir = os.environ.get("DAEP_OUTPUT_DIR")
    if output_dir:
        config.output_dir = Path(output_dir)
