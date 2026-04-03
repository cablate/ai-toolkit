# darkseoking — SEO & Threads Algorithm Skills

Three-layer skill set built on the methodology of [@darkseoking](https://www.threads.net/@darkseoking) — an SEO practitioner and Threads creator with 10+ years of hands-on experience, 17k+ followers grown through algorithm-informed content strategy. He spent real money on controlled experiments and reverse-engineered Meta/Google algorithm patents to understand how content distribution actually works. Every insight in these skills is backed by patent filings or tested data — no speculation, no "industry consensus" parroting.

## Architecture

```
Knowledge        →  darkseoking-mindset         8 mental models + 8 reference docs
Operations       →  darkseoking-post-optimizer   Pre-publish checklist (PASS/WARN/FAIL)
Prediction       →  darkseoking-post-predictor   Engagement ceiling estimation
```

## Skills

### darkseoking-mindset

**Triggers:** SEO algorithm questions, content strategy, Threads growth, GEO optimization, vendor evaluation

The knowledge layer. Eight core mental models (reverse-engineer from patents, pay to test, question consensus, cross-platform logic, boundary conditions, minimize cost, toolify knowledge, account positioning) plus eight deep-dive reference docs covering algorithm analysis, content strategy, Threads growth, GEO/AI citation, vendor evaluation, AI tooling, experiment design, and operational philosophy.

### darkseoking-post-optimizer

**Triggers:** Writing/reviewing Threads posts, post-viral strategy, posting timing

The operations layer. Runs an 8-item pre-publish checklist — each item rated PASS/WARN/FAIL with specific reasoning:

1. First Line (info density, no clickbait)
2. Semantic Precision (domain-specific terms)
3. Topic Distance (diversity penalty avoidance)
4. External Links (authority + relevance)
5. Thread Structure (standalone main + value-add threads)
6. Timing (self-competition avoidance)
7. Post-Viral Strategy (only after viral post)
8. Topic Suggestion (only when asked "what to write")

#### Example: Optimizer in Action

**Draft:**
> Claude Code is amazing — compact, resume, and several other long-standing issues that people have been reporting on GitHub for ages about burning tokens, all got fixed within two days of the source code leaking!! Anyway the result is good, you can use it with more peace of mind now

**Checklist result:**

| # | Check | Rating | Reason |
|---|-------|--------|--------|
| 1 | First Line | WARN | "is amazing" is low-density; the real hook (source code leak → bugs fixed in 2 days) is buried in the middle |
| 2 | Semantic Precision | WARN | "burning tokens" and "several versions" are vague — which versions? what cost reduction? |
| 4 | External Links | PASS | No external links |
| 5 | Thread Structure | PASS | Single post, content density matches format |

**Suggested rewrite:**
> Claude Code's source code leaked, and within two days compact, resume, and other token-burning bugs that sat in GitHub Issues for multiple versions all got fixed. Coincidence? I don't know, but the result is good — it genuinely feels safer to use now.

The optimizer moved the core hook (source code leak → 2-day fix) to the first line, replaced vague terms with specifics, and kept the conversational tone.

---

### darkseoking-post-predictor

**Triggers:** Predicting post performance, analyzing history, estimating engagement ceiling

The prediction layer. Estimates engagement ceiling for a draft, with or without personal post history data. With data (15+ posts): builds personal baseline, extracts patterns, predicts against them. Without data: uses darkseoking's 84-post benchmark as fallback for directional guidance.

## Shared Data

- `darkseoking-all-posts.csv` — 84 posts with engagement metrics (likes, reposts, comments, thread count, content), used as benchmark data across all three skills

## Key Patents Referenced

| Patent | Mechanism |
|--------|-----------|
| US10579688B2 | Semantic vector matching for content distribution |
| US9336553B2 | Diversity mechanism (penalizes same-source density) |
| US10558714B2 | Creator Embedding (account positioning) |
| US9378529B2 | Expected Engagement Value |
| US8402094B2 | Self-competition penalty for rapid posting |
| US10565267B1 | Rapid posting distribution penalty |
| US20140172877A1 | Priority distribution pool after pause |
| EP2977948A1 | Domain authority evaluation for links |
| US10268763B2 | Content relevance scoring for links |

## Setup

> New to Claude Code skills? See the [ai-toolkit main README](../../README.md) for general setup instructions.

1. Copy the three skill directories (`darkseoking-mindset/`, `darkseoking-post-optimizer/`, `darkseoking-post-predictor/`) into your project's `.claude/skills/`
2. Place `darkseoking-all-posts.csv` where the skills can reference it (e.g., alongside the skill directories, then adjust paths in SKILL.md)
3. Claude Code will auto-detect the skills based on their `description` triggers — no manual activation needed

Each skill works independently but they complement each other:

1. **mindset** gives you the "why" — algorithm mechanics and strategy principles
2. **optimizer** gives you the "check" — systematic review before publishing
3. **predictor** gives you the "what if" — performance estimation before committing
