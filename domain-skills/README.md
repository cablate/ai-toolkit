# Domain Skills

Domain-specific skill sets for Claude Code. Unlike the generic infrastructure skills in `skills/`, these are built around a particular topic or practitioner's methodology.

Each subdirectory is a self-contained skill set with its own README, shared data, and multiple skills that work together.

## Available Domain Skills

| Directory | Topic | Skills |
|-----------|-------|--------|
| [darkseoking](darkseoking/) | SEO & Threads Algorithm | 3 skills (mindset, post-optimizer, post-predictor) |
| [claude-code](claude-code/) | Claude Code Reverse Engineering | 6 skills (prompt-craft, cost-engineering, harness-patterns, security-patterns, agent-design, agent-audit) |

## Structure

```
domain-skills/
├── README.md              ← you are here
└── {topic}/               ← one directory per domain
    ├── README.md           ← topic overview + setup
    ├── shared-data.csv     ← shared data files (if any)
    ├── skill-a/
    │   ├── SKILL.md
    │   └── references/
    └── skill-b/
        ├── SKILL.md
        └── references/
```

## Adding a New Domain Skill Set

1. Create a directory under `domain-skills/` named after the topic
2. Add a `README.md` explaining the skill set, its architecture, and setup instructions
3. Place each skill in its own subdirectory with `SKILL.md` + `references/`
4. Shared data files go at the topic root level
