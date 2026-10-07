# Workflow Hook

## Purpose

Design the execution workflow.

---

## Trigger

Runs after the Harness Hook.

---

## Responsibilities

Generate:

- State Machine
- Workflow Diagram
- Execution Order
- Recovery Flow

---

## Execution Steps

1. Read Harness Specification and Architecture.
2. Define workflow states.
3. Define state transitions.
4. Design execution order.
5. Design recovery and fallback flows.
6. Generate Workflow Specification.

---

## Expected Outputs

- workflow-specification.md

---

## Validation

Workflow satisfies architecture.

---

## Failure Handling

If workflow cannot satisfy architecture:

- Re-evaluate harness constraints.
- Request clarification on execution flow.
- Stop pipeline if unresolvable.

---

## Hook Contract

```yaml
hook:
  id: workflow-hook
  stage: workflow
input:
  - harness-specification.md
  - architecture.md
output:
  - workflow-specification.md
success:
  next: memory-hook
failure:
  retry: false
  request_clarification: true
  stop_pipeline: true
```

---

## Next Hook

Memory Hook
