# Runtime Harness — Design

## Overview

The Runtime Harness is designed as a framework with a common base and specialized implementations for each execution pattern. The framework provides lifecycle management, state management, tool coordination, checkpointing, and observability as shared infrastructure, while each harness variant (Coding, Research, Workflow, Enterprise, Distributed) extends the base with pattern-specific behaviors.

## Architecture

The harness sits between the agent logic and the platform infrastructure. It provides a uniform execution contract to agents while abstracting platform concerns (tool access, persistence, observability). The Harness Engine (from Engineering Engines) selects the appropriate harness at design time; the GOE instantiates and manages the harness at runtime.

## Key Design Decisions

### DD-1: Framework + Specialization Pattern
- **Context:** Five distinct execution patterns exist, each with unique requirements (Coding needs file system access, Research needs web search, Enterprise needs approval workflows, Distributed needs coordination), but they share common infrastructure needs.
- **Decision:** Implement a common Harness Framework providing lifecycle, state, tools, checkpointing, and observability, with each harness type extending the framework with pattern-specific capabilities.
- **Consequences:** Shared infrastructure code is maintained once; new harness types inherit full capability; but framework changes may impact all harness types.

### DD-2: Checkpoint-Based Durability
- **Context:** Long-running agent executions may fail at any point; re-executing from scratch is expensive and may produce different results.
- **Decision:** Implement automatic checkpointing after each significant execution step, storing the full execution state to filesystem. Recovery loads the latest valid checkpoint and resumes.
- **Consequences:** Execution is durable; recovery is fast; but checkpoint storage grows over time and must be managed (TTL, cleanup policies).

### DD-3: Tool Coordinator as Intermediary
- **Context:** Agents need access to tools (MCP servers, file system, APIs) but direct access creates security risks, makes testing difficult, and prevents usage tracking.
- **Decision:** All tool access flows through the Tool Coordinator which handles discovery, access control, rate limiting, timeout enforcement, and usage metrics.
- **Consequences:** Centralized security enforcement; full tool usage observability; but adds latency to tool calls (minimal, <5ms overhead).

## Components and Interfaces

### Components

- **Harness Framework** — Base class with lifecycle methods, state access, tool coordination, checkpointing
- **Coding Harness** — Extends framework with file system access, code execution, test runner integration
- **Research Harness** — Extends framework with web search, document retrieval, knowledge synthesis
- **Workflow Harness** — Extends framework with step orchestration, branching logic, approval gates
- **Enterprise Harness** — Extends framework with compliance checks, audit logging, approval workflows, SSO integration
- **Distributed Harness** — Extends framework with multi-agent coordination, message passing, consensus
- **Tool Coordinator** — Discovers, registers, and governs tool access
- **State Store** — Manages execution state with transactional guarantees
- **Checkpoint Manager** — Creates, stores, validates, and restores execution checkpoints
- **Metrics Emitter** — Emits structured metrics for observability

### Interfaces

- **Agent Interface:** `HarnessContext` provided to agents with methods for state access, tool invocation, memory management
- **Lifecycle Interface:** `initialize()`, `execute()`, `suspend()`, `resume()`, `terminate()`
- **Tool Interface:** `invokeTool(name, params): ToolResult` — governed tool access
- **State Interface:** `getState(key)`, `setState(key, value)`, `getFullState()` — state management
- **Checkpoint Interface:** `checkpoint()`, `restore(checkpointId)`, `listCheckpoints()` — durability

## Data Models

```yaml
HarnessContext:
  sessionId: string
  harnessType: enum (coding | research | workflow | enterprise | distributed)
  state: StateStore
  tools: ToolCoordinator
  checkpoints: CheckpointManager
  metrics: MetricsEmitter
  config: HarnessConfig

Checkpoint:
  id: string (UUID)
  sessionId: string
  sequenceNumber: number
  state: object (serialized execution state)
  checksum: string
  createdAt: timestamp
  expiresAt: timestamp

ToolInvocation:
  toolName: string
  params: object
  callerSession: string
  timeout: number (ms)
  result: ToolResult | null
  startTime: timestamp
  endTime: timestamp | null
  status: enum (pending | success | failed | timeout)

ToolResult:
  success: boolean
  data: object | null
  error: string | null
  duration: number (ms)

HarnessConfig:
  harnessType: string
  checkpointInterval: number (steps)
  checkpointRetention: number (count)
  toolTimeout: number (ms)
  toolRateLimit: number (calls/min)
  maxConcurrentTools: number
  observability: ObservabilityConfig
```

## Data Flow

1. GOE requests harness instantiation with agent configuration
2. Harness Framework initializes (loads config, discovers tools, creates state store)
3. Specialized harness adds pattern-specific capabilities
4. Agent executes within harness context (accesses tools via coordinator, state via store)
5. Checkpoint Manager captures state at configured intervals
6. Metrics Emitter streams observability data to configured sinks
7. On completion/failure, harness performs cleanup and returns results to GOE

## Error Handling

- **Agent Execution Failure:** State is checkpointed, error context captured, recovery attempted from last checkpoint
- **Tool Invocation Failure:** Retried with backoff if transient; logged and surfaced to agent if permanent
- **State Corruption:** Detected via integrity checks; recovered from nearest valid checkpoint
- **Resource Exhaustion:** Token limits, time limits, and memory limits enforced; graceful degradation on breach
- **Harness Framework Failure:** Critical error logged; session terminated; state preserved for post-mortem

## Correctness Properties

### Property 1: Lifecycle State Machine
Harness transitions follow a strict state machine: initialized → executing → (suspended ↔ executing) → terminated. No invalid transitions are possible.

### Property 2: State Isolation
State operations within one session are invisible to all other sessions, even under concurrent execution.

### Property 3: Checkpoint Consistency
A restored checkpoint produces an agent state identical to the state at checkpoint creation time (byte-level checksum match).

### Property 4: Tool Access Control
No tool invocation bypasses the Tool Coordinator; all invocations are subject to access policy evaluation.

### Property 5: Resource Bounding
No single agent execution can exceed configured resource limits (tokens, time, memory) without triggering graceful degradation.

### Property 6: Cleanup Guarantee
On termination (success or failure), all acquired resources (file handles, connections, locks) are released.

## Testing Strategy

- **Unit Tests:** Test Harness Framework lifecycle, State Store operations, Tool Coordinator access policies, and Checkpoint Manager integrity.
- **Integration Tests:** Run a complete agent execution within each harness type, verifying lifecycle transitions, tool access, and state persistence.
- **Checkpoint Recovery Tests:** Create checkpoints at various execution points, simulate failures, and verify recovery produces correct state.
- **Concurrency Tests:** Run 5 concurrent agent sessions and verify state isolation, resource limits, and no cross-contamination.
- **Tool Coordinator Tests:** Verify rate limiting, timeout enforcement, access control, and usage metric accuracy.
- **Harness Specialization Tests:** Test each harness variant's unique capabilities (file access for Coding, search for Research, etc.) in isolation.

## Extension Points

- New harness types via framework extension
- Custom tool providers registered through Tool Coordinator
- Alternative state backends (in-memory, database, cloud)
- Custom checkpoint strategies (frequency, retention, compression)
- Pluggable metrics sinks (console, file, external systems)
- Custom lifecycle hooks for enterprise integration
