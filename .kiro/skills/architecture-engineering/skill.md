# Architecture Engineering

## Skill Definition

```yaml
name: architecture-engineering
description: Designs solution architectures by selecting patterns, justifying decisions, and producing architecture artifacts
version: 1.0.0
category: engineering
trigger: Requirements are confirmed and architecture design is needed for a Deep Agent or multi-agent system
```

## Required Inputs
- Confirmed Requirements: Documented functional and non-functional requirements with acceptance criteria
- Constraints: Performance, scalability, reliability, security, and compliance constraints
- Deployment Context: Target runtime environment, infrastructure capabilities, and operational requirements

## Optional Inputs
- Existing Architecture: Current system architecture if extending or integrating
- Preferred Patterns: Developer-specified architectural preferences or organizational standards
- Component Catalog: Available reusable components that may influence architecture decisions
- Reference Architectures: Organization-specific reference architectures to align with

## Workflow

### Step 1: Architectural Driver Analysis
Identify quality attributes and architectural drivers from requirements.
- Engine: Architecture Engineering Engine
- Knowledge: knowledge/architectures/quality-attributes/
- Output: Prioritized list of architectural drivers (scalability, reliability, performance, security, etc.)

### Step 2: Pattern Evaluation
Evaluate candidate architectural patterns against identified drivers.
- Engine: Architecture Engineering Engine
- Knowledge: knowledge/architectures/patterns/
- Output: Pattern evaluation matrix with scores per driver

### Step 3: Pattern Selection
Select the pattern that best satisfies the prioritized drivers. Justify the decision.
- Engine: Architecture Engineering Engine
- Knowledge: knowledge/architectures/patterns/, knowledge/architectures/reference/
- Output: Selected pattern with justification

### Step 4: Architecture Specification
Define the complete architecture including components, boundaries, interfaces, and data flows.
- Engine: Architecture Engineering Engine
- Knowledge: knowledge/architectures/specifications/
- Output: architecture.md — full specification

### Step 5: ADR Generation
Document each significant architectural decision with context, decision, and consequences.
- Engine: Architecture Engineering Engine
- Knowledge: knowledge/architectures/adrs/
- Output: ADR documents (one per significant decision)

### Step 6: Diagram Generation
Generate architecture diagrams at appropriate abstraction levels.
- Engine: Architecture Engineering Engine
- Knowledge: knowledge/architectures/diagrams/
- Output: Component diagram, sequence diagrams, deployment diagram

### Step 7: Interface Definition
Define interfaces between major architectural components.
- Engine: Architecture Engineering Engine
- Knowledge: knowledge/architectures/interfaces/
- Output: Interface specifications with contracts

### Step 8: Architecture Validation
Validate the architecture against requirements, constraints, and quality standards.
- Engine: Architecture Engineering Engine, Validation Engine
- Knowledge: knowledge/validation/architecture/
- Output: Architecture validation report

## Engineering Rules
- Never select a pattern without justifying it against requirements
- Always document rejected alternatives and the reasons for rejection
- Architecture must support observability (logging, metrics, tracing) as a first-class concern
- Design for failure — every architecture must include error handling and recovery strategies
- Interfaces must be defined before implementation begins
- Architecture changes after implementation begins require a new ADR

## Knowledge Sources
- knowledge/architectures/patterns/ — catalog of available architectural patterns
- knowledge/architectures/quality-attributes/ — quality attribute taxonomies and trade-offs
- knowledge/architectures/reference/ — enterprise reference architectures
- knowledge/architectures/adrs/ — ADR templates and examples
- knowledge/architectures/diagrams/ — diagram conventions and notation
- knowledge/architectures/interfaces/ — interface definition patterns

## Templates Used
- templates/architecture/architecture-spec.md — architecture specification template
- templates/architecture/adr.md — Architecture Decision Record template
- templates/architecture/diagram.md — diagram notation template
- templates/architecture/interface.md — interface definition template
- templates/architecture/evaluation-matrix.md — pattern evaluation template

## Engineering Engines Invoked
- Architecture Engineering Engine (primary)
- Validation Engine (architecture quality validation)

## Hooks Invoked
- pre-architecture — fires before architecture design begins
- post-pattern-selection — fires after pattern is selected and justified
- post-architecture — fires after architecture artifacts are complete

## Validation
- Selected pattern is justified against all architectural drivers
- Architecture addresses all non-functional requirements
- All component interfaces are defined with clear contracts
- Failure modes and recovery strategies are documented
- Architecture supports required observability capabilities
- ADRs are complete for all significant decisions
- Diagrams accurately represent the specified architecture

## Expected Outputs
- architecture.md — complete architecture specification
- ADR documents — one per significant architectural decision
- Architecture diagrams — component, sequence, and deployment views
- Interface definitions — contracts between major components
- Pattern evaluation matrix — analysis showing pattern selection rationale
- Architecture validation report — confirmation of quality standards

## Completion Criteria
- Architecture pattern selected and justified against requirements
- All architectural drivers addressed with documented trade-offs
- ADRs written for all significant decisions
- Diagrams generated at appropriate abstraction levels
- Interfaces defined for all component boundaries
- Architecture validated by Architecture Engineering Engine
- Downstream skills (component, workflow, harness) can proceed with clear guidance
