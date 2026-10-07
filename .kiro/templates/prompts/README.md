# Prompt Templates

## Purpose

The Prompt Templates directory contains reusable prompt engineering blueprints used by the Deep Agent Engineering Platform (DAEP) to generate standardized, consistent, and high-quality prompts for Deep Agents.

These templates define the structure, behavior, reasoning strategies, interaction patterns, and response formats used by AI agents throughout the platform.

The Prompt Engineering Engine uses these templates to generate optimized prompts for planning, execution, reasoning, evaluation, reflection, verification, and orchestration.

---

# Objectives

The Prompt Templates directory is responsible for:

- Standardizing prompt generation.
- Promoting reusable prompt patterns.
- Supporting multiple reasoning strategies.
- Improving response consistency.
- Reducing prompt duplication.
- Supporting agent specialization.
- Enabling deterministic AI behavior.
- Integrating with the Generation Orchestration Engine (GOE).

---

# Scope

Prompt templates define:

- System prompts.
- Task prompts.
- Planning prompts.
- Execution prompts.
- Reflection prompts.
- Verification prompts.
- Evaluation prompts.
- Tool selection prompts.
- Memory prompts.
- Workflow prompts.
- Agent collaboration prompts.
- Output formatting prompts.

Templates define prompt structure only and do not contain project-specific content.

---

# Expected Templates

Kiro should generate reusable prompt templates for the following categories.

## Core Prompts

- System Prompt
- User Prompt
- Task Prompt
- Context Prompt
- Goal Prompt

---

## Planning Prompts

- Planning Prompt
- Decomposition Prompt
- Strategy Prompt
- Task Prioritization Prompt

---

## Execution Prompts

- Execution Prompt
- Action Prompt
- Tool Invocation Prompt
- Workflow Execution Prompt

---

## Reflection Prompts

- Reflection Prompt
- Self-Review Prompt
- Improvement Prompt
- Learning Prompt

---

## Verification Prompts

- Verification Prompt
- Validation Prompt
- Consistency Check Prompt
- Compliance Prompt

---

## Evaluation Prompts

- Evaluation Prompt
- Quality Assessment Prompt
- Performance Assessment Prompt
- Benchmark Prompt

---

## Memory Prompts

- Context Retrieval Prompt
- Memory Update Prompt
- Knowledge Retrieval Prompt
- Memory Consolidation Prompt

---

## Multi-Agent Prompts

- Agent Collaboration Prompt
- Manager Prompt
- Worker Prompt
- Agent Communication Prompt
- Coordination Prompt

---

## Output Prompts

- Structured Response Prompt
- Markdown Output Prompt
- JSON Output Prompt
- Report Generation Prompt
- Documentation Prompt

---

# Template Requirements

Every generated prompt template should include:

- Prompt Metadata
- Purpose
- Role Definition
- Objectives
- Context Requirements
- Inputs
- Expected Outputs
- Reasoning Strategy
- Constraints
- Rules
- Response Format
- Validation Criteria
- Error Handling Guidance
- Extension Points

---

# Engineering Standards

Generated prompt templates shall:

- Follow DAEP engineering standards.
- Be modular and reusable.
- Encourage deterministic responses.
- Minimize ambiguity.
- Support structured outputs.
- Support chain-of-thought alternatives without exposing internal reasoning.
- Be extensible.
- Support multiple AI models.
- Promote consistent agent behavior.
- Be easy to maintain.

---

# Generation Requirements

When generating prompt templates, Kiro shall:

- Produce production-ready prompt templates.
- Use placeholder variables where project-specific values are required.
- Clearly separate system instructions, user context, constraints, and expected outputs.
- Define response formatting requirements.
- Include validation guidance.
- Maintain consistent formatting across all prompt templates.

Generated templates should remain model-agnostic wherever possible.

---

# Integration with DAEP

Prompt templates integrate with:

- Generation Orchestration Engine (GOE)
- Prompt Engineering Engine
- Workflow Engineering Engine
- Memory Engineering Engine
- Component Engineering Engine
- Harness Engineering Engine
- Validation Framework

Prompt templates should consume outputs from:

- Architecture Templates
- Workflow Templates
- Component Templates
- Memory Templates
- Knowledge Base
- Steering Rules

---

# Related Directories

Prompt templates work closely with:

- `templates/workflows`
- `templates/components`
- `templates/agents`
- `templates/harnesses`
- `templates/testing`
- `templates/documentation`

They also leverage engineering knowledge from:

- `knowledge/prompts`
- `knowledge/workflows`
- `knowledge/memory`
- `knowledge/capabilities`
- `knowledge/decision_rules`

---

# Best Practices

Prompt templates should:

- Clearly define the AI's role.
- Establish explicit objectives.
- Provide sufficient context.
- Specify expected output formats.
- Include operational constraints.
- Encourage reliable and repeatable responses.
- Minimize hallucinations through clear instructions.
- Support future extensibility.
- Be understandable by both humans and AI systems.

---

# Quality Requirements

Every generated prompt template should:

- Produce consistent responses.
- Support structured outputs.
- Minimize ambiguity.
- Align with engineering objectives.
- Support validation.
- Be reusable across multiple agent types.
- Integrate seamlessly with DAEP components.

---

# Generation Prompt

When generating prompt templates, Kiro should:

1. Analyze the intended prompt category and agent responsibilities.
2. Generate standardized prompt templates following DAEP engineering standards.
3. Include metadata, objectives, context, reasoning strategy, constraints, expected outputs, validation guidance, and extension points.
4. Use placeholder variables for configurable or project-specific values.
5. Ensure compatibility with the Generation Orchestration Engine, Prompt Engineering Engine, Hooks, Knowledge Base, Components, and Steering Rules.
6. Produce reusable, modular, and model-agnostic prompt templates suitable for enterprise-grade AI systems.
7. Maintain consistency, extensibility, and high engineering quality across all generated prompts.

---

# Summary

The Prompt Templates directory provides the reusable prompt blueprints used by the Deep Agent Engineering Platform to generate consistent, reliable, and production-ready AI prompts.

By standardizing prompt structure, reasoning strategies, response formats, validation rules, and interaction patterns, these templates enable the Prompt Engineering Engine to consistently produce high-quality prompts that drive intelligent, predictable, and maintainable Deep Agent behavior across the platform.
