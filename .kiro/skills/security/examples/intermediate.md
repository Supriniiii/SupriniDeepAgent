# Intermediate Example

## Prompt
"Design security for a multi-tenant data processing agent with OAuth2 authentication, role-based access control, encrypted data at rest, and compliance audit logging."

## Expected Behavior
The skill designs OAuth2 authentication with OIDC integration, creates a role-based access control model with tenant isolation, configures AES-256 encryption for stored data, implements compliance-grade audit logging with tamper-proof storage, and validates multi-tenant data isolation boundaries.

## Expected Output
- security-requirements.md with multi-tenant security controls and compliance mapping
- OAuth2/OIDC authentication configuration with token validation and refresh
- RBAC model with roles, permissions, and tenant-scoped access policies
- Encryption configuration for data at rest (AES-256) and in transit (TLS 1.3)
- Audit logging configuration with compliance retention and tamper detection
