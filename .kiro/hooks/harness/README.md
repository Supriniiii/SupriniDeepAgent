# Harness Hook

## Purpose

Generate the runtime architecture.

---

## Trigger

Runs after the Component Selection Hook.

---

## Responsibilities

Determine:

- Execution Model
- Scheduling
- Checkpointing
- Recovery
- Reflection
- Observability

---

## Execution Steps

1. Read Component Plan and Architecture.
2. Select execution model.
3. Define scheduling strategy.
4. Design checkpointing mechanism.
5. Design recovery flow.
6. Configure reflection points.
7. Configure observability hooks.
8. Generate Harness Specification.

---

## Expected Outputs

- harness-specification.md

---

## Validation

Harness supports architecture.

---

## Failure Handling

If harness cannot support architecture:

- Re-evaluate architecture constraints.
- Request clarification on execution requirements.
- Stop pipeline if unresolvable.

---

## Hook Contract

```yaml
hook:
  id: harness-hook
  stage: harness
input:
  - component-plan.md
  - architecture.md
output:
  - harness-specification.md
success:
  next: workflow-hook
failure:
  retry: false
  request_clarification: true
  stop_pipeline: true
```

---

## Next Hook

Workflow Hook
