# Evaluation Engineering Standards

1. **Comprehensive Coverage**: Every evaluation must assess all defined quality dimensions (architecture, engineering, workflow, memory, prompts, security, testing, documentation). No dimension may be omitted without explicit justification.

2. **Quantitative Scoring**: All evaluations must produce numeric scores on a consistent scale. Qualitative assessments complement but never replace quantitative metrics.

3. **Benchmark Reproducibility**: Evaluation methodology must be fully documented such that the same artifacts evaluated under the same benchmarks produce identical scores regardless of when or by whom the evaluation is performed.

4. **Actionable Recommendations**: Every identified gap must include a specific, actionable recommendation with clear priority (critical/high/medium/low) and estimated implementation effort.

5. **Production Readiness Gate**: Evaluation results must include an explicit production-readiness verdict (READY/NOT READY) with clear blocking items listed when the verdict is NOT READY.
