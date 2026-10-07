# Memory Engineering Standards

## 1. Business-Justified Memory
Every memory type selected must have a documented business justification. Memory adds operational complexity, storage costs, and governance overhead. The default decision is "no memory" — memory is only added when a specific requirement demands it. Unjustified memory types must be removed.

## 2. Access-Pattern-First Design
Memory type selection must be driven by the access pattern, not the storage technology. First define how memory will be queried (key-value, similarity search, time-series, graph traversal), then select storage that supports that pattern efficiently. Storage technology is an implementation detail.

## 3. Governed from Day One
Retention policies, cleanup schedules, privacy rules, and access controls must be defined during memory design — not deferred to operations. Memory without governance becomes a liability. Every memory type must have: defined retention period, cleanup mechanism, access scope, and deletion procedure.

## 4. Recovery-Ready Checkpoints
Any workflow step that takes longer than 60 seconds or involves external systems must have checkpoint support. Checkpoints must capture sufficient state for full recovery without re-execution of completed work. Recovery procedures must be defined and testable.

## 5. Bounded Capacity
All memory types must have defined capacity limits with explicit overflow behavior. Unbounded memory growth is prohibited. Overflow strategies include: eviction (LRU, LFU), summarization, archival, or graceful rejection. Monitoring must alert before capacity limits are reached.
