# Prompt Engineering

## Skill Definition

```yaml
name: prompt-engineering
description: Designs the complete reasoning layer including system prompts, planning prompts, reflection prompts, context assembly, and output specifications
version: 1.0.0
category: engineering
trigger: Workflow and memory strategies are defined, and the reasoning layer (prompts) needs to be designed for agent execution
```

## Required Inputs
- Workflow Specification: Defined workflow with steps that require LLM reasoning
- Agent Roles: Architecture-defined agent responsibilities and capabilities
- Output Requirements: Expected output formats and contracts for downstream components

## Optional Inputs
- Domain Knowledge: Specialized terminology, business rules, and constraints
- Model Preferences: Preferred models, context window limits, or capability requirements
- Few-Shot Examples: Domain-specific examples for in-context learning
- Existing Prompt Library: Organization's prompt catalog for reuse
- Evaluation Data: Test cases for prompt quality measurement

## Workflow

### Step 1: Prompt Needs Analysis
Identify all points in the workflow where LLM reasoning is required.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/patterns/
- Output: Prompt inventory — list of all required prompts with purpose

### Step 2: Prompt Hierarchy Design
Define the prompt hierarchy: system, planning, execution, reflection, evaluation.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/hierarchies/
- Output: Prompt hierarchy with relationships and invocation order

### Step 3: System Prompt Design
Create the foundational system prompt defining agent identity, capabilities, and constraints.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/system/, knowledge/models/capabilities/
- Output: System prompt with role, capabilities, constraints, and behavioral guidelines

### Step 4: Planning Prompt Design
Create prompts for task decomposition, strategy selection, and plan generation.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/planning/
- Output: Planning prompts with decomposition strategies and output structures

### Step 5: Execution Prompt Design
Create prompts for step-level reasoning during workflow execution.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/execution/
- Output: Execution prompts for each reasoning-dependent workflow step

### Step 6: Reflection Prompt Design
Create prompts for self-assessment, quality evaluation, and correction.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/reflection/
- Output: Reflection prompts with quality criteria and correction strategies

### Step 7: Context Assembly Strategy
Define how context is assembled, prioritized, and compressed for each prompt.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/context/, knowledge/models/limits/
- Output: Context assembly specification (sources, priority, compression, window management)

### Step 8: Output Format Specification
Define structured output formats, parsing rules, and validation criteria.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/outputs/
- Output: Output format specifications (schemas, examples, validation rules)

### Step 9: Model Routing Logic
Define which models handle which prompts based on capability requirements.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/models/routing/
- Output: Model routing table (prompt → model mapping with fallback)

### Step 10: Evaluation Criteria Definition
Define how prompt effectiveness is measured and tested.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/evaluation/, knowledge/evaluation/
- Output: Evaluation criteria, test cases, and quality thresholds

### Step 11: Prompt Package Assembly
Assemble all prompts into the complete prompt package.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/packaging/
- Output: prompt-package.md — complete prompt catalog

### Step 12: Prompt Validation
Validate prompts against evaluation criteria with test cases.
- Engine: Prompt Engineering Engine, Validation Engine
- Knowledge: knowledge/validation/prompts/
- Output: Prompt validation report with quality scores

## Engineering Rules
- Every prompt must have a defined purpose, inputs, outputs, and evaluation criteria
- Prompts must be externalized from implementation code — never inline large prompts
- All prompts must be versioned with documented change history
- Context assembly must respect model token limits with explicit overflow strategy
- Output formats must be parseable and validatable by downstream components
- Reflection prompts must include criteria for determining when quality is sufficient

## Knowledge Sources
- knowledge/prompts/patterns/ — prompt design patterns and techniques
- knowledge/prompts/hierarchies/ — prompt hierarchy structures
- knowledge/prompts/system/ — system prompt best practices
- knowledge/prompts/planning/ — planning and decomposition prompts
- knowledge/prompts/reflection/ — self-assessment and correction patterns
- knowledge/prompts/context/ — context assembly and management strategies
- knowledge/prompts/evaluation/ — prompt quality metrics and testing
- knowledge/models/ — model capabilities, limits, and routing strategies

## Templates Used
- templates/prompt/system-prompt.md — system prompt template
- templates/prompt/planning-prompt.md — planning prompt template
- templates/prompt/reflection-prompt.md — reflection prompt template
- templates/prompt/output-format.md — output format specification template
- templates/prompt/evaluation.md — evaluation criteria template
- templates/prompt/prompt-package.md — complete package template

## Engineering Engines Invoked
- Prompt Engineering Engine (primary)
- Validation Engine (prompt quality validation)

## Hooks Invoked
- pre-prompt-design — fires before prompt engineering begins
- post-system-prompt — fires after system prompt designed
- post-prompt-package — fires after complete package assembled
- post-prompt-evaluation — fires after evaluation criteria validated

## Validation
- All workflow reasoning points have corresponding prompts
- Every prompt has defined purpose, inputs, outputs, constraints, and evaluation criteria
- System prompt correctly establishes agent identity and capabilities
- Context assembly respects model token limits for all configured models
- Output formats are parseable and include examples
- Reflection prompts include clear quality thresholds
- Model routing is defined for all prompts with fallback paths
- Evaluation test cases cover happy path and edge cases
- Prompt package is complete and self-contained

## Expected Outputs
- prompt-package.md — complete catalog of all designed prompts
- System prompt — agent identity and behavioral foundation
- Planning prompts — task decomposition and strategy selection
- Execution prompts — step-level reasoning prompts
- Reflection prompts — quality assessment and self-correction
- Context assembly specification — how context is built for each prompt
- Output format specifications — structured response contracts
- Model routing table — prompt-to-model mapping
- Evaluation criteria — quality metrics and test cases

## Completion Criteria
- All required prompts identified and designed
- Prompt hierarchy established with clear invocation relationships
- Context assembly strategy defined and validated against token limits
- Output formats specified with parsing rules and examples
- Model routing defined with fallback strategies
- Evaluation criteria established with test cases
- Prompt package assembled and validated
- Downstream implementation has unambiguous prompt specifications
