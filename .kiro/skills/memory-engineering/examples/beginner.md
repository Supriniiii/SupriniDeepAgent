# Beginner Example

## Prompt
"Design the memory strategy for a simple FAQ chatbot with stateless request-response interaction."

## Expected Behavior
The memory-engineering skill:
1. Analyzes workflow: linear pipeline, single request-response, no session continuity required
2. Identifies memory needs: potentially conversation memory for multi-turn, working memory for active processing
3. Assesses requirements: stateless design specified — no session persistence needed
4. Selects memory types: Working Memory only (holds current query and retrieved context during processing)
5. Determines: no conversation memory (stateless), no semantic memory (retriever handles this externally), no checkpoints (fast pipeline, no recovery needed)
6. Retrieval pattern: simple key-value lookup for current request state
7. Persistence: in-memory only, no durable storage needed
8. Governance: auto-cleanup after response delivered (no retention)

## Expected Output
- `memory-strategy.md` with minimal memory architecture:
  - Working Memory: active query context during processing (in-memory, no persistence)
  - No other memory types selected (justified: stateless design, fast pipeline)
- Retrieval: direct access to current request state
- Persistence: none (ephemeral, request-scoped)
- Governance: automatic cleanup after request completion
- Justification: business requirements specify stateless interaction, no learning or persistence needed
