# AI Engineering Standards

## Purpose

This directory contains approved reference implementations for AI-related technologies used within the organization.

Kiro should consult these implementations when generating AI-powered solutions to ensure alignment with the organization's preferred tools, libraries, and engineering patterns.

---

# Approved Technologies

- Azure OpenAI (Chat Models, Embeddings)
- LangChain (Agents, Chains, Prompt Templates)
- ChromaDB (Vector Storage, Similarity Search)
- Retrieval-Augmented Generation (RAG)

---

# Contents

| File | Description |
|------|-------------|
| azure-openai-chat.py | Approved pattern for Azure OpenAI chat completion |
| chromadb-embeddings.py | Approved pattern for ChromaDB embedding storage and retrieval |
| rag-basic.py | Approved pattern for basic RAG implementation |
| langchain-prompts.py | Approved pattern for LangChain prompt templates |

---

# Engineering Principles

- Use Azure OpenAI as the default LLM provider.
- Authenticate using Azure Key Vault or environment variables.
- Never hardcode API keys or endpoints.
- Use LangChain for agent orchestration.
- Use ChromaDB for vector storage.
- Follow modular design for prompt construction.
- Include error handling and retry logic.
- Log AI interactions for observability.

---

# Usage

When generating AI implementations, Kiro should reference these files as the approved implementation standard and adapt them to the specific engineering requirements.
