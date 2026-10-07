# Deployment Engineering

## Purpose
Generates production-ready deployment assets including container images, orchestration manifests, CI/CD pipelines, and monitoring configurations. Ensures every Deep Agent is deployable, observable, and operationally sound from day one.

## Responsibilities
- Analyze agent architecture for deployment requirements
- Select appropriate deployment strategy (blue-green, canary, rolling)
- Generate Dockerfile and container configurations
- Generate Kubernetes manifests and Helm charts
- Generate CI/CD pipeline configurations
- Configure monitoring, alerting, and health checks
- Produce comprehensive deployment plans

## Inputs
- Agent architecture specification
- Infrastructure requirements and constraints
- Target deployment environment (cloud, on-prem, hybrid)
- Performance and availability SLOs

## Outputs
- Dockerfile
- docker-compose.yml
- Kubernetes manifests
- CI/CD pipeline configuration
- deployment-plan.md

## Dependencies
- Deployment Engineering Engine (conceptual)
- Knowledge Base (deployment/)
- Deployment Templates
- Infrastructure Patterns Library

## Integration
- Generation Orchestration Engine
- Deployment Engineering Engine
- Observability Engine
- Validation Engineering Engine

## Usage
Invoke this skill when a generated agent requires deployment assets, when existing deployment configurations need updating, or when a new deployment strategy needs to be designed.

## Best Practices
- Keep deployment configuration separate from business logic
- Use infrastructure-as-code for all deployment assets
- Design for zero-downtime deployments
- Include health checks at every service boundary
- Externalize all environment-specific configuration

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Produces deterministic outputs
