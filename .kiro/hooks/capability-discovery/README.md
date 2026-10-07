# Capability Discovery Hook

## Purpose

Identify reusable enterprise capabilities before creating new implementations.

---

## Trigger

Runs after the Architecture Hook.

---

## Responsibilities

Search:

- Capability Registry
- Component Catalog
- Tool Catalog
- Prompt Library
- Workflow Library

Reuse before creating.

---

## Execution Steps

1. Read Architecture.
2. Search catalogs.
3. Identify reusable assets.
4. Generate Capability Plan.
5. Record reuse decisions.

---

## Expected Outputs

- capability-plan.md

---

## Validation

Ensure duplicate functionality is avoided.

---

## Failure Handling

If catalogs are unavailable:

- Log warning.
- Proceed with new component creation.
- Flag for post-generation catalog update.

---

## Hook Contract

```yaml
hook:
  id: capability-discovery-hook
  stage: capability-discovery
input:
  - architecture.md
output:
  - capability-plan.md
success:
  next: component-selection-hook
failure:
  retry: true
  request_clarification: false
  stop_pipeline: false
```

---

## Next Hook

Component Selection Hook
