"""
No Code Frontend Agent

An AI agent that generates front-end UI components, layouts, and pages from natural language descriptions without requiring manual coding. Uses LangChain and Azure OpenAI to interpret design requests and produce HTML/CSS/JavaScript.
Architecture: planner-executor
"""

from __future__ import annotations

import logging
from pathlib import Path

from no_code_frontend_agent.config import load_agent_config
from no_code_frontend_agent.prompts import PromptManager
from no_code_frontend_agent.tools import ToolManager
from no_code_frontend_agent.memory import MemoryManager

logger = logging.getLogger(__name__)


class NoCodeFrontendAgent:
    """Main agent class.

    Implements the planner-executor pattern:
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
            HumanMessage(content=f"{planning_prompt}\n\nRequest: {request}\n\nContext: {context}"),
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
            HumanMessage(content=f"{execution_prompt}\n\nPlan: {plan}\n\nContext: {context}"),
        ]
        result = llm.invoke(messages)
        return result.content
