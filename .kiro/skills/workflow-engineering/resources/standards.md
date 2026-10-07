# Workflow Engineering Standards

## 1. Formal State Machine Modeling
Every workflow must be modeled as a formal state machine with explicit states, transitions, guards, and actions. Informal flow descriptions are insufficient. State machines must be validated for completeness (all states reachable, no deadlocks, defined terminal states).

## 2. Comprehensive Error Handling
Every workflow step must have defined error handling. There are no acceptable "unhandled" error conditions. Error handling must specify: retry policy (count, backoff), fallback behavior, escalation path, and dead-letter strategy for unrecoverable failures.

## 3. Timeout Discipline
Every step that involves external systems, I/O operations, or human interaction must have an explicit timeout configuration. Timeout behavior must be specified: retry, fallback, escalation, or workflow termination. Unbounded waits are prohibited.

## 4. Idempotent Step Design
Workflow steps should be designed for idempotent execution wherever possible. This enables safe retry after failures without side effects. Steps that cannot be made idempotent must document their non-idempotent behavior and compensating actions.

## 5. Observable Execution
Workflows must emit state transition events, step timing metrics, and error signals suitable for monitoring and debugging. Every state entry and exit must be observable. Long-running workflows must support progress reporting.
