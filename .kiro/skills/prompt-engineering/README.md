# Prompt Engineering

## Purpose
Designs the complete reasoning layer for Deep Agents by creating modular, versioned, and evaluatable prompts. This skill produces system prompts, planning prompts, reflection prompts, and evaluation prompts while handling context assembly, model routing, and output format specifications.

## Responsibilities
- Design system prompts that define agent identity, capabilities, and constraints
- Create planning prompts for multi-step reasoning and task decomposition
- Develop reflection prompts for self-assessment and quality evaluation
- Define output format specifications and structured response contracts
- Design context assembly strategies for optimal model utilization
- Specify model routing logic for multi-model architectures
- Establish prompt versioning and lifecycle management
- Define evaluation criteria for measuring prompt effectiveness

## Inputs
- Architecture specification (agent roles, reasoning requirements)
- Workflow specification (which steps need prompts, decision points)
- Component interfaces (what prompts need to produce for downstream components)
- Business rules (domain constraints, terminology, behavioral requirements)
- Model capabilities (context window sizes, supported formats, strengths)

## Outputs
- prompt-package.md — complete prompt catalog with all prompts defined
- System prompts (agent identity, role, constraints)
- Planning prompts (task decomposition, strategy selection)
- Reflection prompts (quality assessment, self-correction)
- Output format specifications (structured response contracts)
- Prompt evaluation criteria and test cases

## Dependencies
- Engineering Engines: Prompt Engineering Engine
- Knowledge Domains: knowledge/prompts/, knowledge/models/, knowledge/evaluation/
- Templates: templates/prompt/, templates/evaluation/
- Upstream: Architecture Engineering (agent roles), Workflow Engineering (prompt placement)
- Downstream: Implementation Generation, Evaluation

## Integration
- DAEP Orchestration Layer (invoked during Phase 9 of generation pipeline)
- Prompt Engineering Engine (primary engine)
- Knowledge Base (prompt patterns, model capabilities)
- Template Engine (prompt structure generation)
- Model Registry (capabilities, context limits, routing rules)
- Evaluation Framework (prompt quality measurement)

## Usage
This skill activates during Phase 9 of the Deep Agent Generation pipeline, after workflow and memory strategies are defined.

```
Workflow + Memory defined → prompt-engineering skill activates
  → Identifies all prompt needs from workflow
  → Designs prompt hierarchy (system, planning, execution, reflection)
  → Assembles context strategies
  → Specifies output formats
  → Produces prompt package with evaluation criteria
```

## Best Practices
- Keep prompts modular — one prompt per concern, composable for complex reasoning
- Version every prompt and document changes between versions
- Define evaluation criteria before writing the prompt (test-first prompt design)
- Design context assembly to maximize relevant information within model limits
- Never embed large prompts directly in code — externalize and reference
- Include few-shot examples in prompts where task ambiguity exists

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Triggers Hooks
- Produces deterministic outputs
