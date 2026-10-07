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
