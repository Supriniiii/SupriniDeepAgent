# Intermediate Example

## Prompt
"Design observability for a multi-service agent system with API gateway, processing service, and database layer. Include distributed tracing, SLO-based alerting, and Grafana dashboards."

## Expected Behavior
The skill maps all three services and their interaction points, defines distributed tracing with context propagation across service boundaries, creates SLO-based alerting with error budget tracking, configures metrics for each service using RED patterns, and designs Grafana dashboards for operational visibility.

## Expected Output
- observability-plan.md with multi-service observability architecture
- Distributed tracing configuration with OpenTelemetry setup
- SLO-based alerting rules with error budget burn-rate alerts
- Grafana dashboard definitions for each service and system-wide overview
- Health check endpoints for each service including dependency checks
