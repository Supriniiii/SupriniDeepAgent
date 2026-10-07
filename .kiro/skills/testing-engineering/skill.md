# Testing Engineering

## Skill Definition

name: testing-engineering
description: Generates comprehensive test suites covering all testing levels for Deep Agents
version: 1.0.0
category: engineering
trigger: When a generated agent requires test coverage or when test strategy design is needed

## Required Inputs
- Agent requirements specification: Functional and non-functional requirements to derive test cases from
- Architecture documentation: Component structure and interaction patterns to determine test boundaries
- Component interfaces: API contracts and data schemas to validate against

## Optional Inputs
- Performance SLOs for load test threshold definition
- Existing test suites for coverage gap analysis
- Security threat model for targeted security testing

## Workflow

### Step 1: Analyze Requirements
Extract testable requirements and acceptance criteria from the agent specification.
- Engine: Testing Engineering Engine
- Knowledge: testing/
- Output: Test requirements matrix

### Step 2: Design Test Strategy
Define the overall testing approach, coverage targets, and test architecture.
- Engine: Testing Engineering Engine
- Knowledge: testing/
- Output: Test strategy document

### Step 3: Generate Unit Tests
Create unit tests for individual components, functions, and modules.
- Engine: Testing Engineering Engine
- Knowledge: testing/
- Output: Unit test suite

### Step 4: Generate Integration Tests
Create tests validating interactions between components and external dependencies.
- Engine: Testing Engineering Engine
- Knowledge: testing/
- Output: Integration test suite

### Step 5: Generate Workflow Tests
Create end-to-end tests validating complete execution paths and scenarios.
- Engine: Testing Engineering Engine
- Knowledge: testing/
- Output: Workflow test suite

### Step 6: Generate Performance Tests
Create load, stress, and endurance tests validating performance requirements.
- Engine: Testing Engineering Engine
- Knowledge: testing/
- Output: Performance test suite

### Step 7: Generate Security Tests
Create tests targeting authentication, authorization, input validation, and known vulnerabilities.
- Engine: Testing Engineering Engine
- Knowledge: testing/
- Output: Security test suite

### Step 8: Produce Test Plan
Compile all test artifacts into a comprehensive test plan with execution instructions.
- Engine: Testing Engineering Engine
- Knowledge: testing/
- Output: Complete test plan

## Engineering Rules
- Every requirement must have at least one corresponding test
- Tests must be deterministic and produce consistent results
- Integration tests must use controlled test doubles where appropriate
- Performance tests must define clear pass/fail thresholds
- Security tests must cover OWASP top risks relevant to the architecture

## Knowledge Sources
- testing/

## Templates Used
- test-plan-template
- unit-test-template
- integration-test-template
- workflow-test-template
- performance-test-template

## Engineering Engines Invoked
- Testing Engineering Engine
- Validation Engineering Engine

## Hooks Invoked
- pre-test-generation
- post-test-generation
- coverage-analysis-trigger

## Validation
- All testable requirements have corresponding test cases
- Test coverage meets minimum thresholds
- Tests are executable and produce deterministic results
- No orphan tests exist without requirement traceability

## Expected Outputs
- test-plan.md
- Unit test suite
- Integration test suite
- Workflow test suite

## Completion Criteria
- Test plan covers all testing levels
- All testable requirements are traced to test cases
- Tests are generated, syntactically valid, and ready for execution
- Coverage analysis confirms threshold compliance
