# Domain Skills

Domain-specific skill sets for Claude Code. Unlike the generic infrastructure skills in `skills/`, these are built around a particular topic or practitioner's methodology.

Skills are organized flat with prefix-based grouping (e.g., `darkseoking-*`).

---

## darkseoking — SEO & Threads Algorithm Skills

Three-layer skill set distilled from [darkseoking](https://www.threads.net/@darkseoking), an SEO practitioner with 10+ years of experience. Every insight is backed by Meta/Google algorithm patents or controlled experiments with real data.

### Architecture

```
Knowledge        →  darkseoking-mindset         8 mental models + 8 reference docs
Operations       →  darkseoking-post-optimizer   Pre-publish checklist (PASS/WARN/FAIL)
Prediction       →  darkseoking-post-predictor   Engagement ceiling estimation
```

### Skills

| Skill | Triggers on | What it does |
|-------|------------|--------------|
| `darkseoking-mindset` | SEO algorithm questions, content strategy, Threads growth, GEO optimization, vendor evaluation | Provides battle-tested mental models and deep reference material on algorithms, content strategy, and growth |
| `darkseoking-post-optimizer` | Writing/reviewing Threads posts, post-viral strategy, posting timing | Runs 8-item pre-publish checklist based on Meta algorithm patents |
| `darkseoking-post-predictor` | Predicting post performance, analyzing history, estimating engagement ceiling | Predicts engagement ceiling with or without personal data (uses darkseoking benchmark as fallback) |

### Shared Data

- `darkseoking-all-posts.csv` — 84 posts with engagement metrics, used as benchmark data across all three skills

### Key Patents Referenced

| Patent | Mechanism |
|--------|-----------|
| US10579688B2 | Semantic vector matching for content distribution |
| US9336553B2 | Diversity mechanism (penalizes same-source density) |
| US10558714B2 | Creator Embedding (account positioning) |
| US9378529B2 | Expected Engagement Value |
| US8402094B2 | Self-competition penalty for rapid posting |

### Setup

Copy the skill directories into your Claude Code project's `.claude/skills/` and add the CSV path to your configuration. Each skill works independently but they complement each other:

1. **mindset** gives you the "why" — algorithm mechanics and strategy principles
2. **optimizer** gives you the "check" — systematic review before publishing
3. **predictor** gives you the "what if" — performance estimation before committing
