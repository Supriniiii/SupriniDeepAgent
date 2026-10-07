# Post-Generation Hook

## Purpose

Finalize generation and register reusable assets.

---

## Trigger

Runs after the Validation Hook (only if validation succeeds).

---

## Responsibilities

- Update Component Catalog.
- Update Capability Registry.
- Update Prompt Catalog.
- Generate metrics.
- Generate engineering report.
- Store reusable artifacts.

---

## Execution Steps

1. Read Validation Report.
2. Extract reusable components.
3. Update Component Catalog with new entries.
4. Update Capability Registry with new capabilities.
5. Update Prompt Catalog with new prompts.
6. Generate generation metrics.
7. Generate engineering report.
8. Store all reusable artifacts for future discovery.

---

## Expected Outputs

- generation-report.md
- catalog-updates.md
- metrics.md

---

## Validation

Ensure reusable knowledge has been captured.

---

## Failure Handling

If catalog updates fail:

- Log warning.
- Generation is still considered successful.
- Flag for manual catalog update.

---

## Hook Contract

```yaml
hook:
  id: post-generation

stage: post-generation

trigger:
  after: validation

inputs:
  - validation-report.md
  - production-readiness-report.md

outputs:
  - generation-summary.md
  - engineering-metrics.md
  - catalog-updates.md

success:
  pipeline_complete: true

failure:
  stop_pipeline: false
  notify_team: true

---

## Pipeline Complete
