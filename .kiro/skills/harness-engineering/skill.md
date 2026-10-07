# Harness Engineering

## Skill Definition

name: harness-engineering
description: Designs and generates runtime environments and execution infrastructure for Deep Agents
version: 1.0.0
category: engineering
trigger: When a Deep Agent requires a runtime harness or execution environment design

## Required Inputs
- Agent architecture specification: The architectural design describing the agent's structure and patterns
- Business requirements: Functional and non-functional requirements driving harness decisions
- Execution model preference: Synchronous, asynchronous, event-driven, or hybrid execution needs

## Optional Inputs
- Existing harness catalog reference
- Performance and scalability constraints
- Target deployment environment

## Workflow

### Step 1: Analyze Architecture
Review the agent architecture to understand execution patterns, component interactions, and runtime needs.
- Engine: Harness Engineering Engine
- Knowledge: harnesses/, architecture/
- Output: Architecture analysis summary

### Step 2: Determine Runtime Requirements
Extract runtime requirements from business and non-functional requirements.
- Engine: Harness Engineering Engine
- Knowledge: harnesses/, workflows/
- Output: Runtime requirements document

### Step 3: Select Harness Type
Choose the appropriate harness pattern (loop, pipeline, event-driven, distributed).
- Engine: Harness Engineering Engine
- Knowledge: harnesses/
- Output: Harness type selection with justification

### Step 4: Define Lifecycle
Design the agent lifecycle including initialization, execution, pause, resume, and termination.
- Engine: Harness Engineering Engine
- Knowledge: harnesses/, workflows/
- Output: Lifecycle state machine definition

### Step 5: Design State Management
Define how agent state is stored, accessed, and mutated during execution.
- Engine: Harness Engineering Engine
- Knowledge: harnesses/, memory/
- Output: State management specification

### Step 6: Define Checkpointing
Design checkpointing strategy for durability and recovery.
- Engine: Harness Engineering Engine
- Knowledge: harnesses/, observability/
- Output: Checkpointing specification

### Step 7: Define Recovery
Design recovery mechanisms for failure scenarios.
- Engine: Harness Engineering Engine
- Knowledge: harnesses/, observability/
- Output: Recovery strategy document

### Step 8: Produce Specification
Compile all designs into the final harness specification package.
- Engine: Harness Engineering Engine
- Knowledge: harnesses/, workflows/, observability/
- Output: Complete harness specification

## Engineering Rules
- Never generate business logic before harness design is complete
- Always validate harness compatibility with selected architecture
- Ensure checkpointing does not introduce unacceptable latency
- Design for observability from the start
- Recovery mechanisms must handle both transient and permanent failures

## Knowledge Sources
- harnesses/
- workflows/
- observability/
- architecture/

## Templates Used
- harness-specification-template
- lifecycle-model-template
- execution-model-template
- runtime-architecture-template

## Engineering Engines Invoked
- Harness Engineering Engine
- Validation Engineering Engine

## Hooks Invoked
- pre-harness-validation
- post-harness-generation
- architecture-compatibility-check

## Validation
- Harness specification is complete and internally consistent
- Lifecycle covers all required state transitions
- Recovery handles all identified failure modes
- Checkpointing meets durability requirements

## Expected Outputs
- harness-specification.md
- runtime-architecture.md
- execution-model.md
- lifecycle-model.md

## Completion Criteria
- All harness specification documents are generated
- Validation confirms architectural compatibility
- Lifecycle, state, checkpointing, and recovery are fully defined
- Specification is ready to guide implementation
