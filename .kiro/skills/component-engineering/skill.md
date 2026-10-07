# Component Engineering

## Skill Definition

```yaml
name: component-engineering
description: Identifies, selects, and defines reusable components while maximizing reuse from existing registries
version: 1.0.0
category: engineering
trigger: Architecture is established and component boundaries need to be defined or existing components need to be selected
```

## Required Inputs
- Architecture Specification: Documented architecture with component boundaries and interfaces
- Requirements Map: Functional capabilities mapped to architectural components
- Component Registry: Access to existing component catalog for reuse discovery

## Optional Inputs
- Technology Constraints: Language, framework, or platform limitations
- Performance Requirements: Throughput, latency, or resource constraints per component
- Existing Codebase: Current implementation to assess for reusable functionality
- Security Classification: Data sensitivity levels affecting component isolation

## Workflow

### Step 1: Component Inventory
Extract all required components from the architecture specification.
- Engine: Component Engineering Engine
- Knowledge: knowledge/components/patterns/
- Output: Complete list of required components with high-level responsibilities

### Step 2: Registry Search
Search existing component registries for reusable matches.
- Engine: Component Engineering Engine
- Knowledge: knowledge/components/registry/, knowledge/registries/
- Output: Reuse assessment — matched components with compatibility scores

### Step 3: Reuse Decision
For each required component, decide: reuse as-is, adapt existing, or build new.
- Engine: Component Engineering Engine
- Knowledge: knowledge/components/evaluation/
- Output: Reuse decision matrix with justifications

### Step 4: New Component Specification
For components that must be built, define detailed specifications.
- Engine: Component Engineering Engine
- Knowledge: knowledge/components/specifications/
- Output: Component specification (responsibility, interface, dependencies, constraints)

### Step 5: Interface Design
Define interface contracts for all components (reused and new).
- Engine: Component Engineering Engine
- Knowledge: knowledge/interfaces/, knowledge/components/contracts/
- Output: Interface definitions with input/output types, error contracts, versioning

### Step 6: Dependency Analysis
Map dependencies between components, identify circular dependencies, optimize.
- Engine: Component Engineering Engine
- Knowledge: knowledge/components/dependencies/
- Output: Dependency graph, dependency inversion opportunities

### Step 7: Component Plan Assembly
Assemble the complete component plan with build order and integration sequence.
- Engine: Component Engineering Engine
- Knowledge: knowledge/components/planning/
- Output: component-plan.md — comprehensive component plan

### Step 8: Component Validation
Validate component plan against architecture and requirements.
- Engine: Component Engineering Engine, Validation Engine
- Knowledge: knowledge/validation/components/
- Output: Component validation report

## Engineering Rules
- Never duplicate functionality available in existing registries
- Every component must have a single, clearly defined responsibility
- Interfaces must be defined before implementation starts
- All components must be independently testable
- Dependencies must flow in one direction — no circular dependencies
- New components must be designed for future reuse and registry promotion

## Knowledge Sources
- knowledge/components/registry/ — enterprise component catalog
- knowledge/components/patterns/ — component design patterns
- knowledge/components/specifications/ — specification templates and examples
- knowledge/components/contracts/ — interface contract patterns
- knowledge/components/dependencies/ — dependency management practices
- knowledge/interfaces/ — interface definition standards

## Templates Used
- templates/component/specification.md — component specification template
- templates/component/interface.md — interface definition template
- templates/component/plan.md — component plan template
- templates/component/dependency-map.md — dependency visualization template

## Engineering Engines Invoked
- Component Engineering Engine (primary)
- Validation Engine (component plan validation)

## Hooks Invoked
- pre-component-selection — fires before registry search begins
- post-reuse-assessment — fires after reuse opportunities identified
- post-component-selection — fires after all component decisions made
- post-component-plan — fires after component plan assembled

## Validation
- All architectural components are accounted for in the component plan
- No duplicated functionality — reuse maximized from registry
- Every component has a defined single responsibility
- All interfaces have complete contracts (inputs, outputs, errors)
- No circular dependencies exist in the dependency graph
- New components are designed for independent testing
- Component plan provides clear build order for implementation

## Expected Outputs
- component-plan.md — complete component inventory with responsibilities and decisions
- Interface specifications — contracts for all component boundaries
- Reuse assessment report — what was reused vs. what is new
- Dependency map — component relationship graph
- Component specifications — detailed specs for new components
- Component validation report — confirmation of quality standards

## Completion Criteria
- All required components identified from architecture specification
- Registry search performed — all reuse opportunities evaluated
- Reuse decisions documented with justifications
- New components fully specified (responsibility, interface, dependencies)
- Dependency graph clean (no circular dependencies)
- Component plan validated against architecture and requirements
- Downstream skills (workflow, implementation) have clear component contracts
