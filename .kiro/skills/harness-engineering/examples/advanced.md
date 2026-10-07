# Advanced Example

## Prompt
"Design a harness for a distributed multi-agent system that coordinates planning, execution, and review agents with event-driven communication, durable state, automatic recovery from partial failures, and horizontal scaling support."

## Expected Behavior
The skill analyzes the distributed multi-agent architecture, selects an event-driven distributed harness, designs lifecycle management for each agent role, implements durable state with event sourcing, configures fine-grained checkpointing with saga-pattern recovery, and defines scaling policies based on workload.

## Expected Output
- harness-specification.md with distributed event-driven model, saga recovery, and scaling policies
- runtime-architecture.md describing event bus, agent coordination, and state distribution
- execution-model.md with event-driven async patterns, message routing, and back-pressure handling
- lifecycle-model.md with full state machines for each agent role including failure, recovery, and scale-out states
