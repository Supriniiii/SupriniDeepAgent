# Prompt Hook

## Purpose

Generate reusable prompt packages.

---

## Trigger

Runs after the Memory Hook.

---

## Responsibilities

Generate:

- System Prompt
- Planner Prompt
- Reflection Prompt
- Verification Prompt
- Evaluation Prompt

---

## Execution Steps

1. Read Architecture, Workflow, and Memory Strategy.
2. Identify required prompt roles.
3. Design each prompt with purpose, inputs, outputs, constraints.
4. Version each prompt.
5. Document evaluation criteria.
6. Generate Prompt Package.

---

## Expected Outputs

- prompt-package.md

---

## Validation

Prompts are modular, versioned, and documented.

---

## Failure Handling

If prompt design is unclear:

- Request clarification on agent behavior expectations.
- Provide default prompt templates as fallback.

---

## Hook Contract

```yaml
hook:
  id: prompts-hook
  stage: prompts
input:
  - architecture.md
  - workflow-specification.md
  - memory-strategy.md
output:
  - prompt-package.md
success:
  next: generation-hook
failure:
  retry: true
  request_clarification: true
  stop_pipeline: false
```

---

## Next Hook

Generation Hook
