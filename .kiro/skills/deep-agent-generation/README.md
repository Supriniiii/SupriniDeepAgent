# Deep Agent Generation

## Purpose
The master orchestration skill that drives the entire Deep Agent Engineering Platform pipeline. It transforms developer business requests into production-ready Deep Agent solutions by invoking all Engineering Engines in sequence, enforcing engineering-before-implementation discipline, and producing complete, validated, deployable artifacts.

## Responsibilities
- Receive and interpret developer requests, resolving ambiguities before proceeding
- Orchestrate the full 15-phase generation workflow from intake to production package
- Invoke all Engineering Engines in correct sequence with proper inputs
- Trigger all lifecycle Hooks at appropriate phases
- Coordinate sub-skills (architecture, component, workflow, prompt, memory engineering)
- Enforce engineering-before-implementation discipline across all phases
- Produce complete, validated, production-ready Deep Agent solutions
- Generate comprehensive documentation, tests, and deployment artifacts

## Inputs
- Developer business request (natural language description of desired capability)
- Constraints and non-functional requirements (performance, security, compliance)
- Existing project context (current architecture, available components, registry state)
- Target deployment environment (cloud provider, infrastructure, runtime)
- Success criteria and acceptance conditions

## Outputs
- Complete Deep Agent solution package (code, config, prompts, workflows)
- Architecture documentation (architecture.md, ADRs, diagrams)
- Test suites (unit, integration, workflow, prompt evaluation, security)
- Deployment package (Dockerfile, manifests, CI/CD pipelines)
- Validation report with quality scores and production-readiness assessment

## Dependencies
- Engineering Engines: All (Architecture, Component, Workflow, Memory, Prompt, Harness, Validation)
- Knowledge Domains: knowledge/architectures/, knowledge/components/, knowledge/workflows/, knowledge/memory/, knowledge/prompts/, knowledge/harnesses/
- Templates: All generation templates (agent, harness, component, workflow, prompt, deployment, documentation)
- Sub-Skills: architecture-engineering, component-engineering, workflow-engineering, prompt-engineering, memory-engineering

## Integration
- DAEP Orchestration Layer (primary entry point)
- Engineering Engine Bus (invokes all engines)
- Hook System (triggers all lifecycle hooks)
- Component Registry (capability discovery)
- Knowledge Base (domain knowledge retrieval)
- Template Engine (artifact generation)
- Validation Engine (quality gates)

## Usage
Invoke this skill when a developer submits a request for a new Deep Agent, multi-agent system, or significant capability extension. The skill automatically orchestrates all sub-skills and engines.

```
Developer Request → deep-agent-generation skill activates
  → Phase 1-15 execute in sequence
  → Sub-skills invoked at appropriate phases
  → All engines engaged
  → Production package delivered
```

## Best Practices
- Never skip phases — if a phase is not applicable, document why and proceed
- Always resolve ambiguities in Phase 1 before advancing
- Validate outputs at each phase boundary before proceeding
- Reuse existing components discovered during capability discovery
- Generate documentation alongside implementation, not after
- Run validation as a final gate — generation is incomplete until validation passes

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Triggers Hooks
- Produces deterministic outputs
