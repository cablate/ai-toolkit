---
name: darkseoking-post-predictor
description: Use when predicting Threads post performance, analyzing post history patterns, estimating engagement ceiling for a draft, or deciding what content type to write next. Works with or without personal data — uses darkseoking benchmark as fallback.
---

# Threads Post Predictor

Analyzes historical Threads post data using algorithm knowledge from `darkseoking-mindset` to predict post performance and recommend optimal content strategy.

## How to Use

### With personal data (more precise)

1. User provides post history — see **Data Format** below
2. Load [historical-analysis.md](references/historical-analysis.md) — build personal baseline and patterns
3. Load [prediction-model.md](references/prediction-model.md) — predict ceiling using personal patterns
4. Present findings: ceiling range, optimization suggestions, content-type recommendation

### Without personal data (still useful)

1. Skip historical-analysis.md
2. Load [prediction-model.md](references/prediction-model.md) — use darkseoking benchmark patterns directly
3. Predict based on content type hierarchy, thread structure, and algorithm rules
4. Note: predictions are directional (which content type has higher ceiling) rather than numeric

## Data Format

**Minimum useful data per post:** content (or topic summary) + at least one engagement metric (likes, comments, or reposts).

**Ideal CSV columns:** rank, likes, reposts, comments, link, content, thread_count, thread_content

**Minimum posts:** 15+ for meaningful baseline. 30+ for pattern extraction. Under 15 — use darkseoking benchmark with caveats.

**Accepted formats:** CSV, pasted list, verbal description of recent 5-10 posts with approximate engagement numbers.

## Scenes

| Scenario | Action |
|----------|--------|
| User provides full post history | Run complete analysis + prediction |
| User asks "what should I write next?" with data context | Run content-type recommendation |
| User wants to know ceiling before posting | Run prediction on draft + historical context |
| User wants to understand why a post underperformed | Run gap analysis against historical patterns |
| User has no data, just wants general guidance | Use darkseoking benchmark patterns from prediction-model.md |

## References

- [historical-analysis.md](references/historical-analysis.md) — how to extract patterns from post data
- [prediction-model.md](references/prediction-model.md) — how to predict ceiling and recommend strategy
- Benchmark data → `darkseoking-mindset/references/darkseoking-all-posts.csv`
- Algorithm knowledge → `darkseoking-mindset` skill
