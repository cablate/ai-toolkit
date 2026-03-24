<p align="center">
  <img src="assets/banner.svg" alt="AI Toolkit" width="100%">
</p>

<p align="center">
  <a href="README.zh-TW.md">繁體中文</a>
</p>

A batteries-included working environment for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Dispatch agents, skills, and statusline — all extracted from daily production use.

## What's Inside

```
ai-toolkit/
├── agents/                  # SOP agents (symlink to ~/.claude/agents/)
│   ├── analyst.md           # Architecture / Planning / Audit
│   ├── investigator.md      # Search / Explore / Debug / External research
│   ├── builder.md           # Code implementation / Testing
│   ├── reviewer.md          # Code review / Dead code cleanup
│   ├── doc-sync.md          # Doc init / Doc sync
│   └── agent-factory.md     # Design and generate new agents
├── skills/                  # Skills (symlink to ~/.claude/skills/)
│   ├── handoff/             # Session handoff
│   ├── thorough/            # Relentless delivery mode
│   ├── project-docs/        # Project documentation structure
│   ├── agentskill-expertise/ # Skill design knowledge base
│   ├── collaboration-style/ # AI-human collaboration framework
│   └── self-growth/         # Continuous learning framework
└── statusline/              # Cost & context monitoring
```

## Dispatch Agents

When `/thorough` dispatches parallel subagents, prompt quality determines output quality. Dispatch agents are **SOP-style prompts** designed primarily for this scenario — step-based workflows with hard thresholds, classification heuristics, and structured output formats. They also improve quality whenever Claude Code spawns subagents via the Agent tool in general.

| Agent | Model | Modes | When dispatched |
|-------|-------|-------|-----------------|
| [`analyst`](agents/analyst.md) | opus | Architecture / Planning / Audit | "design this", "plan the implementation", "audit codebase health" |
| [`investigator`](agents/investigator.md) | sonnet | Search / Explore / Debug / External | "find all usages of X", "how does this work", "why does this fail" |
| [`builder`](agents/builder.md) | sonnet | Create / Modify / Test | "implement this", "modify the handler", "write tests for X" |
| [`reviewer`](agents/reviewer.md) | sonnet | Review / Cleanup | "review this code", "find dead code", "clean up unused exports" |
| [`doc-sync`](agents/doc-sync.md) | sonnet | Init / Sync | "set up project docs", "sync docs after changes" |

Each agent auto-detects its mode from dispatch context. One agent, multiple workflows.

### Design Principles

1. **Zero concept explanation** — All operational instructions. Claude already knows what CQRS is.
2. **Step-based SOP** — "Do X, then Y, if Z threshold → action." Not "You are an expert at..."
3. **Hard rules as threshold + trigger** — `>50 lines → flag`, `>4 nesting levels → flag`. Not "keep functions small."
4. **Classification heuristics** — `AUTO-FIX / ASK / CRITICAL` with concrete criteria. Not checklists.
5. **Structured output** — Every agent ends with a report template. Consistent, parseable.

## Interactive Agents

| Agent | Description |
|-------|-------------|
| [`agent-factory`](agents/agent-factory.md) | Design and generate new agents — research best practices, analyze requirements, output production-ready agent prompts |

## Skills

| Skill | Description |
|-------|-------------|
| [`/handoff`](skills/handoff/SKILL.md) | Session handoff — compress context into a structured prompt for seamless continuation |
| [`/thorough`](skills/thorough/SKILL.md) | Relentless delivery mode — exhaust all options, cost-aware model selection, verify before done |
| [`/project-docs`](skills/project-docs/SKILL.md) | Project documentation structure — standard `proj-[name]/` layout with ADRs, stories, and operations guides |
| [`/agentskill-expertise`](skills/agentskill-expertise/SKILL.md) | Agent Skill design knowledge base — mechanisms, philosophy, patterns, pitfalls |
| [`/collaboration-style`](skills/collaboration-style/skill.md) | AI-human collaboration norms — friction cases, coding style, behavioral guidelines |
| [`/self-growth`](skills/self-growth/SKILL.md) | Continuous learning framework — learn from work, organize knowledge, build feedback loops |

## Statusline

Cost and context monitoring for Claude Code. Token usage (K precision), context bar, idle time, plan usage rates.

> [`statusline/statusline.ps1`](statusline/statusline.ps1)

```jsonc
// ~/.claude/settings.json
{ "status_line_command": "powershell -NoProfile -File C:/Users/YOU/.claude/statusline.ps1" }
```

## License

[MIT](LICENSE)
