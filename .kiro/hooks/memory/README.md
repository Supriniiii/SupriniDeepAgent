# Memory Hook

## Purpose

Select and configure memory strategies.

---

## Trigger

Runs after the Workflow Hook.

---

## Responsibilities

Choose from:

- Working Memory
- Conversation Memory
- Semantic Memory
- Long-Term Memory
- Checkpoint Memory
- Artifact Memory

---

## Execution Steps

1. Read Workflow Specification and Requirements.
2. Identify memory needs per workflow state.
3. Select appropriate memory types.
4. Define memory lifecycle (creation, update, eviction).
5. Configure memory boundaries and limits.
6. Generate Memory Strategy.

---

## Expected Outputs

- memory-strategy.md

---

## Validation

Memory aligns with workflow requirements.

---

## Failure Handling

If memory requirements conflict:

- Simplify memory strategy.
- Request clarification on persistence needs.

---

## Hook Contract

```yaml
hook:
  id: memory-hook
  stage: memory
input:
  - workflow-specification.md
  - requirements.md
output:
  - memory-strategy.md
success:
  next: prompts-hook
failure:
  retry: false
  request_clarification: true
  stop_pipeline: true
```

---

## Next Hook

Prompt Hook
