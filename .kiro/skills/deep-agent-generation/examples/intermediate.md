# Intermediate Example

## Prompt
"Generate a research agent that can search multiple knowledge sources, synthesize findings, and produce structured research reports. It should support iterative refinement based on user feedback and remember previous research sessions."

## Expected Behavior
The deep-agent-generation skill activates the full pipeline with increased complexity:
1. Captures intent: multi-source research agent with memory and iterative refinement
2. Extracts requirements: multiple data sources, synthesis capability, structured output, feedback loops, session persistence
3. Selects architecture: planner-executor with reflection loop (research requires planning, execution, and quality reflection)
4. Discovers capabilities: searches for existing search connectors, document parsers, synthesis components
5. Selects components: search adapters (web, internal docs, APIs), document parser, synthesis engine, report formatter, feedback processor
6. Selects harness: stateful agent harness with checkpointing and recovery
7. Designs workflow: plan research → execute searches → parse results → synthesize → reflect on quality → refine if needed → format report → present → accept feedback → iterate
8. Memory strategy: working memory (current research plan), conversation memory (user feedback), semantic memory (knowledge retrieval), checkpoint memory (session persistence)
9. Prompt strategy: planning prompt, search query generation prompt, synthesis prompt, reflection prompt, refinement prompt
10. Generates full implementation with multi-component architecture
11. Validates with comprehensive test coverage including prompt evaluation

## Expected Output
- `/agents/research-agent/` — complete multi-component agent
- `/agents/research-agent/architecture.md` — planner-executor architecture with reflection
- `/agents/research-agent/components/` — search adapters, parser, synthesizer, formatter
- `/agents/research-agent/workflows/` — state machine with feedback loops
- `/agents/research-agent/memory/` — memory configuration (4 memory types)
- `/agents/research-agent/prompts/` — 5 specialized prompts with versions
- `/agents/research-agent/tests/` — unit, integration, workflow, and prompt eval tests
- `/agents/research-agent/deploy/` — containerized deployment with persistence
- `/agents/research-agent/docs/` — complete documentation package
- `validation-report.md` — quality score ≥87%, production-ready: YES
