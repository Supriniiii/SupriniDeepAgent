# Security Checklist

- [ ] No secrets, credentials, or tokens are hard-coded in any generated artifact
- [ ] Authentication is configured for all entry points with appropriate mechanism strength
- [ ] Authorization enforces least privilege with explicit deny-by-default policy
- [ ] All data in transit is encrypted (TLS 1.2+ minimum) and sensitive data at rest is encrypted
- [ ] Audit logging captures all authentication, authorization, and data access events with tamper protection
