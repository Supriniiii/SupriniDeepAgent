# Beginner Example

## Prompt
"Design a simple harness for a single-step code review agent that reviews pull requests."

## Expected Behavior
The skill analyzes the simple single-step architecture, determines a basic loop harness is sufficient, defines a minimal lifecycle (init → execute → complete), and produces a lightweight harness specification with simple state management and no checkpointing required.

## Expected Output
- harness-specification.md with a loop-based execution model
- runtime-architecture.md describing single-step execution
- execution-model.md with synchronous request-response pattern
- lifecycle-model.md with init, execute, and complete states
