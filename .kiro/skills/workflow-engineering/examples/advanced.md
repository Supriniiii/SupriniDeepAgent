# Advanced Example

## Prompt
"Design the execution workflow for an enterprise incident response system with: alert intake, severity triage, parallel diagnostic investigation and stakeholder notification, root cause analysis, remediation proposal with human approval gate, execution with rollback capability, verification, and post-incident review. Must support concurrent incidents and escalation paths."

## Expected Behavior
The workflow-engineering skill:
1. Identifies workflow scope: long-running incident lifecycle, triggered by alert intake, supports concurrent instances
2. Enumerates states: ALERT_RECEIVED, TRIAGING, INVESTIGATING (parallel: DIAGNOSING + NOTIFYING), ANALYZING_ROOT_CAUSE, PROPOSING_REMEDIATION, AWAITING_APPROVAL, EXECUTING_REMEDIATION, ROLLING_BACK, VERIFYING, CLOSING, POST_REVIEW, RESOLVED, ESCALATED, FAILED
3. Defines transitions: complex graph with parallel paths, decision points, and escalation branches
4. Decision points: severity classification (P1-P4), approval/rejection, verification pass/fail, escalation threshold
5. Error handling per state: diagnostic failure (escalate), remediation failure (immediate rollback), approval timeout (auto-escalate)
6. Parallel paths: diagnostic investigation AND stakeholder notification execute concurrently
7. Human-in-the-loop: approval gate blocks execution until authorized human approves
8. Rollback workflow: sub-state-machine within ROLLING_BACK for safe reversal
9. Escalation paths: time-based escalation, severity-based escalation, failure-based escalation
10. Concurrency model: instance-per-incident with shared resource coordination
11. Checkpoints: after triage, after diagnosis, after approval, after execution, after verification
12. Timeouts: triage (2 min), diagnosis (15 min P1 / 60 min P2+), approval (10 min P1 / 30 min P2+)

## Expected Output
- `workflow-specification.md` — enterprise incident lifecycle workflow with 14 states
- State machine definition with severity-dependent timeout configurations
- Parallel execution: diagnosis + notification fork with configurable join semantics
- Human approval gate specification with escalation-on-timeout
- Rollback sub-workflow: reverse execution steps in LIFO order with verification
- Escalation matrix: conditions, thresholds, and targets for each escalation level
- Concurrency specification: instance isolation, shared resource locking
- Checkpoint strategy: 5 durable checkpoints for crash recovery
- Error handling: state-specific retry/escalate/rollback decisions
- Decision point specifications: severity triage rules, approval criteria, verification conditions
- Step contracts: all 14 states with input/output types and validation
- Workflow diagrams: main flow, escalation paths, rollback sub-flow
- SLA mapping: states to SLA timers with violation alerts
