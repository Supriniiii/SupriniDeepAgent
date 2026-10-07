# Evaluation Engineering

## Purpose
Evaluates the quality, performance, and correctness of generated Deep Agents against engineering standards and benchmarks. Produces quantitative quality metrics and actionable optimization recommendations to ensure production readiness.

## Responsibilities
- Review validation reports for completeness and accuracy
- Evaluate engineering quality against DAEP standards
- Evaluate architectural decisions and patterns
- Assess workflow efficiency and execution performance
- Evaluate memory strategy effectiveness
- Evaluate prompt quality and effectiveness
- Calculate composite quality scores and benchmarks
- Produce evaluation reports with optimization recommendations

## Inputs
- Generated agent artifacts (code, config, docs)
- Validation report from validation skill
- Engineering quality benchmarks
- Performance baselines and SLOs

## Outputs
- evaluation-report.md
- quality-metrics.md
- benchmark-results.md
- optimization-recommendations.md

## Dependencies
- Evaluation Engineering Engine
- Knowledge Base (testing/, validation/, observability/)
- Quality Benchmark Templates
- Scoring Rubrics

## Integration
- Generation Orchestration Engine
- Evaluation Engineering Engine
- Validation Engineering Engine
- Testing Engineering Engine

## Usage
Invoke this skill when a generated agent needs quality evaluation, when benchmark comparisons are required, or when optimization opportunities need to be identified before production deployment.

## Best Practices
- Evaluate against consistent, versioned quality benchmarks
- Separate objective metrics from subjective assessments
- Provide actionable recommendations with clear priority ordering
- Compare against baseline scores from previous evaluations
- Document evaluation methodology for reproducibility

## Engineering Standards
- Follows DAEP Engineering Standards
- Uses Knowledge Base
- Invokes Engineering Engines
- Consumes Templates
- Produces deterministic outputs
