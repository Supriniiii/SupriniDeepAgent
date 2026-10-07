# Workflow Engineering

## Skill Definition

```yaml
name: workflow-engineering
description: Designs execution workflows with states, transitions, decision points, error handling, and recovery strategies
version: 1.0.0
category: engineering
trigger: Architecture and components are defined and execution flow needs to be specified as a workflow
```

## Required Inputs
- Architecture Specification: Documented execution flow and component interaction patterns
- Component Plan: Available components with their interfaces and capabilities
- Business Rules: Conditions, constraints, and logic that govern execution flow

## Optional Inputs
- SLA Requirements: Response time, throughput, and availability targets
- Recovery Requirements: Checkpointing, replay, and durability expectations
- Concurrency Model: Parallel execution needs and synchronization constraints
- External System Timings: Latency characteristics of integrated services
- Existing Workflows: Current workflow definitions if extending or modifying

## Workflow

### Step 1: Workflow Scope Identification
Determine workflow boundaries, triggers, and terminal states from architecture.
- Engine: Workflow Engineering Engine
- Knowledge: knowledge/workflows/patterns/
- Output: Workflow scope definition (trigger, boundary, success/failure states)

### Step 2: State Enumeration
Identify all possible states the workflow can occupy.
- Engine: Workflow Engineering Engine
- Knowledge: knowledge/workflows/states/, knowledge/state-machines/
- Output: Complete state enumeration with descriptions

### Step 3: Transition Design
Define transitions between states including guards, actions, and triggers.
- Engine: Workflow Engineering Engine
- Knowledge: knowledge/workflows/transitions/
- Output: Transition table (from → to, trigger, guard, action)

### Step 4: Decision Point Specification
Define branching logic, conditional paths, and decision criteria.
- Engine: Workflow Engineering Engine
- Knowledge: knowledge/workflows/decisions/
- Output: Decision point specifications with conditions and outcomes

### Step 5: Error Path Design
Design error handling for each step: retry, fallback, escalation, and dead-letter paths.
- Engine: Workflow Engineering Engine
- Knowledge: knowledge/workflows/error-handling/, knowledge/error-handling/
- Output: Error handling specification per state/transition

### Step 6: Timeout and Recovery Design
Define timeout durations, recovery procedures, and checkpoint strategies.
- Engine: Workflow Engineering Engine
- Knowledge: knowledge/workflows/recovery/, knowledge/memory/checkpoints/
- Output: Timeout configuration, checkpoint strategy, recovery procedures

### Step 7: Step Contract Definition
Define input/output contracts for each workflow step.
- Engine: Workflow Engineering Engine
- Knowledge: knowledge/workflows/contracts/
- Output: Step contracts with types, validation rules, and transformation specs

### Step 8: Parallel Path Design
Identify parallelizable steps, define fork/join semantics, and synchronization points.
- Engine: Workflow Engineering Engine
- Knowledge: knowledge/workflows/concurrency/
- Output: Parallel execution specification, synchronization barriers

### Step 9: Workflow Assembly
Assemble the complete workflow specification from all designed elements.
- Engine: Workflow Engineering Engine
- Knowledge: knowledge/workflows/assembly/
- Output: workflow-specification.md — complete workflow definition

### Step 10: Workflow Validation
Validate workflow for completeness, reachability, deadlock freedom, and requirements coverage.
- Engine: Workflow Engineering Engine, Validation Engine
- Knowledge: knowledge/validation/workflows/
- Output: Workflow validation report

## Engineering Rules
- Every state must be reachable from the initial state
- Every non-terminal state must have at least one outgoing transition
- All error conditions must have defined handling (no unhandled errors)
- Timeout must be specified for every step involving external systems or I/O
- Workflows must have defined terminal states (success and failure)
- Parallel paths must have explicit synchronization points (join semantics)

## Knowledge Sources
- knowledge/workflows/patterns/ — workflow design patterns
- knowledge/workflows/states/ — state modeling practices
- knowledge/workflows/transitions/ — transition design patterns
- knowledge/workflows/error-handling/ — error recovery strategies
- knowledge/workflows/recovery/ — checkpoint and replay patterns
- knowledge/state-machines/ — formal state machine references
- knowledge/error-handling/ — cross-cutting error handling patterns

## Templates Used
- templates/workflow/specification.md — workflow specification template
- templates/workflow/state-machine.md — state machine definition template
- templates/workflow/error-handling.md — error handling specification template
- templates/workflow/step-contract.md — step contract template
- templates/workflow/diagram.md — workflow diagram template

## Engineering Engines Invoked
- Workflow Engineering Engine (primary)
- Validation Engine (workflow completeness and correctness validation)

## Hooks Invoked
- pre-workflow-design — fires before workflow design begins
- post-state-design — fires after states and transitions defined
- post-workflow-design — fires after complete workflow assembled

## Validation
- All states reachable from initial state (no orphan states)
- All non-terminal states have outgoing transitions (no deadlocks)
- Terminal states are well-defined (explicit success and failure conditions)
- Error handling specified for every step (no unhandled errors)
- Timeouts configured for all external interactions
- Parallel paths have proper synchronization (no race conditions)
- Step contracts are complete and type-consistent
- Workflow satisfies SLA requirements (if specified)
- Checkpoint strategy supports recovery for long-running workflows

## Expected Outputs
- workflow-specification.md — complete workflow with all elements
- State machine definition — formal states and transitions
- Error handling specification — retry, fallback, escalation paths per step
- Step contracts — input/output definitions for every workflow step
- Workflow diagrams — visual representation of flow and decision points
- Workflow validation report — completeness and correctness confirmation

## Completion Criteria
- All workflow states enumerated and described
- All transitions defined with guards and actions
- Decision points specified with clear conditions
- Error handling complete for every step
- Timeout and recovery strategies defined
- Step contracts specified for all steps
- Workflow validated (no deadlocks, all states reachable, all errors handled)
- Downstream implementation has unambiguous workflow specification to follow
