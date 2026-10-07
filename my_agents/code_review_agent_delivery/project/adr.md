# ADR: Architecture Pattern Selection for Code Review Agent

## Status

Accepted

## Context

The agent requires a structured execution model that separates planning from execution.

## Decision

Selected the planner-executor architecture pattern.

## Consequences

- Clear separation of concerns.
- Supports iterative refinement.
- Enables independent testing of planner and executor.
