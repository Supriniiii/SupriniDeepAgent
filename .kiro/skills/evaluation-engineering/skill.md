# Evaluation Engineering

## Skill Definition

name: evaluation-engineering
description: Evaluates generated Deep Agents against quality benchmarks and produces optimization recommendations
version: 1.0.0
category: engineering
trigger: When a generated agent requires quality evaluation or benchmark comparison before production deployment

## Required Inputs
- Agent artifacts: The complete set of generated artifacts including code, configuration, and documentation
- Validation report: Results from the validation skill confirming structural completeness
- Quality benchmarks: Target metrics and thresholds for evaluation scoring

## Optional Inputs
- Previous evaluation results for trend comparison
- Custom scoring rubrics
- Performance test results

## Workflow

### Step 1: Review Validation Report
Analyze the validation report to confirm prerequisites are met before evaluation begins.
- Engine: Evaluation Engineering Engine
- Knowledge: validation/
- Output: Validation status confirmation

### Step 2: Evaluate Engineering Quality
Assess code quality, modularity, SOLID adherence, and engineering best practices.
- Engine: Evaluation Engineering Engine
- Knowledge: testing/, validation/
- Output: Engineering quality scores

### Step 3: Evaluate Architecture
Assess architectural decisions, pattern selection, separation of concerns, and scalability.
- Engine: Evaluation Engineering Engine
- Knowledge: validation/, architecture/
- Output: Architecture quality scores

### Step 4: Evaluate Workflow Efficiency
Assess workflow design, execution paths, error handling, and performance characteristics.
- Engine: Evaluation Engineering Engine
- Knowledge: testing/, observability/
- Output: Workflow efficiency scores

### Step 5: Evaluate Memory
Assess memory strategy selection, utilization efficiency, and appropriateness.
- Engine: Evaluation Engineering Engine
- Knowledge: validation/, memory/
- Output: Memory effectiveness scores

### Step 6: Evaluate Prompts
Assess prompt quality, modularity, versioning, and effectiveness.
- Engine: Evaluation Engineering Engine
- Knowledge: testing/, prompts/
- Output: Prompt quality scores

### Step 7: Calculate Scores
Aggregate individual scores into composite quality metrics using weighted scoring.
- Engine: Evaluation Engineering Engine
- Knowledge: validation/
- Output: Composite quality scores

### Step 8: Produce Report
Compile all evaluation data into the final evaluation report with recommendations.
- Engine: Evaluation Engineering Engine
- Knowledge: testing/, validation/, observability/
- Output: Complete evaluation package

## Engineering Rules
- Never skip evaluation dimensions even if partial data is available
- Always compare against established benchmarks
- Provide quantitative scores alongside qualitative assessments
- Recommendations must be actionable and prioritized
- Evaluation methodology must be reproducible

## Knowledge Sources
- testing/
- validation/
- observability/
- architecture/

## Templates Used
- evaluation-report-template
- quality-metrics-template
- benchmark-comparison-template
- optimization-recommendations-template

## Engineering Engines Invoked
- Evaluation Engineering Engine
- Validation Engineering Engine

## Hooks Invoked
- pre-evaluation-check
- post-evaluation-report
- benchmark-comparison-trigger

## Validation
- All evaluation dimensions are scored
- Composite score is calculated correctly
- Recommendations are actionable and prioritized
- Report is complete and internally consistent

## Expected Outputs
- evaluation-report.md
- quality-metrics.md
- benchmark-results.md
- optimization-recommendations.md

## Completion Criteria
- All quality dimensions evaluated and scored
- Composite scores calculated with weighted aggregation
- Benchmark comparison completed
- Optimization recommendations produced with clear priorities
- Evaluation report is ready for stakeholder review
