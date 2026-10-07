# Intermediate Example

## Prompt
"Design the execution workflow for a research agent that plans research, executes searches in parallel, synthesizes results, reflects on quality, and iterates if quality is insufficient."

## Expected Behavior
The workflow-engineering skill:
1. Identifies workflow scope: multi-step with reflection loop, triggered by research request
2. Enumerates states: IDLE, PLANNING, SEARCHING (parallel), SYNTHESIZING, REFLECTING, REFINING, PRESENTING, AWAITING_FEEDBACK, ITERATING, COMPLETE, FAILED
3. Defines transitions: plan → fork to parallel search → join → synthesize → reflect → (decision: quality sufficient?) → present or refine
4. Decision points: quality threshold check after reflection, max-iteration guard
5. Error handling: search failure (partial results acceptable if ≥50% succeed), synthesis failure (retry with reduced scope), reflection timeout (proceed with current quality)
6. Timeouts: search timeout (30s per source), synthesis timeout (60s), total workflow timeout (5 min)
7. Parallel paths: multiple search operations execute concurrently with join barrier
8. Step contracts: research plan → search queries → search results → synthesis → quality score → final report
9. Checkpoint strategy: after planning, after searches complete, after each synthesis attempt

## Expected Output
- `workflow-specification.md` — iterative workflow with reflection loop and parallel execution
- State machine with 11 states, including reflection decision branch
- Parallel execution specification: fork to N search workers, join with partial-success tolerance
- Error handling: graceful degradation (proceed with partial results)
- Checkpoint strategy: 3 checkpoint points for recovery
- Decision point: quality threshold (configurable, default 0.8)
- Maximum iteration guard (3 refinement cycles)
- Step contracts for all steps with type definitions
- Workflow diagram showing parallel paths and reflection loop
