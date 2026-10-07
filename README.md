# Deep Agent Engineering Platform (DAEP)

Enterprise AI agent generation framework that transforms developer requests into production-ready Deep Agents through a deterministic engineering process.

## Quick Start

```bash
pip install -e ".[dev]"
pytest
```

## Usage

```python
from pathlib import Path
from daep.orchestration import GenerationOrchestrationEngine, GenerationRequest

request = GenerationRequest(
    name="Code Review Agent",
    description="An agent that reviews pull requests",
    specification=Path(".kiro"),
    output_directory=Path("outputs/code-review-agent"),
)

goe = GenerationOrchestrationEngine()
report = goe.generate(request)
print(report.summary())
```

## Architecture

```
src/daep/
├── orchestration/   ← Generation Orchestration Engine (GOE)
├── engines/         ← Engineering Engine implementations
├── runtime/         ← Agent harnesses
├── components/      ← Reusable runtime components
├── memory/          ← Memory management
├── tools/           ← Tool integration
├── generation/      ← Code/artifact generation
├── outputs/         ← Output packaging
├── validation/      ← Quality gates
├── integrations/    ← Azure OpenAI, ChromaDB, etc.
├── cli/             ← Developer CLI
└── shared/          ← Models and enums
```

## License

MIT


##VERSION 2##***
# Deep Agent Engineering Platform (DAEP)

An enterprise AI engineering platform that transforms natural-language requests into production-ready Deep Agents through a deterministic, engineering-first process.

Instead of generating code directly from a prompt, DAEP performs full engineering — requirements, architecture, components, workflows, prompts, memory, validation — and *then* produces a complete, runnable Python project you can take to your lab and run.

---

## Table of Contents

1. [What DAEP Does](#what-daep-does)
2. [Project Layout](#project-layout)
3. [Part A — Developer Guide (build and extend DAEP)](#part-a--developer-guide)
4. [Part B — User Guide (generate agents)](#part-b--user-guide)
5. [Part C — Running a Generated Agent in the Lab](#part-c--running-a-generated-agent-in-the-lab)
6. [Troubleshooting](#troubleshooting)
7. [Current Status and Roadmap](#current-status-and-roadmap)

---

## What DAEP Does

```
Natural language request
        │
        ▼
  Engineering Pipeline (GOE + 13 Engineering Engines)
        │
        ├── requirements.md
        ├── architecture.md / adr.md
        ├── component-plan.md
        ├── workflow-specification.md
        ├── prompt-package.md
        ├── memory-strategy.md
        ├── validation-report.md
        └── evaluation-report.md
        │
        ▼
  Code Generation (ProjectGenerator)
        │
        ▼
  Runnable Python project (LangChain + Azure OpenAI)
        │
        ▼
  Delivery package (engineering artifacts + project + manifest)
```

---

## Project Layout

```
deep-agent-engineering-platform/
├── .kiro/                      # The engineering framework (knowledge layer)
│   ├── steering/               # Global generation rules
│   ├── hooks/                  # 15 pipeline stage definitions
│   ├── engines/                # 10 engine specifications + contracts
│   ├── knowledge/              # 18 engineering knowledge domains
│   ├── templates/              # 170+ reusable blueprints
│   ├── standards/              # Your lab's approved code (Azure, Chroma, Teradata)
│   ├── skills/                 # 14 Kiro skill definitions
│   ├── specs/                  # 7 formal specifications
│   └── docs/                   # Architecture, developer, contribution guides
│
├── src/daep/                   # The runtime (execution layer)
│   ├── orchestration/          # GOE — coordinates the pipeline
│   ├── engines/                # 13 Engineering Engine implementations
│   ├── integrations/           # Azure OpenAI client + config loading
│   ├── generation/             # ProjectGenerator — renders Python code
│   ├── outputs/                # OutputPackager — bundles deliverables
│   ├── cli/                    # Developer CLI
│   └── shared/                 # Models and enums
│
├── tests/                      # 98 tests
├── configs/                    # Platform config (dev / prod / lab)
├── scripts/                    # Helper scripts
├── my_agents/                  # Generated agents land here
├── pyproject.toml
└── README.md                   # This file
```

---

## Part A — Developer Guide

For engineers building, extending, or maintaining DAEP itself.

### Step 1: Prerequisites

- Python 3.11 or newer
- pip (or `uv` if preferred)
- Git

Check your Python version:

```bash
python --version
```

### Step 2: Install DAEP in editable mode

From the project root:

```bash
pip install -e ".[dev]"
```

This installs DAEP plus development tools (pytest, ruff, mypy).

To also install the AI dependencies (LangChain, Azure OpenAI, ChromaDB):

```bash
pip install -e ".[ai,dev]"
```

### Step 3: Verify the installation

```bash
pytest
```

You should see **98 passing tests**. If pytest is not on your PATH:

```bash
python -m pytest
```

### Step 4: Explore the platform

```bash
python -m daep.cli.main status      # Show platform health
python -m daep.cli.main engines     # List Engineering Engines
python -m daep.cli.main version     # Show version
```

> Note: once installed, the `daep` command may be available directly. If your
> scripts directory is not on PATH, use `python -m daep.cli.main` instead.

### Step 5: Understand the two layers

| Layer | Location | Role |
|-------|----------|------|
| Knowledge | `.kiro/` | What DAEP knows (steering, knowledge, templates, standards) |
| Runtime | `src/daep/` | What DAEP does (orchestration, engines, generation) |

The runtime **reads** the knowledge layer. You rarely change the runtime to add engineering knowledge — you extend `.kiro/` instead.

### Step 6: Run the full suite with coverage

```bash
python -m pytest --cov=daep --cov-report=term-missing
```

### Step 7: Finish building the platform (remaining work)

DAEP's deterministic pipeline is complete. To make engines produce
AI-generated content instead of template content, implement these in order:

1. **Wire the LLM into engines**
   - Each engine in `src/daep/engines/` currently returns template content.
   - Inject `daep.integrations.get_llm_client()` and call `client.generate(...)`
     using the knowledge/standards already loaded into the context.

2. **Add retrieval (RAG) over the knowledge base**
   - Use ChromaDB (already in your standards) to embed `.kiro/knowledge/`.
   - Give engines a `retrieve(domain, query)` helper for relevant context.

3. **Enhance the ProjectGenerator**
   - Expand `src/daep/generation/renderer.py` to produce richer code using
     the engineering artifacts (not just the request).

4. **Add agent-type variants**
   - Extend `renderer.py` with `data` and `workflow` tool sets
     (coding and research already exist).

Each change is additive — the public interfaces (`GenerationRequest`,
`GenerationReport`, CLI commands) stay stable.

### Step 8: Development standards

- Follow PEP 8; run `ruff check src/`
- Type-check with `mypy src/daep`
- Every new module needs tests in `tests/`
- Reuse `.kiro/standards/` reference implementations for AI and data code
- Never hardcode secrets — use `config.ini` or environment variables

---

## Part B — User Guide

For developers using DAEP to generate agents.

### Step 1: Install (if not already done)

```bash
pip install -e ".[ai]"
```

### Step 2: Generate an agent

```bash
python -m daep.cli.main generate "Code Review Agent" --type coding --output ./my_agents
```

Options:

| Flag | Default | Description |
|------|---------|-------------|
| `--type` / `-t` | `coding` | Agent type: `coding`, `research`, `data`, `workflow` |
| `--arch` / `-a` | `planner-executor` | Architecture pattern |
| `--output` / `-o` | `outputs` | Where to write the project |
| `--workspace` / `-w` | `.kiro` | Path to the DAEP framework |

### Step 3: Review what was generated

```
my_agents/code_review_agent/
├── src/code_review_agent/
│   ├── agent.py        # Main agent (LangChain + Azure OpenAI)
│   ├── prompts.py      # Loads externalized prompts
│   ├── tools.py        # Domain tools (file read/write for coding)
│   ├── memory.py       # Session memory
│   └── config.py       # Config loading
├── prompts/
│   ├── system.md
│   ├── planning.md
│   └── execution.md
├── tests/
├── config.ini          # Fill in your Azure endpoint
├── pyproject.toml
└── README.md
```

### Step 4: Example requests

```bash
# A coding agent
python -m daep.cli.main generate "Bug Fix Agent" --type coding

# A research agent (adds search + synthesis tools)
python -m daep.cli.main generate "Market Research Assistant" --type research

# A data agent
python -m daep.cli.main generate "Data Quality Agent" --type data

# A workflow agent
python -m daep.cli.main generate "Onboarding Workflow Agent" --type workflow
```

### Step 5: Generate via a script (alternative)

See `scripts/generate_agent.py` for a programmatic example that also
packages a delivery bundle (engineering artifacts + project + manifest).

```bash
python scripts/generate_agent.py
```

### Step 6: Understand the delivery package

When you generate via the packager (as the scripts do), you also get a
self-contained delivery bundle alongside the project:

```
my_agents/<agent>_delivery/
├── manifest.json       # Inventory + validation status
├── project/            # The runnable agent project
└── engineering/        # Engineering artifacts for review
```

`manifest.json` records the agent name, version, type, architecture, every
file produced, and whether validation passed. Hand this bundle to reviewers
or deploy it as a unit.

---

## Part C — Running a Generated Agent in the Lab

Once you take the generated project to your lab environment:

### Step 1: Enter the project

```bash
cd my_agents/code_review_agent
```

### Step 2: Install it

```bash
pip install -e .
```

### Step 3: Configure Azure OpenAI

Edit `config.ini` with your lab endpoint:

```ini
[aim]
url = https://your-endpoint.openai.azure.com/
api_version = 2024-06-01
type = azure
models = aim-gpt-4o-mini-lab
```

Set your API key (never hardcode it):

```bash
# Linux/Mac
export AIM_API_KEY=your-key-here

# Windows PowerShell
$env:AIM_API_KEY="your-key-here"
```

### Step 4: Run the tests

```bash
pip install -e ".[dev]"
pytest
```

### Step 5: Run the agent

```python
from code_review_agent.agent import CodeReviewAgent

agent = CodeReviewAgent()
result = agent.run("Review this function for security issues: ...")
print(result)
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `No module named pytest` | `pip install pytest` or `pip install -e ".[dev]"` |
| `No module named yaml` | `pip install pyyaml` |
| `requires a different Python` | Install Python 3.11+ |
| `No API key configured` | Set `AIM_API_KEY` environment variable |
| `daep: command not found` | Use `python -m daep.cli.main` instead |
| Generated agent import errors | Run `pip install -e .` inside the generated project |
| LLM call fails | Verify `config.ini` endpoint and `AIM_API_KEY` are correct |

---

## Current Status and Roadmap

**Complete (v0.1):**

- ✅ Generation Orchestration Engine (GOE)
- ✅ 13 Engineering Engines + registry
- ✅ Azure OpenAI integration (config.ini + .env + env vars)
- ✅ Project generator (produces runnable Python projects)
- ✅ Output packager (delivery bundles with manifest)
- ✅ Developer CLI
- ✅ 98 passing tests

**Next (v0.2+):**

- ⬜ AI-assisted engines (LLM-generated artifacts, not templates)
- ⬜ RAG over the knowledge base (ChromaDB)
- ⬜ Richer code generation from engineering artifacts
- ⬜ Reflection and self-healing loops
- ⬜ Multi-agent generation
- ⬜ Data and workflow tool sets in the generator

---

## License

MIT

## Generated Agents

Generated agents are the property of the developer who creates them.
Each generated project is self-contained and independently licensed.

