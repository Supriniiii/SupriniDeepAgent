# Workflow Specification: Code Review Agent

## Execution Flow

Receive Request → Plan → Execute → Reflect → Verify → Deliver

## States

- pending
- planning
- executing
- reflecting
- verifying
- completed
- failed

## Transitions

| From | To | Condition |
|------|-----|-----------|
| pending | planning | Request received |
| planning | executing | Plan approved |
| executing | reflecting | Task complete |
| reflecting | verifying | Reflection complete |
| verifying | completed | Verification passed |
| verifying | executing | Verification failed (retry) |
| any | failed | Unrecoverable error |

## Recovery

- Retry: Up to 3 times per step
- Checkpoint: After each state transition
- Fallback: Return partial results with warning

## Decision Points

- After reflection: Continue or revise plan?
- After verification: Accept or retry?
- On failure: Retry, skip, or terminate?
