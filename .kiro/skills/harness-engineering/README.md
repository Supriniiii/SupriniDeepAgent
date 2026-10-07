# Harness Engineering

## Purpose
Designs and generates runtime environments (Agent Harnesses) that provide execution infrastructure for Deep Agents. Ensures every agent has a well-defined lifecycle, state management, checkpointing, and recovery model before business logic is implemented.

## Responsibilities
- Analyze agent architecture to determine runtime requirements
- Select appropriate harness type based on execution model
- Define agent lifecycle management (start, pause, resume, stop)
- Design state management strategy
- Define checkpointing and recovery mechanisms
- Generate harness specification documents
- Validate harness compatibility with target architecture

## Inputs
- Agent architecture specification
- Business requirements and constraints
- Execution model preferences (sync, async, event-driven)
- Non-functional requirements (availability, durability)

## Outputs
- harness-specification.md
- runtime-architecture.md
- execution-model.md
- lifecycle-model.md

## Dependencies
- Harness Engineering Engine
- Knowledge Base (harnesses/, workflows/, observability/)
- Harness Templates
- Architecture Decision Records

## Integration
- Generation Orchestration Engine
- Harness Engineering Engine
- Validation Engineering Engine
- Observability Engine

## Usage
Invoke this skill when a new Deep Agent requires a runtime harness, when an existing harness needs modification, or when execution infrastructure must be designed before implementation begins.

## Best Practices
- Always design the harness before business logic implementation
- Select the simplest harness that satisfies requirements
- Ensure checkpointing granularity matches workflow complexity
- Design for graceful degradation and recovery
- Document all lifecycle transitions and state invariants

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Produces deterministic outputs
