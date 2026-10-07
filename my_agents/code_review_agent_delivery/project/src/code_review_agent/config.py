"""Configuration loading for the agent."""

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
    config: dict[str, Any] = {
        "ai": {
            "model": "aim-gpt-4o-mini-lab",
            "endpoint": "",
            "api_key": "",
            "api_version": "2024-06-01",
        }
    }

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
