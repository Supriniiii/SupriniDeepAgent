# Prompt Engineering Standards

## 1. Complete Prompt Specification
Every prompt must document: purpose, version, inputs (with types), expected outputs (with format), constraints, few-shot examples, and evaluation criteria. Incomplete prompt specifications are not permitted to proceed to implementation.

## 2. External and Versioned
All prompts must be externalized from implementation code and managed as versioned artifacts. Prompt changes must be tracked with semantic versioning. Inline prompts exceeding 100 tokens are prohibited in source code.

## 3. Model-Aware Design
Prompts must be designed with awareness of the target model's capabilities, context window, and limitations. Context assembly must never exceed model token limits. Prompts should include explicit handling for context overflow (summarization, priority-based truncation).

## 4. Evaluatable by Design
Every prompt must have defined evaluation criteria before it is deployed. Evaluation must include: accuracy/relevance metrics, structured output compliance, constraint adherence, and edge case handling. Prompts without evaluation criteria cannot pass validation.

## 5. Modular and Composable
Prompts must follow single-responsibility design. Complex reasoning should be achieved by composing multiple focused prompts rather than creating monolithic prompts. Each prompt should be independently testable and independently replaceable.
