# Observability Standards

1. **Three Pillars Coverage**: Every observable system must implement all three observability pillars (logging, metrics, tracing). No pillar may be omitted. Each provides distinct diagnostic value that cannot be replaced by the others.

2. **SLO-Driven Alerting**: All alerts must be derived from Service Level Objectives. Alerts not tied to SLOs or user impact must be justified. Alert rules must use multi-window burn-rate calculations to balance sensitivity with noise.

3. **Structured Consistency**: All logs must use structured format (JSON) with a consistent field schema across all services. Required fields include timestamp, level, service, correlation_id, and message. Custom fields extend but never replace the base schema.

4. **Dependency Health Awareness**: Health checks must verify not just component self-health but also the availability of critical dependencies. Cascading failures must be detectable through dependency health propagation.

5. **Correlation Across Boundaries**: Every request must carry a correlation ID that propagates across all service boundaries, enabling end-to-end trace reconstruction from any single log entry, metric data point, or trace span.
