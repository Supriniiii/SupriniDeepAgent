# Memory Engineering

## Skill Definition

```yaml
name: memory-engineering
description: Designs memory architecture by selecting memory types, defining retrieval patterns, persistence strategies, and governance rules
version: 1.0.0
category: engineering
trigger: Workflow is designed and memory requirements need to be determined for agent state management, learning, and retrieval
```

## Required Inputs
- Workflow Specification: Workflow states, long-running operations, and recovery needs
- Architecture Specification: Data flows, component interactions, agent communication patterns
- Business Requirements: Persistence needs, learning requirements, knowledge retrieval expectations

## Optional Inputs
- Compliance Requirements: Data retention policies, privacy regulations, deletion requirements
- Performance Constraints: Latency targets, throughput requirements, storage budgets
- Existing Storage Infrastructure: Available databases, vector stores, caches
- Data Classification: Sensitivity levels affecting storage and access decisions
- Scaling Requirements: Growth projections, multi-tenancy needs

## Workflow

### Step 1: Memory Needs Assessment
Analyze workflow and architecture to identify where memory is required.
- Engine: Memory Engineering Engine
- Knowledge: knowledge/memory/assessment/
- Output: Memory needs inventory — where and why memory is required

### Step 2: Memory Type Selection
For each identified need, select the appropriate memory type.
- Engine: Memory Engineering Engine
- Knowledge: knowledge/memory/types/
- Output: Memory type selections with justifications:
  - Working Memory: active computation state, current plan
  - Conversation Memory: multi-turn dialogue context
  - Semantic Memory: knowledge retrieval (vector-based)
  - Long-Term Memory: learned patterns, accumulated knowledge
  - Checkpoint Memory: workflow recovery state
  - Artifact Memory: generated outputs, intermediate results

### Step 3: Retrieval Pattern Design
Design how each memory type is queried, filtered, and returned.
- Engine: Memory Engineering Engine
- Knowledge: knowledge/memory/retrieval/, knowledge/retrieval/
- Output: Retrieval specifications (query patterns, relevance scoring, filtering)

### Step 4: Persistence Strategy
Define storage backends, durability requirements, and replication approach.
- Engine: Memory Engineering Engine
- Knowledge: knowledge/memory/persistence/, knowledge/persistence/
- Output: Persistence configuration (backend selection, durability level, replication)

### Step 5: Capacity and Performance Design
Define capacity limits, eviction policies, and performance budgets.
- Engine: Memory Engineering Engine
- Knowledge: knowledge/memory/performance/
- Output: Capacity limits, eviction strategies, latency budgets per memory type

### Step 6: Memory Interaction Design
Define how different memory types interact and compose.
- Engine: Memory Engineering Engine
- Knowledge: knowledge/memory/interactions/
- Output: Memory interaction map (how memories feed into each other)

### Step 7: Governance Rules Definition
Establish retention, privacy, cleanup, audit, and access control policies.
- Engine: Memory Engineering Engine
- Knowledge: knowledge/memory/governance/, knowledge/compliance/
- Output: Governance specification (retention, privacy, cleanup schedules, access rules)

### Step 8: Checkpoint Strategy
Design checkpoint mechanisms for workflow recovery and state persistence.
- Engine: Memory Engineering Engine
- Knowledge: knowledge/memory/checkpoints/
- Output: Checkpoint specification (what, when, where, recovery procedure)

### Step 9: Memory Strategy Assembly
Assemble all elements into the complete memory strategy.
- Engine: Memory Engineering Engine
- Knowledge: knowledge/memory/assembly/
- Output: memory-strategy.md — complete memory architecture

### Step 10: Memory Validation
Validate memory strategy against requirements, performance, and governance.
- Engine: Memory Engineering Engine, Validation Engine
- Knowledge: knowledge/validation/memory/
- Output: Memory validation report

## Engineering Rules
- Never add memory types without a documented business justification
- Memory type selection must match the access pattern (not the storage technology)
- Retrieval patterns must be defined before storage backend selection
- Governance rules (retention, cleanup) must be defined at design time, not deferred
- Checkpoint strategy is mandatory for any workflow with steps exceeding 60 seconds
- Memory capacity limits must be explicit with defined overflow behavior

## Knowledge Sources
- knowledge/memory/types/ — memory type catalog and selection criteria
- knowledge/memory/retrieval/ — retrieval patterns and query strategies
- knowledge/memory/persistence/ — storage backend options and trade-offs
- knowledge/memory/governance/ — retention, privacy, and lifecycle policies
- knowledge/memory/checkpoints/ — checkpoint patterns for workflow recovery
- knowledge/memory/performance/ — capacity planning and performance optimization
- knowledge/persistence/ — cross-cutting persistence patterns

## Templates Used
- templates/memory/strategy.md — memory strategy document template
- templates/memory/type-config.md — per-type configuration template
- templates/memory/retrieval.md — retrieval pattern specification template
- templates/memory/governance.md — governance rules template
- templates/memory/checkpoint.md — checkpoint strategy template

## Engineering Engines Invoked
- Memory Engineering Engine (primary)
- Validation Engine (memory strategy validation)

## Hooks Invoked
- pre-memory-design — fires before memory analysis begins
- post-type-selection — fires after memory types selected
- post-memory-design — fires after complete strategy assembled

## Validation
- Every selected memory type has a documented business justification
- Memory type matches access pattern (not over-engineered)
- Retrieval patterns are defined with performance expectations
- Persistence strategy addresses durability and availability requirements
- Governance rules cover retention, privacy, cleanup, and access control
- Checkpoint strategy covers all long-running workflow operations
- Capacity limits are defined with overflow behavior
- Memory interactions are documented and do not create circular dependencies
- Compliance requirements (if any) are fully addressed

## Expected Outputs
- memory-strategy.md — complete memory architecture and configuration
- Memory type selections — each type with justification and access patterns
- Retrieval specifications — query patterns, relevance scoring, filtering rules
- Persistence configuration — storage backends, durability settings, replication
- Governance rules — retention policies, cleanup schedules, access controls
- Checkpoint strategy — recovery mechanisms for long-running workflows
- Memory validation report — confirmation of correctness and completeness

## Completion Criteria
- All memory needs identified from workflow and architecture analysis
- Memory types selected with business justification (no unnecessary memory)
- Retrieval patterns defined for all memory types
- Persistence strategy addresses durability and performance requirements
- Governance rules established (retention, privacy, cleanup)
- Checkpoint strategy defined for long-running workflow recovery
- Memory strategy validated against requirements and compliance
- Downstream implementation has unambiguous memory specifications
