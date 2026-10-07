# Observability

## Purpose
Designs comprehensive monitoring, logging, metrics, and tracing strategies for Deep Agents. Ensures every generated system is observable, diagnosable, and operable from the moment of deployment.

## Responsibilities
- Identify observable components and interaction points
- Define structured logging strategy with correlation
- Define metrics collection and aggregation strategy
- Define distributed tracing configuration
- Configure health checks and readiness probes
- Define alerting rules and escalation policies
- Produce comprehensive observability plans

## Inputs
- Agent architecture specification
- Component interaction diagrams
- Performance SLOs and error budgets
- Deployment topology

## Outputs
- observability-plan.md
- Logging configuration
- Metrics configuration
- Health check definitions

## Dependencies
- Harness Engineering Engine (observability aspect)
- Knowledge Base (observability/)
- Observability Templates
- Monitoring Stack Configurations

## Integration
- Generation Orchestration Engine
- Harness Engineering Engine
- Deployment Engineering Engine
- Validation Engineering Engine

## Usage
Invoke this skill when a generated agent requires observability design, when monitoring gaps need to be addressed, or when alerting and health check strategies need to be defined.

## Best Practices
- Design observability as a first-class concern, not an afterthought
- Use structured logging with consistent field schemas
- Define meaningful SLIs that directly measure user experience
- Keep alert rules actionable to avoid alert fatigue
- Include correlation IDs across all observable boundaries

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Produces deterministic outputs
