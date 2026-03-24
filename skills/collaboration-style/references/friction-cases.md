# Friction Case Catalog

> Anti-patterns collected from real sessions. Kept abstract — no project-specific names or file paths.
>
> **How to use this file**: Add new entries as friction surfaces during sessions. Must be abstracted to the pattern level. When the same root cause appears 3+ times, strengthen the corresponding operating principle in SKILL.md.

---

## Efficiency

| # | Anti-pattern | Root cause |
|---|---|---|
| E1 | Starts exploring the codebase before executing the actual task | Over-preparation |
| E2 | Runs independent tasks sequentially instead of in parallel | Not using concurrency |
| E3 | Produces a long output without checkpointing | Not managing output cadence |
| E4 | Core task incomplete because detours consumed the time budget | Premature scope expansion |

## Precision

| # | Anti-pattern | Root cause |
|---|---|---|
| P1 | Asked to change A/B/C, also changed D/E/F | Self-expanded scope |
| P2 | Debugged wrong file or used wrong logger | Did not confirm error source |
| P3 | Described content by fabricating details | Did not check primary source |
| P4 | Cross-session development left no record of design decisions | No ADR habit |
| P5 | `git add -A` included credentials or tokens | Imprecise file staging |
| P6 | Public-facing doc used wrong language for the audience | Did not consider target audience |
| P7 | Solution was over-engineered; user pointed out the obvious simpler path | Over-engineering |
| P8 | Acted without checking external state first (e.g., pushed to an already-merged branch) | Did not verify current state before acting |

## Root Cause Thinking

| # | Anti-pattern | Root cause |
|---|---|---|
| R1 | Iterated on symptoms (tuning filters, adjusting thresholds) without verifying that upstream functions are actually called with correct arguments | Treating symptoms, not causes |
| R2 | Designed a fix based on reading code and inferring behavior, rather than checking actual logs | Inference over data |
| R3 | Adopted a suggestion from a code review or subagent without validating assumptions against runtime data | Trusting reasoning over evidence |
| R4 | Spent N rounds on the same problem, each round a minor tweak rather than questioning the approach | Sunk cost thinking |
| R5 | Did not verify new code is live after deploy (build passing ≠ runtime running the new version) | Deploy not confirmed |

## Global Awareness

| # | Anti-pattern | Root cause |
|---|---|---|
| H1 | Changed one instance of a pattern; other instances not updated | Local-only fix |
| H2 | Answered a UX question with a purely technical/API analysis | Perspective mismatch |
| H3 | Noticed dead code or duplicate logic but did not flag or address it | No quality initiative |
| H4 | Changed code without updating docs, README, or tests | No change checklist |
| H5 | Committed large binary assets without compression | No asset quality awareness |
| H6 | "Check the logs" interpreted as "check the code diff" | Misread actual user need |

---

## Update Rules

- New friction type → append to the matching category
- **Must be abstract**: remove all project names, file names, and session-specific details; keep only the pattern
- Same root cause appears 3+ times → strengthen the corresponding principle in SKILL.md
- Fully internalized cases → mark `[internalized]` to reduce reading overhead
