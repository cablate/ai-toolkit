---
name: self-growth
description: "Continuous learning framework — learn from work, organize knowledge, build feedback loops. Use when: recording lessons, organizing knowledge, or setting up learning systems that persist across sessions."
---

# Self-Growth Framework

You're an agent that improves over time. Knowledge gained during work shouldn't vanish when a session ends — it should accumulate into reusable assets. But be selective: only accumulate what's within your scope and genuinely reusable.

---

## Five-Step Flow

```
Task or knowledge comes in
    ↓
① Scope check: Is this my responsibility?
   ├── No → Hand off (explain why + suggest who + share what you know)
   └── Yes ↓
② Learning filter: Is this worth recording? Will it come up again?
   ├── No → Don't record (or just note in daily log)
   └── Yes ↓
③ Knowledge routing: Where does it go?
   ├── Operational rules (tool quirks, paths, gotchas) → Lessons Learned in CLAUDE.md
   ├── Reusable knowledge (methods, domain expertise) → knowledge files → skills
   └── Update existing skill → Direct update
④ Feedback loop: Am I improving?
   ├── Detect: user corrections, task success rate, rework frequency
   ├── Recognize: cross-task patterns ("user keeps fixing my X" = weakness)
   └── Calibrate: is this learning aligned with my growth direction?
⑤ Reflection cadence: When do I do all this?
   └── End of session / daily reflection
```

---

## ① Scope Check

Before acting on a task or recording knowledge, ask:

1. Is this within my defined responsibilities? → Yes = proceed, No = hand off
2. Does it require my specific expertise? → Yes = likely mine, No = likely someone else's
3. Will doing this pull me away from core duties? → Yes = hand off

**How to hand off well:** Explain why it's not yours + suggest who should handle it + share any relevant context you have. Don't just refuse.

---

## ② Learning Filter

Trigger this when you:
- Solve a tricky problem (will this recur?)
- Discover a better approach (method or one-off trick?)
- Complete a complex task (any reusable knowledge in the process?)
- End a session (anything worth preserving?)

### Routing Decision

```
What I learned
    │
    ├── Operational rule (how tools work, paths, gotchas)
    │   → CLAUDE.md Lessons Learned
    │
    ├── Reusable knowledge (methodology, domain expertise)
    │   → Knowledge file → eventually a skill
    │
    └── One-off, won't repeat
        → Don't record (or just daily log)
```

**Test:** "Would this knowledge be useful in a different project?" Yes → it's reusable. No → Lessons Learned at most.

---

## ③ Knowledge Routing

| Type | Where | When to promote |
|------|-------|-----------------|
| Operational rules, gotchas | CLAUDE.md Lessons Learned | Immediately on discovery |
| Research, analysis in progress | Knowledge files (e.g., `knowledge/`) | When pattern appears 3+ times |
| Validated methodology | Skill (`.claude/skills/`) | When proven across 2+ projects/tasks |
| Daily work log | Session notes / memory files | Don't promote — it's context, not knowledge |

### Knowledge Lifecycle

```
Raw learning (notes, observations)
    ↓ Appears 3+ times or across 2+ contexts
Validated pattern (documented methodology)
    ↓ Proven reusable, clear scope
Skill (formal capability in .claude/skills/)
```

### Promotion Signals

- Same problem keeps appearing → extract a pattern
- You keep explaining the same thing → document it once
- A knowledge file grows past useful size → split or formalize

---

## ④ Feedback Loop

At reflection time, ask yourself:

1. **Signal detection:** What feedback did I get today? User corrections? Rework? Praise?
2. **Pattern recognition:** Across recent sessions — what keeps getting corrected? What's improving?
3. **Direction check:** Are my learnings aligned with becoming better at my core job?

### Without explicit growth goals

If you don't have defined growth objectives, focus on:
- Reducing rework (fewer corrections from user)
- Increasing first-attempt success rate
- Expanding the situations you can handle independently

---

## ⑤ Reflection Cadence

At the end of each session:
- Review tasks and learnings from this session
- Check if any knowledge should be promoted (notes → methodology → skill)
- Execute knowledge routing for anything new
- Note any recurring patterns or weaknesses

### Reflection Principles

- **Synthesize, don't collect** — Don't repeat what happened; extract what matters
- **Search when you find gaps** — If you realize you don't know something, look it up now
- **Record or it didn't happen** — Saying "I learned X" without writing it down = didn't learn
- **"Nothing to note" is usually wrong** — Look harder

---

## Red Lines

1. **Don't record everything** — One-off facts aren't worth the overhead. Be selective.
2. **Don't build catch-all containers** — Each knowledge file/skill should have clear scope.
3. **Don't record outside your scope** — Valuable knowledge that's not your domain? Pass it to the right owner.
4. **Don't reinvent** — Check if an existing skill/file already covers this before creating new ones.
5. **Don't skip the filter** — Every piece of knowledge goes through ②. No exceptions.
