# Advanced Example

## Prompt
"Design the complete prompt architecture for an enterprise incident response multi-agent system with 4 specialized agents (coordinator, diagnostic, remediation, communication). Each agent needs its own reasoning layer with coordination prompts for inter-agent communication."

## Expected Behavior
The prompt-engineering skill:
1. Identifies prompt needs: 4 system prompts (one per agent) + 6 specialized prompts per agent + 3 coordination prompts = 31 prompts
2. Designs multi-agent prompt hierarchy:
   - Coordinator: system, triage, delegation, escalation, coordination, summary
   - Diagnostic: system, investigation planning, hypothesis generation, evidence analysis, root cause, reporting
   - Remediation: system, fix planning, risk assessment, execution planning, rollback planning, verification
   - Communication: system, stakeholder identification, severity communication, update generation, resolution summary, post-incident
   - Shared: inter-agent handoff, escalation request, status synthesis
3. Creates all system prompts with agent-specific identities, responsibilities, and boundaries
4. Creates specialized execution prompts for each agent's workflow steps
5. Creates coordination prompts for inter-agent communication protocol
6. Designs context assembly per agent: each agent receives its relevant context, coordinator assembles cross-agent state
7. Output formats: structured JSON for decisions, markdown for communications, typed events for inter-agent messages
8. Model routing: large model for diagnosis and remediation planning, medium for coordination, small for status formatting
9. Defines prompt versioning across all 31 prompts
10. Evaluation: per-agent quality metrics, coordination accuracy, escalation appropriateness, communication clarity

## Expected Output
- `prompt-package.md` — complete 31-prompt catalog organized by agent
- 4 system prompts: coordinator, diagnostic, remediation, communication agent identities
- 24 specialized prompts: 6 per agent for workflow-specific reasoning
- 3 coordination prompts: handoff, escalation, status synthesis for inter-agent protocol
- Context assembly strategy per agent with cross-agent state management
- Output format specifications: decision objects, communication templates, event schemas
- Model routing table: prompt → model mapping across all 31 prompts with cost optimization
- Inter-agent communication protocol: structured message format and handoff semantics
- Evaluation framework: per-agent quality metrics, end-to-end incident resolution quality
- Prompt dependency map showing which prompts feed into which (context chains)
