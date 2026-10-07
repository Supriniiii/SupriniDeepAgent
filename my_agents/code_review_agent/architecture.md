# Architecture: Code Review Agent

## Pattern

Planner Executor

## Overview

An AI agent that reviews code for quality, best practices, security vulnerabilities, and maintainability issues. Analyzes pull requests and produces structured review feedback.

## Components

| Component | Responsibility |
|-----------|---------------|
| Planner | Decomposes objectives into tasks |
| Executor | Performs planned tasks |
| Memory | Maintains execution context |
| Tool Manager | Coordinates external tools |
| Verifier | Validates outputs |

## Data Flow

Request → Planner → Execution Plan → Executor → Artifacts → Verifier → Output

## Interfaces

- Input: GenerationRequest
- Output: EngineeringArtifacts
- Internal: Context-based artifact passing

## Technology

- Runtime: Python 3.11+
- Framework: DAEP
- Pattern: planner-executor
