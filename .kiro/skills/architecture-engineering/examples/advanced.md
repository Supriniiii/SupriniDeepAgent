# Advanced Example

## Prompt
"Design the architecture for an enterprise compliance monitoring multi-agent system that continuously monitors regulatory changes across 12 jurisdictions, evaluates impact on existing policies, drafts policy amendments, routes them through approval workflows, and integrates with GRC (Governance, Risk, Compliance) platforms. Must support horizontal scaling, real-time alerting, and maintain complete audit trails for SOX compliance."

## Expected Behavior
The architecture-engineering skill:
1. Identifies architectural drivers: scalability (12 jurisdictions, real-time), reliability (compliance-critical, cannot miss changes), auditability (SOX), extensibility (new jurisdictions), security (sensitive policy data)
2. Evaluates patterns: hierarchical (coordination of specialized agents), event-driven (real-time regulatory monitoring), distributed (horizontal scaling), hybrid approaches
3. Selects hierarchical + event-driven hybrid — hierarchy for agent coordination, event-driven for real-time monitoring and alerting
4. Specifies multi-layer architecture:
   - Monitoring layer: jurisdiction-specific regulatory watchers (event-driven)
   - Analysis layer: impact assessment agents (hierarchical coordination)
   - Drafting layer: policy amendment agents with approval routing
   - Integration layer: GRC platform adapters
   - Cross-cutting: audit service, alert service, state management
5. Generates ADRs: hybrid pattern justification, scaling strategy, audit architecture, GRC integration approach, data classification
6. Produces comprehensive diagrams: system context, container view, component view per layer, deployment view (Kubernetes with auto-scaling)

## Expected Output
- `architecture.md` — hierarchical + event-driven hybrid architecture, 4 layers, cross-cutting services
- `adrs/001-hybrid-architecture.md` — justification for combining hierarchical and event-driven patterns
- `adrs/002-scaling-strategy.md` — horizontal scaling with jurisdiction-based partitioning
- `adrs/003-audit-architecture.md` — immutable audit trail for SOX compliance
- `adrs/004-grc-integration.md` — adapter pattern for GRC platform connectivity
- `adrs/005-data-classification.md` — sensitivity classification for regulatory and policy data
- `adrs/006-real-time-alerting.md` — event stream architecture for compliance alerts
- `diagrams/system-context.md` — enterprise context showing external systems
- `diagrams/container-view.md` — services, databases, message buses, GRC connections
- `diagrams/component-monitoring-layer.md` — regulatory watchers and event processors
- `diagrams/component-analysis-layer.md` — impact assessment agent hierarchy
- `diagrams/component-drafting-layer.md` — amendment generation and approval routing
- `diagrams/deployment-view.md` — Kubernetes with auto-scaling, multi-region
- `interfaces/` — contracts between all layers and external integrations
- `architecture-validation-report.md` — all quality attributes addressed, SOX controls verified
