# Deep Agent Generator — Design

## Overview

The Deep Agent Generator is designed as a multi-stage template-driven assembler that consumes engineering artifacts from all upstream engines and produces a complete, deployable project. The design separates concerns between project structure decisions, code generation, configuration assembly, and documentation production, each driven by versioned templates and customizable through override mechanisms.

## Architecture

The generator sits downstream of all Engineering Engines, consuming their collective output through the GOE's artifact system. It operates as a pipeline of generation stages: Structure → Code → Configuration → Documentation → Assembly. Each stage applies templates to engineering artifacts, producing file-level outputs that are assembled into the final project package.

## Key Design Decisions

### DD-1: Template-Driven Generation
- **Context:** Generated projects must be consistent, repeatable, and customizable without modifying generator code.
- **Decision:** All generation is driven by versioned templates (Handlebars-style) that receive engineering artifacts as context. Templates are resolved in priority order: custom project templates > skill-level templates > built-in defaults.
- **Consequences:** Generation is predictable and auditable; customization is explicit; but template maintenance overhead scales with supported project types.

### DD-2: Multi-Stage Assembly Pipeline
- **Context:** Generating a complete project involves heterogeneous outputs (code, YAML, markdown, Dockerfile) with cross-file dependencies.
- **Decision:** Generation proceeds in ordered stages — structure first, then code, then configuration, then documentation — allowing later stages to reference outputs of earlier stages.
- **Consequences:** Cross-file references resolve correctly; generation is debuggable stage by stage; but adds complexity to the generation flow.

### DD-3: Non-Destructive Regeneration
- **Context:** Developers may customize generated projects and later want to regenerate parts without losing their changes.
- **Decision:** The generator marks generated sections with boundary comments (`// GENERATED: DO NOT EDIT BELOW` / `// END GENERATED`). Regeneration only replaces marked sections, preserving manual edits outside boundaries.
- **Consequences:** Safe regeneration; developer freedom to extend; but boundary markers add slight noise to generated code.

## Components and Interfaces

### Components

- **Project Scaffolder** — Creates directory structure and initial files from the project template
- **Code Generator** — Produces implementation code from engineering artifacts and code templates
- **Config Generator** — Produces configuration files from architecture and component decisions
- **Documentation Generator** — Produces documentation from engineering artifacts and doc templates
- **Template Engine** — Resolves, loads, and renders templates with artifact context
- **Template Registry** — Manages template versions, overrides, and resolution order
- **Output Assembler** — Collects all stage outputs into the final project package
- **Generation Hook** — Extension point for custom generation logic

### Interfaces

- **Input Interface:** Receives `GenerationContext` containing all engineering artifacts from upstream engines
- **Template Interface:** `resolve(templateName, type): Template` — template lookup and loading
- **Output Interface:** Produces `ProjectPackage` containing all generated files with metadata
- **Hook Interface:** `onPreGenerate(context)`, `onPostGenerate(package)` — custom generation logic

## Data Models

```yaml
GenerationContext:
  sessionId: string
  engineArtifacts:
    requirements: RequirementsArtifact
    architecture: ArchitectureArtifact
    components: ComponentArtifact[]
    harness: HarnessArtifact
    workflow: WorkflowArtifact
    memory: MemoryArtifact
    prompts: PromptArtifact[]
  config: GenerationConfig

Template:
  name: string
  version: string
  type: enum (structure | code | config | documentation)
  source: enum (custom | project | default)
  content: string (template markup)
  metadata: object

ProjectPackage:
  sessionId: string
  files: GeneratedFile[]
  manifest: PackageManifest
  completenessReport: CompletenessCheck
  generatedAt: timestamp

GeneratedFile:
  path: string (workspace-relative)
  content: string
  type: enum (code | config | documentation | deployment | test)
  sourceTemplate: string
  sourceArtifact: string
  hasBoundaryMarkers: boolean
  checksum: string

GenerationConfig:
  templateOverrides: Map<templateName, templatePath>
  languages: string[]
  formatting: FormattingConfig
  boundaryMarkers: boolean
  hooks: HookConfig[]
```

## Data Flow

1. GOE provides complete `GenerationContext` (all engineering artifacts) to generator
2. Project Scaffolder creates directory structure from architecture decisions
3. Code Generator renders code templates with component, workflow, and harness artifacts
4. Config Generator renders configuration templates with architecture and integration artifacts
5. Documentation Generator renders doc templates with all engineering artifacts
6. Output Assembler collects all files, verifies completeness, produces `ProjectPackage`
7. Generation Hook runs post-generation logic (e.g., formatting, linting)
8. `ProjectPackage` is emitted to the Output Generation system

## Error Handling

- **Missing Engineering Artifact:** Generator reports which artifact is missing and which engine should have produced it; generation halts.
- **Template Resolution Failure:** Falls back to default template; if no default exists, reports error and halts.
- **Code Generation Error:** Generated code that fails syntax checks is reported with the template and context that produced it.
- **Assembly Conflict:** File path collisions are detected and reported; first-writer-wins with warning.
- **Completeness Check Failure:** Missing required files are reported; generation marked as incomplete.

## Correctness Properties

### Property 1: Template Resolution Determinism
Given the same template registry state, template resolution for a given name always returns the same template (priority order: custom > project > default).

### Property 2: Completeness Invariant
A `ProjectPackage` marked as complete contains every file required by the DAEP project structure standard for the given agent type.

### Property 3: Boundary Marker Integrity
Regeneration never modifies content outside boundary markers; content within markers is always replaced completely.

### Property 4: Cross-Reference Resolution
All internal references (imports, links, config keys) within a `ProjectPackage` resolve to existing files within the same package.

### Property 5: Idempotency
Running the generator with identical `GenerationContext` produces byte-identical output files (excluding timestamps in metadata).

## Testing Strategy

- **Unit Tests:** Test each generator stage in isolation (Scaffolder, Code Generator, Config Generator, Doc Generator, Assembler) with known artifact inputs and expected file outputs.
- **Template Tests:** Verify template resolution priority (custom > project > default) and correct rendering with various context inputs.
- **Boundary Marker Tests:** Generate, modify external sections, regenerate, and verify external modifications are preserved while marked sections are updated.
- **Completeness Tests:** Generate projects for each supported agent type and verify all required files are present.
- **Idempotency Tests:** Run generation twice with identical inputs and verify byte-identical outputs.
- **Error Handling Tests:** Simulate missing artifacts, missing templates, and syntax errors in generated code, verifying correct error reporting.

## Extension Points

- Custom project templates for new agent types
- Custom code generators for new languages or frameworks
- Generation hooks for post-processing (formatting, linting, optimization)
- Template registry extensions for enterprise-specific patterns
- Custom documentation generators for non-standard formats
