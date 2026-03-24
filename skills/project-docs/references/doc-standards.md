# Documentation Standards

## Core Principles

- **Concise**: Each document covers one thing only
- **Concrete**: Avoid vague descriptions — use examples
- **Maintainable**: Write docs that are easy to update; avoid hardcoded assumptions

## ADR (Architecture Decision Record) Format

```markdown
# ADR-[number]: [title]

## Status
[Proposed / Accepted / Deprecated]

## Context
[Why does this decision need to be made? What problem are we facing?]

## Decision
[What did we choose?]

## Rationale
[Why this option? What alternatives were considered?]

## Consequences
[What are the implications of this decision? Include both positive and negative outcomes.]
```

## Feature Story Format

```markdown
# [Feature Name]

## Background
[Why does this feature exist?]

## Problem
[What pain point does it address?]

## Solution
[How did we implement it?]

## Evolution
[How has this feature changed over time?]
```

## Naming Conventions

- ADR files: `adr-[number]-[kebab-case-title].md` (e.g. `adr-001-use-event-bus.md`)
- Feature stories: `[kebab-case-feature-name].md` (e.g. `multi-agent-delegation.md`)
