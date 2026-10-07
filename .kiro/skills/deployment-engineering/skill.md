# Deployment Engineering

## Skill Definition

name: deployment-engineering
description: Generates production-ready deployment assets and CI/CD pipelines for Deep Agents
version: 1.0.0
category: engineering
trigger: When a generated agent requires deployment configuration or when deployment strategy design is needed

## Required Inputs
- Agent architecture specification: Describes components, dependencies, and runtime requirements
- Infrastructure requirements: Target environment, resource constraints, and scaling needs
- Availability SLOs: Uptime targets and acceptable deployment downtime

## Optional Inputs
- Existing CI/CD pipeline configuration
- Cloud provider preferences
- Network topology constraints

## Workflow

### Step 1: Analyze Architecture
Review agent architecture to identify deployable components and their dependencies.
- Engine: Deployment Engineering Engine
- Knowledge: deployment/
- Output: Deployment requirements analysis

### Step 2: Select Deployment Strategy
Choose deployment approach (blue-green, canary, rolling) based on availability requirements.
- Engine: Deployment Engineering Engine
- Knowledge: deployment/
- Output: Deployment strategy decision with justification

### Step 3: Generate Dockerfile
Create optimized container image definitions for each deployable component.
- Engine: Deployment Engineering Engine
- Knowledge: deployment/
- Output: Dockerfile(s)

### Step 4: Generate Kubernetes Manifests
Create orchestration configurations including deployments, services, and ingress.
- Engine: Deployment Engineering Engine
- Knowledge: deployment/
- Output: Kubernetes YAML manifests

### Step 5: Generate CI/CD Pipeline
Create automated build, test, and deployment pipeline configuration.
- Engine: Deployment Engineering Engine
- Knowledge: deployment/
- Output: CI/CD pipeline configuration

### Step 6: Configure Monitoring
Set up monitoring, alerting, and dashboards for deployed services.
- Engine: Deployment Engineering Engine
- Knowledge: deployment/, observability/
- Output: Monitoring configuration

### Step 7: Configure Health Checks
Define liveness, readiness, and startup probes for all components.
- Engine: Deployment Engineering Engine
- Knowledge: deployment/, observability/
- Output: Health check definitions

### Step 8: Produce Deployment Plan
Compile all assets into a comprehensive deployment plan with runbook.
- Engine: Deployment Engineering Engine
- Knowledge: deployment/
- Output: deployment-plan.md

## Engineering Rules
- Never hard-code environment-specific values in deployment assets
- Always include resource limits and requests in container specifications
- Deployment must support rollback without data loss
- CI/CD pipelines must include automated testing gates
- Health checks must cover all external dependencies

## Knowledge Sources
- deployment/

## Templates Used
- dockerfile-template
- kubernetes-manifest-template
- cicd-pipeline-template
- deployment-plan-template
- docker-compose-template

## Engineering Engines Invoked
- Deployment Engineering Engine
- Validation Engineering Engine

## Hooks Invoked
- pre-deployment-validation
- post-deployment-generation
- security-scan-trigger

## Validation
- Dockerfile builds successfully with no security vulnerabilities
- Kubernetes manifests pass schema validation
- CI/CD pipeline includes all required stages
- Health checks cover all critical paths

## Expected Outputs
- Dockerfile
- docker-compose.yml
- Kubernetes manifests
- CI/CD pipeline configuration
- deployment-plan.md

## Completion Criteria
- All deployment assets are generated and validated
- Deployment strategy is documented and justified
- CI/CD pipeline covers build, test, and deploy stages
- Monitoring and health checks are configured
- Deployment plan includes rollback procedures
