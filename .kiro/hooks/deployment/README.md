# Deployment Hook

## Purpose

Generate deployment assets.

---

## Trigger

Runs after the Documentation Hook.

---

## Responsibilities

Generate:

- Dockerfile
- Docker Compose
- Kubernetes
- Helm
- CI/CD
- Monitoring
- Health Checks

---

## Execution Steps

1. Read generated project and architecture.
2. Generate Dockerfile.
3. Generate Docker Compose for local development.
4. Generate Kubernetes manifests.
5. Generate Helm charts.
6. Generate CI/CD pipeline configuration.
7. Generate monitoring configuration.
8. Generate health check endpoints.

---

## Expected Outputs

- deployment/

---

## Validation

Deployment assets are production-ready.

---

## Failure Handling

If deployment generation fails:

- Generate minimal deployment (Dockerfile only).
- Flag gaps in validation report.

---

## Hook Contract

```yaml
hook:
  id: deployment-hook
  stage: deployment
input:
  - generated-project/
  - architecture.md
output:
  - deployment/
success:
  next: validation-hook
failure:
  retry: true
  request_clarification: false
  stop_pipeline: false
```

---

## Next Hook

Validation Hook
