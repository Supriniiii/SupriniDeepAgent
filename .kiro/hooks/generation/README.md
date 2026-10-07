# Generation Hook

## Purpose

Generate the implementation artifacts.

---

## Trigger

Runs after the Prompt Hook.

---

## Responsibilities

Generate:

- Source Code
- Configuration
- Components
- Harness
- Project Structure

---

## Execution Steps

1. Read all prior specifications (architecture, components, harness, workflow, memory, prompts).
2. Generate project structure.
3. Generate harness implementation.
4. Generate component implementations.
5. Generate configuration files.
6. Generate entry points.
7. Verify implementation matches architecture.

---

## Expected Outputs

- Generated Project

---

## Validation

Implementation matches architecture.

---

## Failure Handling

If generation fails:

- Log failure reason.
- Retry with simplified implementation.
- Stop pipeline if critical failures persist.

---

## Hook Contract

```yaml
hook:
  id: generation-hook
  stage: generation
input:
  - architecture.md
  - component-plan.md
  - harness-specification.md
  - workflow-specification.md
  - memory-strategy.md
  - prompt-package.md
output:
  - generated-project/
success:
  next: testing-hook
failure:
  retry: true
  request_clarification: false
  stop_pipeline: true
```

---

## Next Hook

Testing Hook
