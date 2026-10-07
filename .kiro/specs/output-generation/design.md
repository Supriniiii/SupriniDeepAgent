# Output Generation — Design

## Overview

The Output Generation system is designed as a pipeline that receives generated artifact packages, validates them, applies formatting and compliance rules, and delivers them atomically to the target workspace. The design emphasizes integrity (no data loss), traceability (every file has a source), and atomicity (all-or-nothing delivery).

## Architecture

The system operates as the final stage of the DAEP generation pipeline, receiving `ProjectPackage` objects from the Deep Agent Generator and delivering validated, formatted outputs to the workspace. It coordinates with the Validation Framework for output-level validation and with the GOE for delivery lifecycle management.

## Key Design Decisions

### DD-1: Staged Output Pipeline
- **Context:** Output delivery requires multiple processing steps (validation, formatting, conflict resolution, writing) that must execute in order with clear failure semantics.
- **Decision:** Implement as a staged pipeline: Receive → Validate → Format → Resolve Conflicts → Deliver → Manifest. Each stage can reject the output with specific reasons.
- **Consequences:** Clear failure semantics at each stage; easy to diagnose where delivery failed; but adds processing time to the delivery path.

### DD-2: Atomic Delivery via Staging Directory
- **Context:** Partial delivery (some files written, some not) leaves the workspace in an inconsistent state that's hard to recover from.
- **Decision:** Write all output to a staging directory first; after full validation of the staged output, move atomically to the target location. If any failure occurs during staging, the staging directory is cleaned up.
- **Consequences:** Workspace never in inconsistent state; failed deliveries leave no trace; but requires temporary disk space for staging.

### DD-3: Template-Driven Formatting
- **Context:** Output formats must be consistent and standards-compliant, but formatting rules vary by file type and project configuration.
- **Decision:** Apply formatting as a pipeline stage using registered formatters keyed by file type (e.g., Prettier for JS/TS, Black for Python, rustfmt for Rust). Formatters are configurable and skippable.
- **Consequences:** Consistent output formatting; formatter registration is extensible; but formatter availability must be checked at startup.

## Components and Interfaces

### Components

- **Package Receiver** — Accepts `ProjectPackage` from upstream, validates package structure
- **Output Validator** — Runs validation rules against all artifacts (syntax, schema, completeness)
- **Output Formatter** — Applies language-specific formatting to code artifacts
- **Conflict Resolver** — Detects and resolves conflicts with existing workspace files
- **Staging Manager** — Manages the staging directory for atomic delivery
- **Delivery Writer** — Performs the final atomic move from staging to target
- **Manifest Generator** — Produces the output manifest with checksums and traceability
- **Delivery Reporter** — Produces human-readable delivery reports

### Interfaces

- **Input Interface:** Receives `ProjectPackage` from Deep Agent Generator via GOE
- **Validation Interface:** Delegates to Validation Framework for rule execution
- **Formatter Interface:** `format(content, fileType, config): FormattedContent` — pluggable formatting
- **Output Interface:** Writes files to workspace; produces `DeliveryManifest` and `DeliveryReport`

## Data Models

```yaml
DeliveryManifest:
  sessionId: string
  deliveredAt: timestamp
  files: DeliveredFile[]
  totalFiles: number
  totalSize: number (bytes)
  checksum: string (package-level)

DeliveredFile:
  path: string (workspace-relative)
  type: enum (code | config | documentation | deployment | test)
  size: number (bytes)
  checksum: string
  sourceArtifact: string
  sourceEngine: string
  formatted: boolean
  conflictResolution: enum (none | overwrite | merge | skip) | null

ConflictReport:
  filePath: string
  existingChecksum: string
  newChecksum: string
  resolution: enum (overwrite | merge | skip | unresolvable)
  mergeStrategy: string | null

DeliveryReport:
  sessionId: string
  status: enum (success | partial | failed)
  filesDelivered: number
  filesSkipped: number
  conflictsResolved: number
  validationPassed: boolean
  formattingApplied: boolean
  duration: number (ms)
  errors: string[]

StagingContext:
  stagingDir: string (absolute path)
  targetDir: string (absolute path)
  files: StagedFile[]
  integrityVerified: boolean
  cleanupOnFailure: boolean
```

## Data Flow

1. GOE passes `ProjectPackage` to Package Receiver
2. Output Validator checks all artifacts for integrity and correctness
3. Output Formatter applies formatting rules per file type
4. Conflict Resolver checks target paths against existing workspace state
5. Staging Manager writes all files to temporary staging directory
6. Staging Manager verifies staged output integrity (checksums)
7. Delivery Writer performs atomic move from staging to target
8. Manifest Generator produces `DeliveryManifest` with full traceability
9. Delivery Reporter produces human-readable summary

## Error Handling

- **Package Structure Error:** Rejected at reception; GOE notified with specific structural issue
- **Validation Failure:** Artifacts failing validation are reported with fix suggestions; delivery halted
- **Formatting Error:** Formatter failure on specific file is logged; file delivered unformatted with warning
- **Conflict Detected:** Resolution strategy applied (overwrite/merge/skip per configuration); unresolvable conflicts halt delivery
- **Staging Failure:** Staging directory cleaned up; GOE notified; partial state does not persist
- **Delivery Write Failure:** Atomic move fails; staging preserved for retry; workspace unchanged

## Correctness Properties

### Property 1: Atomicity
After delivery completes, either all files in the package exist at their target paths or none do — no partial state.

### Property 2: Integrity
The checksum of every delivered file matches the checksum recorded in the `DeliveryManifest`.

### Property 3: Traceability
Every file in the `DeliveryManifest` has a non-null `sourceArtifact` and `sourceEngine` linking it to its origin.

### Property 4: Staging Cleanup
If delivery fails at any stage, the staging directory is removed and the workspace remains unchanged from its pre-delivery state.

### Property 5: Conflict Safety
No file in the workspace is overwritten unless the configured conflict resolution strategy explicitly permits it.

### Property 6: Idempotent Delivery
Delivering the same package twice to the same target produces identical workspace state.

## Testing Strategy

- **Unit Tests:** Test Package Receiver validation, Output Validator rules, Formatter registry and execution, Conflict Resolver strategies, and Manifest Generator accuracy.
- **Atomicity Tests:** Simulate failures at each pipeline stage and verify the workspace is unchanged (no partial delivery).
- **Integrity Tests:** Deliver packages and verify all file checksums match the manifest.
- **Conflict Resolution Tests:** Set up existing workspace files with known content, deliver conflicting packages, and verify resolution strategies apply correctly.
- **Staging Tests:** Verify staging directory creation, isolation from target, integrity verification, and cleanup on failure.
- **End-to-End Tests:** Deliver complete project packages and verify all files exist, are correctly formatted, and the manifest is accurate.

## Extension Points

- Custom formatters registered per file type
- Custom validation rules for enterprise-specific compliance
- Alternative delivery targets (Git branch, archive, remote)
- Custom conflict resolution strategies
- Post-delivery hooks (e.g., Git commit, CI trigger)
- Custom manifest formats for enterprise tooling integration
