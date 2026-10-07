# Component Templates

## Purpose

The Component Templates directory contains reusable component blueprints used by the Deep Agent Engineering Platform (DAEP) to generate standardized, modular, and production-ready software components for Deep Agents.

These templates define the structure, responsibilities, interfaces, lifecycle, configuration, interactions, and operational behavior of reusable components that form the foundation of every generated AI system.

The Component Engineering Engine uses these templates to generate consistent implementations that integrate seamlessly with the Generation Orchestration Engine (GOE), Engineering Engines, Hooks, Harnesses, and Workflows.

---

# Objectives

The Component Templates directory is responsible for:

- Standardizing component generation.
- Promoting reusable software components.
- Supporting modular architecture.
- Defining component contracts.
- Enabling plug-and-play components.
- Supporting independent development and testing.
- Improving maintainability.
- Supporting enterprise-scale systems.
- Integrating with all DAEP engineering processes.

---

# Scope

Component templates define:

- Component metadata.
- Responsibilities.
- Interfaces.
- Inputs and outputs.
- Internal workflows.
- Configuration.
- State management.
- Error handling.
- Dependencies.
- Validation requirements.
- Monitoring requirements.
- Extension points.

Templates define reusable component structures only and remain implementation-independent.

---

# Expected Templates

Kiro should generate reusable templates for the following core platform components.

## Planning Components

- Planner
- Task Planner
- Strategy Planner
- Goal Planner

---

## Execution Components

- Executor
- Task Executor
- Workflow Executor
- Action Executor

---

## Reflection Components

- Reflection Engine
- Self-Review Component
- Improvement Component
- Learning Component

---

## Verification Components

- Verifier
- Consistency Verifier
- Policy Verifier
- Output Validator

---

## Evaluation Components

- Evaluator
- Quality Evaluator
- Performance Evaluator
- Benchmark Evaluator

---

## Memory Components

- Memory Manager
- Context Manager
- Long-Term Memory
- Short-Term Memory
- Retrieval Manager

---

## Tool Components

- Tool Manager
- Tool Registry
- Tool Selector
- Tool Executor

---

## Workflow Components

- Workflow Manager
- Workflow Coordinator
- Task Scheduler
- Orchestrator

---

## State Components

- State Manager
- Session Manager
- Checkpoint Manager
- Recovery Manager

---

# Template Requirements

Every generated component template should include:

- Component Metadata
- Purpose
- Responsibilities
- Scope
- Inputs
- Outputs
- Interfaces
- Internal Workflow
- Dependencies
- Configuration
- State Management
- Error Handling
- Logging
- Monitoring
- Validation Requirements
- Extension Points
- Engineering Notes

---

# Engineering Standards

Generated component templates shall:

- Follow DAEP engineering standards.
- Follow the Single Responsibility Principle.
- Be modular.
- Be reusable.
- Be loosely coupled.
- Be highly cohesive.
- Support dependency injection.
- Be technology independent where possible.
- Support testing.
- Support observability.
- Support enterprise deployments.

---

# Generation Requirements

When generating component templates, Kiro shall:

- Produce production-ready component templates.
- Use placeholder variables where project-specific values are required.
- Clearly define interfaces and responsibilities.
- Include configuration sections.
- Define lifecycle behavior.
- Support validation.
- Maintain consistent formatting across all templates.

Generated templates should focus on component architecture rather than implementation details.

---

# Integration with DAEP

Component templates integrate with:

- Generation Orchestration Engine (GOE)
- Component Engineering Engine
- Architecture Engineering Engine
- Workflow Engineering Engine
- Memory Engineering Engine
- Prompt Engineering Engine
- Harness Engineering Engine
- Validation Framework

Component templates consume outputs from:

- Architecture Templates
- Workflow Templates
- Prompt Templates
- Harness Templates
- Knowledge Base
- Steering Rules

---

# Related Directories

Component templates work closely with:

- `templates/architectures`
- `templates/workflows`
- `templates/prompts`
- `templates/harnesses`
- `templates/testing`
- `templates/validation`

They also leverage engineering knowledge from:

- `knowledge/components`
- `knowledge/capabilities`
- `knowledge/workflows`
- `knowledge/memory`
- `knowledge/tools`
- `knowledge/security`
- `knowledge/decision_rules`

---

# Best Practices

Component templates should:

- Define one clear responsibility.
- Expose well-defined interfaces.
- Minimize dependencies.
- Be independently testable.
- Support configuration over hardcoding.
- Encourage composition over inheritance.
- Support future extensibility.
- Be understandable by both engineers and AI systems.

---

# Quality Requirements

Every generated component template should:

- Be internally consistent.
- Clearly define responsibilities.
- Include interface specifications.
- Support automated validation.
- Integrate seamlessly with other DAEP components.
- Follow repository engineering standards.
- Produce reusable, enterprise-ready components.

---

# Generation Prompt

When generating component templates, Kiro should:

1. Analyze the intended component type and its responsibilities.
2. Generate standardized component templates following DAEP engineering standards.
3. Include metadata, responsibilities, interfaces, configuration, lifecycle, dependencies, validation requirements, monitoring, and extension points.
4. Use placeholder variables for project-specific values.
5. Ensure compatibility with the Generation Orchestration Engine, Component Engineering Engine, Hooks, Knowledge Base, Engineering Engines, and Steering Rules.
6. Produce reusable, modular, technology-agnostic, and production-ready component templates suitable for enterprise AI engineering systems.
7. Maintain consistency, extensibility, traceability, and high engineering quality across all generated component templates.

---

# Summary

The Component Templates directory provides the reusable component blueprints used by the Deep Agent Engineering Platform to generate modular, maintainable, and enterprise-ready software components.

By standardizing component structure, responsibilities, interfaces, lifecycle management, validation, and integration, these templates enable the Component Engineering Engine to consistently generate high-quality building blocks that form the foundation of every Deep Agent and AI engineering solution produced by DAEP.
