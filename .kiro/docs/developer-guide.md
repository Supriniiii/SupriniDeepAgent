# Developer Guide

## Purpose

The Developer Guide provides instructions for developers using the Deep Agent Engineering Platform (DAEP).

It explains how to use the Kiro Skill to engineer Deep Agents, understand the engineering process, extend generated solutions, and interpret the engineering artifacts produced during generation.

This guide is intended for developers consuming the platform rather than contributing to its implementation.

---

# Getting Started

## Prerequisites

Before using the Deep Agent Engineering Platform, ensure you have:

- Kiro IDE installed
- Access to the DAEP Skill
- Access to an approved Large Language Model (LLM)
- Required credentials and API keys
- Access to the project repository

---

# Repository Structure

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

Each directory has a specific engineering responsibility.

Developers should become familiar with the repository before extending the platform.

---

# Creating a Deep Agent

The primary purpose of the platform is to generate enterprise-grade Deep Agents.

A typical request might be:

- Build a Code Review Agent
- Build a Security Analysis Agent
- Build a Documentation Agent
- Build a Customer Support Agent
- Build a Multi-Agent Research Assistant

The developer provides the request, and the platform performs the engineering process automatically.

---

# Engineering Process

Every request follows the same engineering lifecycle.

```text
Developer Request
│
▼
Generation Orchestration Engine
│
▼
Engineering Pipeline
│
▼
Generated Deep Agent
```

Developers are not required to invoke individual Engineering Engines manually.

The Generation Orchestration Engine manages the complete lifecycle.

---

# Understanding the Engineering Pipeline

Each generated Deep Agent passes through the following Engineering Engines:

1. Requirements Engineering
2. Architecture Engineering
3. Capability Engineering
4. Component Engineering
5. Harness Engineering
6. Workflow Engineering
7. Memory Engineering
8. Prompt Engineering
9. Validation Engineering
10. Evaluation Engineering

Each stage produces engineering artifacts that become inputs for subsequent stages.

---

# Generated Outputs

The platform may generate:

- Source code
- Engineering documentation
- Prompt packages
- Configuration files
- Deployment assets
- Test assets
- Validation reports
- Evaluation reports
- Engineering metrics

Generated outputs are stored in the `outputs/` directory unless otherwise configured.

---

# Engineering Artifacts

Throughout the generation process, the platform creates engineering artifacts.

Examples include:

- requirements.md
- architecture.md
- capability-plan.md
- component-plan.md
- harness-specification.md
- workflow-specification.md
- memory-strategy.md
- prompt-package.md
- validation-report.md
- evaluation-report.md

These artifacts provide complete engineering traceability.

---

# Steering

The Steering directory defines global engineering guidance.

The platform loads the following steering documents before generation begins:

- product.md
- structure.md
- tech.md

Developers should update these documents when organizational engineering standards change.

---

# Hooks

Hooks coordinate the engineering process.

Developers generally do not modify Hooks unless extending the platform.

Each Hook invokes one or more Engineering Engines through the Generation Orchestration Engine.

---

# Engineering Engines

Engineering Engines perform specialized engineering analysis.

Developers should avoid bypassing Engineering Engines, as doing so may reduce consistency and traceability.

Each engine has a dedicated README and contract describing its responsibilities.

---

# Knowledge

The Knowledge directory contains reusable engineering knowledge.

Examples include:

- Architectural patterns
- Workflow patterns
- Prompt patterns
- Best practices
- Organizational standards

Developers should extend the Knowledge repository rather than duplicating engineering logic.

---

# Registries

Registries provide reusable engineering assets.

Examples include:

- Components
- Capabilities
- Prompts
- Harnesses
- Workflows

Whenever possible, developers should reuse registered assets before creating new ones.

---

# Templates

Templates define reusable blueprints used during generation.

Examples include:

- Agent templates
- Workflow templates
- Prompt templates
- Documentation templates

Templates promote consistency across generated solutions.

---

# Outputs

The Outputs directory contains the final engineering deliverables produced by the platform.

Depending on the requested solution, outputs may include:

- Source code
- Documentation
- Configuration
- Reports
- Deployment assets

---

# Troubleshooting

Common issues include:

## Incomplete Developer Request

Ensure the request clearly describes the desired Deep Agent.

---

## Missing Knowledge

If required engineering knowledge is unavailable, extend the Knowledge repository before regeneration.

---

## Missing Templates

Ensure appropriate templates exist for the requested solution.

---

## Validation Failures

Review the generated Validation Report to identify missing engineering requirements.

---

## Evaluation Recommendations

Review the Evaluation Report for suggested improvements to the generated solution.

---

# Best Practices

Developers should:

- Provide clear engineering requirements.
- Reuse existing knowledge where possible.
- Reuse templates before creating new ones.
- Avoid bypassing the engineering pipeline.
- Review validation and evaluation reports.
- Keep steering documents up to date.
- Maintain engineering artifacts for traceability.

---

# Additional Documentation

For more information, refer to:

- README.md
- architecture.md
- generation-orchestration-engine.md
- contribution-guide.md

These documents provide additional guidance on the platform architecture, engineering lifecycle, and contribution process.

---

# Conclusion

The Deep Agent Engineering Platform enables developers to engineer production-ready Deep Agents through a structured, reusable, and traceable engineering process.

By following this guide and leveraging the platform's Engineering Engines, Knowledge Base, Registries, Templates, and Generation Orchestration Engine, developers can consistently produce high-quality Deep Agent solutions while adhering to organizational engineering standards.
