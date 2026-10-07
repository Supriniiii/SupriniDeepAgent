# Architecture Engineering

## Purpose
Designs solution architectures for Deep Agents and multi-agent systems. This skill selects appropriate architectural patterns, justifies decisions against requirements, documents trade-offs, and produces comprehensive architecture artifacts that guide all downstream engineering activities.

## Responsibilities
- Analyze requirements to determine architectural needs and constraints
- Select appropriate architectural patterns (planner-executor, manager-worker, hierarchical, pipeline, swarm, event-driven)
- Justify architecture decisions against functional and non-functional requirements
- Document trade-offs, constraints, and rejected alternatives
- Produce Architecture Decision Records (ADRs) for significant decisions
- Generate architecture diagrams showing component relationships and data flows
- Define system boundaries, interfaces, and integration points
- Ensure architecture supports observability, security, and extensibility

## Inputs
- Confirmed requirements document (functional and non-functional requirements)
- Constraints (performance, scalability, compliance, budget, timeline)
- Existing system context (current architecture, integration targets)
- Available component catalog (reusable capabilities)
- Deployment environment specifications

## Outputs
- architecture.md — complete architecture specification
- Architecture Decision Records (ADRs) for each significant decision
- Architecture diagrams (component, sequence, deployment views)
- Interface definitions between major components
- Dependency map showing component relationships

## Dependencies
- Engineering Engines: Architecture Engineering Engine
- Knowledge Domains: knowledge/architectures/, knowledge/patterns/, knowledge/reference-architectures/
- Templates: templates/architecture/, templates/adrs/
- Upstream: Requirements Engineering (provides confirmed requirements)
- Downstream: Component Engineering, Workflow Engineering, Harness Selection

## Integration
- DAEP Orchestration Layer (invoked during Phase 3 of generation pipeline)
- Architecture Engineering Engine (primary engine)
- Knowledge Base (pattern retrieval, reference architectures)
- Template Engine (ADR and diagram generation)
- Component Registry (capability-aware architecture decisions)
- Validation Engine (architecture quality assessment)

## Usage
This skill activates during Phase 3 of the Deep Agent Generation pipeline, or independently when architecture design is needed for an existing system.

```
Requirements confirmed → architecture-engineering skill activates
  → Analyzes requirements for architectural drivers
  → Evaluates candidate patterns
  → Selects and justifies pattern
  → Generates architecture artifacts
  → Passes architecture to downstream skills
```

## Best Practices
- Always analyze architectural drivers (quality attributes) before selecting patterns
- Document why alternatives were rejected, not just what was chosen
- Design for extensibility — components should be replaceable without architectural changes
- Validate architecture against non-functional requirements before proceeding
- Keep architecture diagrams at appropriate abstraction levels for their audience
- Consider failure modes and recovery strategies as first-class architectural concerns

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Triggers Hooks
- Produces deterministic outputs
