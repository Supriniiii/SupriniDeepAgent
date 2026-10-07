# Component Selection Hook

## Purpose

Determine the reusable and new components required for implementation.

---

## Trigger

Runs after the Capability Discovery Hook.

---

## Responsibilities

Select:

- Planner
- Executor
- Reflection
- Verification
- Memory
- Tool Manager
- Workflow Manager

Create new components only when necessary.

---

## Execution Steps

1. Read Capability Plan.
2. Match required capabilities to existing components.
3. Identify gaps requiring new components.
4. Define interfaces for new components.
5. Generate Component Plan.

---

## Expected Outputs

- component-plan.md

---

## Validation

No duplicated responsibilities.

---

## Failure Handling

If component conflicts are detected:

- Resolve responsibility overlap.
- Request clarification if ambiguous.

---

## Hook Contract

```yaml
hook:
  id: component-selection-hook
  stage: component-selection
input:
  - capability-plan.md
  - architecture.md
output:
  - component-plan.md
success:
  next: harness-hook
failure:
  retry: false
  request_clarification: true
  stop_pipeline: true
```

---

## Next Hook

Harness Hook
