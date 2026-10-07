# Planner–Executor Architecture

## Purpose

The Planner–Executor architecture separates strategic planning from task execution by assigning planning responsibilities to one component (the Planner) and execution responsibilities to another component (the Executor).

This architecture enables Deep Agents to reason about complex problems, decompose them into manageable tasks, and execute those tasks in a controlled and traceable manner.

It is one of the most common architectural patterns used for Deep Agents because it promotes modularity, flexibility, and iterative problem solving.

---

# Objectives

The Planner–Executor architecture aims to:

- Separate planning from execution.
- Improve reasoning quality.
- Support complex, multi-step tasks.
- Enable iterative execution.
- Allow dynamic replanning when required.
- Increase transparency of the engineering process.
- Support human review and intervention.

---

# Core Components

The architecture consists of two primary components:

### Planner

The Planner is responsible for:

- Understanding the developer request.
- Defining objectives.
- Decomposing complex tasks.
- Creating an execution strategy.
- Prioritizing work.
- Revising plans when necessary.

---

### Executor

The Executor is responsible for:

- Performing the planned tasks.
- Calling tools and external services.
- Producing outputs.
- Reporting execution status.
- Returning results to the Planner.

---

# Execution Flow

The Planner–Executor architecture follows this high-level workflow:

```text
Developer Request
│
▼
Planner
│
▼
Execution Plan
│
▼
Executor
│
▼
Task Results
│
▼
Planner Review
│
┌────┴────┐
│         │
Complete   Replan
```

The Planner evaluates execution results and either finalizes the process or generates a revised plan for further execution.

---

# When to Use

The Planner–Executor architecture is suitable when:

- Tasks require multiple steps.
- Planning is separate from execution.
- The solution may need iterative refinement.
- External tools or APIs are involved.
- Human approval may be required between stages.
- Task dependencies must be managed.

Typical use cases include:

- Code review agents.
- Software engineering agents.
- Research agents.
- Documentation agents.
- Enterprise workflow agents.

---

# When Not to Use

This architecture may not be appropriate when:

- The task consists of a single, simple action.
- Real-time responses with minimal latency are required.
- The workflow is completely deterministic.
- Planning overhead outweighs the complexity of the task.

For simple use cases, a single-agent architecture may be more appropriate.

---

# Advantages

The Planner–Executor architecture provides:

- Clear separation of responsibilities.
- Improved reasoning quality.
- Easier debugging.
- Better traceability.
- Reusable planning logic.
- Flexible execution strategies.
- Support for iterative refinement.

---

# Limitations

Potential limitations include:

- Increased implementation complexity.
- Additional execution overhead.
- Higher latency due to planning stages.
- Greater coordination requirements.
- More engineering artifacts to manage.

These trade-offs should be considered during architecture selection.

---

# Integration with DAEP

Within the Deep Agent Engineering Platform, the Planner–Executor architecture is engineered through the coordinated work of multiple Engineering Engines.

- The Requirements Engineering Engine identifies whether planning and execution should be separated.
- The Architecture Engineering Engine selects the Planner–Executor pattern when appropriate.
- The Component Engineering Engine identifies the required planner and executor components.
- The Workflow Engineering Engine defines the execution lifecycle.
- The Memory Engineering Engine determines how planning context and execution state are managed.
- The Prompt Engineering Engine generates prompts for both planning and execution activities.
- The Validation and Evaluation Engineering Engines verify that the architecture satisfies engineering and quality requirements.

---

# Best Practices

When implementing the Planner–Executor architecture:

- Keep planning and execution responsibilities separate.
- Ensure execution plans are explicit and traceable.
- Allow the Planner to revise plans when execution fails.
- Record planning decisions for auditing.
- Minimize unnecessary replanning.
- Validate execution outputs before continuing.

---

# Common Anti-Patterns

Avoid the following:

- Mixing planning and execution logic in a single component.
- Allowing Executors to modify the overall strategy.
- Creating excessively detailed plans for simple tasks.
- Ignoring execution feedback.
- Skipping validation between planning and execution.

---

# Related Knowledge

This architecture works closely with the following knowledge domains:

- Components
- Capabilities
- Workflows
- Memory
- Prompts
- Harnesses
- Validation
- Evaluation

---

# Summary

The Planner–Executor architecture provides a structured approach to solving complex problems by separating planning from execution.

Within the Deep Agent Engineering Platform, it serves as a foundational architectural pattern for engineering Deep Agents that require iterative reasoning, coordinated execution, and production-ready engineering practices.
