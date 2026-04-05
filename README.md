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
│   ├── vector-memory/       # Persistent vector memory usage guide
│   ├── project-docs/        # Project documentation structure
│   ├── agentskill-expertise/ # Skill design knowledge base
│   ├── collaboration-style/ # AI-human collaboration framework
│   └── self-growth/         # Continuous learning framework
├── domain-skills/           # Domain-specific skill sets
│   ├── darkseoking/         # SEO & Threads algorithm (3 skills)
│   └── claude-code/         # Claude Code reverse engineering (6 skills)
├── mcp.example.json         # MCP server config template
└── statusline/              # Cost & context monitoring
```

## Agents

SOP-style prompts for Claude Code's Agent tool. When `/thorough` dispatches parallel subagents, prompt quality determines output quality — these agents provide step-based workflows with hard thresholds, classification heuristics, and structured output formats.

| Agent | Model | When to use |
|-------|-------|-------------|
| [`analyst`](agents/analyst.md) | sonnet | "design this", "plan the implementation", "audit codebase health" |
| [`investigator`](agents/investigator.md) | haiku | "find all usages of X", "how does this work", "why does this fail" |
| [`builder`](agents/builder.md) | sonnet | "implement this", "modify the handler", "write tests for X" |
| [`reviewer`](agents/reviewer.md) | sonnet | "review this code", "find dead code", "clean up unused exports" |
| [`doc-sync`](agents/doc-sync.md) | haiku | "set up project docs", "sync docs after changes" |
| [`agent-factory`](agents/agent-factory.md) | opus | "create a new agent", "improve this agent's prompt" |

Each agent auto-detects its mode from dispatch context. One agent, multiple workflows.

### Design Principles

1. **Zero concept explanation** — All operational instructions. Claude already knows what CQRS is.
2. **Step-based SOP** — "Do X, then Y, if Z threshold → action." Not "You are an expert at..."
3. **Hard rules as threshold + trigger** — `>50 lines → flag`, `>4 nesting levels → flag`. Not "keep functions small."
4. **Classification heuristics** — `AUTO-FIX / ASK / CRITICAL` with concrete criteria. Not checklists.
5. **Structured output** — Every agent ends with a report template. Consistent, parseable.

## Skills

| Skill | Description |
|-------|-------------|
| [`/handoff`](skills/handoff/SKILL.md) | Session handoff — compress context into a structured prompt for seamless continuation |
| [`/thorough`](skills/thorough/SKILL.md) | Relentless delivery mode — exhaust all options, cost-aware model selection, verify before done |
| [`/vector-memory`](skills/vector-memory/SKILL.md) | Persistent vector memory via LanceDB — store facts, decisions, lessons across sessions |
| [`/project-docs`](skills/project-docs/SKILL.md) | Project documentation structure — standard `proj-[name]/` layout with ADRs, stories, and operations guides |
| [`/agentskill-expertise`](skills/agentskill-expertise/SKILL.md) | Agent Skill design knowledge base — mechanisms, philosophy, patterns, pitfalls |
| [`/collaboration-style`](skills/collaboration-style/skill.md) | AI-human collaboration norms — friction cases, coding style, behavioral guidelines |
| [`/self-growth`](skills/self-growth/SKILL.md) | Continuous learning framework — learn from work, organize knowledge, build feedback loops |

## Domain Skills

Deep skill sets built around specific topics or practitioners' methodologies. Unlike generic skills, these encode domain expertise with layered architecture (knowledge → operations → prediction).

| Domain | Skills | Description |
|--------|--------|-------------|
| [darkseoking](domain-skills/darkseoking/) | 3 | SEO & Threads algorithm — mindset (8 mental models), post optimizer (pre-publish checklist), post predictor (V2 dual-stage Views×ER) |
| [claude-code](domain-skills/claude-code/) | 6 | Claude Code reverse engineering — prompt craft, cost engineering, harness patterns, security, agent design, agent audit |

> Each domain has its own README with setup instructions and architecture overview.

## MCP Servers

Example configuration for the MCP servers used in this toolkit.

> [`mcp.example.json`](mcp.example.json) — copy to your project as `.mcp.json` and fill in your API keys.

| Server | What it does |
|--------|-------------|
| [`@cablate/memory-lancedb-mcp`](https://www.npmjs.com/package/@cablate/memory-lancedb-mcp) | Persistent vector memory with hybrid search (semantic + keyword) |
| [Serena](https://github.com/oraios/serena) | Semantic code intelligence — symbol search, references, refactoring |

## Statusline

Cost and context monitoring for Claude Code. Two-line display with context alerts and plan usage tracking.

```
 Normal (< 60% context):
┌──────────────────────────────────────────────────────────────────┐
│ Claude Opus 4  | [=======--------------] 45.2K/200.0K 22.6%    │
│ 5h: 12.3% (4h 22m) | 7d: 8.1% (6d 3h)                        │
└──────────────────────────────────────────────────────────────────┘

 Warning (>= 60% context):
┌──────────────────────────────────────────────────────────────────┐
│ Claude Sonnet 4 | concise | [============--------] 130.5K/200.0K 65.3%  /handoff soon │
│ 5h: 45.0% (2h 10m) | 7d: 22.4% (5d 1h)                       │
└──────────────────────────────────────────────────────────────────┘

 Critical (>= 80% context):
┌──────────────────────────────────────────────────────────────────┐
│ Claude Opus 4  | [==================--] 310.0K/200.0K 95.0%  !! HANDOFF NOW !! │
│ 5h: 78.2% (1h 05m) | 7d: 51.3% (3d 12h)                      │
│ !! DO NOT close/resume -- use /handoff first, or waste 6%+ of 5h tokens !! │
└──────────────────────────────────────────────────────────────────┘
```

**Line 1** — Model name, output style (if not default), context progress bar with K-precision token counts, usage %, and alerts at 150K/200K/300K thresholds.

**Line 2** — 5-hour and 7-day plan usage rates with reset countdowns. Fetched from Claude API (cached 5min) or inline `rate_limits` (v2.1.80+).

**Line 3** — Appears at 250K+ tokens. Hard warning against closing/resuming without handoff.

> [`statusline/statusline.ps1`](statusline/statusline.ps1)

```jsonc
// ~/.claude/settings.json
{ "status_line_command": "powershell -NoProfile -File C:/Users/YOU/.claude/statusline.ps1" }
```

## License

[MIT](LICENSE)
