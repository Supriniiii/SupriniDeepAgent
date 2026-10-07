# Engineering Standards Index

## Purpose

This index provides a high-level overview of the organization's approved technologies, implementation patterns, and reference examples.

Kiro should consult this index before generating implementation code to ensure generated solutions align with the organization's engineering standards.

---

# Approved AI Technologies

| Category | Approved Standard |
|-----------|-------------------|
| LLM Provider | Azure OpenAI |
| Chat Models | Azure OpenAI Chat Models |
| Embeddings | Azure OpenAI Embeddings |
| Agent Framework | LangChain |
| Prompt Framework | LangChain Prompt Templates |
| Vector Database | ChromaDB |
| Retrieval | Retrieval-Augmented Generation (RAG) |

---

# Approved Data Technologies

| Category | Approved Standard |
|-----------|-------------------|
| Enterprise Database | Teradata |
| Big Data Platform | Hive |
| SQL Access | SQLAlchemy |
| JDBC Access | JayDeBeAPI |
| Analytics | Pandas |
| Visualisation | Plotly |

---

# Authentication Standards

Use organization-approved authentication mechanisms.

Preferred approaches include:

- Azure Key Vault
- Environment Variables
- Configuration Files (`config.ini`)
- Secure Secret Management

Sensitive credentials must never be hardcoded.

---

# Configuration Standards

Configuration should be externalized.

Preferred mechanisms include:

- `config.ini`
- Environment Variables
- Secure Secret Stores

Configuration values should not be embedded directly in source code.

---

# Reference Implementations

The following directories contain approved implementation examples.

| Directory | Purpose |
|----------|---------|
| `ai/` | AI engineering reference implementations |
| `data/` | Enterprise data access examples |
| `examples/` | Complete end-to-end examples |

---

# Code Generation Guidelines

When generating implementation code, Kiro should:

- Prefer the approved technologies listed in this index.
- Follow the reference implementations in the corresponding directories.
- Reuse approved implementation patterns where appropriate.
- Avoid introducing alternative technologies unless explicitly requested.
- Generate secure, maintainable, and production-ready code.

---

# Maintenance

This index should be updated whenever new organizational standards, technologies, or approved implementation patterns are adopted.
