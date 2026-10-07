# Observability Checklist

- [ ] All components emit structured logs with consistent field schemas and correlation IDs
- [ ] Application metrics cover RED patterns (Rate, Errors, Duration) for all endpoints
- [ ] Distributed tracing spans all service boundaries with context propagation configured
- [ ] Health check endpoints verify both component health and critical dependency availability
- [ ] Alerting rules are tied to SLOs with clear runbook references and escalation paths
