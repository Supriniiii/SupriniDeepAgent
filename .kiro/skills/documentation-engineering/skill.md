# Documentation Engineering

## Skill Definition

name: documentation-engineering
description: Generates comprehensive documentation packages for Deep Agents and their components
version: 1.0.0
category: engineering
trigger: When generated artifacts require documentation or when documentation completeness must be validated

## Required Inputs
- Engineering artifacts: Complete set of generated code, configuration, and specifications
- Architecture documentation: ADRs, component diagrams, and system architecture
- API contracts: Interface definitions, request/response schemas, and protocols

## Optional Inputs
- Existing documentation for update/extension
- Target audience specification
- Documentation style guide preferences

## Workflow

### Step 1: Analyze Engineering Artifacts
Review all generated artifacts to determine documentation scope and content requirements.
- Engine: Documentation Engineering Engine
- Knowledge: all domains
- Output: Documentation scope and outline

### Step 2: Generate README
Create the project README with purpose, quickstart, configuration, and usage instructions.
- Engine: Documentation Engineering Engine
- Knowledge: all domains
- Output: README.md

### Step 3: Generate Architecture Docs
Create architecture documentation including diagrams, patterns, and decision records.
- Engine: Documentation Engineering Engine
- Knowledge: architecture/
- Output: Architecture documentation

### Step 4: Generate API Docs
Create API documentation from interfaces, contracts, and schemas.
- Engine: Documentation Engineering Engine
- Knowledge: components/, interfaces/
- Output: API documentation

### Step 5: Generate Deployment Guide
Create deployment and operations documentation from deployment assets.
- Engine: Documentation Engineering Engine
- Knowledge: deployment/
- Output: Deployment guide

### Step 6: Generate Developer Guide
Create developer-focused documentation for contribution and extension.
- Engine: Documentation Engineering Engine
- Knowledge: all domains
- Output: Developer guide

### Step 7: Validate Completeness
Check documentation against completeness criteria and identify gaps.
- Engine: Documentation Engineering Engine
- Knowledge: validation/
- Output: Documentation completeness report

### Step 8: Produce Documentation Package
Compile all documentation into a cohesive, navigable package.
- Engine: Documentation Engineering Engine
- Knowledge: all domains
- Output: Complete documentation package

## Engineering Rules
- Documentation must accurately reflect the current state of implementation
- Every public interface must be documented with examples
- Architecture decisions must include rationale and alternatives considered
- Deployment docs must include troubleshooting guides
- Developer docs must include local development setup instructions

## Knowledge Sources
- All knowledge domains (architecture/, components/, deployment/, testing/, observability/, security/)

## Templates Used
- readme-template
- architecture-doc-template
- api-doc-template
- deployment-guide-template
- developer-guide-template

## Engineering Engines Invoked
- Documentation Engineering Engine
- Validation Engineering Engine

## Hooks Invoked
- pre-documentation-generation
- post-documentation-validation
- completeness-check-trigger

## Validation
- All required documentation sections are present
- Documentation accurately reflects implementation
- Examples are runnable and produce expected results
- No broken links or missing references

## Expected Outputs
- README.md
- Architecture documentation
- API documentation
- Developer and deployment guides

## Completion Criteria
- All documentation sections generated and validated
- Completeness check passes against documentation standards
- Cross-references are consistent and accurate
- Documentation package is navigable and cohesive
