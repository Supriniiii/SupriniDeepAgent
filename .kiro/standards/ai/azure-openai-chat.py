# Simple query to Azure OpenAI model: GPT 4o-mini
# Shows how to incorporate LangChain prompt templates

import os
from configparser import ConfigParser
from langchain_openai.chat_models import AzureChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


# --- Configuration ---
# Read API key from OpenShift secrets
# Get API details from config.ini

config = ConfigParser()
with open("config.ini") as f:
    config.read_file(f)

OPENAI_API_BASE = config.get("aim", "url")
OPENAI_API_VERSION = config.get("aim", "api_version")
OPENAI_API_TYPE = config.get("aim", "type")
OPENAI_API_KEY = os.environ["AIM_API_KEY"]

print(OPENAI_API_BASE)
print(f"List of models: {config.get('aim', 'models')}")


# --- Initialise LLM ---

llm = AzureChatOpenAI(
    deployment_name="aim-gpt-4o-mini-lab",
    temperature=0.7,
    azure_endpoint=OPENAI_API_BASE,
    openai_api_key=OPENAI_API_KEY,
    openai_api_version=OPENAI_API_VERSION
)


# --- Build Prompt Chain ---

system_message = "You are an AI assistant that tells jokes."
system_message_prompt = SystemMessagePromptTemplate.from_template(system_message)

human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])


# --- Execute Chain ---

chain = chat_prompt | llm
result = chain.invoke(f"Tell me a joke about a basketball player")
print(result.content)
