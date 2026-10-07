# Memory Engineering

## Purpose
Designs memory architectures for Deep Agents by selecting appropriate memory types, defining retrieval strategies, establishing persistence mechanisms, and specifying governance rules. This skill ensures agents have the right memory capabilities to support their workflows without unnecessary complexity.

## Responsibilities
- Analyze workflow requirements to determine needed memory types
- Select appropriate memory strategies (working, conversation, semantic, long-term, checkpoint, artifact)
- Design retrieval patterns optimized for each memory type's access patterns
- Define persistence strategies (storage, durability, replication)
- Establish memory governance (retention, privacy, cleanup, capacity management)
- Specify memory interfaces for component integration
- Design checkpoint strategies for workflow recovery
- Prevent unnecessary memory additions that add complexity without business value

## Inputs
- Workflow specification (state management needs, long-running steps, recovery requirements)
- Architecture specification (data flow patterns, component interactions)
- Business requirements (persistence needs, learning capability, knowledge retrieval)
- Compliance requirements (data retention, privacy, right-to-deletion)
- Performance constraints (latency, throughput, storage limits)

## Outputs
- memory-strategy.md — complete memory architecture and strategy
- Memory type selections with justifications
- Retrieval pattern specifications (how memory is queried and used)
- Persistence configuration (storage backends, durability, replication)
- Governance rules (retention policies, privacy controls, cleanup procedures)

## Dependencies
- Engineering Engines: Memory Engineering Engine
- Knowledge Domains: knowledge/memory/, knowledge/persistence/, knowledge/retrieval/
- Templates: templates/memory/, templates/persistence/
- Upstream: Architecture Engineering (data flow), Workflow Engineering (state needs)
- Downstream: Implementation Generation, Deployment Engineering

## Integration
- DAEP Orchestration Layer (invoked during Phase 8 of generation pipeline)
- Memory Engineering Engine (primary engine)
- Knowledge Base (memory patterns, storage options)
- Template Engine (memory configuration generation)
- Workflow specification (drives checkpoint and state requirements)
- Component plan (memory interfaces for component integration)

## Usage
This skill activates during Phase 8 of the Deep Agent Generation pipeline, after workflow is designed and before prompts.

```
Workflow defined → memory-engineering skill activates
  → Analyzes workflow for memory requirements
  → Selects memory types with justification
  → Designs retrieval and persistence strategies
  → Establishes governance rules
  → Produces memory strategy
```

## Best Practices
- Only add memory types that serve a documented business requirement
- Select the simplest memory type that satisfies the requirement
- Design retrieval patterns before choosing storage implementations
- Define retention and cleanup policies from the start, not after deployment
- Consider memory interaction patterns (how different memory types compose)
- Document memory capacity limits and overflow strategies

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Triggers Hooks
- Produces deterministic outputs
