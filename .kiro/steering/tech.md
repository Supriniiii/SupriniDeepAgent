# Technology Stack

## Engineering Philosophy

The platform follows an architecture-first engineering methodology.

Technology choices are driven by business capabilities rather than developer preferences.

Implementation should always follow completed architecture and design activities.

---

## AI Engineering

Deep Agents should be designed using modular AI engineering principles.

Prefer:

- Planner-Executor architectures
- Reflection patterns
- Verification stages
- Memory-aware workflows
- Retrieval where appropriate
- Multi-step reasoning

Simple single-prompt solutions should only be used when complexity does not justify a deeper architecture.

---

## Components

Always search for reusable components before creating new ones.

Components should have:

- Clear responsibilities
- Well-defined interfaces
- Independent testing
- Independent documentation

Avoid duplicated functionality.

---

## Tool Integration

Prefer approved enterprise integrations.

Avoid direct API implementations when reusable adapters, MCP servers, or existing enterprise capabilities are available.

---

## Memory

Select memory strategies based on business requirements.

Possible memory types include:

- Working Memory
- Conversation Memory
- Semantic Memory
- Long-Term Memory
- Checkpoint Memory
- Artifact Memory

Memory should never be added unnecessarily.

---

## Prompt Engineering

Prompts should be:

- Modular
- Versioned
- Documented
- Reusable
- Evaluated

Avoid embedding long prompts directly inside implementation code.

---

## Observability

Generated systems should support:

- Structured logging
- Metrics
- Distributed tracing
- Health checks
- Error reporting

Observability should be considered a first-class capability.

---

## Security

Always:

- Externalize secrets.
- Apply least privilege.
- Use secure authentication.
- Protect sensitive information.
- Enable audit logging.

Never:

- Hard-code credentials.
- Store secrets in source code.
- Disable security checks.

---

## Validation

Every generated solution should be validated before completion.

Validation should cover:

- Requirements
- Architecture
- Components
- AI quality
- Testing
- Security
- Documentation
- Deployment

Generation is not complete until validation succeeds.
