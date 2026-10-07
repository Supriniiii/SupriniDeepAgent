# Beginner Example

## Prompt
"Design the prompts for a simple FAQ chatbot that retrieves answers from a knowledge base and responds conversationally."

## Expected Behavior
The prompt-engineering skill:
1. Identifies prompt needs: system prompt (defines chatbot identity) + execution prompt (guides answer generation from retrieved context)
2. Designs hierarchy: system prompt → execution prompt (simple, no planning/reflection needed)
3. Creates system prompt: friendly assistant role, knowledge-base grounded, no hallucination constraints
4. Creates execution prompt: takes user question + retrieved context, generates conversational answer
5. Defines output format: plain text response, optional confidence indicator
6. Context assembly: user question + top-3 retrieved passages (fits within any model's limits)
7. Model routing: single model, no routing needed
8. Evaluation: answer relevance score, hallucination check, tone consistency

## Expected Output
- `prompt-package.md` with 2 prompts:
  - System prompt: chatbot identity, behavioral constraints
  - Execution prompt: answer generation from retrieved context
- Output format: plain text with optional metadata
- Context assembly: simple (question + retrieved passages)
- Evaluation criteria: relevance, groundedness, tone
