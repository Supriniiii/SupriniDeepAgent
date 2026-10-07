# Contribution Guide

## Purpose

This document defines the contribution standards for the Deep Agent Engineering Platform (DAEP).

The objective is to ensure that all contributions follow consistent engineering practices, maintain the modular architecture of the platform, and preserve the deterministic engineering process used to generate Deep Agents.

Contributors should prioritize maintainability, reusability, traceability, and engineering quality over rapid implementation.

---

# Engineering Philosophy

The platform follows an engineering-first approach.

Every contribution should:

- Preserve the engineering pipeline.
- Maintain separation of concerns.
- Reuse existing knowledge before introducing new assets.
- Follow the established architecture.
- Be fully documented.
- Be traceable.
- Be testable.
- Support future extensibility.

Contributors should avoid introducing functionality that bypasses the Generation Orchestration Engine or the Engineering Engine pipeline.

---

# Repository Structure

Contributors should understand the responsibility of each directory before making changes.

```text
.kiro/
├── steering/
├── hooks/
├── engines/
├── knowledge/
├── registries/
├── templates/
├── outputs/
├── docs/
└── README.md
```

Each directory has a single architectural responsibility.

Do not move functionality between directories unless the platform architecture changes.

---

# Contribution Principles

All contributions should:

- Follow the existing architecture.
- Maintain modularity.
- Preserve deterministic behavior.
- Promote reuse.
- Avoid duplication.
- Include documentation.
- Include validation where appropriate.

---

# Working with Steering

The Steering directory contains global engineering guidance.

Only modify Steering when organizational engineering policies or standards change.

Changes to Steering affect the entire platform and should be reviewed carefully.

---

# Working with Hooks

Hooks coordinate the engineering lifecycle.

When modifying Hooks:

- Preserve execution order.
- Maintain Hook responsibilities.
- Avoid embedding engineering logic inside Hooks.
- Keep Hooks focused on orchestration.

Engineering decisions belong inside Engineering Engines.

---

# Working with Engineering Engines

Each Engineering Engine has a dedicated responsibility.

When extending an engine:

- Update the engine README.
- Update the engine contract.
- Preserve existing responsibilities.
- Avoid duplicating functionality from other engines.
- Maintain artifact-based communication.

If new engineering capabilities are required, consider whether they belong in an existing engine before creating a new one.

---

# Working with Knowledge

The Knowledge repository contains reusable engineering knowledge.

Examples include:

- Architectural patterns
- Workflow patterns
- Prompt patterns
- Engineering guidelines
- Best practices
- Organizational standards

Contributors should extend existing knowledge before creating duplicate content.

Knowledge should remain implementation-independent wherever possible.

---

# Working with Registries

Registries catalog reusable engineering assets.

Examples include:

- Capabilities
- Components
- Harnesses
- Prompts
- Workflows

Before adding a new registry entry:

- Verify that an equivalent asset does not already exist.
- Ensure metadata is complete.
- Follow naming conventions.
- Document intended usage.

---

# Working with Templates

Templates provide reusable engineering blueprints.

Templates should:

- Be generic.
- Be reusable.
- Be well documented.
- Avoid implementation-specific assumptions.
- Follow organizational standards.

Contributors should update existing templates before creating new ones whenever practical.

---

# Documentation Standards

Every significant contribution should include documentation updates where applicable.

Documentation should be:

- Accurate
- Consistent
- Clear
- Up to date
- Easy to navigate

Relevant documentation includes:

- README.md
- Architecture documentation
- Engine documentation
- Developer Guide
- Contribution Guide
- Roadmap

---

# Naming Conventions

Use clear and descriptive names.

Examples:

- requirements-engine
- workflow-engine
- prompt-package
- component-registry

Avoid abbreviations unless they are well established within the platform.

Maintain consistency across directories, documentation, and generated artifacts.

---

# Validation

Before submitting changes, contributors should verify:

- Documentation is complete.
- Directory structure is preserved.
- Engineering responsibilities remain separated.
- Existing functionality is not broken.
- New functionality aligns with the platform architecture.

---

# Pull Request Checklist

Before requesting a review, ensure:

- Engineering changes are complete.
- Documentation has been updated.
- New templates are documented.
- Registry entries are complete.
- Knowledge additions are validated.
- Naming conventions are followed.
- No unnecessary duplication has been introduced.

---

# Code Review Guidelines

Reviewers should verify:

- Architectural consistency.
- Engineering quality.
- Modularity.
- Documentation quality.
- Reusability.
- Maintainability.
- Traceability.

Feedback should be constructive and aligned with the platform's engineering philosophy.

---

# Future Contributions

As the platform evolves, contributors may introduce:

- New Engineering Engines
- Additional Hooks
- New Templates
- Expanded Knowledge repositories
- New Registry types
- Enhanced evaluation strategies
- Multi-agent capabilities

All future enhancements should integrate with the existing architecture rather than bypassing it.

---

# Conclusion

The Deep Agent Engineering Platform is intended to be an extensible engineering framework for building enterprise-grade Deep Agents.

By following this Contribution Guide, contributors help ensure that the platform remains modular, maintainable, reusable, and aligned with the engineering principles established by the Deep Agent Engineering Platform.
