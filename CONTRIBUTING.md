# Contributing to AI Toolkit

Thank you for your interest in contributing. This toolkit is extracted from daily production use of Claude Code — contributions should meet that same bar.

## Table of Contents

- [What We Accept](#what-we-accept)
- [Agent Design Guidelines](#agent-design-guidelines)
- [Skill Design Guidelines](#skill-design-guidelines)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)

---

## What We Accept

- New dispatch agents (SOP-style, zero concept explanation)
- New skills (SKILL.md + references/ structure)
- Improvements to existing agents or skills
- Statusline enhancements
- Bug fixes and corrections
- Documentation improvements

We do **not** accept:

- Agents or skills that explain concepts Claude already knows
- Vague instructions without hard thresholds or triggers
- Agents that duplicate an existing agent's scope without clear differentiation
- Skills without a `references/` directory structure

---

## Agent Design Guidelines

Agents live in `agents/`. Each agent is a single `.md` file.

### The Five Rules

1. **Zero concept explanation** — Do not explain what REST, CQRS, or TDD is. Claude knows. Every sentence must be an operational instruction.

2. **Step-based SOP** — Structure as "Do X, then Y, if Z → action." Not "You are an expert in..."

   Bad:
   ```
   You are an expert code reviewer with deep knowledge of software engineering principles.
   ```

   Good:
   ```
   ## Phase 1: Read Before Review
   a) Read the target file top to bottom
   b) grep for all callers of each public function
   c) If >5 callers → flag for impact analysis before suggesting changes
   ```

3. **Hard rules as threshold + trigger** — Quantify the threshold. Name the trigger action.

   Bad: "Keep functions small and readable."

   Good: "`>40 lines` → flag for splitting. `>4 nesting levels` → flag for early return refactor."

4. **Classification heuristics** — Use explicit categories with concrete criteria.

   Example:
   ```
   | Severity | Criteria | Action |
   |----------|----------|--------|
   | AUTO-FIX | Pure style, no logic change | Fix immediately |
   | ASK | Ambiguous intent | Ask before changing |
   | CRITICAL | Data loss / security / breaking API | Block PR, report |
   ```

5. **Structured output** — Every agent must end with a report template. The output must be consistent and parseable across runs.

### Agent File Structure

```markdown
# Agent Name

[One-sentence description of what this agent does and when it's dispatched]

## Mode Detection

[How the agent determines which mode/workflow to run from dispatch context]

## Phase 1: [First Phase Name]

[Step-by-step instructions]

## Phase 2: [Second Phase Name]

[Step-by-step instructions]

## Output Report

[Fixed template for structured output]

## Rules

[Hard thresholds, constraints, and non-negotiables as a numbered list]
```

### Agent Model Selection

- `opus` — Complex reasoning, architecture decisions, planning
- `sonnet` — Implementation, search, review, doc tasks

Specify the intended model in the agent header comment if it differs from default.

---

## Skill Design Guidelines

Skills live in `skills/`. Each skill is a directory with this structure:

```
skills/your-skill-name/
├── SKILL.md          # The skill itself — loaded by Claude when invoked
└── references/       # Supporting data, lookup tables, examples
    ├── something.md
    └── another.md
```

### SKILL.md Requirements

- **Trigger conditions** — When should this skill be loaded? List exact scenarios.
- **Hard rules** — Same as agents: thresholds with explicit triggers, not vague principles.
- **References** — If the skill references a file in `references/`, that file must exist.
- **No concept tutorials** — The skill is a runtime operating procedure, not a knowledge base.

### references/ Requirements

- Each file covers one topic or lookup table
- Filenames use kebab-case: `error-patterns.md`, `commit-format.md`
- No file should duplicate content already in `SKILL.md`

### Skill Naming

Use lowercase kebab-case: `vector-memory`, `project-docs`, `code-review`.

---

## Testing

This toolkit has no automated test suite. Testing is manual with Claude Code.

### How to Test an Agent

1. Symlink your agent into `~/.claude/agents/`:
   ```bash
   ln -s /path/to/ai-toolkit/agents/your-agent.md ~/.claude/agents/your-agent.md
   ```
2. Open Claude Code in a real project
3. Dispatch the agent with a realistic task
4. Verify: Does it follow the SOP steps? Does it produce the structured output report?
5. Check edge cases listed in the agent's Mode Detection section

### How to Test a Skill

1. Symlink your skill into `~/.claude/skills/`:
   ```bash
   ln -s /path/to/ai-toolkit/skills/your-skill ~/.claude/skills/your-skill
   ```
2. Open Claude Code
3. Invoke the skill: `/your-skill`
4. Verify: Does it load correctly? Are references accessible? Do the hard rules trigger correctly?

### Acceptance Bar

Before submitting a PR, run the agent or skill on at least two real tasks. Include a brief description of what you tested in the PR body.

---

## Pull Request Process

1. **Fork** the repository and create a branch from `main`
2. **Name your branch** descriptively: `feat/test-runner-agent`, `fix/thorough-trigger`
3. **Write the code** following the design guidelines above
4. **Test manually** as described in the Testing section
5. **Submit the PR** with:
   - What the agent/skill does and when it triggers
   - What you tested and what the output looked like
   - Any design decisions that are non-obvious

### PR Checklist

- [ ] Agent follows all five design rules (zero concept explanation, SOP steps, hard thresholds, classification heuristics, structured output)
- [ ] Skill has both `SKILL.md` and `references/` directory
- [ ] No duplicate scope with existing agents or skills
- [ ] Manually tested on at least two real tasks
- [ ] `README.md` updated if adding a new agent or skill

---

## Code Style

### Markdown Formatting

- Use ATX headers (`##`), not Setext (`---` underlines)
- One blank line before and after headers
- Tables use `|---|` separator rows with at least one `-` per cell
- Code blocks specify a language: ` ```bash `, ` ```typescript `, ` ```markdown `
- No trailing whitespace

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Agent files | kebab-case `.md` | `code-review.md` |
| Skill directories | kebab-case | `vector-memory/` |
| Skill reference files | kebab-case `.md` | `tier-thresholds.md` |

### Agent/Skill Descriptions

One sentence. No fluff. Describes what it does and when it's used.

Bad: "A powerful and flexible agent for all your code review needs."

Good: "Reviews code for correctness, dead code, and breaking changes — dispatched after implementation."
