# Documentation Hook

## Purpose

Generate project documentation.

---

## Trigger

Runs after the Testing Hook.

---

## Responsibilities

Generate:

- README
- ADR
- Architecture
- Deployment Guide
- Configuration Guide
- Prompt Catalog
- Component Catalog

---

## Execution Steps

1. Read generated project and all specifications.
2. Generate README with overview, setup, and usage.
3. Generate Architecture Decision Records.
4. Generate architecture documentation.
5. Generate deployment guide.
6. Generate configuration guide.
7. Generate prompt catalog.
8. Generate component catalog.

---

## Expected Outputs

- docs/

---

## Validation

Documentation reflects generated implementation.

---

## Failure Handling

If documentation generation is incomplete:

- Generate partial documentation.
- Flag gaps in validation report.

---

## Hook Contract

```yaml
hook:
  id: documentation-hook
  stage: documentation
input:
  - generated-project/
  - architecture.md
  - component-plan.md
  - prompt-package.md
output:
  - docs/
success:
  next: deployment-hook
failure:
  retry: true
  request_clarification: false
  stop_pipeline: false
```

---

## Next Hook

Deployment Hook
