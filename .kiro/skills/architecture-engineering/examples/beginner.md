# Beginner Example

## Prompt
"Design the architecture for a simple FAQ chatbot that answers questions from a knowledge base."

## Expected Behavior
The architecture-engineering skill:
1. Identifies architectural drivers: simplicity, response quality, low latency
2. Evaluates patterns: pipeline (receive → retrieve → respond) vs planner-executor (overhead not justified)
3. Selects pipeline pattern — minimal complexity, clear data flow, sufficient for single-purpose retrieval
4. Specifies architecture: input handler → retrieval component → response formatter → output handler
5. Generates ADR documenting why pipeline was chosen over more complex patterns
6. Produces component diagram showing linear flow

## Expected Output
- `architecture.md` — pipeline architecture specification with 4 components
- `adrs/001-pipeline-pattern.md` — justification for pipeline over planner-executor
- `diagrams/component-diagram.md` — linear pipeline visualization
- `interfaces/` — interface definitions between pipeline stages
