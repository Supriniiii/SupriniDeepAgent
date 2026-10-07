# Advanced Example

## Prompt
"Generate a full production deployment package for a distributed multi-agent system with canary deployment strategy, Helm charts for multi-environment deployment, GitOps-based CI/CD with ArgoCD, auto-scaling policies, network policies, and comprehensive observability stack."

## Expected Behavior
The skill designs a full production deployment architecture with canary release strategy, generates Helm charts with environment-specific value files, configures ArgoCD ApplicationSets for GitOps delivery, defines HPA and VPA for auto-scaling, creates NetworkPolicies for zero-trust networking, and deploys a complete observability stack with distributed tracing.

## Expected Output
- Helm chart with templates, values files for dev/staging/prod
- ArgoCD Application manifests with canary analysis configuration
- HorizontalPodAutoscaler and VerticalPodAutoscaler manifests
- NetworkPolicy manifests enforcing least-privilege communication
- Full observability stack (Prometheus, Grafana, Jaeger, Loki)
- deployment-plan.md with canary progression criteria and rollback procedures
