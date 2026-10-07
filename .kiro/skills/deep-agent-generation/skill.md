# Deep Agent Generation

## Skill Definition

```yaml
name: deep-agent-generation
description: Master orchestration skill that drives the entire DAEP pipeline from developer request to production-ready Deep Agent
version: 1.0.0
category: master
trigger: Developer submits a request to generate a new Deep Agent, multi-agent system, or major capability
```

## Required Inputs
- Developer Request: Natural language description of the business capability or agent to build
- Target Environment: Deployment target (cloud, on-premise, hybrid) and runtime constraints
- Success Criteria: Measurable conditions that define when the solution is complete and correct

## Optional Inputs
- Existing Architecture Context: Current system architecture if extending an existing solution
- Priority Constraints: Time, cost, or resource limitations
- Compliance Requirements: Regulatory or organizational policies to enforce
- Preferred Patterns: Developer-specified architectural preferences
- Integration Targets: External systems the agent must connect to

## Workflow

### Step 1: Request Intake & Clarification
Capture the developer's intent, identify ambiguities, resolve unknowns, and confirm scope.
- Engine: Requirements Engineering Engine
- Knowledge: knowledge/requirements/, knowledge/domain-models/
- Output: Clarified request document with confirmed scope

### Step 2: Requirements Engineering
Extract functional and non-functional requirements, define acceptance criteria, identify dependencies.
- Engine: Requirements Engineering Engine
- Knowledge: knowledge/requirements/, knowledge/constraints/
- Output: requirements.md with acceptance criteria

### Step 3: Architecture Design
Select architectural pattern, justify against requirements, document trade-offs, produce architecture artifacts.
- Engine: Architecture Engineering Engine
- Knowledge: knowledge/architectures/, knowledge/patterns/
- Output: architecture.md, ADRs, architecture diagram

### Step 4: Capability Discovery
Search existing codebase and registries for reusable capabilities, MCP servers, and enterprise integrations.
- Engine: Component Engineering Engine
- Knowledge: knowledge/components/, knowledge/registries/
- Output: Capability inventory (exists vs. must-build)

### Step 5: Component Selection & Design
Select existing components, define new component boundaries, interfaces, and responsibilities.
- Engine: Component Engineering Engine
- Knowledge: knowledge/components/, knowledge/interfaces/
- Output: component-plan.md, interface definitions

### Step 6: Harness Selection
Select execution harness matching architecture and component requirements.
- Engine: Harness Engineering Engine
- Knowledge: knowledge/harnesses/, knowledge/runtimes/
- Output: harness-specification.md

### Step 7: Workflow Design
Define execution flow, states, transitions, decision points, error handling, and recovery paths.
- Engine: Workflow Engineering Engine
- Knowledge: knowledge/workflows/, knowledge/state-machines/
- Output: workflow-specification.md, state machine definition

### Step 8: Memory Strategy
Determine required memory types, retrieval patterns, persistence strategy, and governance rules.
- Engine: Memory Engineering Engine
- Knowledge: knowledge/memory/, knowledge/persistence/
- Output: memory-strategy.md

### Step 9: Prompt Strategy
Design modular, versioned prompts for planning, execution, reflection, and evaluation.
- Engine: Prompt Engineering Engine
- Knowledge: knowledge/prompts/, knowledge/models/
- Output: prompt-package.md, prompt catalog

### Step 10: Implementation Planning
Produce step-by-step build plan with ordering, parallelization opportunities, and verification checkpoints.
- Engine: Generation Planning Engine
- Knowledge: knowledge/implementation/, knowledge/patterns/
- Output: implementation-plan.md

### Step 11: Code Generation
Generate implementation following the plan, architecture, and project conventions.
- Engine: Code Generation Engine
- Knowledge: knowledge/code-standards/, knowledge/frameworks/
- Output: Source code, configuration files

### Step 12: Test Generation
Generate comprehensive test suites covering all layers and quality dimensions.
- Engine: Test Generation Engine
- Knowledge: knowledge/testing/, knowledge/evaluation/
- Output: Test suites (unit, integration, workflow, prompt eval, security)

### Step 13: Documentation Generation
Generate complete documentation package including README, architecture docs, guides, and catalogs.
- Engine: Documentation Engine
- Knowledge: knowledge/documentation/, knowledge/templates/
- Output: Documentation package

### Step 14: Deployment Generation
Generate deployment configuration, infrastructure code, and CI/CD pipelines.
- Engine: Deployment Engine
- Knowledge: knowledge/deployment/, knowledge/infrastructure/
- Output: Deployment package (Dockerfile, manifests, pipelines)

### Step 15: Validation & Quality Gate
Run full validation across all dimensions, produce quality score, determine production readiness.
- Engine: Validation Engine
- Knowledge: knowledge/validation/, knowledge/quality/
- Output: validation-report.md, quality scores, production-readiness decision

## Engineering Rules
- Never generate implementation before completing architecture and design phases
- Always resolve ambiguities before advancing past Phase 1
- Reuse existing components — never duplicate functionality available in registries
- Every phase must produce an explicit, documented output
- Validation must pass before generation is considered complete
- All secrets must be externalized; no hardcoded credentials permitted

## Knowledge Sources
- knowledge/architectures/ — architectural patterns and reference architectures
- knowledge/components/ — component catalog and reuse registry
- knowledge/workflows/ — workflow patterns and state machines
- knowledge/memory/ — memory strategies and implementations
- knowledge/prompts/ — prompt patterns, templates, and evaluation criteria
- knowledge/harnesses/ — agent harness specifications and configurations
- knowledge/requirements/ — requirements engineering patterns
- knowledge/validation/ — validation criteria and quality standards

## Templates Used
- templates/agent/ — Deep Agent generation templates
- templates/harness/ — Agent Harness templates
- templates/component/ — Component scaffolding templates
- templates/workflow/ — Workflow definition templates
- templates/prompt/ — Prompt package templates
- templates/deployment/ — Deployment artifact templates
- templates/documentation/ — Documentation structure templates
- templates/testing/ — Test suite templates

## Engineering Engines Invoked
- Requirements Engineering Engine
- Architecture Engineering Engine
- Component Engineering Engine
- Harness Engineering Engine
- Workflow Engineering Engine
- Memory Engineering Engine
- Prompt Engineering Engine
- Code Generation Engine
- Test Generation Engine
- Documentation Engine
- Deployment Engine
- Validation Engine

## Hooks Invoked
- pre-generation — fires before pipeline begins
- post-requirements — fires after requirements confirmed
- post-architecture — fires after architecture designed
- post-component-selection — fires after components selected
- post-harness-selection — fires after harness chosen
- post-workflow-design — fires after workflow defined
- post-memory-design — fires after memory strategy set
- post-prompt-design — fires after prompts designed
- pre-implementation — fires before code generation begins
- post-implementation — fires after code generated
- post-testing — fires after tests generated
- post-documentation — fires after docs generated
- post-deployment — fires after deployment artifacts generated
- pre-validation — fires before final validation
- post-validation — fires after validation complete
- post-generation — fires when entire pipeline completes

## Validation
- All 15 phases produced documented outputs
- Architecture pattern justified against requirements
- No duplicated components — reuse maximized
- All tests pass (unit, integration, workflow, prompt eval)
- Security review passed (no hardcoded secrets, least privilege enforced)
- Documentation complete (README, architecture, ADRs, guides)
- Deployment artifacts present and valid
- Quality score meets threshold (≥87%)
- Production-readiness assessment: YES

## Expected Outputs
- Complete Deep Agent source code
- Agent Harness configuration
- Component implementations and interfaces
- Workflow definitions and state machines
- Memory configuration and persistence setup
- Prompt package (system, planning, reflection, evaluation prompts)
- Test suites (all categories)
- Documentation package
- Deployment package
- Validation report with quality scores

## Completion Criteria
- All 15 phases executed successfully with documented outputs
- Validation Engine reports production-ready status
- Quality score meets or exceeds 87% threshold
- All generated tests pass
- No unresolved ambiguities or missing requirements
- Developer confirms acceptance criteria are met
