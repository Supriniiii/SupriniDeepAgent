# Validation

## Skill Definition

name: validation
description: Quality gate that validates all generated artifacts against engineering standards and compliance requirements
version: 1.0.0
category: platform
trigger: When generated artifacts require validation before deployment or when quality gate checks are needed

## Required Inputs
- Generated artifacts: Complete set of code, configuration, documentation, and specifications
- Engineering standards: Quality benchmarks and validation criteria to check against
- Requirements specification: Original requirements for traceability validation

## Optional Inputs
- Compliance policy documents
- Previous validation results for trend comparison
- Custom validation rules

## Workflow

### Step 1: Validate Requirements
Check that all requirements are addressed and traceable to implementation artifacts.
- Engine: Validation Engineering Engine
- Knowledge: validation/
- Output: Requirements validation result

### Step 2: Validate Architecture
Verify architecture decisions are documented, justified, and correctly implemented.
- Engine: Validation Engineering Engine
- Knowledge: validation/, architecture/
- Output: Architecture validation result

### Step 3: Validate Components
Check component design, interfaces, and implementation against standards.
- Engine: Validation Engineering Engine
- Knowledge: validation/, components/
- Output: Component validation result

### Step 4: Validate Workflow
Verify workflow correctness, completeness of paths, and error handling.
- Engine: Validation Engineering Engine
- Knowledge: validation/, workflows/
- Output: Workflow validation result

### Step 5: Validate Memory
Check memory strategy appropriateness and implementation correctness.
- Engine: Validation Engineering Engine
- Knowledge: validation/, memory/
- Output: Memory validation result

### Step 6: Validate Prompts
Verify prompt quality, modularity, versioning, and documentation.
- Engine: Validation Engineering Engine
- Knowledge: validation/, prompts/
- Output: Prompt validation result

### Step 7: Validate Security
Check security posture including authentication, authorization, and secrets management.
- Engine: Validation Engineering Engine
- Knowledge: validation/, security/
- Output: Security validation result

### Step 8: Validate Governance
Verify compliance with governance policies and regulatory requirements.
- Engine: Validation Engineering Engine
- Knowledge: validation/, governance/
- Output: Governance validation result

### Step 9: Produce Report
Compile all validation results into a comprehensive report with pass/fail verdict.
- Engine: Validation Engineering Engine
- Knowledge: validation/
- Output: Complete validation package

## Engineering Rules
- All validation dimensions must be checked; partial validation is not acceptable
- Any critical failure blocks production deployment
- Validation results must be reproducible given the same inputs
- Remediation guidance must accompany every failure
- Validation criteria must be versioned alongside artifacts

## Knowledge Sources
- validation/
- governance/
- security/
- architecture/

## Templates Used
- validation-report-template
- compliance-report-template
- traceability-matrix-template
- production-readiness-template

## Engineering Engines Invoked
- Validation Engineering Engine

## Hooks Invoked
- pre-validation-check
- post-validation-report
- critical-failure-alert

## Validation
- All dimensions produce pass/fail results with evidence
- Traceability matrix is complete and accurate
- Compliance checks cover all applicable regulations
- Production readiness verdict is justified by evidence

## Expected Outputs
- validation-report.md
- compliance-report.md
- traceability-matrix.md
- production-readiness.md

## Completion Criteria
- All validation dimensions are checked
- Pass/fail verdict is produced with evidence
- Remediation guidance is provided for all failures
- Traceability matrix is complete
- Production readiness determination is justified
