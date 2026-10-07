# Project Structure

## General Principle

All generated projects must follow a modular, scalable, enterprise architecture.

Projects should separate concerns and avoid monolithic implementations.

---

## Recommended Structure

Each generated Deep Agent should contain dedicated areas for:

- Agent logic
- Agent Harness
- Components
- Workflows
- Memory
- Tool integrations
- Prompts
- Configuration
- Documentation
- Testing
- Deployment
- Validation
- Observability

Business logic must remain independent of infrastructure and AI providers.

---

## Engineering Rules

Always organize reusable functionality into independent modules.

Avoid placing unrelated responsibilities inside the same file.

Large files should be decomposed into reusable components.

Prefer composition over duplication.

Prefer interfaces over concrete implementations.

---

## Documentation

Every generated project should include:

- README
- Architecture documentation
- Architecture Decision Records (ADR)
- Configuration Guide
- Deployment Guide
- Operations Guide
- Prompt Catalog
- Component Catalog

---

## Testing

Every project should include:

- Unit tests
- Integration tests
- Workflow tests
- AI evaluation tests
- Security tests
- Performance tests

---

## Deployment

Generated projects should support containerized deployment and include deployment configuration where appropriate.

Deployment assets should remain independent from business logic.

---

## Extensibility

Projects should be designed so that:

- Components can be replaced.
- Harnesses can evolve.
- New tools can be added.
- Additional workflows can be introduced.
- Memory implementations can change without affecting business logic.

Favor plugin-style architecture whenever practical.