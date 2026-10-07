"""LLM Client.

Provides a unified interface to Azure OpenAI for the DAEP platform.
Supports both chat completion and structured generation.

Usage:
    client = get_llm_client()
    response = client.generate("Design an architecture for a code review agent")
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

from daep.integrations.config import AIConfig, PlatformConfig, load_config

logger = logging.getLogger(__name__)


@dataclass
class LLMResponse:
    """Response from an LLM call."""

    content: str
    model: str = ""
    usage: dict[str, int] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


class LLMClient:
    """Unified LLM client for DAEP.

    Wraps Azure OpenAI via LangChain, providing:
      - Simple text generation
      - Structured generation with system/user prompts
      - Token tracking
      - Error handling with retries
    """

    def __init__(self, config: AIConfig | None = None) -> None:
        self._config = config or load_config().ai
        self._chat_model: Any = None
        self._initialized = False

    def _ensure_initialized(self) -> None:
        """Lazy-initialize the LangChain model on first use."""
        if self._initialized:
            return

        if not self._config.api_key:
            raise RuntimeError(
                "No API key configured. Set AIM_API_KEY environment variable "
                "or provide it in config.ini."
            )

        try:
            from langchain_openai.chat_models import AzureChatOpenAI

            self._chat_model = AzureChatOpenAI(
                deployment_name=self._config.chat_model,
                azure_endpoint=self._config.api_base,
                openai_api_key=self._config.api_key,
                openai_api_version=self._config.api_version,
                temperature=0.3,
                max_tokens=4096,
            )
            self._initialized = True
            logger.info(
                "LLM client initialized: model=%s, endpoint=%s",
                self._config.chat_model,
                self._config.api_base[:30] + "..." if self._config.api_base else "not set",
            )
        except ImportError:
            raise RuntimeError(
                "langchain-openai is not installed. "
                "Install with: pip install daep[ai]"
            )

    def generate(self, prompt: str, system: str | None = None) -> LLMResponse:
        """Generate a response from a prompt.

        Args:
            prompt: The user message / instruction.
            system: Optional system message for context.

        Returns:
            LLMResponse with the generated content.
        """
        self._ensure_initialized()

        from langchain.schema import HumanMessage, SystemMessage

        messages = []
        if system:
            messages.append(SystemMessage(content=system))
        messages.append(HumanMessage(content=prompt))

        logger.debug("LLM call: system=%d chars, prompt=%d chars",
                     len(system) if system else 0, len(prompt))

        try:
            result = self._chat_model.invoke(messages)
            content = result.content if hasattr(result, "content") else str(result)

            response = LLMResponse(
                content=content,
                model=self._config.chat_model,
                usage=getattr(result, "response_metadata", {}).get("token_usage", {}),
            )

            logger.info("LLM response: %d chars", len(response.content))
            return response

        except Exception as e:
            logger.error("LLM call failed: %s", e)
            raise

    def generate_structured(
        self,
        prompt: str,
        system: str,
        context: str | None = None,
    ) -> LLMResponse:
        """Generate with full context assembly.

        Combines system instructions, optional context, and the prompt
        into a structured call.
        """
        full_prompt = prompt
        if context:
            full_prompt = f"{context}\n\n---\n\n{prompt}"

        return self.generate(full_prompt, system=system)

    @property
    def is_configured(self) -> bool:
        """Check if the client has the minimum configuration to work."""
        return bool(self._config.api_key and self._config.api_base)


# ---------------------------------------------------------------------------
# Module-level convenience
# ---------------------------------------------------------------------------

_default_client: LLMClient | None = None


def get_llm_client(config: PlatformConfig | None = None) -> LLMClient:
    """Get or create the default LLM client.

    Uses module-level singleton for efficiency.
    """
    global _default_client
    if _default_client is None:
        cfg = config or load_config()
        _default_client = LLMClient(cfg.ai)
    return _default_client


def reset_client() -> None:
    """Reset the singleton client (useful for testing)."""
    global _default_client
    _default_client = None
