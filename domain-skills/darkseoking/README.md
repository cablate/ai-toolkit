# darkseoking — SEO & Threads Algorithm Skills

Three-layer skill set distilled from [darkseoking](https://www.threads.net/@darkseoking), an SEO practitioner with 10+ years of experience. Every insight is backed by Meta/Google algorithm patents or controlled experiments with real data.

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

Copy the skill directories into your Claude Code project's `.claude/skills/` and place the CSV where skills can reference it.

Each skill works independently but they complement each other:

1. **mindset** gives you the "why" — algorithm mechanics and strategy principles
2. **optimizer** gives you the "check" — systematic review before publishing
3. **predictor** gives you the "what if" — performance estimation before committing
