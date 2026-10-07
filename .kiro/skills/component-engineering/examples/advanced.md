# Advanced Example

## Prompt
"Identify and define components for an enterprise incident response multi-agent system with hierarchical architecture. Requires: coordinator agent, diagnostic agent, remediation agent, communication agent, PagerDuty integration, Datadog integration, Slack integration, JIRA integration, audit service, health monitor, state manager, approval workflow engine, and escalation engine."

## Expected Behavior
The component-engineering skill:
1. Extracts 13+ required components from architecture specification
2. Performs comprehensive registry search across enterprise catalogs
3. Finds existing: Slack adapter (v4.1), JIRA connector (v3.2), health monitor (v2.0), audit logger (v2.5), state manager (v1.9)
4. Partial matches: PagerDuty adapter (v1.0 — needs extension for bidirectional), Datadog connector (v2.1 — needs custom metric support)
5. Reuse assessment: 5 reuse as-is, 2 adapt, 6 build new
6. Defines new components: CoordinatorAgent, DiagnosticAgent, RemediationAgent, CommunicationAgent, ApprovalWorkflowEngine, EscalationEngine
7. Defines adapters: EnhancedPagerDuty (extends existing with bidirectional webhook), EnhancedDatadog (extends with custom metrics)
8. Identifies shared interfaces: AgentInterface (all agents), IntegrationAdapter (all external connectors), EventEmitter (cross-cutting)
9. Maps complex dependency graph with service mesh communication
10. Identifies potential circular dependency (coordinator ↔ escalation) and resolves via event-driven decoupling
11. Defines component groups for deployment isolation (core agents, integrations, infrastructure)

## Expected Output
- `component-plan.md` — 13 components across 3 groups: core agents (4), integrations (4), infrastructure (5)
- Shared interfaces: AgentInterface, IntegrationAdapter, EventEmitter, AuditableAction
- Reuse report: 5 reused, 2 adapted, 6 new — 54% reuse rate
- Detailed specifications for all 6 new components with security annotations
- Dependency graph with service mesh topology and event flows
- Circular dependency resolution documented (coordinator/escalation decoupled via events)
- Component group definitions for deployment isolation
- Build order: infrastructure → integrations → core agents → coordinator
