# Intermediate Example

## Prompt
"Design the prompts for a research agent that plans research strategies, executes multi-source searches, synthesizes findings, and reflects on research quality."

## Expected Behavior
The prompt-engineering skill:
1. Identifies prompt needs: system prompt, planning prompt, search query prompt, synthesis prompt, reflection prompt (5 prompts)
2. Designs hierarchy: system → planning → [execution (search + synthesis)] → reflection → (loop back to planning if quality insufficient)
3. Creates system prompt: research specialist role, multi-source synthesis capability, quality standards
4. Creates planning prompt: decomposes research question into search strategies, identifies sources
5. Creates search query prompt: generates optimized queries per data source (adapts format to source type)
6. Creates synthesis prompt: combines findings, identifies themes, resolves contradictions
7. Creates reflection prompt: evaluates completeness, identifies gaps, scores quality against criteria
8. Context assembly: progressive — plan context for search, accumulated results for synthesis, full context for reflection (manages window carefully)
9. Output formats: structured JSON for plan (parseable by executor), markdown for synthesis, quality object for reflection
10. Model routing: larger model for synthesis/reflection, smaller for search query generation
11. Evaluation: plan quality, search coverage, synthesis coherence, reflection accuracy

## Expected Output
- `prompt-package.md` with 5 versioned prompts:
  - System prompt: research specialist identity (v1.0)
  - Planning prompt: research decomposition (v1.0)
  - Search query prompt: source-adaptive query generation (v1.0)
  - Synthesis prompt: multi-source combination (v1.0)
  - Reflection prompt: quality assessment with scoring (v1.0)
- Context assembly strategy: progressive accumulation with summarization at window boundary
- Output format specs: JSON (plan), structured queries (search), markdown (synthesis), quality object (reflection)
- Model routing table: synthesis/reflection → large model, search queries → small model
- Evaluation criteria per prompt with test cases
