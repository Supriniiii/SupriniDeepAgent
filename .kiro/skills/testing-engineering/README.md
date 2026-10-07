# Testing Engineering

## Purpose
Generates comprehensive test suites for Deep Agents covering unit, integration, workflow, performance, and security testing. Ensures every generated agent is thoroughly tested before deployment with automated verification at every layer.

## Responsibilities
- Analyze agent requirements to derive test requirements
- Design test strategies aligned with agent architecture
- Generate unit tests for individual components
- Generate integration tests for component interactions
- Generate workflow tests for end-to-end execution paths
- Generate performance tests for load and stress scenarios
- Generate security tests for vulnerability detection

## Inputs
- Agent requirements specification
- Architecture documentation
- Component interfaces and contracts
- Performance SLOs and constraints

## Outputs
- test-plan.md
- Unit test suite
- Integration test suite
- Workflow test suite

## Dependencies
- Testing Engineering Engine (conceptual)
- Knowledge Base (testing/)
- Test Templates
- Coverage Analysis Tools

## Integration
- Generation Orchestration Engine
- Testing Engineering Engine
- Validation Engineering Engine
- Evaluation Engineering Engine

## Usage
Invoke this skill when a generated agent requires test coverage, when test suites need updating after changes, or when test strategy design is needed for a new agent architecture.

## Best Practices
- Design tests before or alongside implementation, not after
- Ensure tests are deterministic and repeatable
- Cover both happy path and error scenarios
- Include boundary conditions and edge cases
- Maintain test independence to avoid cascading failures

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Produces deterministic outputs
