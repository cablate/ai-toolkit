# Historical Data Analysis

How to extract actionable patterns from a user's Threads post history. Output feeds directly into prediction-model.md.

## Step 1: Data Intake

Accept any format: CSV, pasted list, verbal description of recent posts. Minimum useful data per post:
- Content (or topic summary)
- Engagement metrics (likes, comments, reposts — at least one)

Optional but improves accuracy:
- Post date/time
- Thread count
- Whether it went viral relative to account baseline

**Minimum posts:** 15+ for baseline. 30+ for pattern extraction. Under 15 — skip to prediction-model.md and use darkseoking benchmark.

## Step 2: Establish Baseline

Calculate the user's **engagement baseline** — the typical performance range for their account.

- **Median engagement** (not average — outliers skew averages)
- **Baseline range**: 25th-75th percentile
- **Viral threshold**: posts above 90th percentile for this account
- **Underperformance threshold**: posts below 25th percentile

This baseline is account-specific. A 200-like post is viral for a 1k-follower account, underperformance for a 50k account.

## Step 3: Content Categorization

Tag each post on these dimensions. Categories align with prediction-model.md Pattern 1 hierarchy:

| Dimension | How to categorize |
|-----------|-------------------|
| **Content type** | Original research/deep-dive, Actionable framework (numbered steps/checklist), Industry exposé/contrarian take, Tool/tech review with personal results, Personal story with hard numbers, Series/challenge log, Meta/admin (thanks/intro/announcement) |
| **Content source** | First-hand (own experiment, own data, own mistake) vs Second-hand (commentary, news reaction, tool review without personal data) |
| **Thread count** | 0 (single), 1, 2-4, 5-7, 8+ |
| **Topic cluster** | Group by semantic similarity (what the post is about) |
| **Series membership** | Is this part of a recurring series? Which one? What installment number? |

## Step 4: Pattern Extraction

Cross-reference categories with engagement to find:

### 4a. Content type performance ranking
Map each content type to its average engagement as a multiple of baseline. This directly feeds prediction-model.md Pattern 1. Example: "Original research posts average 5.2x baseline; tool reviews average 1.1x baseline."

### 4b. Thread structure correlation
Do multi-thread posts consistently outperform singles? What thread count range correlates with highest engagement? Feeds Pattern 2.

### 4c. Series decay curve
For each series: plot engagement from installment #1 → #N. Does it decay? At what rate? Does it stabilize? Feeds Pattern 3.

### 4d. Post-viral sequence analysis
After each viral post (>90th percentile), what happened to the next 3 posts? Categorize the sequence by topic distance (same angle / same niche different angle / different niche). Feeds Pattern 4.

### 4e. First-hand vs second-hand premium
Compare average engagement of first-hand content vs second-hand content. Feeds Pattern 5.

### 4f. Timing patterns (if dates available)
- Optimal gap between posts
- Post-viral recovery time (how many days/posts until baseline returns)

## Step 5: Output Summary

Present findings in this format (prediction-model.md expects these exact fields):

```
ACCOUNT PROFILE
- Baseline: [median] likes, range [25th]-[75th]
- Viral threshold: [90th percentile]+ likes
- Creator Embedding sweet spot: [topic] × [content type] × [thread count]

CONTENT TYPE RANKING (feeds Pattern 1)
1. [Content type] → [avg engagement] ([X]× baseline)
2. [Content type] → [avg engagement] ([X]× baseline)
3. [Content type] → [avg engagement] ([X]× baseline)
...

THREAD STRUCTURE (feeds Pattern 2)
- Optimal thread count: [range]
- Single vs multi-thread performance ratio: [X]

SERIES DECAY (feeds Pattern 3, if applicable)
- [Series name]: #1 [likes] → #2 [likes] → ... stabilizes at [X]% of #1

FIRST-HAND PREMIUM (feeds Pattern 5)
- First-hand avg: [X]× baseline
- Second-hand avg: [X]× baseline

RISK PATTERNS
- [Pattern that consistently underperforms]
- [Topic showing saturation / diminishing returns]

RECOMMENDATIONS
- Next post: [content type with highest probability]
- Avoid: [specific thing to avoid based on data]
```
