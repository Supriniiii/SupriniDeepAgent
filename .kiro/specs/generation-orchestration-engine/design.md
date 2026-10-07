# Generation Orchestration Engine — Design

## Overview

The GOE is designed as a Pipeline/Orchestrator architecture that coordinates the sequential execution of engineering phases. It acts as the central nervous system of DAEP, managing the flow of control and data through specialized engines while providing durability, observability, and extensibility.

## Architecture

The GOE sits at the center of the DAEP architecture, receiving generation requests from the Developer CLI, coordinating all Engineering Engines, managing artifacts through the Output Generation system, and enforcing quality through the Validation Framework. It operates as a stateful pipeline orchestrator with hook-based extensibility.

## Key Design Decisions

### DD-1: Pipeline Orchestrator Pattern
- **Context:** The generation lifecycle is inherently sequential (requirements → architecture → components → harness → implementation → validation), requiring ordered execution with data flow between phases.
- **Decision:** Adopt a Pipeline Orchestrator pattern where the GOE defines the phase sequence, manages transitions, and passes artifacts forward through the pipeline.
- **Consequences:** Simple mental model, easy to debug and trace, but limits parallelism to within-phase concurrency only.

### DD-2: Hook-Based Extensibility
- **Context:** The orchestration flow must support customization (e.g., enterprise compliance checks, custom logging, approval gates) without modifying core logic.
- **Decision:** Implement a hook system with defined extension points (pre/post phase, pre/post engine, on-error, on-complete) that external logic can register against.
- **Consequences:** Core orchestration remains stable while behavior can be extended; hooks must be carefully ordered and timeout-bounded to prevent pipeline stalls.

### DD-3: File-Based State Persistence
- **Context:** The platform operates within the Kiro workspace model where file-based storage is the natural persistence mechanism.
- **Decision:** Persist session state as structured YAML files within the workspace, enabling resumption, inspection, and version control of generation state.
- **Consequences:** State is human-readable and diffable; concurrent access must be managed through file locking or single-writer guarantees.

## Components and Interfaces

### Components

- **Session Manager** — Creates, tracks, and terminates generation sessions
- **Pipeline Controller** — Defines and executes the phase sequence
- **Hook Runner** — Manages hook registration and invocation at extension points
- **Engine Invoker** — Calls engines per contract, validates inputs/outputs
- **Artifact Manager** — Stores, retrieves, and validates artifacts between phases
- **State Manager** — Persists and recovers pipeline state
- **Failure Handler** — Classifies and responds to failures with appropriate strategies
- **Logger** — Produces structured logs, metrics, and traces

### Interfaces

- **Inbound:** Receives `GenerationRequest` from Developer CLI or programmatic API
- **Engine Interface:** Invokes engines via the standardized `EngineContract` interface
- **Hook Interface:** Calls registered hooks via the `HookContract` interface
- **Artifact Interface:** Reads/writes artifacts via the `ArtifactStore` interface
- **State Interface:** Persists/recovers state via the `StateStore` interface
- **Outbound:** Emits `GenerationResult` containing all produced artifacts and validation reports

## Data Models

```yaml
GenerationRequest:
  sessionId: string (UUID)
  requestType: enum (generate | engineer | validate)
  input: object (user request payload)
  config: object (pipeline configuration overrides)
  createdAt: timestamp

GenerationSession:
  sessionId: string (UUID)
  status: enum (active | paused | completed | failed | cancelled)
  currentPhase: string
  completedPhases: string[]
  pendingPhases: string[]
  artifacts: Map<phaseId, Artifact[]>
  decisionHistory: Decision[]
  startTime: timestamp
  endTime: timestamp | null

Artifact:
  id: string (UUID)
  type: string (artifact schema type)
  producerEngine: string
  phase: string
  checksum: string
  content: object
  metadata: object
  createdAt: timestamp

HookRegistration:
  hookId: string
  extensionPoint: enum (pre-phase | post-phase | pre-engine | post-engine | on-error | on-complete)
  handler: callable
  timeout: number (ms)
  priority: number
  failureMode: enum (skip | abort)

GenerationResult:
  sessionId: string
  status: enum (success | failed | partial)
  artifacts: Artifact[]
  validationReport: ValidationReport
  metrics: PipelineMetrics
```

## Data Flow

1. `GenerationRequest` → Session Manager (creates session)
2. Session → Pipeline Controller (begins phase execution)
3. Phase N → Hook Runner (pre-phase hooks)
4. Phase N → Engine Invoker (calls engine per contract)
5. Engine Output → Artifact Manager (stores artifacts)
6. Artifact Manager → Hook Runner (post-phase hooks)
7. Pipeline Controller → State Manager (persists progress)
8. Repeat for each phase until pipeline completes or fails
9. Pipeline Complete → Hook Runner (on-complete hooks)
10. Final artifacts → `GenerationResult`

## Error Handling

- **Transient Failures:** Retried with exponential backoff (max 3 attempts)
- **Permanent Failures:** Pipeline aborted, state preserved, diagnostic context emitted
- **Hook Failures:** Logged and optionally skipped (configurable per hook)
- **Engine Contract Violations:** Treated as permanent failures with detailed contract mismatch reporting
- **State Corruption:** Detected via checksums, triggers recovery from last known good state

## Correctness Properties

### Property 1: Session Uniqueness
No two active sessions share the same session ID.

### Property 2: Phase Ordering Invariant
A phase N+1 never begins execution before phase N completes successfully or is explicitly skipped.

### Property 3: Artifact Integrity
For any artifact retrieved by a downstream engine, its checksum matches the checksum recorded at creation time.

### Property 4: State Durability
If a phase transition is acknowledged as complete, the state reflecting that completion survives process restart.

### Property 5: Hook Isolation
A hook failure (timeout or exception) never corrupts pipeline state or prevents the failure handler from executing.

### Property 6: Atomic Termination
A session in terminal state (completed, failed, cancelled) cannot transition to any other state.

## Testing Strategy

- **Unit Tests:** Test each component in isolation (Session Manager, Pipeline Controller, Hook Runner, Engine Invoker, Artifact Manager, State Manager, Failure Handler) with mocked dependencies.
- **Integration Tests:** Test the full pipeline flow with stub engines that produce known artifacts, verifying correct phase ordering, artifact passing, and state persistence.
- **Hook Tests:** Verify hook registration, invocation order, timeout enforcement, and error isolation with configurable test hooks.
- **Failure Recovery Tests:** Simulate transient and permanent failures at each phase, verifying retry behavior, abort semantics, and state preservation for resumption.
- **State Persistence Tests:** Kill and restart the pipeline mid-execution, verifying recovery from persisted state and correct resumption.
- **Contract Validation Tests:** Provide malformed engine inputs/outputs and verify contract violation detection and reporting.

## Extension Points

- Pre/Post phase hooks for each pipeline phase
- Custom engine registration for new engineering capabilities
- Custom artifact transformers for format conversion
- Alternative state backends (database, cloud storage)
- Custom failure recovery strategies
- Pipeline phase ordering customization
