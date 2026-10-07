# Validation

## Purpose
Acts as the quality gate for all generated artifacts, ensuring completeness, correctness, and compliance with engineering standards. Produces validation reports that determine whether a generated solution is production-ready.

## Responsibilities
- Validate requirements completeness and traceability
- Validate architecture decisions and patterns
- Validate component design and interfaces
- Validate workflow correctness and efficiency
- Validate memory strategy appropriateness
- Validate prompt quality and effectiveness
- Validate security posture and compliance
- Validate governance and regulatory requirements
- Produce comprehensive validation reports

## Inputs
- Generated agent artifacts (all layers)
- Engineering standards and benchmarks
- Security policies and compliance requirements
- Architecture decision records

## Outputs
- validation-report.md
- compliance-report.md
- traceability-matrix.md
- production-readiness.md

## Dependencies
- Validation Engineering Engine
- Knowledge Base (validation/, governance/)
- Compliance Templates
- Quality Benchmarks

## Integration
- Generation Orchestration Engine
- Validation Engineering Engine
- Evaluation Engineering Engine
- Security Engine

## Usage
Invoke this skill when generated artifacts need quality validation, when compliance checks are required, or when production-readiness determination is needed before deployment.

## Best Practices
- Validate early and often during the generation process
- Fail fast on critical validation errors
- Provide clear remediation guidance for every failure
- Maintain traceability from requirements to implementation
- Version validation criteria alongside the artifacts they check

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Produces deterministic outputs
