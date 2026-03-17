# Claude Code Skills

[繁體中文](README.zh-TW.md)

A collection of battle-tested [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills designed to push AI agents toward higher-quality, end-to-end delivery.

## Skills

### `/handoff` — Session Handoff

Compresses an entire conversation's context into a structured prompt that can be pasted into a new session — enabling seamless continuation without losing critical decisions, user instructions, or shared understanding.

**Key features:**
- P0/P1 priority triage — carry what matters, trim what doesn't
- Verbatim preservation of user instructions (no paraphrasing)
- "Shared understanding" section for implicit knowledge transfer
- Multi-workstream support for complex sessions
- Self-contained output — works in any AI environment, not just Claude Code

→ [`skills/handoff/SKILL.md`](skills/handoff/SKILL.md)

### `/thorough` — Relentless Delivery Mode

Activates a high-accountability execution mode. The AI stops being polite and starts being an owner — exhausting every option, parallelizing aggressively, and refusing to quit until the job is verifiably done.

**Key features:**
- Three iron rules: exhaust all options, investigate before asking, proactively extend scope
- Escalating pressure system (L1→L4) with mandatory actions at each level
- 5-step de-loop protocol for stuck situations
- Parallel execution with model-appropriate delegation
- Strict delivery checklist with build verification

→ [`skills/thorough/SKILL.md`](skills/thorough/SKILL.md)

## Installation

### Option 1: Symlink (recommended)

Clone this repo and symlink each skill into your Claude Code skills directory:

```bash
git clone https://github.com/cablate/claude-code-skills.git

# Linux / macOS
ln -s "$(pwd)/claude-code-skills/skills/handoff" ~/.claude/skills/handoff
ln -s "$(pwd)/claude-code-skills/skills/thorough" ~/.claude/skills/thorough

# Windows (PowerShell as Admin)
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\handoff" -Target ".\claude-code-skills\skills\handoff"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\thorough" -Target ".\claude-code-skills\skills\thorough"
```

### Option 2: Direct copy

```bash
git clone https://github.com/cablate/claude-code-skills.git
cp -r claude-code-skills/skills/handoff ~/.claude/skills/
cp -r claude-code-skills/skills/thorough ~/.claude/skills/
```

## Usage

In any Claude Code session:

```
/handoff          # Generate a context handoff prompt
/thorough <task>  # Execute a task in relentless delivery mode
```

`/handoff` is also triggered by natural language like "help me switch sessions", "context is getting long", or "token is running out".

`/thorough` can be combined with any task — it changes *how* the AI works, not *what* it works on.

## Philosophy

These skills are opinionated. They exist because:

1. **AI agents quit too early.** They say "done" without verification, suggest "the user should manually check", and treat partial completion as success. `/thorough` fixes this.

2. **Session continuity is broken by design.** When a conversation hits context limits, all the implicit understanding, user corrections, and decision history evaporates. `/handoff` fixes this.

Both skills are designed around a single principle: **the AI is an owner, not an assistant.** Owners don't stop at "good enough." Owners don't lose context when switching shifts.

## Contributing

Issues and PRs welcome. If you have a skill that follows the same philosophy — high accountability, concrete behavior change, no hand-waving — feel free to submit it.

## License

[MIT](LICENSE)
