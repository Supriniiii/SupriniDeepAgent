# Validation Framework — Design

## Overview

The Validation Framework is designed as a rule-based evaluation system with a pluggable rule engine, configurable quality gates, and scored reporting. It operates both as a pipeline participant (invoked by the GOE at quality gates) and as a standalone validator (invoked by CLI for ad-hoc checks). The architecture separates rule definition from rule execution, enabling declarative rule authoring and independent rule testing.

## Architecture

The framework operates at multiple integration points within DAEP: between engineering phases (inter-engine validation), at the output stage (delivery validation), and on-demand (developer-triggered validation). It consists of a Rule Engine that evaluates declarative rules, a Gate Controller that enforces pass/fail thresholds, and a Report Generator that produces scored assessment reports.

## Key Design Decisions

### DD-1: Declarative Rule System
- **Context:** Validation rules must be maintainable, auditable, and extensible by non-developers (e.g., security team, compliance team).
- **Decision:** Express validation rules as YAML declarations with conditions, severity, category, and message templates. The Rule Engine interprets and executes these declarations against artifacts.
- **Consequences:** Rules are readable and auditable; new rules require no code changes; but complex validation logic may require custom evaluators behind the declarative facade.

### DD-2: Multi-Dimensional Scoring
- **Context:** Production readiness is not binary — different projects have different quality priorities and thresholds.
- **Decision:** Score across configurable dimensions (Architecture: 20, Security: 20, Testing: 20, Documentation: 15, Deployment: 15, Performance: 10) with configurable weights and thresholds per project.
- **Consequences:** Flexible quality assessment; projects can emphasize specific dimensions; but scoring configuration must be managed and versioned.

### DD-3: Gate Controller as Policy Enforcer
- **Context:** Different quality gates in the pipeline have different pass/fail criteria (inter-engine gates are lenient, production gates are strict).
- **Decision:** Implement a Gate Controller that maps quality gate identifiers to threshold configurations, evaluating scores against the appropriate threshold for each gate.
- **Consequences:** Pipeline gates are configurable; same validation logic works at different strictness levels; but gate configuration complexity increases with pipeline length.

## Components and Interfaces

### Components

- **Rule Engine** — Loads, interprets, and executes validation rules against artifacts
- **Rule Registry** — Manages rule definitions, versions, and categories
- **Gate Controller** — Enforces pass/fail thresholds at configured quality gates
- **Scorer** — Calculates dimension scores and composite production readiness scores
- **Report Generator** — Produces structured validation reports with findings, scores, and recommendations
- **Findings Collector** — Aggregates validation findings across all rules and categories
- **Custom Evaluator Host** — Runs imperative validation logic for rules that exceed declarative capabilities

### Interfaces

- **Validation Interface:** `validate(artifacts, gateName): ValidationReport` — primary validation entry point
- **Rule Interface:** `evaluate(artifact, ruleContext): Finding[]` — individual rule execution
- **Gate Interface:** `checkGate(report, gateName): GateResult` — quality gate pass/fail check
- **Report Interface:** `generateReport(findings, scores): ValidationReport` — report production
- **Configuration Interface:** `loadConfig(projectPath): ValidationConfig` — loads project-specific configuration

## Data Models

```yaml
ValidationRule:
  ruleId: string
  category: enum (architecture | security | testing | documentation | deployment | performance)
  severity: enum (error | warning | info)
  condition: string (expression to evaluate)
  message: string (template with placeholders)
  version: string
  gate: string[] (which gates this rule applies to)

Finding:
  ruleId: string
  severity: enum (error | warning | info)
  category: string
  message: string
  location: string (artifact path or section)
  recommendation: string
  evaluatedAt: timestamp

ValidationReport:
  sessionId: string
  gateName: string
  gateResult: enum (pass | fail)
  findings: Finding[]
  scores:
    architecture: number
    security: number
    testing: number
    documentation: number
    deployment: number
    performance: number
  compositeScore: number
  productionReady: boolean
  generatedAt: timestamp

GateConfiguration:
  gateName: string
  thresholds:
    minimum: number (composite score)
    perDimension: Map<dimension, minimumScore>
  failOnError: boolean
  failOnWarning: boolean

ValidationConfig:
  projectPath: string
  gates: GateConfiguration[]
  ruleOverrides: Map<ruleId, override>
  dimensions: DimensionWeight[]
  customEvaluators: string[]
```

## Data Flow

1. GOE or CLI invokes validation with artifacts and gate identifier
2. Rule Engine loads applicable rules from Registry (filtered by gate and artifact type)
3. Rules are evaluated against artifacts, producing Findings
4. Findings Collector aggregates and deduplicates findings
5. Scorer calculates per-dimension and composite scores
6. Gate Controller checks scores against gate thresholds
7. Report Generator produces `ValidationReport` with findings, scores, and gate result
8. Report returned to invoker (GOE or CLI)

## Error Handling

- **Rule Loading Failure:** Missing or invalid rule files are logged; validation proceeds with available rules; report notes skipped rules
- **Evaluation Error:** Individual rule execution failure is caught and logged; finding is marked as "evaluation error"; other rules continue
- **Configuration Error:** Invalid configuration is rejected at startup with specific issues; defaults are not silently applied
- **Gate Threshold Missing:** Missing gate configuration falls back to "strict" defaults; warning emitted
- **Scorer Error:** Scoring failures produce explicit "unable to score" result rather than false pass

## Correctness Properties

### Property 1: Rule Completeness
All rules applicable to the specified gate and artifact type are evaluated; no applicable rule is silently skipped (unless it fails to load, which is reported).

### Property 2: Score Accuracy
The composite score equals the weighted sum of dimension scores using the configured weights, with no rounding errors exceeding 0.01.

### Property 3: Gate Determinism
Given the same findings and gate configuration, the Gate Controller always produces the same pass/fail result.

### Property 4: Finding Deduplication
No two findings in a report share the same (ruleId, location) pair — duplicates are merged.

### Property 5: Fail-Safe Default
If gate configuration is missing or corrupted, the system defaults to strict thresholds (never a false pass).

### Property 6: Evaluation Isolation
A failing custom evaluator does not prevent other rules from executing or corrupt the findings collection.

## Testing Strategy

- **Unit Tests:** Test Rule Engine evaluation logic, Scorer calculation accuracy, Gate Controller threshold checking, and Findings Collector deduplication.
- **Rule Tests:** Test each validation rule category (architecture, security, testing, documentation, deployment, performance) against known-good and known-bad artifacts.
- **Scoring Tests:** Verify dimension score calculations with various findings and weights, including edge cases (zero findings, all failures).
- **Gate Tests:** Test gate pass/fail logic with scores at boundary values (exactly at threshold, just below, just above).
- **Integration Tests:** Run full validation pipeline with realistic artifacts through multiple gates and verify correct report generation.
- **Error Isolation Tests:** Inject failing rules and evaluators, verifying other rules still execute and reports correctly note failures.

## Extension Points

- Custom validation rules added via YAML in the rule registry
- Custom evaluators for complex validation logic
- Custom report formats (JSON, HTML, PDF)
- Custom scoring dimensions and weights
- Custom gate configurations per environment
- Integration with external validation tools (linters, security scanners)
