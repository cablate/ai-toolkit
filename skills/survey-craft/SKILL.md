---
name: survey-craft
description: "Survey design, iteration, and analysis expertise. Use when: designing new surveys/questionnaires, reviewing survey quality, planning A/B tests for surveys, analyzing survey data (cross-tabulation, root cause analysis), or strategizing survey distribution and respondent retention."
version: 202603
---

# Survey Craft - Survey Lifecycle Expertise

## Overview

End-to-end knowledge system for survey work: from question design to data analysis. Without this, surveys tend to be too long, untested, analyzed superficially, and treated as one-off events. With this, surveys become iterative, data-driven instruments that produce actionable insights.

---

## Core Principles

| Principle | Explanation | Contrast |
|-----------|-------------|----------|
| **Brevity is survival** | Every extra question costs completions. 3-5 min / 8-12 questions is the sweet spot (2026 data). | ❌ "We need 30 questions to be thorough" → ✅ "What's the minimum to answer our research question?" |
| **One variable per test** | A/B tests must isolate a single change. Otherwise you learn nothing. | ❌ Change wording + order + incentive simultaneously → ✅ Test question order alone, measure completion rate |
| **Mobile-first design** | 50%+ respondents are on mobile. Complex question types (ranking, large multi-select) kill mobile completion. | ❌ Design on desktop, hope mobile works → ✅ Test on mobile first, simplify complex interactions |
| **Surveys are relationships** | A survey is not a one-off extraction. Treat respondents as a panel you nurture across versions. | ❌ Blast survey, ghost respondents → ✅ Thank → share findings → invite back |
| **Root cause before redesign** | When metrics disappoint, diagnose first (cross-tab, RCA). Don't redesign based on gut feeling. | ❌ "Completion rate is low, let's cut questions" → ✅ "Where exactly do people drop? Why?" |

---

## Survey Design Quick Reference

### Question Quality Checklist

- No double-barreled questions (asking two things at once)
- No double negatives or jargon
- 5-point or 7-point Likert scale for consistency
- Randomize option order to reduce order bias
- Multi-select: max 5 options on mobile, max 2-3 selections
- Start with easy/engaging questions (ice-breakers), end with demographics

### Completion Rate Benchmarks

| Type | Good | Excellent |
|------|------|-----------|
| NPS | 20%+ | 30%+ |
| Email survey | 12-25% | 25%+ |
| In-App survey | 30%+ | 50%+ |
| Community survey | 15-20% | 30%+ |

### 7 Levers for Higher Response Rate

1. **Length & timing** (high impact) — 3-5 min, send after key user actions
2. **Personalization** (high impact) — Use name, reference specific context
3. **Connect to their experience** (high impact) — Explain "why this survey matters to YOU"
4. **Strategic incentives** (medium) — Instant feedback > distant lottery
5. **Multi-channel distribution** (medium) — Email + social + in-app
6. **Respondent panel** (medium) — Build a long-term participant pool
7. **Adaptive follow-up** (lower) — AI-driven personalized reminders

---

## Iteration Framework

### Version Semantics

| Change scope | Version bump | Example |
|-------------|-------------|---------|
| Typo, option reorder | v1.0 → v1.1 | Reorder Q2 options |
| Add/remove 1-2 questions | v1.0 → v1.2 | Add one demographic question |
| Structural change (new branching) | v1.0 → v2.0 | Add early screening flow |
| Core questions rewritten | v2.0 → v3.0 | Completely rewrite pain-point section |

### When to Trigger a Patch (vX.1)

| Signal | Threshold |
|--------|-----------|
| Completion rate too low | < 25% |
| Single-question drop-off | > 50% abandon at one question |
| Mobile vs desktop gap | > 25 percentage points |
| Invalid responses | > 20% of total |

### Monitoring Cadence (Post-Launch)

- **Day 3**: Completion rate + avg time. If < 15%, review questions immediately.
- **Day 5**: Per-question drop-off. If any > 50%, adjust that question.
- **Day 7**: Sample size target check. If < 50% of goal, boost promotion.
- **Day 14**: Mobile vs desktop split, complex question completion rates.
- **Week 3-4**: Demographic distribution, data quality, branching ratios.

---

## Analysis Framework

### Three-Step Analysis

```
1. DESCRIBE — What happened?
   Descriptive stats, distributions, visualizations

2. DIAGNOSE — Why did it happen?
   Cross-tabulation (find sub-group differences)
   Root Cause Analysis (5 Whys, Fishbone)

3. DECIDE — What do we do?
   Prioritize by impact, define concrete actions
   "So what?" → "Now what?"
```

### Cross-Tabulation Decision Guide

Cross-tab when you suspect a metric hides sub-group differences. Pick two variables (e.g., tenure x satisfaction) and look for divergent patterns. Use chi-square test for significance. Details in `references/analysis-methods.md`.

### Root Cause Analysis (RCA) — When to Use

Use RCA when a metric is below threshold but the cause isn't obvious. Follow: Define problem → Collect data → Identify possible causes (5 Whys / Fishbone) → Validate root cause → Plan fix. Details in `references/analysis-methods.md`.

---

## Respondent Retention (Longitudinal)

For multi-wave surveys, the three enemies are **attrition**, **fatigue**, and **rising cost**.

Counter-strategies (in priority order):
1. **Cash/gift on completion** — Cash > gift cards. Immediate > delayed.
2. **Reminder sequence** — 24-48h → 1 week → 2 weeks. Max 3 touches.
3. **Multi-channel contact** — Email (primary) + SMS (high open rate) + postcard (warmth).
4. **Community building** — Share findings back, thank publicly, invite to events.

Details and specific tactics in `references/retention-playbook.md`.

---

## When to Update This Skill

| Situation | Update What | Operation |
|-----------|------------|-----------|
| Completed a survey cycle (design → analysis) | `references/case-library.md` | Append learnings |
| Found new benchmark data (newer than 2026) | Completion Rate Benchmarks table | Update numbers |
| Discovered a new analysis technique that worked | `references/analysis-methods.md` | Append method |
| A/B test produced surprising result | `references/case-library.md` | Append finding |
| Retention strategy succeeded/failed | `references/retention-playbook.md` | Append evidence |

---

## Reference Resources

- **Analysis Methods**: `references/analysis-methods.md` — Cross-tabulation walkthrough, RCA frameworks, data cleaning checklist
- **Retention Playbook**: `references/retention-playbook.md` — Longitudinal retention tactics, promotion strategies, incentive design
