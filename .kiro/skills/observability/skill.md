# Observability

## Skill Definition

name: observability
description: Designs monitoring, logging, metrics, and tracing strategies for Deep Agents
version: 1.0.0
category: platform
trigger: When a generated agent requires observability design or when monitoring strategy must be defined

## Required Inputs
- Agent architecture specification: Component structure and interaction patterns to determine observation points
- Performance SLOs: Service level objectives that drive alerting thresholds and metric selection
- Deployment topology: Infrastructure layout that determines tracing boundaries and log aggregation

## Optional Inputs
- Existing monitoring infrastructure details
- Custom metric requirements
- Compliance-driven logging requirements

## Workflow

### Step 1: Identify Observable Components
Map all components, interfaces, and interaction points that require observation.
- Engine: Harness Engineering Engine
- Knowledge: observability/
- Output: Observability map

### Step 2: Define Logging Strategy
Design structured logging with levels, field schemas, and correlation patterns.
- Engine: Harness Engineering Engine
- Knowledge: observability/
- Output: Logging strategy document

### Step 3: Define Metrics
Select and define application metrics, business metrics, and infrastructure metrics.
- Engine: Harness Engineering Engine
- Knowledge: observability/
- Output: Metrics catalog and configuration

### Step 4: Define Tracing
Configure distributed tracing with span definitions and propagation context.
- Engine: Harness Engineering Engine
- Knowledge: observability/
- Output: Tracing configuration

### Step 5: Configure Health Checks
Define liveness, readiness, and startup probes for all components.
- Engine: Harness Engineering Engine
- Knowledge: observability/
- Output: Health check specifications

### Step 6: Define Alerting
Create alerting rules based on SLOs with escalation policies and runbooks.
- Engine: Harness Engineering Engine
- Knowledge: observability/
- Output: Alerting rules and escalation policy

### Step 7: Produce Observability Plan
Compile all observability designs into a comprehensive plan.
- Engine: Harness Engineering Engine
- Knowledge: observability/
- Output: Complete observability plan

## Engineering Rules
- Every component boundary must have logging, metrics, and tracing
- Alerts must be actionable with clear runbook references
- Health checks must verify all critical dependencies
- Log levels must be consistent across the entire system
- Metrics must include both RED (Rate, Errors, Duration) and USE (Utilization, Saturation, Errors) patterns

## Knowledge Sources
- observability/

## Templates Used
- observability-plan-template
- logging-config-template
- metrics-config-template
- alerting-rules-template
- health-check-template

## Engineering Engines Invoked
- Harness Engineering Engine (observability aspect)
- Validation Engineering Engine

## Hooks Invoked
- pre-observability-design
- post-observability-validation
- slo-compliance-check

## Validation
- All components have logging, metrics, and tracing configured
- Health checks cover all critical paths and dependencies
- Alerting rules align with defined SLOs
- Observability plan is complete and internally consistent

## Expected Outputs
- observability-plan.md
- Logging configuration
- Metrics configuration
- Health check definitions

## Completion Criteria
- All observable components are mapped and instrumented
- Logging, metrics, and tracing strategies are defined
- Health checks and alerting rules are configured
- Observability plan is validated against architecture
