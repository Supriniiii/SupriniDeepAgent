# Workflow Engineering Checklist

- [ ] All workflow states enumerated with clear descriptions and entry/exit conditions
- [ ] All transitions defined with triggers, guards, and actions
- [ ] Decision points specified with conditions, branches, and default paths
- [ ] Error handling defined for every step (retry, fallback, escalation, dead-letter)
- [ ] Timeouts configured for all external interactions and long-running operations
- [ ] Parallel paths have explicit fork/join semantics and synchronization barriers
- [ ] Terminal states defined for both success and failure scenarios
- [ ] Step contracts complete with input/output types and validation rules
- [ ] Checkpoint strategy defined for long-running workflows
- [ ] Workflow validated: no deadlocks, all states reachable, all errors handled
