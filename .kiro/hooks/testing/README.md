# Testing Hook

## Purpose

Generate the complete testing suite.

---

## Trigger

Runs after the Generation Hook.

---

## Responsibilities

Generate:

- Unit Tests
- Integration Tests
- Workflow Tests
- AI Evaluation Tests
- Performance Tests
- Security Tests

---

## Execution Steps

1. Read generated project and requirements.
2. Generate unit tests for each component.
3. Generate integration tests for component interactions.
4. Generate workflow tests for end-to-end flows.
5. Generate AI evaluation tests for prompt quality.
6. Generate performance tests for latency and throughput.
7. Generate security tests for vulnerabilities.

---

## Expected Outputs

- tests/

---

## Validation

Coverage is sufficient.

---

## Failure Handling

If test generation fails:

- Log missing coverage areas.
- Generate partial test suite.
- Flag gaps in validation report.

---

## Hook Contract

```yaml
hook:
  id: testing-hook
  stage: testing
input:
  - generated-project/
  - requirements.md
output:
  - tests/
success:
  next: documentation-hook
failure:
  retry: true
  request_clarification: false
  stop_pipeline: false
```

---

## Next Hook

Documentation Hook
