# Architecture Hook

## Purpose

Design the solution architecture.

---

## Trigger

Runs after the Requirements Hook.

---

## Responsibilities

Determine:

- Architecture Pattern
- Agent Type
- Harness
- Components
- Interfaces
- Data Flow
- Memory Strategy
- Technology Recommendations

---

## Execution Steps

1. Read Requirements Specification.
2. Assess complexity.
3. Select architecture.
4. Generate Architecture Diagram.
5. Create Architecture Decision Record.
6. Generate Component Plan.
7. Generate Workflow Plan.

---

## Expected Outputs

- architecture.md
- architecture-diagram.md
- ADR.md

---

## Validation

Ensure:

- Architecture satisfies all requirements.

---

## Failure Handling

If architecture cannot satisfy requirements:

- Revisit requirements for constraints.
- Request clarification on conflicting needs.
- Stop pipeline if unresolvable.

---

## Hook Contract

```yaml
hook:
  id: architecture-hook
  stage: architecture
input:
  - requirements.md
output:
  - architecture.md
  - architecture-diagram.md
  - ADR.md
success:
  next: capability-discovery-hook
failure:
  retry: false
  request_clarification: true
  stop_pipeline: true
```

---

## Next Hook

Capability Discovery Hook
