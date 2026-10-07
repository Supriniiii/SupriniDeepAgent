# Beginner Example

## Prompt
"Identify and define components for a simple FAQ chatbot with pipeline architecture (input handler → retrieval → response formatter → output handler)."

## Expected Behavior
The component-engineering skill:
1. Extracts required components from architecture: input handler, retrieval engine, response formatter, output handler
2. Searches registry for existing implementations of each
3. Finds existing retrieval component (vector-search-retriever v2.1) and response formatter (markdown-formatter v1.3)
4. Decides: reuse retrieval and formatter, build input handler and output handler
5. Defines new components with single responsibility
6. Specifies interfaces for all four components
7. Maps dependencies: linear pipeline, no circular dependencies

## Expected Output
- `component-plan.md` with 4 components: 2 reused, 2 new
- Interface definitions for InputHandler, Retriever, ResponseFormatter, OutputHandler
- Dependency map showing linear pipeline flow
- Specifications for new InputHandler and OutputHandler components
