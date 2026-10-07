# Advanced Example

## Prompt
"Design the memory strategy for an enterprise incident response multi-agent system. Requires: active incident state across 4 agents, historical incident patterns for learning, evidence preservation for audit, communication history for stakeholders, checkpoint-based recovery for long-running incidents, and SOC2-compliant data governance."

## Expected Behavior
The memory-engineering skill:
1. Analyzes workflow: long-running (hours/days), multi-agent, concurrent incidents, regulatory compliance
2. Identifies memory needs: active incident state, inter-agent coordination, pattern learning, audit trail, stakeholder communication, fault tolerance
3. Selects memory types:
   - Working Memory: active incident state per agent (current investigation, pending actions)
   - Conversation Memory: stakeholder communications and inter-agent messages
   - Semantic Memory: historical incident patterns, resolution playbooks (for similar-incident matching)
   - Long-Term Memory: learned patterns, effectiveness metrics, organizational knowledge
   - Checkpoint Memory: incident state snapshots for recovery (critical for long-running incidents)
   - Artifact Memory: evidence, logs, remediation scripts, post-mortems (audit-grade preservation)
4. Designs retrieval patterns:
   - Working Memory: key-value with agent-scoped namespacing (per-incident, per-agent)
   - Conversation Memory: chronological retrieval with stakeholder filtering
   - Semantic Memory: similarity search (symptom matching to historical incidents)
   - Long-Term Memory: pattern matching with time-weighted scoring
   - Checkpoint Memory: latest + point-in-time retrieval for replay
   - Artifact Memory: indexed retrieval by incident, type, timestamp with chain-of-custody
5. Persistence strategy:
   - Working Memory: distributed cache (Redis Cluster) with replication
   - Conversation: append-only log (event store) with stakeholder indexing
   - Semantic: vector database with metadata filtering (Pinecone/Weaviate)
   - Long-Term: knowledge graph with temporal edges
   - Checkpoint: durable event-sourced store with point-in-time recovery
   - Artifact: immutable object store (S3) with cryptographic integrity verification
6. Governance (SOC2 compliant):
   - Retention: incidents retained for 7 years (compliance), working memory cleaned after resolution
   - Privacy: PII redaction in semantic/long-term stores, full PII in artifact store (access-controlled)
   - Access control: role-based per memory type, agent-scoped for working memory
   - Audit: all memory operations logged with timestamps, actor, and action
   - Deletion: soft-delete with legal hold support, hard-delete after retention period
   - Encryption: at-rest and in-transit for all memory types
7. Memory interactions:
   - Working → Checkpoint (periodic snapshots)
   - Artifact ← Working + Conversation (evidence collection)
   - Semantic ← Long-Term (pattern indexing)
   - Long-Term ← Artifact (post-incident learning)
8. Capacity planning: per-incident memory budget, concurrent incident limit, auto-scaling triggers

## Expected Output
- `memory-strategy.md` — enterprise memory architecture with 6 memory types:
  - Working Memory: per-agent per-incident state (Redis Cluster, replicated)
  - Conversation Memory: stakeholder + inter-agent communication (event store)
  - Semantic Memory: historical incident patterns (vector DB, similarity retrieval)
  - Long-Term Memory: organizational learning (knowledge graph, pattern matching)
  - Checkpoint Memory: incident state recovery (event-sourced, point-in-time)
  - Artifact Memory: audit evidence (S3, immutable, integrity-verified)
- Retrieval specifications for all 6 types with performance budgets
- Persistence: 5 different backends optimized per access pattern
- Governance: SOC2-compliant policies (7-year retention, encryption, RBAC, audit, legal hold)
- Memory interaction map showing cross-type data flows and lifecycle
- Capacity plan: per-incident budgets, scaling triggers, overflow strategies
- Recovery procedures: checkpoint-based incident state recovery
- Compliance documentation: SOC2 control mapping to memory governance rules
