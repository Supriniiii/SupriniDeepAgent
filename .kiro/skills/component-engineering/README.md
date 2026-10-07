# Component Engineering

## Purpose
Identifies, selects, and defines reusable components for Deep Agent solutions. This skill maximizes reuse from existing registries, defines clear responsibilities and interfaces for new components, and produces component plans that guide implementation while preventing duplication of functionality.

## Responsibilities
- Search existing component registries and catalogs for reusable functionality
- Identify reuse opportunities across the enterprise component ecosystem
- Define new component boundaries, responsibilities, and interfaces
- Specify component dependencies and integration contracts
- Prevent duplication of existing functionality
- Design components for independent testing and documentation
- Establish component versioning and lifecycle management
- Promote newly created components to the reuse registry

## Inputs
- Architecture specification (architecture.md with component boundaries)
- Confirmed requirements (functional capabilities each component must provide)
- Existing component catalog (registry of available reusable components)
- Interface definitions (contracts components must satisfy)
- Constraints (technology, performance, security)

## Outputs
- component-plan.md — component inventory with responsibilities and boundaries
- Interface specifications for each component
- Dependency map showing component relationships
- Reuse assessment report (what exists vs. what must be built)
- Component scaffolding specifications for new components

## Dependencies
- Engineering Engines: Component Engineering Engine
- Knowledge Domains: knowledge/components/, knowledge/registries/, knowledge/interfaces/
- Templates: templates/component/, templates/interfaces/
- Upstream: Architecture Engineering (provides architecture specification)
- Downstream: Workflow Engineering, Implementation Generation

## Integration
- DAEP Orchestration Layer (invoked during Phase 5 of generation pipeline)
- Component Engineering Engine (primary engine)
- Component Registry (search and retrieval of existing components)
- Knowledge Base (component patterns and best practices)
- Template Engine (component scaffolding generation)
- Architecture artifacts (drives component boundaries)

## Usage
This skill activates during Phase 4-5 of the Deep Agent Generation pipeline, after architecture is established and component boundaries are defined.

```
Architecture complete → component-engineering skill activates
  → Searches registries for reusable components
  → Identifies reuse opportunities
  → Defines new components where needed
  → Specifies interfaces and dependencies
  → Produces component plan for implementation
```

## Best Practices
- Always search the component catalog before defining a new component
- Prefer composition of existing components over building from scratch
- Design components with single responsibility — one reason to change
- Define interfaces before implementation, not after
- Ensure every component can be tested independently
- Document component contracts including error cases and edge conditions

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Triggers Hooks
- Produces deterministic outputs
