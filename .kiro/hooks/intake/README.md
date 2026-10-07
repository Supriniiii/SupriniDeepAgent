# Intake Hook

## Purpose

Receive and normalize developer requests into a structured request package.

---

## Trigger

Runs whenever a new request is submitted to the Deep Agent Engineering Skill.

---

## Responsibilities

- Identify the requested artifact.
- Determine whether the request is for:
  - Deep Agent
  - Multi-Agent System
  - Agent Harness
  - Component
  - Kiro Skill
  - Workflow
- Extract the business objective.
- Identify the target domain.
- Determine complexity.
- Detect ambiguous requests.

---

## Execution Steps

1. Read the developer request.
2. Extract the primary objective.
3. Identify expected deliverables.
4. Identify business domain.
5. Estimate implementation complexity.
6. Create a normalized Request Package.
7. Pass the Request Package to the Requirements Hook.

---

## Expected Outputs

- Request Package
- Request Classification
- Complexity Assessment

---

## Validation

Ensure:

- Request is understandable.
- Business objective exists.
- Deliverable is identified.

---

## Failure Handling

If information is missing:

- Ask clarification questions.
- Pause generation.

---

## Hook Contract

```yaml
hook:
  id: intake-hook
  stage: intake
input:
  - developer-request
output:
  - request-package.md
  - request-classification.md
  - complexity-assessment.md
success:
  next: requirements-hook
failure:
  retry: false
  request_clarification: true
  stop_pipeline: true
```

---

## Next Hook

Requirements Hook
