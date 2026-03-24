# Skill Design Template

> Based on agentskill-expertise design principles. Copy this template, fill in the content following the guidance, and delete all `💡` guide text when done.

---

## Frontmatter

```yaml
---
name: [skill-name]
description: [see Description Writing Guide below]
---
```

### Description Writing Guide

💡 **Principle**: Describe "usage scenarios", not "feature categories"

- ❌ "Project knowledge management Skill" → Unclear when to trigger
- ✅ "Trigger when discussing architecture decisions or technology selection" → Clear trigger condition

**Recommended structure**: One-sentence positioning + list of usage scenarios + proactive update triggers

**Constraint**: All Skills share a 15,000 character budget — be concise but information-dense

---

## SKILL.md Body

```markdown
# {Skill Name} - {One-sentence positioning}

## Overview

[What problem does this Skill solve? What happens without it? What's different with it?]

💡 2-3 sentences to make the core value clear.

---

## Core Principles

[List 3-5 core principles/values]

💡 Give principles, not rules.
- One principle covers a wide range of rules
- 10+ specific rules → try to distill into 2-3 principles
- Suggested format: principle name + one-sentence explanation + contrast (❌ vs ✅)

| Principle | Explanation | Contrast |
|-----------|-------------|---------|
| [Principle 1] | [Why this matters] | ❌ ... → ✅ ... |
| [Principle 2] | [Why this matters] | ❌ ... → ✅ ... |

---

## [Core Content Section — Name It Freely]

[Organize the main body of knowledge freely based on the Skill type]

💡 Notes:
- SKILL.md total < 5k tokens
- Long content (case libraries, detailed reference) → references/
- Include at least one concrete example

---

## When to Update This Skill

> **AI proactive update rule**: When the following situations occur, AI should proactively propose updates without waiting for the user to ask.

| Situation | Update What | Operation |
|-----------|------------|-----------|
| [Trigger situation 1] | [Which file/section] | [append/modify/add] |
| [Trigger situation 2] | [Which file/section] | [append/modify/add] |

### Update Principles

1. **Evidence-driven**: Only document insights validated through practice
2. **Preserve context**: When updating, note "when and what prompted this discovery"
3. **Lean is paramount**: This Skill itself must follow "less is more"

### AI Behavior Guidelines

- Discovered a new pattern during collaboration → **proactively propose** an update
- After completing relevant work → **automatically ask** whether to append to the case library
- User's need clearly triggers this Skill but they didn't specify → **proactively suggest loading**

---

## Reference Resources

- **[Resource Name]**: `references/[filename].md`
```

---

## references/ Structure

```
references/
├── [core extension].md      ← primary detailed content
├── [case or pattern library].md   ← accumulative document, can be appended continuously
└── [others added as needed]
```

💡 References are Level 3 (loaded on demand). Good fits:
- Detailed case libraries (continuously accumulating type)
- Official citations and evidence
- Extended reference material
- Long content that doesn't belong in SKILL.md

---

## Post-Completion Self-Check

### Description
- [ ] Situation-oriented, not feature-category-oriented
- [ ] After reading, AI can judge "when to load this"
- [ ] Concise but information-dense
- [ ] Includes proactive update triggers

### Content
- [ ] Primarily principles/values, not rule enumeration
- [ ] Has concrete examples (at least one)
- [ ] SKILL.md < 5k tokens
- [ ] Long content is in references/

### Architecture
- [ ] One Skill solves one class of problems
- [ ] No significant overlap with other Skills

### Maintainability
- [ ] Has a "when to update" statement
- [ ] Structure allows appending without requiring a rewrite
- [ ] References are independent documents that can be updated separately
