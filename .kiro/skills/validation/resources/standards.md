# Validation Standards

1. **Complete Dimension Coverage**: Validation must check all defined dimensions (requirements, architecture, components, workflow, memory, prompts, security, governance). Partial validation is never acceptable for production-readiness determination.

2. **Evidence-Based Verdicts**: Every pass/fail determination must be accompanied by specific evidence. Claims without evidence are treated as failures. Evidence must be traceable to specific artifacts and criteria.

3. **Blocking Failure Escalation**: Critical failures must immediately block the deployment pipeline. The validation system must distinguish between critical (blocking), major (requires remediation plan), and minor (advisory) findings.

4. **Remediation Guidance**: Every failure must include specific, actionable remediation guidance. Guidance must identify the exact artifact to fix, the criteria not met, and a suggested approach to resolution.

5. **Reproducibility**: Validation results must be deterministic. Running validation against the same artifacts with the same criteria must produce identical results regardless of execution timing or environment.
