---
inclusion: always
---

# Generation Workflow

Follow this sequence for every generation request. Do not skip steps. Each phase must produce an explicit output or decision before proceeding to the next.

## Phase 1: Receive Request

- Capture the user's intent, constraints, and success criteria.
- Identify ambiguities and resolve them before continuing.
- Determine scope: new capability, modification, or extension.

## Phase 2: Requirement Engineering

- Extract functional and non-functional requirements.
- Define acceptance criteria for each requirement.
- Identify dependencies on existing components or external systems.
- Confirm requirements with the user before proceeding.

## Phase 3: Architecture Decision

- Select the appropriate architectural pattern (e.g., planner-executor, pipeline, event-driven).
- Justify the choice against the requirements.
- Document key trade-offs and constraints.
- Reference the `02_architecture.md` steering document for project conventions.

## Phase 4: Capability Discovery

- Search the existing codebase for reusable capabilities.
- Identify available MCP servers, adapters, and enterprise integrations.
- List what exists versus what must be built.
- Reference the `06_tools.md` steering document for tool integration guidance.

## Phase 5: Component Selection

- Choose existing components that satisfy requirements.
- For new components, define responsibility, interface, and boundaries.
- Avoid duplicating functionality already present in the project.
- Reference the `03_components.md` steering document.

## Phase 6: Harness Selection

- Select the execution harness or runtime framework.
- Ensure compatibility with chosen architecture and components.
- Reference the `04_harness.md` steering document.

## Phase 7: Workflow Design

- Define the execution flow, branching logic, and error paths.
- Specify input/output contracts between steps.
- Include retry, fallback, and timeout strategies where applicable.

## Phase 8: Memory Strategy

- Determine which memory types are needed (working, conversation, semantic, long-term, checkpoint, artifact).
- Only add memory when a business requirement justifies it.
- Reference the `05_memory.md` steering document.

## Phase 9: Prompt Strategy

- Design prompts as modular, versioned, and reusable artifacts.
- Keep prompts external to implementation code.
- Document each prompt's purpose, inputs, and expected outputs.
- Reference the `07_prompts.md` steering document.

## Phase 10: Implementation Plan

- Produce a step-by-step build plan with clear ordering.
- Identify parallelizable tasks.
- Define verification checkpoints between major steps.

## Phase 11: Generate Code

- Implement according to the plan.
- Follow project code style and conventions.
- Include structured logging, error handling, and health checks.
- Externalize all secrets and configuration.
- Reference the `08_code_generation.md` steering document.

## Phase 12: Generate Tests

- Write unit tests covering core logic.
- Write integration tests covering component interactions.
- Include property-based tests where correctness properties are defined.
- Reference the `09_testing.md` steering document.

## Phase 13: Generate Documentation

- Document public interfaces, configuration, and usage.
- Include architecture decision records where relevant.
- Reference the `10_documentation.md` steering document.

## Phase 14: Generate Deployment

- Produce deployment configuration (infrastructure-as-code, manifests, scripts).
- Include environment-specific overrides.
- Reference the `11_deployment.md` steering document.

## Phase 15: Run Validation

- Verify all tests pass.
- Confirm security requirements are met (no hardcoded secrets, least privilege applied).
- Check observability is in place (logging, metrics, tracing).
- Validate documentation completeness.
- Reference the `13_validation.md` and `14_quality.md` steering documents.

## Phase 16: Production Package

- Bundle all artifacts: code, tests, docs, deployment config.
- Confirm the package is deployable and self-contained.
- Generation is not complete until validation succeeds.

## Rules

- Never skip a phase. If a phase is not applicable, explicitly state why and move on.
- Each phase must produce a visible output (decision, artifact, or confirmation).
- If blockers are encountered, surface them immediately rather than proceeding with assumptions.
- Refer to numbered steering documents (`00_platform.md` through `15_examples.md`) for domain-specific guidance at each phase.
