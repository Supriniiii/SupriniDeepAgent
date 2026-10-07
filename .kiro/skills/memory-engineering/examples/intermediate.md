# Intermediate Example

## Prompt
"Design the memory strategy for a research agent that conducts iterative research sessions, remembers past research topics, retrieves relevant background knowledge, and supports session recovery if interrupted."

## Expected Behavior
The memory-engineering skill:
1. Analyzes workflow: multi-step iterative research, reflection loops, user feedback, session continuity
2. Identifies memory needs: active research state, session continuity, background knowledge retrieval, session recovery
3. Selects memory types:
   - Working Memory: current research plan, active hypotheses, accumulated findings (during session)
   - Conversation Memory: user interactions, feedback, refinement requests (within session)
   - Semantic Memory: background knowledge, past research findings (vector-based retrieval)
   - Checkpoint Memory: session state for recovery (after each major step)
4. Designs retrieval patterns:
   - Working Memory: direct access by key (plan, findings, hypotheses)
   - Conversation Memory: sliding window (last N interactions) + full session retrieval
   - Semantic Memory: vector similarity search with topic filtering
   - Checkpoint Memory: latest checkpoint retrieval for recovery
5. Persistence strategy:
   - Working/Conversation: session-scoped storage (Redis)
   - Semantic: vector database (persistent, grows over time)
   - Checkpoint: durable storage (database with TTL)
6. Governance:
   - Working/Conversation: deleted after session closes (24h TTL for abandoned sessions)
   - Semantic: retained indefinitely with periodic relevance decay
   - Checkpoint: retained for 7 days after session completion
7. Memory interactions: semantic memory feeds into working memory context; checkpoint captures working + conversation state

## Expected Output
- `memory-strategy.md` with 4 memory types:
  - Working Memory: current research state (Redis, session-scoped)
  - Conversation Memory: user dialogue (Redis, sliding window + full)
  - Semantic Memory: knowledge base (vector DB, persistent, similarity retrieval)
  - Checkpoint Memory: session recovery (database, 7-day TTL)
- Retrieval specs: key-value, sliding window, vector similarity, latest checkpoint
- Persistence: Redis (ephemeral), vector DB (durable), database (TTL-managed)
- Governance: session cleanup, 24h abandoned TTL, 7-day checkpoint retention
- Memory interaction map: semantic → working, checkpoint captures working + conversation
