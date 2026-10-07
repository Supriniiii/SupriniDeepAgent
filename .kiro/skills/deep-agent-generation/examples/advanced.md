# Advanced Example

## Prompt
"Generate an enterprise incident response multi-agent system. It needs a coordinator agent that receives alerts, a diagnostic agent that investigates root causes, a remediation agent that proposes and executes fixes, and a communication agent that notifies stakeholders. The system must integrate with PagerDuty, Datadog, Slack, and JIRA. It must support concurrent incident handling, maintain audit trails, comply with SOC2 requirements, and operate 24/7 with automatic failover."

## Expected Behavior
The deep-agent-generation skill orchestrates a complex multi-agent generation:
1. Captures intent: enterprise multi-agent incident response with 4 specialized agents, 4 integrations, compliance, HA
2. Extracts requirements: concurrent incidents, audit logging, SOC2 compliance, 24/7 uptime, failover, 4 external integrations
3. Selects architecture: hierarchical manager-worker pattern with event-driven communication (coordinator manages specialist agents)
4. Discovers capabilities: checks registry for PagerDuty connector, Datadog adapter, Slack integration, JIRA client, audit logging component
5. Selects components: alert receiver, diagnostic engine, remediation executor (with approval gates), notification router, audit logger, state coordinator, health monitor
6. Selects harness: distributed multi-agent harness with message bus, failover support, and health monitoring
7. Designs workflow: alert intake → triage → parallel diagnostic + notification → root cause analysis → remediation proposal → approval gate → execution → verification → close-out → audit
8. Memory strategy: working memory (active incidents), conversation memory (stakeholder communication), checkpoint memory (incident state), long-term memory (past incident patterns), artifact memory (evidence and logs)
9. Prompt strategy: triage prompt, diagnostic reasoning prompt, remediation planning prompt, stakeholder communication prompt, reflection prompt, escalation decision prompt
10. Generates full multi-agent implementation with distributed architecture
11. Generates comprehensive security controls (SOC2 compliance, audit trails)
12. Generates HA/failover configuration
13. Generates integration adapters for all 4 external systems
14. Validates across all quality dimensions including security and compliance

## Expected Output
- `/agents/incident-response-system/` — complete multi-agent system
- `/agents/incident-response-system/architecture.md` — hierarchical manager-worker architecture
- `/agents/incident-response-system/adrs/` — ADRs for pattern choice, HA strategy, compliance approach
- `/agents/incident-response-system/agents/coordinator/` — coordinator agent
- `/agents/incident-response-system/agents/diagnostic/` — diagnostic specialist
- `/agents/incident-response-system/agents/remediation/` — remediation specialist with approval gates
- `/agents/incident-response-system/agents/communication/` — notification specialist
- `/agents/incident-response-system/components/` — shared components (audit, health, state)
- `/agents/incident-response-system/integrations/` — PagerDuty, Datadog, Slack, JIRA adapters
- `/agents/incident-response-system/workflows/` — incident lifecycle state machines
- `/agents/incident-response-system/memory/` — 5 memory type configurations
- `/agents/incident-response-system/prompts/` — 6+ specialized prompts
- `/agents/incident-response-system/security/` — SOC2 controls, audit configuration
- `/agents/incident-response-system/deploy/` — Kubernetes manifests, Helm charts, HA config, CI/CD
- `/agents/incident-response-system/monitoring/` — Datadog dashboards, alerts, SLOs
- `/agents/incident-response-system/tests/` — full test coverage (unit, integration, workflow, security, chaos)
- `/agents/incident-response-system/docs/` — complete documentation (architecture, runbooks, API docs, compliance evidence)
- `validation-report.md` — quality score ≥90%, production-ready: YES, compliance: SOC2 VERIFIED
