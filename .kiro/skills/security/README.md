# Security

## Purpose
Designs comprehensive security postures for Deep Agents covering authentication, authorization, secrets management, encryption, and audit logging. Ensures every generated system meets enterprise security standards and compliance requirements.

## Responsibilities
- Identify security requirements from business and compliance needs
- Define authentication mechanisms and identity management
- Define authorization models and access control policies
- Configure secrets management and key rotation
- Define encryption strategies for data at rest and in transit
- Configure audit logging for security events
- Validate security posture against standards

## Inputs
- Agent architecture specification
- Security and compliance requirements
- Data classification and sensitivity levels
- Integration points with external systems

## Outputs
- security-requirements.md
- Authentication configuration
- Authorization configuration
- Audit logging configuration

## Dependencies
- Validation Engineering Engine (security aspect)
- Knowledge Base (security/)
- Security Templates
- Compliance Frameworks

## Integration
- Generation Orchestration Engine
- Validation Engineering Engine
- Harness Engineering Engine
- Observability Engine

## Usage
Invoke this skill when a generated agent requires security design, when security posture needs assessment, or when compliance requirements mandate specific security controls.

## Best Practices
- Apply defense in depth with multiple security layers
- Follow the principle of least privilege for all access controls
- Never hard-code secrets or credentials in any artifact
- Design for auditability from the start
- Assume breach and design containment strategies

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Produces deterministic outputs
