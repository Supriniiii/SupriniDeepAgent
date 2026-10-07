# Intermediate Example

## Prompt
"Design a harness for a multi-step research agent that gathers information from multiple sources, synthesizes findings, and produces a report. The agent should be able to resume if interrupted."

## Expected Behavior
The skill analyzes the multi-step pipeline architecture, selects a pipeline harness with checkpointing, defines lifecycle states including pause and resume capabilities, designs state management for intermediate results, and configures step-level checkpointing for recoverability.

## Expected Output
- harness-specification.md with pipeline execution model and checkpoint configuration
- runtime-architecture.md describing multi-step execution with intermediate state storage
- execution-model.md with async pipeline pattern and step transitions
- lifecycle-model.md with init, execute, pause, resume, checkpoint, and complete states
