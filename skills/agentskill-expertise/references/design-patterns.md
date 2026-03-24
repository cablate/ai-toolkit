# Agent Skill Design Patterns and Anti-Patterns

> **Relationship to SKILL.md**: This is a quick-reference companion to the "Design Principles" and "Common Misconceptions" sections of SKILL.md. SKILL.md has the full explanations and source citations; this file provides a coded quick-reference format for fast lookup during review or design sessions.

## Design Patterns

### P1: Principle-Driven
**Situation**: You want AI to handle unforeseen situations
**Approach**: Give core principles and values, don't enumerate rules
**Contrast**:
- ❌ "If A, do X; if B, do Y" → Cases not covered don't get handled
- ✅ "Proactively anticipate problems, let the user focus on what matters" → AI judges when to intervene

### P2: Worldview-Driven
**Situation**: You want AI output to have "soul", not just technical correctness
**Approach**: Define the role's worldview/values, let style emerge naturally from the worldview
**Contrast**:
- ❌ "Don't use certain words" → AI writes around them, the problem remains
- ✅ "I don't want the tone to feel anxious" → AI understands why, automatically avoids all anxiety-inducing patterns

### P3: Protocol and Persona Separation
**Situation**: Building a maintainable, portable AI assistant
**Approach**: Split "how to behave" and "who it is" into two independent Skills; CLAUDE.md only holds the entry point
**Benefits**: Lean entry point, portable persona, protocols and persona can be flexibly combined

### P4: Situation-Triggered Description
**Situation**: You want the Skill to be loaded at the right moment
**Approach**: description describes "usage scenarios" not "feature categories"
**Contrast**:
- ❌ "Project knowledge management Skill" → Unclear when to trigger
- ✅ "Trigger when discussing architecture decisions or technology selection" → Clear trigger condition

### P5: Split First, Merge Later
**Situation**: Uncertain about Skill granularity
**Approach**: Create a separate Skill for each scenario first; once you discover overlapping core principles, merge into one Skill with situation-based branching

### P6: Passive Pre-load Architecture
**Situation**: Multiple documents you want AI to read on demand
**Approach**: Don't enumerate "remember to read X" in CLAUDE.md; make them Skill references so metadata pre-loads automatically

---

## Anti-Patterns

| Code | Symptom | Problem | Fix |
|------|---------|---------|-----|
| A1 Rule enumeration | SKILL.md with 50+ rules | Fails on uncovered cases | Distill into core principles |
| A2 Feature-oriented description | "This is an XXX Skill" | AI doesn't know when to trigger | Switch to situation-oriented |
| A3 CLAUDE.md bloat | 200+ lines, full of "remember to read X" | Forgotten entries don't get read | Split into Skills, passive pre-load |
| A4 Perfectionism | Never ships a v1.0 | Will never be finished | MV Skill, test then iterate |
| A5 Copying templates | Directly copying someone else's Skill | Their pain points aren't yours | Start from your own collaboration pain points |
| A6 Tool overload | 30+ Skills | Context confusion, AI hallucinations | Trim to only what's genuinely needed |
