# Security Standards

1. **Zero Trust Principle**: No implicit trust is granted based on network location or previous authentication. Every request must be authenticated, authorized, and encrypted regardless of source. Defense in depth is mandatory.

2. **Secrets Externalization**: All secrets, credentials, tokens, and cryptographic keys must be managed through approved secrets management systems. No secret may exist in source code, configuration files, container images, or logs at any point in the lifecycle.

3. **Least Privilege Enforcement**: Every identity (user, service, agent) must be granted only the minimum permissions required to perform its function. Permissions must be scoped to specific resources and actions. Broad permissions require documented justification and periodic review.

4. **Audit Trail Completeness**: All security-relevant events must be logged with sufficient detail for forensic investigation. Audit logs must be tamper-proof, retained per compliance requirements, and queryable for incident response.

5. **Encryption Coverage**: All data in transit must use TLS 1.2 or higher. Sensitive data at rest must be encrypted using approved algorithms (AES-256 minimum). Encryption keys must be rotated on schedule and support emergency rotation without service interruption.
