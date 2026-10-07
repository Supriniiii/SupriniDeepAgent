# Security

## Skill Definition

name: security
description: Designs security postures and controls for Deep Agents including authentication, authorization, and compliance
version: 1.0.0
category: platform
trigger: When a generated agent requires security design or when security compliance must be validated

## Required Inputs
- Agent architecture specification: Component structure and interaction points requiring security controls
- Security requirements: Business and regulatory security mandates
- Data classification: Sensitivity levels of data processed by the agent

## Optional Inputs
- Compliance framework requirements (SOC2, GDPR, HIPAA)
- Existing identity provider configuration
- Threat model or risk assessment

## Workflow

### Step 1: Identify Security Requirements
Extract security requirements from business needs, compliance mandates, and data classification.
- Engine: Validation Engineering Engine
- Knowledge: security/
- Output: Security requirements matrix

### Step 2: Define Authentication
Design authentication mechanisms, identity management, and session handling.
- Engine: Validation Engineering Engine
- Knowledge: security/
- Output: Authentication design

### Step 3: Define Authorization
Design role-based or attribute-based access control models and policies.
- Engine: Validation Engineering Engine
- Knowledge: security/
- Output: Authorization model

### Step 4: Configure Secrets Management
Design secrets storage, rotation, and access patterns.
- Engine: Validation Engineering Engine
- Knowledge: security/
- Output: Secrets management configuration

### Step 5: Define Encryption
Design encryption strategies for data at rest, in transit, and in use.
- Engine: Validation Engineering Engine
- Knowledge: security/
- Output: Encryption specification

### Step 6: Configure Audit Logging
Design security event logging with tamper-proof storage and analysis.
- Engine: Validation Engineering Engine
- Knowledge: security/, observability/
- Output: Audit logging configuration

### Step 7: Validate Security Posture
Verify the complete security design against standards and known threats.
- Engine: Validation Engineering Engine
- Knowledge: security/, validation/
- Output: Security posture assessment

### Step 8: Produce Security Plan
Compile all security designs into a comprehensive security plan.
- Engine: Validation Engineering Engine
- Knowledge: security/
- Output: Complete security plan

## Engineering Rules
- Never hard-code credentials, tokens, or secrets in any artifact
- Apply least privilege to all access controls without exception
- Encrypt all data in transit using TLS 1.2+
- Audit log all authentication and authorization events
- Secrets must support rotation without service interruption

## Knowledge Sources
- security/

## Templates Used
- security-requirements-template
- authentication-config-template
- authorization-config-template
- audit-logging-template
- encryption-specification-template

## Engineering Engines Invoked
- Validation Engineering Engine (security aspect)

## Hooks Invoked
- pre-security-design
- post-security-validation
- secrets-scan-trigger
- compliance-check-trigger

## Validation
- No hard-coded secrets exist in any artifact
- Authentication covers all entry points
- Authorization enforces least privilege
- Audit logging captures all security-relevant events

## Expected Outputs
- security-requirements.md
- Authentication configuration
- Authorization configuration
- Audit logging configuration

## Completion Criteria
- All security controls are designed and documented
- No secrets are exposed in any generated artifact
- Authentication and authorization cover all access paths
- Audit logging is configured for all security events
- Security posture assessment passes validation
