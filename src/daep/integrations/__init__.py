"""External integrations.

Provides configured clients for Azure OpenAI and other
enterprise services used by the DAEP platform.
"""

from daep.integrations.llm import LLMClient, get_llm_client

__all__ = ["LLMClient", "get_llm_client"]
