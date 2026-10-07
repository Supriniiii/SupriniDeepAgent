# Engineering Engines — Design

## Overview

The Engineering Engines are designed as a family of stateless, contract-driven modules following a uniform execution pattern. Each engine implements the same abstract interface but applies domain-specific reasoning, knowledge, and validation to produce specialized engineering artifacts. The design emphasizes composability, replaceability, and testability.

## Architecture

The engines are organized as a flat collection of peer modules, each registered with the GOE through their `engine-contract.yaml` declaration. The GOE invokes them in sequence; engines themselves have no awareness of pipeline position or peer engines. Knowledge is injected through a Knowledge Loader that resolves the engine's declared knowledge dependencies before invocation.

## Key Design Decisions

### DD-1: Contract-First Engine Design
- **Context:** Multiple engines must work together through the GOE without tight coupling, and new engines must be addable without modifying existing ones.
- **Decision:** Each engine declares a YAML contract (`engine-contract.yaml`) specifying inputs, outputs, knowledge dependencies, validation rules, and execution constraints. The GOE uses this contract for invocation, validation, and orchestration.
- **Consequences:** Engines are fully decoupled; contracts serve as documentation and runtime validation; contract drift must be detected via CI checks.

### DD-2: Stateless Engine Execution
- **Context:** Engines must be independently testable and their outputs must be reproducible given the same inputs.
- **Decision:** Engines are stateless functions: they receive all required context through inputs (including knowledge), perform analysis, and return artifacts. No engine maintains internal state between invocations.
- **Consequences:** Simple testing model; no state synchronization issues; but large context windows may be needed for complex inputs.

### DD-3: Knowledge Injection Pattern
- **Context:** Engines need access to DAEP knowledge (steering files, catalogs, templates) but should not be responsible for locating and loading that knowledge.
- **Decision:** A Knowledge Loader component resolves each engine's declared knowledge dependencies and injects the resolved knowledge as part of the engine's input context.
- **Consequences:** Engines remain decoupled from knowledge storage; knowledge resolution can be cached and optimized centrally; knowledge availability failures are detected early.

## Components and Interfaces

### Components

- **Engine Framework** — Base interface, contract loader, input/output validation, lifecycle methods
- **Requirements Engine** — Extracts and structures functional/non-functional requirements
- **Architecture Engine** — Selects patterns, produces architecture decisions and diagrams
- **Capability Engine** — Discovers reusable capabilities in the existing codebase
- **Component Engine** — Selects or designs components satisfying requirements
- **Harness Engine** — Selects the appropriate runtime harness for the agent
- **Workflow Engine** — Designs execution flows, branching, error paths
- **Memory Engine** — Selects and configures memory strategies
- **Prompt Engine** — Designs modular, versioned prompt templates
- **Validation Engine** — Defines validation rules and quality gates
- **Evaluation Engine** — Evaluates generated output against quality criteria
- **Knowledge Loader** — Resolves and injects knowledge dependencies
- **Contract Validator** — Validates engine inputs/outputs against declared contracts

### Interfaces

- **EngineContract Interface:** `execute(input: EngineInput): EngineOutput` — uniform invocation interface
- **Knowledge Interface:** `loadKnowledge(dependencies: string[]): KnowledgeContext` — knowledge resolution
- **Validation Interface:** `validate(output: EngineOutput, contract: Contract): ValidationResult` — output validation
- **Registration Interface:** `register(contract: EngineContractYAML): void` — engine registration with GOE

## Data Models

```yaml
EngineContractYAML:
  engineId: string
  version: string
  inputs:
    required: FieldDefinition[]
    optional: FieldDefinition[]
  outputs:
    schema: JSONSchema
  knowledgeDependencies: string[]
  validationRules: ValidationRule[]
  executionConstraints:
    timeout: number (ms)
    maxTokens: number
    temperature: number

EngineInput:
  requestContext: object (original generation request)
  upstreamArtifacts: Artifact[]
  knowledgeContext: KnowledgeContext
  config: EngineConfig

EngineOutput:
  engineId: string
  artifacts: Artifact[]
  rationale: string
  knowledgeCitations: Citation[]
  validationScore: number
  metadata: object

KnowledgeContext:
  sources: KnowledgeSource[]
  resolvedAt: timestamp
  cacheHit: boolean

ValidationResult:
  valid: boolean
  violations: FieldViolation[]
  score: number
```

## Data Flow

1. GOE passes `EngineInput` (upstream artifacts + request context) to Engine
2. Knowledge Loader resolves and attaches knowledge dependencies
3. Engine performs domain-specific analysis using input + knowledge
4. Engine produces `EngineOutput` (artifacts + metadata + rationale)
5. Contract Validator checks output against declared contract
6. Validated output returned to GOE for artifact storage

## Error Handling

- **Knowledge Loading Failure:** Engine reports missing knowledge; GOE applies fallback or aborts
- **Contract Violation (Input):** Engine refuses to execute; reports specific missing/invalid fields
- **Contract Violation (Output):** Output is rejected; engine may retry with adjusted parameters
- **Execution Timeout:** Engine is terminated; GOE applies timeout recovery strategy
- **Quality Gate Failure:** Output below minimum quality is rejected with improvement suggestions

## Correctness Properties

### Property 1: Contract Conformance
Every engine output passes validation against its declared contract schema before being stored as an artifact.

### Property 2: Statelessness
An engine invoked twice with identical inputs and knowledge context produces structurally equivalent outputs (modulo LLM temperature variance).

### Property 3: Knowledge Completeness
An engine never executes if any of its declared knowledge dependencies fail to resolve.

### Property 4: Isolation
No engine reads or writes shared mutable state; all data flows through the input/output contract.

### Property 5: Quality Floor
No artifact with a validation score below the configured minimum threshold is emitted to the GOE artifact store.

## Testing Strategy

- **Unit Tests:** Test each engine in isolation with mocked inputs and knowledge, verifying artifact output structure and contract compliance.
- **Contract Validation Tests:** Feed malformed inputs and outputs to the Contract Validator, verifying field-level violation reporting.
- **Knowledge Loader Tests:** Test knowledge resolution with present, missing, and partially available knowledge sources.
- **Integration Tests:** Run the full engine pipeline with stub GOE, verifying correct sequencing and artifact passing between engines.
- **Determinism Tests:** Invoke engines multiple times with identical inputs (temperature=0) and verify output consistency.
- **Performance Tests:** Measure engine execution time against the 30-second threshold for standard complexity inputs.

## Extension Points

- New engines added via contract declaration (no core code changes)
- Custom knowledge sources registered through the Knowledge Loader
- Alternative validation rule sets per engine
- Engine-specific configuration overrides
- Custom output formatters per artifact type
