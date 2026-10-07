# Beginner Example

## Prompt
"Design the execution workflow for a simple FAQ chatbot with a linear pipeline: receive question → retrieve answer → format response → return."

## Expected Behavior
The workflow-engineering skill:
1. Identifies workflow scope: single request-response cycle, triggered by user message
2. Enumerates states: IDLE, RECEIVING, RETRIEVING, FORMATTING, RESPONDING, COMPLETE, ERROR
3. Defines transitions: linear progression with error transitions from each state
4. No decision points needed (linear pipeline)
5. Error handling: retrieval failure → fallback response; formatting failure → raw response
6. Timeouts: retrieval timeout (5s) → fallback response
7. Step contracts: question text in → retriever result → formatted response → output text

## Expected Output
- `workflow-specification.md` — linear pipeline workflow with 7 states
- State machine: IDLE → RECEIVING → RETRIEVING → FORMATTING → RESPONDING → COMPLETE
- Error paths: any state → ERROR (with specific fallback per step)
- Step contracts for all 4 processing steps
- Simple workflow diagram showing linear flow with error branches
