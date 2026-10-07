# Deep Agent Generation Standards

## 1. Engineering-Before-Implementation
No implementation code shall be generated until requirements engineering, architecture design, component selection, workflow design, memory strategy, and prompt strategy are complete and documented. Each phase must produce an explicit output before the next phase begins.

## 2. Full Pipeline Execution
Every generation request must traverse all 15 phases of the DAEP pipeline. If a phase is not applicable to the request, the skill must explicitly document why and proceed. Skipping phases silently is prohibited.

## 3. Deterministic Orchestration
Given identical inputs, the master skill must produce consistent, reproducible outputs. All decisions must be traceable to requirements, architecture constraints, or documented engineering rationale. No implicit assumptions are permitted.

## 4. Validation-Gated Completion
Generation is not complete until the Validation Engine confirms production readiness. Quality scores must meet the 87% threshold. All tests must pass. Security review must clear. Documentation must be verified complete.

## 5. Reuse Maximization
The skill must search existing component registries, capability catalogs, and enterprise integrations before generating new implementations. Duplication of available functionality is a generation failure requiring correction before validation can pass.
