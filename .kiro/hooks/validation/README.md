# Validation Hook

## Purpose

Evaluate the complete generated solution.

---

## Trigger

Runs after the Deployment Hook.

---

## Responsibilities

Validate:

- Requirements
- Architecture
- Components
- Harness
- Security
- Documentation
- Testing
- Deployment

Generate a Production Readiness Report.

---

## Execution Steps

1. Read all generated artifacts.
2. Validate requirements coverage.
3. Validate architecture compliance.
4. Validate component correctness.
5. Validate harness configuration.
6. Validate security posture.
7. Validate documentation completeness.
8. Validate test coverage.
9. Validate deployment readiness.
10. Calculate Readiness Score.
11. Calculate Engineering Quality Score.
12. Generate Improvement Recommendations.
13. Produce Validation Report.

---

## Expected Outputs

- validation-report.md

---

## Validation

Calculate:

- Readiness Score
- Engineering Quality Score
- Improvement Recommendations

---

## Failure Handling

If validation fails:

- Generate detailed failure report.
- Identify specific failing areas.
- Provide remediation steps.
- Stop pipeline — generation is not complete until validation succeeds.

---

## Hook Contract

```yaml
hook:
  id: validation-hook
  stage: validation
input:
  - generated-project/
  - tests/
  - docs/
  - deployment/
  - requirements.md
  - architecture.md
output:
  - validation-report.md
success:
  next: post-generation-hook
failure:
  retry: false
  request_clarification: false
  stop_pipeline: true
```

---

## Next Hook

Post-Generation Hook
