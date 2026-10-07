# Workflow Engineering

## Purpose
Designs execution workflows for Deep Agents and multi-agent systems. This skill defines states, transitions, decision points, error handling paths, and recovery strategies that govern how agents execute their capabilities from start to completion.

## Responsibilities
- Design execution workflows with clear states and transitions
- Define decision points, branching logic, and conditional paths
- Specify error handling, retry strategies, and recovery mechanisms
- Design timeout handling and fallback behaviors
- Model workflows as state machines with well-defined terminal states
- Ensure workflows support observability (state tracking, step timing, audit trails)
- Define input/output contracts between workflow steps
- Coordinate parallel execution paths where applicable

## Inputs
- Architecture specification (execution flow, component interactions)
- Component plan (available components and their interfaces)
- Requirements (business rules, error handling expectations, SLAs)
- Memory strategy (checkpointing requirements for workflow state)
- Constraints (timeout limits, retry budgets, concurrency limits)

## Outputs
- workflow-specification.md — complete workflow definition with states and transitions
- State machine definitions (formal state/transition models)
- Error handling specifications (retry, fallback, escalation paths)
- Workflow diagrams (flow charts, state diagrams)
- Step contracts (input/output definitions for each workflow step)

## Dependencies
- Engineering Engines: Workflow Engineering Engine
- Knowledge Domains: knowledge/workflows/, knowledge/state-machines/, knowledge/error-handling/
- Templates: templates/workflow/, templates/state-machine/
- Upstream: Architecture Engineering (flow design), Component Engineering (step implementations)
- Downstream: Implementation Generation, Memory Engineering (checkpointing)

## Integration
- DAEP Orchestration Layer (invoked during Phase 7 of generation pipeline)
- Workflow Engineering Engine (primary engine)
- Knowledge Base (workflow patterns, state machine references)
- Template Engine (workflow specification generation)
- Component plan (workflow steps map to components)
- Memory strategy (checkpoint integration for long-running workflows)

## Usage
This skill activates during Phase 7 of the Deep Agent Generation pipeline, after architecture and components are defined.

```
Architecture + Components defined → workflow-engineering skill activates
  → Identifies workflow requirements from architecture
  → Designs state machine with transitions
  → Defines error handling and recovery paths
  → Specifies step contracts
  → Produces workflow specification
```

## Best Practices
- Model every workflow as an explicit state machine with defined start and end states
- Design for failure — every step needs error handling, not just the happy path
- Include timeout handling for every external interaction or long-running operation
- Make workflows idempotent where possible to support safe retry
- Keep individual workflow steps small and focused on a single operation
- Design checkpoint strategies for long-running workflows to support recovery

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Triggers Hooks
- Produces deterministic outputs
