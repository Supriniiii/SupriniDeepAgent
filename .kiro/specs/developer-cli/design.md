# Developer CLI — Design

## Overview

The Developer CLI is designed as a plugin-based command interface that translates developer intent into DAEP platform actions. It integrates with Kiro as the primary IDE surface while maintaining standalone usability. The design emphasizes discoverability, feedback, and progressive disclosure of capabilities.

## Architecture

The CLI operates as the primary human interface to DAEP, sitting above the GOE and providing conversational command-based access to all platform capabilities. It follows a router-handler pattern where command input is parsed, validated, and dispatched to registered command handlers that interact with the underlying platform APIs. Integration with Kiro happens through the skill invocation mechanism.

## Key Design Decisions

### DD-1: Plugin-Based Command Architecture
- **Context:** DAEP capabilities evolve independently; new commands should be addable without modifying the CLI core.
- **Decision:** Implement a plugin-based command architecture where command handlers are registered dynamically. Each command family (generate, validate, config, status) is an independent plugin that registers its commands and arguments.
- **Consequences:** CLI evolves with the platform; new capabilities are instantly accessible; but command namespace management requires coordination.

### DD-2: Kiro Integration as Primary Surface
- **Context:** Developers interact with DAEP through Kiro's AI-powered IDE; the CLI must be a natural extension of that experience.
- **Decision:** Implement the CLI as a Kiro skill interface that can be invoked through natural language in the Kiro chat, through explicit commands in the terminal, or through Kiro hooks.
- **Consequences:** Seamless IDE experience; natural language access to commands; but Kiro dependency for full experience (standalone mode has reduced capability).

### DD-3: Progressive Disclosure
- **Context:** DAEP has deep capability (10 engines, 5 harnesses, validation, generation) that can overwhelm new users.
- **Decision:** Implement progressive disclosure — simple commands (`generate`) show minimal output by default, with flags (`--verbose`, `--detail`) revealing additional information. Help is layered (basic → advanced → full reference).
- **Consequences:** Low barrier to entry; experts can access full detail; but default behavior must be carefully calibrated.

## Components and Interfaces

### Components

- **Command Router** — Parses input, resolves commands, validates arguments, dispatches to handlers
- **Plugin Loader** — Discovers and registers command handler plugins
- **Skill Launcher** — Translates CLI commands into GOE requests and submits them
- **Progress Reporter** — Subscribes to session events and displays real-time progress
- **Output Presenter** — Displays generated artifacts with formatting, highlighting, and navigation
- **Config Manager** — Manages platform configuration with validation
- **History Tracker** — Records and displays session history

### Interfaces

- **User Interface:** Command-line input with argument parsing and validation
- **Kiro Interface:** Skill invocation protocol for IDE-integrated access
- **GOE Interface:** Submits `GenerationRequest` objects and subscribes to session events
- **Configuration Interface:** Reads/writes `daep.config.yaml` for platform settings
- **Output Interface:** Reads delivery manifests and artifact files for presentation

## Data Models

```yaml
CommandDefinition:
  name: string
  family: string (generate | validate | config | status | output)
  description: string
  arguments: ArgumentDef[]
  flags: FlagDef[]
  handler: string (handler function reference)
  plugin: string (owning plugin)

ArgumentDef:
  name: string
  type: enum (string | number | boolean | file | enum)
  required: boolean
  default: any | null
  description: string
  validation: string (regex or constraint)

PluginRegistration:
  pluginId: string
  commands: CommandDefinition[]
  version: string
  loadOrder: number

SessionEvent:
  sessionId: string
  eventType: enum (phase-start | phase-end | engine-start | engine-end | error | complete)
  phase: string | null
  engine: string | null
  message: string
  timestamp: timestamp
  progress: number (0-100)

CLIConfig:
  projectPath: string
  defaultVerbosity: enum (minimal | normal | verbose | debug)
  outputFormat: enum (text | json | yaml)
  colorEnabled: boolean
  progressStyle: enum (bar | spinner | log)
  historyEnabled: boolean
  historyRetention: number (days)
```

## Data Flow

1. Developer enters command (terminal or Kiro chat)
2. Command Router parses and validates input
3. Plugin Loader resolves appropriate command handler
4. Command handler translates to platform action (e.g., Skill Launcher creates GOE request)
5. GOE session begins; Progress Reporter subscribes to events
6. Real-time progress displayed to developer
7. On completion, Output Presenter shows results
8. History Tracker records session outcome

## Error Handling

- **Invalid Command:** Helpful error message with suggestion of similar valid commands
- **Invalid Arguments:** Specific error identifying which argument failed validation and expected format
- **GOE Connection Failure:** Clear message indicating platform unavailability; suggests checking status
- **Session Failure:** Error context from GOE displayed; suggests retry or opens last session state for debugging
- **Configuration Error:** Specific field-level error with current vs. expected value

## Correctness Properties

### Property 1: Command Resolution Determinism
The same input string always resolves to the same command handler given the same plugin registry state.

### Property 2: Argument Validation Completeness
No command handler is invoked with arguments that fail their declared validation constraints.

### Property 3: Progress Accuracy
Progress percentage reported to the user monotonically increases and reaches 100% on successful completion.

### Property 4: History Integrity
Every completed session (success or failure) is recorded in history with accurate timestamps and outcomes.

### Property 5: Configuration Consistency
Configuration changes are validated before persistence; invalid values are never written to the config file.

## Testing Strategy

- **Unit Tests:** Test Command Router parsing, argument validation, Plugin Loader discovery, and Config Manager read/write operations.
- **Command Tests:** Test each command family (generate, validate, config, status, output) with valid and invalid inputs, verifying correct handler dispatch and error messages.
- **Integration Tests:** Run CLI commands end-to-end with a stub GOE, verifying session creation, progress reporting, and result presentation.
- **Plugin Tests:** Test dynamic plugin loading, registration, and command namespace conflict detection.
- **UX Tests:** Verify progressive disclosure behavior (minimal vs. verbose output), error message helpfulness, and command suggestions for typos.
- **Kiro Integration Tests:** Verify skill invocation protocol compliance and natural language command parsing.

## Extension Points

- New command plugins for additional capabilities
- Custom output formatters for different terminal types
- Custom progress visualization styles
- Alternative Kiro integration modes
- Custom history storage backends
- Enterprise-specific command extensions (SSO, compliance commands)
