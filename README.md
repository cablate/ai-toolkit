<p align="center">
  <img src="assets/banner.svg" alt="AI Toolkit" width="100%">
</p>

<p align="center">
  <a href="README.zh-TW.md">繁體中文</a>
</p>

A batteries-included working environment for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Skills, dispatch agents, interactive agents, and statusline — all extracted from daily production use.

## What's Inside

```
ai-toolkit/
├── agents/
│   ├── dispatch/          # SOP agents for subagent quality
│   │   ├── analyst.md     # Architecture / Planning / Audit
│   │   ├── reviewer.md    # Code review / Dead code cleanup
│   │   └── doc-sync.md    # Doc init / Doc sync
│   └── interactive/       # 15 standalone agents
│       ├── agent-factory.md
│       ├── consultation-prep.md
│       ├── cinematic-writing-agent.txt
│       └── ... (15 total)
├── skills/
│   ├── handoff/           # Session handoff
│   ├── thorough/          # Relentless delivery mode
│   ├── project-docs/      # Project documentation structure
│   ├── agentskill-expertise/
│   ├── collaboration-style/
│   └── self-growth/
└── statusline/            # Cost & context monitoring
```

## Dispatch Agents

When Claude Code spawns subagents (via the Agent tool or `/thorough`), prompt quality determines output quality. Dispatch agents are **SOP-style prompts** — step-based workflows with hard thresholds, classification heuristics, and structured output formats. No role definitions, no concept explanations.

| Agent | Model | Modes | When dispatched |
|-------|-------|-------|-----------------|
| [`analyst`](agents/dispatch/analyst.md) | opus | Architecture / Planning / Audit | "design this", "plan the implementation", "audit codebase health" |
| [`reviewer`](agents/dispatch/reviewer.md) | sonnet | Review / Cleanup | "review this code", "find dead code", "clean up unused exports" |
| [`doc-sync`](agents/dispatch/doc-sync.md) | sonnet | Init / Sync | "set up project docs", "sync docs after changes" |

Each agent auto-detects its mode from dispatch context. One agent, multiple workflows.

### Design Principles

These prompts follow a strict SOP pattern (inspired by [gstack](https://github.com/garrytan/gstack)):

1. **Zero concept explanation** — All operational instructions. Claude already knows what CQRS is.
2. **Step-based SOP** — "Do X, then Y, if Z threshold → action." Not "You are an expert at..."
3. **Hard rules as threshold + trigger** — `>50 lines → flag`, `>4 nesting levels → flag`. Not "keep functions small."
4. **Classification heuristics** — `AUTO-FIX / ASK / CRITICAL` with concrete criteria. Not checklists.
5. **Structured output** — Every agent ends with a report template. Consistent, parseable.

## Interactive Agents

Standalone agents for specific tasks. Drop into `~/.claude/agents/` and invoke directly.

| Agent | Description |
|-------|-------------|
| [`agent-factory`](agents/interactive/agent-factory.md) | Design and generate new agents |
| [`consultation-prep`](agents/interactive/consultation-prep.md) | Prepare for consulting sessions |
| [`srt-subtitle-editor`](agents/interactive/srt-subtitle-editor.md) | Edit SRT subtitle files |
| [`cinematic-writing-agent`](agents/interactive/cinematic-writing-agent.txt) | Cinematic narrative writing |
| [`design-pattern-coach`](agents/interactive/design-pattern-coach.md) | Design pattern guidance |
| [`reading-agent`](agents/interactive/reading-agent.md) | Structured reading assistance |
| [`uiux-designer`](agents/interactive/uiux-designer.md) | UI/UX design |
| [`user-value-prd-reviewer`](agents/interactive/user-value-prd-reviewer.md) | PRD review from user value lens |
| [`CodeMender`](agents/interactive/CodeMender.md) | Code repair |
| [`code-review-agent-v2`](agents/interactive/code-review-agent-v2.md) | Code review |
| [`development-agent`](agents/interactive/development-agent.md) | Development workflow |
| [`planning-agent`](agents/interactive/planning-agent.md) | Project planning |
| [`security-helper`](agents/interactive/security-helper.md) | Security analysis |
| [`ai-quick-start-record-agent`](agents/interactive/ai-quick-start-record-agent.md) | Quick-start documentation |

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

## Installation

```bash
git clone https://github.com/cablate/ai-toolkit.git
cd ai-toolkit
```

### Linux / macOS

```bash
# Skills
for skill in skills/*/; do
  name=$(basename "$skill")
  ln -sf "$(pwd)/$skill" ~/.claude/skills/"$name"
done

# Dispatch agents
mkdir -p ~/.claude/agents
for agent in agents/dispatch/*.md; do
  ln -sf "$(pwd)/$agent" ~/.claude/agents/$(basename "$agent")
done

# Interactive agents (pick what you need)
for agent in agents/interactive/*; do
  ln -sf "$(pwd)/$agent" ~/.claude/agents/$(basename "$agent")
done

# Statusline
cp statusline/statusline.ps1 ~/.claude/
```

### Windows (PowerShell as Admin)

```powershell
# Skills
Get-ChildItem -Directory skills | ForEach-Object {
  New-Item -ItemType SymbolicLink -Force `
    -Path "$env:USERPROFILE\.claude\skills\$($_.Name)" `
    -Target "$PWD\skills\$($_.Name)"
}

# Dispatch agents
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\agents"
Get-ChildItem agents\dispatch\*.md | ForEach-Object {
  New-Item -ItemType SymbolicLink -Force `
    -Path "$env:USERPROFILE\.claude\agents\$($_.Name)" `
    -Target "$PWD\agents\dispatch\$($_.Name)"
}

# Interactive agents (pick what you need)
Get-ChildItem agents\interactive\* | ForEach-Object {
  New-Item -ItemType SymbolicLink -Force `
    -Path "$env:USERPROFILE\.claude\agents\$($_.Name)" `
    -Target "$PWD\agents\interactive\$($_.Name)"
}

# Statusline
Copy-Item statusline\statusline.ps1 ~\.claude\
```

### Staying in sync

Symlinks: just `git pull`. Copied: re-run the copy commands after pulling.

## Philosophy

**The AI is an owner, not an assistant.**

1. **AI agents quit too early.** `/thorough` fixes this — pressure escalation, forced retries, no escape hatches.
2. **Subagent quality is unreliable.** Dispatch agents fix this — SOP prompts with hard rules, not vague role descriptions.
3. **Session continuity breaks by design.** `/handoff` fixes this — structured context compression.
4. **You're flying blind on costs.** The statusline fixes this — real-time token and context monitoring.
5. **Project docs rot.** `/project-docs` + `doc-sync` fix this — standard structure and automated staleness detection.

## Contributing

Issues and PRs welcome. Real-world tested, concrete behavior change, no hand-waving.

## License

[MIT](LICENSE)
