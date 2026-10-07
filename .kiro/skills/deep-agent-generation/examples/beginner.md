# Beginner Example

## Prompt
"Generate a simple code review agent that can review Python files and provide feedback on code quality."

## Expected Behavior
The deep-agent-generation skill activates and orchestrates the full pipeline:
1. Captures intent: a single-purpose code review agent for Python
2. Extracts requirements: input is Python files, output is quality feedback
3. Selects architecture: simple planner-executor pattern (lightweight for single-purpose agent)
4. Discovers capabilities: checks for existing linting components, AST parsers
5. Selects components: Python AST parser, rule engine, feedback formatter
6. Selects harness: lightweight single-agent harness with synchronous execution
7. Designs workflow: receive file → parse → analyze → generate feedback → return
8. Memory strategy: working memory only (no persistence needed for stateless reviews)
9. Prompt strategy: system prompt with review guidelines, output format specification
10. Generates implementation, tests, docs, and deployment artifacts
11. Validates and produces final package

## Expected Output
- `/agents/code-review-agent/` — complete agent implementation
- `/agents/code-review-agent/architecture.md` — architecture documentation
- `/agents/code-review-agent/prompts/` — system and analysis prompts
- `/agents/code-review-agent/tests/` — unit and integration tests
- `/agents/code-review-agent/deploy/` — Dockerfile and deployment config
- `/agents/code-review-agent/docs/` — README, usage guide
- `validation-report.md` — quality score ≥87%, production-ready: YES
