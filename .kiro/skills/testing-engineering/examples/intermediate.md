# Intermediate Example

## Prompt
"Generate a complete test suite for a multi-step data processing agent that reads from an API, transforms data, and writes to a database. Include integration tests with mocked external dependencies."

## Expected Behavior
The skill analyzes the multi-component architecture, generates unit tests for each processing stage, creates integration tests with mock API and database layers, generates workflow tests for the full pipeline, and produces a test plan with coverage analysis.

## Expected Output
- test-plan.md with multi-level test strategy and coverage targets
- Unit tests for API client, data transformer, and database writer
- Integration tests with mock HTTP server and in-memory database
- Workflow tests for the complete data pipeline
- Test configuration for different environments
