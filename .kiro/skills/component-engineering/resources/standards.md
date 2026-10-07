# Component Engineering Standards

## 1. Reuse-First Principle
Every required capability must be searched against existing component registries before new development is authorized. A new component may only be created when no existing component satisfies the requirement, either directly or through adaptation. Reuse decisions must be documented with justification.

## 2. Single Responsibility
Each component must have exactly one responsibility — one reason to change. Components that accumulate multiple responsibilities must be decomposed. Responsibility boundaries should align with architectural component boundaries.

## 3. Interface-Driven Design
All components must be defined by their interfaces before implementation details are considered. Interfaces must specify: input types, output types, error contracts, preconditions, postconditions, and versioning strategy. Implementations are interchangeable behind interfaces.

## 4. Independent Testability
Every component must be testable in isolation without requiring the full system to be running. Dependencies must be injectable (dependency inversion). Test boundaries align with component boundaries.

## 5. Registry Promotion
Newly created components that demonstrate reuse potential must be designed for registry promotion from the start. This means clear documentation, versioned interfaces, configurable behavior, and no implicit dependencies on the specific solution they were built for.
