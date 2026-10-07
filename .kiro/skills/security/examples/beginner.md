# Beginner Example

## Prompt
"Design basic security for a simple internal chatbot agent that requires API key authentication."

## Expected Behavior
The skill identifies the single entry point requiring authentication, designs API key-based authentication with key rotation support, configures basic audit logging for authentication events, and ensures the API key is stored in secrets management rather than code.

## Expected Output
- security-requirements.md with basic security controls for internal service
- Authentication configuration with API key validation and rotation
- Basic authorization (all-or-nothing access with valid key)
- Audit logging for authentication success/failure events
