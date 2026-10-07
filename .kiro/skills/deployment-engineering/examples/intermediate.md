# Intermediate Example

## Prompt
"Generate Kubernetes deployment manifests with rolling update strategy, CI/CD pipeline for GitHub Actions, and monitoring configuration for a multi-service agent with API gateway and worker components."

## Expected Behavior
The skill analyzes the multi-service architecture, generates Kubernetes Deployments and Services for each component, configures rolling update strategy with proper readiness gates, creates a GitHub Actions pipeline with build-test-deploy stages, and sets up Prometheus monitoring with Grafana dashboards.

## Expected Output
- Kubernetes manifests (Deployment, Service, Ingress, ConfigMap, Secret references)
- Rolling update configuration with maxSurge and maxUnavailable settings
- GitHub Actions workflow with lint, test, build, push, and deploy stages
- Prometheus ServiceMonitor and Grafana dashboard definitions
- deployment-plan.md with stage-by-stage deployment instructions
