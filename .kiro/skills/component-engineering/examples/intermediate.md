# Intermediate Example

## Prompt
"Identify and define components for a data analysis agent with planner-executor architecture. The agent needs database connectors (PostgreSQL, MongoDB, Snowflake), a transformation engine, visualization generator, and narrative engine."

## Expected Behavior
The component-engineering skill:
1. Extracts required components: planner, executor, 3 database connectors, transformation engine, visualization generator, narrative engine
2. Searches registry: finds PostgreSQL adapter (v3.0), MongoDB connector (v2.4), base visualization component (v1.8)
3. Reuse assessment: PostgreSQL adapter (reuse as-is), MongoDB connector (reuse as-is), Snowflake connector (build new — not in registry), visualization (adapt existing — needs chart extensions), transformation engine (build new), narrative engine (build new)
4. Defines new components: SnowflakeConnector, TransformationEngine, NarrativeEngine
5. Defines adapter: EnhancedVisualization (extends existing with chart capabilities)
6. Specifies interfaces for all 8 components including shared DataResult contract
7. Maps dependencies: planner → executor → [workers] → [output engines]
8. Identifies shared interface patterns: all connectors implement DataSource interface

## Expected Output
- `component-plan.md` with 8 components: 2 reused, 1 adapted, 5 specified for build
- Shared `DataSource` interface that all connectors implement
- Interface definitions for all component boundaries
- Dependency graph showing planner-executor-worker relationships
- Detailed specifications for SnowflakeConnector, TransformationEngine, NarrativeEngine
