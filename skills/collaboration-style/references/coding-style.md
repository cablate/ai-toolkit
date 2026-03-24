# Development Collaboration Style

> Fill in this template with the user's actual preferences. Delete placeholder text when filled in.

## Design Thinking

### Architecture first

Prioritize semantic correctness over "does it run."

> Example values:
> - Correct layering: core does not depend on adapters; types do not depend on higher layers
> - Feature parity: if platform A has it, platform B should too
> - Consistent naming: same conceptual family → same prefix
> - Ask "is the design right" before "is the code correct"

### Semantic precision

Every value and field should reflect its true meaning. "Close enough" is not acceptable.

> Example values:
> - If numbers don't add up, trace to the source — don't guess, check the DB, read the source, compute it
> - Maintain clear semantic boundaries between similar-sounding concepts

### End-to-end closure

Any change must prompt a check of upstream and downstream impact.

> Example values:
> - Changed one place → ask about other paths with the same pattern
> - Added a feature → check docs, tests, and config are in sync
> - After a fix → ask "does this same issue exist elsewhere?"

---

## Quality Baseline

| Dimension | Standard |
|---|---|
| Build | Every change must pass build + test |
| Doc sync | Code change → update all reference points |
| Verification | Verify with actual execution; confirm runtime reflects the new code after deploy |
| Completeness | No stubs, placeholders, or "good enough for now" |
| Audience | _(e.g., open-source docs in English, internal docs in preferred language)_ |

---

## Git Conventions

> Fill in or adjust to match the project's actual conventions.

- **Always use PRs**: feature branch → PR → review → merge
- **Conventional commits**: `feat` / `fix` / `chore` / `docs` / `refactor`
- **Precise staging**: only add the files needed; avoid `git add -A`
- **Post-merge cleanup**: delete remote branch after merge

---

## Decision Principles

| Principle | Detail |
|---|---|
| UX > technical purity | _(e.g., build a composite tool rather than expecting AI to chain primitives)_ |
| Recommend, don't list options | Give one recommendation with reasoning; don't present a menu |
| Pragmatic trade-offs | _(e.g., in early stages, prefer breaking changes over backwards-compat complexity)_ |
| Verify before assuming unsupported | Check first whether something is actually unsupported |
| Leave a decision trail | Record key decisions in CLAUDE.md or an ADR |

---

## Workflow

| Dimension | Preference |
|---|---|
| Task breakdown | _(e.g., list all subtasks before starting)_ |
| Parallelization | Independent tasks must run concurrently |
| Tool selection | If a dedicated tool exists, use it |
| Done criteria | _(e.g., complete a full pass, then review once more)_ |
| Plan validation | Fact-check assumptions before executing |
| Deploy confirmation | Verify runtime log reflects new code after deployment |
