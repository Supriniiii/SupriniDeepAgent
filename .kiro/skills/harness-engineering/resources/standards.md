# Harness Engineering Standards

1. **Architecture-First Design**: The harness must be fully designed and validated before any business logic implementation begins. No implementation without a complete harness specification.

2. **Lifecycle Completeness**: Every harness must define all possible states and transitions including initialization, execution, pause, resume, error, recovery, and termination. No undefined state transitions are permitted.

3. **Observability by Default**: All harness implementations must include structured logging, metrics emission, and distributed tracing hooks at every lifecycle transition and checkpoint boundary.

4. **Recovery Determinism**: Recovery mechanisms must produce deterministic outcomes. Given the same checkpoint state and failure condition, recovery must always follow the same path and produce the same result.

5. **Minimal Overhead Principle**: The harness must introduce minimal runtime overhead. Checkpointing, state management, and observability must be designed to not degrade agent performance beyond acceptable thresholds defined in non-functional requirements.
