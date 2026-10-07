# Intermediate Example

## Prompt
"Design the architecture for a data analysis agent that can query multiple databases, perform transformations, generate visualizations, and explain findings in natural language."

## Expected Behavior
The architecture-engineering skill:
1. Identifies architectural drivers: extensibility (multiple data sources), reliability (query error handling), output quality (accurate analysis), performance (large dataset handling)
2. Evaluates patterns: planner-executor (planning needed for multi-step analysis), pipeline (too rigid for variable analysis paths), manager-worker (workers for parallel queries)
3. Selects planner-executor with worker delegation — planner creates analysis plans, executor coordinates workers for parallel queries and transformations
4. Specifies architecture: planner (creates analysis strategy), executor (orchestrates steps), data workers (query, transform), visualization engine, narrative generator
5. Generates ADRs: pattern selection, parallel query strategy, visualization approach
6. Produces component diagram, sequence diagram for analysis workflow, deployment view

## Expected Output
- `architecture.md` — planner-executor architecture with worker pool for data operations
- `adrs/001-planner-executor-pattern.md` — why planner-executor suits multi-step analysis
- `adrs/002-parallel-query-strategy.md` — approach to concurrent database access
- `adrs/003-visualization-engine.md` — selection rationale for visualization component
- `diagrams/component-diagram.md` — planner, executor, workers, engines
- `diagrams/sequence-analysis-flow.md` — plan → query → transform → visualize → narrate
- `interfaces/` — contracts between planner, executor, workers, and output engines
