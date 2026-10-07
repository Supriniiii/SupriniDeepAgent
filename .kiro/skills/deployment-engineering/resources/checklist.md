# Deployment Engineering Checklist

- [ ] Dockerfile uses multi-stage builds and runs as non-root user with minimal base image
- [ ] All environment-specific configuration is externalized via ConfigMaps, Secrets, or environment variables
- [ ] Kubernetes manifests include resource limits, readiness probes, and liveness probes
- [ ] CI/CD pipeline includes automated testing gate that blocks deployment on test failure
- [ ] Deployment strategy supports zero-downtime rollback without data loss
