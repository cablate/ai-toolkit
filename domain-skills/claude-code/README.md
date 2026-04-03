# claude-code — Claude Code Reverse Engineering Skills

Six skills built from reverse-engineering [Claude Code](https://docs.anthropic.com/en/docs/claude-code) v2.1.88 (92,500 lines of TypeScript). Not speculation — every pattern is traced back to actual source code, with file paths and line counts.

## Architecture

```
Knowledge        →  cc-prompt-craft        System prompt engineering (914-line prompt analysis)
                    cc-cost-engineering     Token cost control & cache optimization
                    cc-harness-patterns     12 transferable harness design principles
                    cc-security-patterns    Seven-layer defense-in-depth architecture
                    cc-agent-design         Agent configuration (6 built-in agent analysis)
Operations       →  cc-agent-audit          Project configuration audit (5-check system)
```

## Skills

### cc-prompt-craft

**Triggers:** Writing system prompts, designing prompt assembly pipelines, optimizing prompt cache efficiency, writing safety instructions

How Claude Code's 914-line system prompt is structured: static/dynamic boundary for cache stability, `DANGEROUS_` naming convention for cache-breaking sections, eval-driven wording decisions, compaction prompt three-mode design, and 8 top prompt design patterns (tool preference pyramid, forced preconditions, output efficiency, git safety protocol, etc.).

### cc-cost-engineering

**Triggers:** Optimizing token consumption, designing cost control mechanisms, analyzing cache efficiency, choosing model configurations

The economics of running AI agents: model cost matrix (Haiku 1x → Opus Fast 37.5x), 12 prompt cache break causes with defenses, user-side cost pitfalls (Auto Mode overhead, cross-midnight cache bust, MCP server bloat), token estimation strategies, and compaction cost traps.

### cc-harness-patterns

**Triggers:** Designing agent system architecture, implementing tool orchestration, designing context management, building agent loops

12 transferable principles from Claude Code's harness: async generator agent loop, read/write tool separation with auto-batching, 7-layer tool execution pipeline, cache stability patterns (Sticky Latch, deterministic IDs, Attachment > Inline), context engineering (10-step message normalization, deferred tool loading), multi-session continuity (forked agents, AutoDream), and observability (PII-safe types, frustration signals).

### cc-security-patterns

**Triggers:** Designing tool safety mechanisms, implementing command filtering, building permission models, designing sandboxes

Seven-layer defense-in-depth from Claude Code's 7,000+ lines of security code: parser differential as core threat model, whitelist-over-blacklist approach, aggressive deny-path sanitization, three-layer read-only validation (Unix/shared/PowerShell), platform-specific sandbox design (bubblewrap/sandbox-exec), and 5-source concurrent permission resolution.

### cc-agent-design

**Triggers:** Designing new agents, optimizing agent prompts, deciding tool/model configurations, writing dispatch prompts

How Claude Code configures its 6 built-in agents: three-layer prompt architecture (identity/environment/context), tool minimization principle (start from zero, not from all), model selection matrix (haiku for search, sonnet for logic, inherit for quality control), `omitClaudeMd` mode for read-only agents, and dispatch prompt writing principles ("never delegate understanding").

### cc-agent-audit

**Triggers:** Reviewing/optimizing CLAUDE.md, skills, settings, periodic cleanup, pre-launch project checks

Systematic 5-check audit for Claude Code projects: CLAUDE.md text quality, skill description quality (three-layer separation principle), settings configuration (tool minimization, deny rules, model fit), rules alignment (no contradictions or cross-file duplication), and cross-file consistency. Operates in review (read-only), fix (with confirmation), or batch mode.

## Key Concepts

| Concept | Source |
|---------|--------|
| Static/Dynamic Boundary | Prompt cache stability — one cache bucket, not 2^N |
| Sticky Latch | Cache-affecting flags never revert mid-session |
| Parser Differential | Harness parser vs. shell parser disagreements — core threat model |
| Three-Layer Separation | description (trigger) → SKILL.md (capability) → references/ (knowledge) |
| Tool Minimization | Start from zero tools, add only what the task needs |
| Deferred Tool Loading | 36 tools don't all go in the prompt — load schemas on demand |

## Setup

> New to Claude Code skills? See the [ai-toolkit main README](../../README.md) for general setup instructions.

1. Copy the six skill directories into your project's `.claude/skills/`
2. Claude Code will auto-detect the skills based on their `description` triggers — no manual activation needed

The skills work independently but reference each other:

- **cc-agent-audit** can load any of the other 5 skills as needed during audits
- **cc-prompt-craft** and **cc-cost-engineering** share cache optimization knowledge
- **cc-agent-design** builds on patterns from **cc-harness-patterns**
