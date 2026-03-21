# Cab's Claude Code Setup

[繁體中文](README.zh-TW.md)

Battle-tested [Claude Code](https://docs.anthropic.com/en/docs/claude-code) configurations, skills, and tools from daily production use. Not theory — everything here is extracted from real workflows with AI agents.

## What's Inside

### Skills

Slash commands that change how your AI agent works.

#### `/handoff` — Session Handoff

Compresses an entire conversation's context into a structured prompt for seamless continuation in a new session.

- P0/P1 priority triage — carry what matters, trim what doesn't
- Verbatim preservation of user instructions
- "Shared understanding" section for implicit knowledge transfer
- Self-contained output — works in any AI environment

→ [`skills/handoff/SKILL.md`](skills/handoff/SKILL.md)

#### `/thorough` — Relentless Delivery Mode

High-accountability execution mode. The AI stops being polite and starts being an owner — exhausting every option, parallelizing aggressively, refusing to quit until verified done.

- Three iron rules: exhaust all options, investigate before asking, proactively extend scope
- Escalating pressure system (L1→L4)
- Cost-aware model selection: haiku (default) → sonnet → opus
- Strict delivery checklist with build verification

→ [`skills/thorough/SKILL.md`](skills/thorough/SKILL.md)

### Statusline

A PowerShell statusline for Claude Code that puts cost and context awareness front and center.

- Token usage precise to K (input/output/cache)
- Context window usage bar with alert threshold
- Session idle time (cache rebuild risk indicator)
- 5h/7d plan usage rates

→ [`statusline/statusline.ps1`](statusline/statusline.ps1)

**Setup:**
```jsonc
// ~/.claude/settings.json
{
  "status_line_command": "powershell -NoProfile -File C:/Users/YOU/.claude/statusline.ps1"
}
```

## Installation

### Clone + Symlink (recommended)

```bash
git clone https://github.com/cablate/cablate-skills.git

# Skills — Linux / macOS
ln -s "$(pwd)/cablate-skills/skills/handoff" ~/.claude/skills/handoff
ln -s "$(pwd)/cablate-skills/skills/thorough" ~/.claude/skills/thorough

# Skills — Windows (PowerShell as Admin)
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\handoff" -Target ".\cablate-skills\skills\handoff"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\thorough" -Target ".\cablate-skills\skills\thorough"

# Statusline
cp cablate-skills/statusline/statusline.ps1 ~/.claude/
```

### Direct copy

```bash
git clone https://github.com/cablate/cablate-skills.git
cp -r cablate-skills/skills/handoff ~/.claude/skills/
cp -r cablate-skills/skills/thorough ~/.claude/skills/
cp cablate-skills/statusline/statusline.ps1 ~/.claude/
```

## Usage

```
/handoff          # Generate a context handoff prompt
/thorough <task>  # Execute a task in relentless delivery mode
```

`/handoff` is also triggered by natural language like "help me switch sessions" or "token is running out".

`/thorough` can be combined with any task — it changes *how* the AI works, not *what* it works on.

## Philosophy

Everything here exists because of real pain points:

1. **AI agents quit too early.** They say "done" without verification, suggest "the user should manually check", and treat partial completion as success. `/thorough` fixes this.

2. **Session continuity is broken by design.** When a conversation hits context limits, all implicit understanding evaporates. `/handoff` fixes this.

3. **You're flying blind on costs.** Default Claude Code gives you no visibility into token consumption or plan usage. The statusline fixes this.

One principle: **the AI is an owner, not an assistant.**

## Contributing

Issues and PRs welcome. If you have something that follows the same philosophy — real-world tested, concrete behavior change, no hand-waving — feel free to submit.

## License

[MIT](LICENSE)
