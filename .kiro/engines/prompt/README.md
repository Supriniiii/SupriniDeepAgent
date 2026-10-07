# Prompt Engineering Engine

## Purpose

The Prompt Engineering Engine is responsible for designing the reasoning layer of the generated Deep Agent.

Rather than producing individual prompts, the engine engineers a complete prompt architecture that defines how the agent reasons, plans, interacts with language models, invokes tools, consumes memory, and produces reliable outputs.

The engine transforms the architectural, workflow, and memory specifications into a reusable prompt system that supports deterministic, high-quality agent behaviour.

---

# Objectives

The Prompt Engineering Engine shall:

- Design the complete prompt architecture.
- Define prompt roles and responsibilities.
- Design reasoning strategies.
- Design planning strategies.
- Design reflection strategies.
- Design tool-calling prompts.
- Design memory injection strategies.
- Design context assembly strategies.
- Define model routing policies.
- Produce reusable prompt packages.

---

# Responsibilities

The engine is responsible for:

- Prompt Architecture
- System Prompt Design
- Planning Prompt Design
- Execution Prompt Design
- Reflection Prompt Design
- Verification Prompt Design
- Tool Invocation Prompt Design
- Memory Injection Strategy
- Context Assembly
- Prompt Composition
- Prompt Versioning
- Prompt Validation
- Model Selection Strategy
- Output Formatting Strategy

---

# Inputs

The engine consumes:

- architecture.md
- workflow-specification.md
- harness-specification.md
- memory-strategy.md
- context-management.md
- retrieval-strategy.md
- component-plan.md
- Steering Documents
- Prompt Knowledge Base
- Decision Rules

---

# Outputs

The engine produces:

- prompt-package.md
- prompt-architecture.md
- system-prompts.md
- reasoning-strategy.md
- prompt-composition.md
- context-assembly.md
- model-routing.md
- output-specification.md
- prompt-validation.md

These artifacts define how the Deep Agent reasons and communicates with language models.

---

# Engineering Activities

The engine performs the following activities:

1. Analyze the approved architecture.
2. Analyze workflow execution.
3. Analyze memory strategy.
4. Define reasoning architecture.
5. Design system prompts.
6. Design planning prompts.
7. Design execution prompts.
8. Design reflection prompts.
9. Design verification prompts.
10. Define context assembly.
11. Define memory injection.
12. Define model routing.
13. Define structured outputs.
14. Produce the Prompt Package.

---

# Prompt Layers

The engine may define multiple prompt layers including:

- System Prompt
- Planner Prompt
- Task Prompt
- Tool Prompt
- Reflection Prompt
- Verification Prompt
- Recovery Prompt
- Evaluation Prompt
- Human Interaction Prompt

Each layer has a clearly defined responsibility and should avoid unnecessary overlap.

---

# Context Assembly

The engine specifies how context is constructed before every model invocation.

Context may include:

- Current task
- Workflow state
- Session memory
- Long-term memory
- Retrieved knowledge
- Component state
- Tool results
- Previous reasoning
- User instructions
- Organizational policies

The engine determines the order, priority, and inclusion rules for each context source.

---

# Model Routing

The engine defines:

- Which model performs planning.
- Which model performs execution.
- Which model performs reflection.
- Which model performs verification.
- Fallback model policies.
- Cost optimization policies.
- Latency optimization policies.

Model routing should remain implementation-independent and support multiple providers.

---

# Output Engineering

The engine defines:

- Structured output formats.
- JSON schemas.
- Markdown formats.
- Validation rules.
- Confidence reporting.
- Citation requirements.
- Error reporting.

Outputs should be deterministic and easily consumable by downstream components.

---

# Validation Rules

The engine validates that:

- Prompt architecture is complete.
- Prompt responsibilities are clearly separated.
- Context assembly is defined.
- Memory integration is documented.
- Model routing is specified.
- Output formats are documented.
- Prompt package satisfies workflow requirements.

Generation shall not continue without a complete Prompt Package.

---

# Design Principles

The Prompt Engineering Engine shall:

- Separate reasoning concerns.
- Promote reusable prompt patterns.
- Support deterministic outputs.
- Minimize prompt duplication.
- Support multiple language models.
- Support structured outputs.
- Integrate seamlessly with memory and workflow.
- Remain independent of specific LLM providers.

---

# Integration

This engine is invoked by the Prompt Engineering Hook.

Inputs are received through the Generation Orchestration Engine.

Outputs are consumed by:

- Validation Engine
- Evaluation Engine
- Generation Hook

The engine communicates exclusively through engineering artifacts.

---

# Knowledge Sources

The engine may consult:

- knowledge/prompts/
- knowledge/workflows/
- knowledge/memory/
- knowledge/examples/
- knowledge/governance/
- knowledge/security/
- knowledge/decision_rules/
- registries/

These repositories provide reusable prompt patterns, reasoning strategies, organizational standards, and enterprise engineering guidance.

---

# Success Criteria

The Prompt Engineering Engine is successful when:

- A complete Prompt Package has been produced.
- Prompt architecture supports the approved workflow.
- Context assembly is fully defined.
- Memory integration is documented.
- Model routing policies are specified.
- Output specifications are complete.
- The generated prompt system enables reliable, deterministic reasoning for the Deep Agent.
