# Anti-Patterns Knowledge

## Purpose

The Anti-Patterns knowledge domain defines common engineering mistakes, poor design decisions, ineffective practices, and architectural pitfalls that should be avoided when developing Deep Agents within the Deep Agent Engineering Platform (DAEP).

While the other knowledge domains describe recommended engineering practices, this knowledge base documents what should **not** be done. It enables Engineering Engines and developers to recognize, prevent, and correct engineering decisions that reduce quality, maintainability, scalability, reliability, or security.

This knowledge base serves as the negative knowledge repository for DAEP engineering.

---

# Objectives

The Anti-Patterns knowledge domain aims to:

- Identify common engineering mistakes.
- Prevent poor architectural decisions.
- Improve engineering quality.
- Promote maintainable solutions.
- Reduce technical debt.
- Support engineering reviews.
- Improve automated validation.
- Encourage best engineering practices.

---

# Scope

This knowledge domain covers anti-patterns related to:

- Architectures.
- Components.
- Workflows.
- Prompts.
- Memory systems.
- Tool integrations.
- Testing.
- Validation.
- Deployment.
- Security.
- Governance.
- Multi-agent systems.

The knowledge base focuses on identifying undesirable engineering practices rather than prescribing implementation details.

---

# Anti-Pattern Definition

An anti-pattern is a commonly observed engineering solution that appears effective initially but consistently leads to poor outcomes.

Each anti-pattern should document:

- Name.
- Description.
- Symptoms.
- Causes.
- Consequences.
- Detection methods.
- Recommended alternatives.
- Related knowledge domains.

Understanding anti-patterns helps prevent repeated engineering failures.

---

# Anti-Pattern Categories

Anti-patterns are grouped into logical engineering categories.

## Architectural Anti-Patterns

Examples include:

- Monolithic agent design.
- Circular dependencies.
- Excessive orchestration.
- Tight coupling.
- Unclear responsibility boundaries.

---

## Component Anti-Patterns

Examples include:

- God components.
- Duplicate functionality.
- Hidden dependencies.
- Overloaded components.
- Poor interface design.

---

## Workflow Anti-Patterns

Examples include:

- Infinite execution loops.
- Missing validation stages.
- Hard-coded workflow logic.
- Excessive branching.
- Uncontrolled recursion.

---

## Prompt Anti-Patterns

Examples include:

- Ambiguous prompts.
- Conflicting instructions.
- Excessively long prompts.
- Missing output constraints.
- Inconsistent prompt structure.

---

## Memory Anti-Patterns

Examples include:

- Unlimited memory growth.
- Stale context retention.
- Duplicate knowledge storage.
- Missing memory lifecycle.
- Poor retrieval strategies.

---

## Operational Anti-Patterns

Examples include:

- No observability.
- Manual deployment only.
- Missing rollback strategy.
- Weak access control.
- Ignored validation failures.

---

# Anti-Pattern Lifecycle

Every anti-pattern follows a standardized lifecycle.

```text
Identify Poor Practice
│
▼
Analyze Root Cause
│
▼
Assess Engineering Impact
│
▼
Recommend Better Practice
│
▼
Update Engineering Guidance
│
▼
Prevent Future Occurrence
```

The lifecycle supports continuous engineering improvement.

---

# Detection

Anti-pattern detection should consider:

- Architecture reviews.
- Component analysis.
- Workflow validation.
- Prompt evaluation.
- Code reviews.
- Test failures.
- Performance degradation.
- Operational incidents.

Early detection reduces engineering risk and technical debt.

---

# Prevention

Anti-patterns can be prevented through:

- Engineering standards.
- Architecture reviews.
- Validation gates.
- Automated quality checks.
- Design reviews.
- Governance controls.
- Developer education.
- Continuous feedback.

Prevention is more effective than correction after implementation.

---

# Integration with DAEP

The Anti-Patterns knowledge domain supports:

- Architecture Engineering Engine.
- Component Engineering Engine.
- Workflow Engineering Engine.
- Prompt Engineering Engine.
- Evaluation Engineering Engine.
- Generation Orchestration Engine.

These platform elements use anti-pattern knowledge to detect poor engineering decisions and recommend compliant alternatives.

---

# Best Practices

When documenting anti-patterns:

- Clearly describe the problem.
- Explain why it is harmful.
- Provide observable symptoms.
- Document root causes.
- Recommend preferred alternatives.
- Link to related best practices.
- Keep examples technology-independent.
- Update guidance as new anti-patterns emerge.

---

# Common Anti-Pattern Examples

Examples include:

- Single component performing multiple responsibilities.
- Workflow without validation stages.
- Prompt containing conflicting instructions.
- Memory with no retention policy.
- Hard-coded tool selection.
- Missing error handling.
- Direct component-to-component dependencies.
- Unvalidated AI-generated outputs.
- Deployment without rollback capability.
- Lack of operational monitoring.

These examples illustrate recurring engineering problems rather than implementation-specific defects.

---

# Related Knowledge Domains

The Anti-Patterns knowledge domain works closely with:

- Architectures.
- Components.
- Workflows.
- Testing.
- Validation.
- Security.
- Governance.
- Decision Rules.
- Examples.
- Observability.

---

# Summary

The Anti-Patterns knowledge domain defines the engineering practices, architectural mistakes, workflow issues, and operational pitfalls that should be avoided throughout the DAEP lifecycle.

By documenting common engineering failures, their causes, impacts, detection methods, and preferred alternatives, this knowledge base enables Engineering Engines and developers to proactively avoid poor design decisions, reduce technical debt, and consistently produce reliable, maintainable, secure, and enterprise-ready Deep Agent solutions.
