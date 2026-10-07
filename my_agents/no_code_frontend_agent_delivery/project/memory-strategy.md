# Memory Strategy: No Code Frontend Agent

## Memory Types

### Working Memory
- Purpose: Current task context
- Lifecycle: Current execution
- Limit: 32KB

### Session Memory
- Purpose: Engineering session continuity
- Lifecycle: Session duration
- Retention: Until session end

### Long-Term Memory
- Purpose: Persistent knowledge and patterns
- Lifecycle: Persistent
- Storage: File-based

## Context Management

- Assembly: Priority-weighted
- Max size: 8000 tokens
- Compression: Summarization when exceeded

## Retrieval Strategy

- Method: Relevance-based
- Freshness: Recent items prioritized
- Fallback: Return empty context (never fail)

## Governance

- Access: Read/write per component
- Audit: Log all memory operations
- Privacy: No PII stored without consent
