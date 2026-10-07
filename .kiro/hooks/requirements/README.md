# Requirements Hook

## Purpose

Transform business intent into engineering requirements.

---

## Trigger

Runs after the Intake Hook.

---

## Responsibilities

Generate:

- Functional Requirements
- Non-Functional Requirements
- Constraints
- Assumptions
- Risks
- Acceptance Criteria

---

## Execution Steps

1. Analyze the Request Package.
2. Extract business goals.
3. Generate Functional Requirements.
4. Generate Non-Functional Requirements.
5. Detect missing requirements.
6. Generate assumptions.
7. Generate acceptance criteria.
8. Produce Requirements Specification.

---

## Expected Outputs

- requirements.md

---

## Validation

Verify:

- Requirements are complete.
- Requirements are testable.
- No contradictions exist.

---

## Failure Handling

Ask for clarification if requirements cannot be inferred.

---

## Hook Contract

```yaml
hook:
  id: requirements-hook
  stage: requirements
input:
  - request-package.md
output:
  - requirements.md
success:
  next: architecture-hook
failure:
  retry: false
  request_clarification: true
  stop_pipeline: true
```

---

## Next Hook

Architecture Hook
