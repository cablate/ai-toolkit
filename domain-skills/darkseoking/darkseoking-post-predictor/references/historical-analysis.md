# Historical Data Analysis

How to extract actionable patterns from a user's Threads post history. Output feeds directly into prediction-model.md.

## Step 1: Data Intake

Accept any format: CSV, pasted list, verbal description of recent posts. Minimum useful data per post:
- Content (or topic summary)
- Engagement metrics (likes, comments, reposts — at least one)

**Critical for V2 dual-stage prediction** (strongly recommended):
- **Views** — required to separate distribution from conversion
- **Engagement rate** (likes/views) — or calculate from likes + views

Optional but improves accuracy:
- Post date/time (enables timing analysis)
- Thread count
- Shares/reposts count (enables share ratio analysis)
- Whether it went viral relative to account baseline

**Minimum posts:** 15+ for baseline. 30+ for pattern extraction. Under 15 — skip to prediction-model.md and use darkseoking benchmark.

**If views data is missing:** V2 dual-stage prediction falls back to V1 single-stage (content type → likes). Note this limitation in output.

## Step 2: Establish Baseline (Dual-Axis)

Calculate **three separate baselines** — likes, views, and ER:

### 2a. Likes baseline (same as V1)
- **Median likes** (not average — outliers skew averages)
- **Baseline range**: 25th-75th percentile
- **Viral threshold**: posts above 90th percentile
- **Underperformance threshold**: posts below 25th percentile

### 2b. Views baseline (V2 — requires views data)
- **Median views**
- **Views range**: 25th-75th percentile
- **High distribution threshold**: 90th percentile views

### 2c. Engagement Rate baseline (V2 — requires views data)
- **Median ER** (likes / views)
- **ER range**: 25th-75th percentile
- **High conversion threshold**: 90th percentile ER

### 2d. Quadrant thresholds
Using views median and ER median as axes, classify every post into one of four quadrants:

| Quadrant | Condition | Meaning |
|----------|-----------|---------|
| HV+HE | views >= median AND ER >= median | Jackpot — both distribution and conversion fire |
| HV+LE | views >= median AND ER < median | Distribution-driven — algorithm pushes but conversion is weak |
| LV+HE | views < median AND ER >= median | Conversion-driven — high resonance but limited distribution |
| LV+LE | views < median AND ER < median | Underperform — neither mechanism fires |

Calculate mean/median likes for each quadrant. This gives the ceiling range per quadrant.

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
- Optimal gap between posts (bucket by <6h, 6-12h, 12-24h, 1-2d, 2-3d, 3d+)
- Day of week performance (mean likes per day)
- Post-viral recovery time (how many days/posts until baseline returns)

### 4g. Quadrant distribution (V2 — requires views data)
Classify each post into the four quadrants from Step 2d. Then for each quadrant:
- How many posts land in this quadrant?
- What's the mean/median likes, views, ER?
- What content types cluster in each quadrant?
- What's the ceiling (max) for each quadrant?

This reveals the account's **success mode**: distribution-driven accounts have most winners in HV+LE, conversion-driven accounts in LV+HE, balanced accounts in HV+HE.

### 4h. Persona profile extraction
From the full post history, extract the creator's **positioning tags** — what recurring identity does this account project?

Look for:
- **Work ethic signal**: "always building", "daily updates", "never stops" → hardworking positioning
- **Expertise signal**: specific domain they repeatedly deep-dive into
- **Style signal**: contrarian, educational, vulnerable, provocative
- **Community role**: helper, critic, entertainer, insider

These tags determine which posts qualify as **Persona Contrast** (Pattern 6 in prediction-model.md) — a post that breaks the established positioning. Without knowing the positioning, you can't predict contrast effects.

### 4i. Content portfolio mix
Classify each post as Core (original research, framework, tool showcase, personal journey with data), Light (life/casual, commentary, quick reaction), or Experimental (new topic/format). Then calculate:
- Overall ratio: X% core / Y% light / Z% experimental
- Recent trend (last 10 posts): is the mix shifting?
- Longest streak of consecutive core posts without a light post

Healthy benchmark: ~60-70% core / 20-30% light / ~10% experimental. If the account is >80% core with very few light posts, flag this — the account may look like a "content machine" and miss diversity/authenticity signals.

### 4j. Account-specific overrides
Some universal patterns reverse on specific accounts. Check and note:
- Text length × performance: does longer text = higher or lower performance? (Universal assumption: shorter is better. Some accounts reverse this.)
- Quote post penalty: how severe? (Universal: moderate. Some accounts: extreme.)
- Media type: does adding images help or not? (Varies by account.)

## Step 5: Output Summary

Present findings in this format. If views data is available, include V2 sections. If not, skip V2 sections and note the limitation.

```
ACCOUNT PROFILE
- Likes baseline: [median] likes, range [25th]-[75th], viral threshold [P90]+
- Views baseline: [median] views, range [25th]-[75th] (V2)
- ER baseline: [median]%, range [25th]-[75th] (V2)
- Creator Embedding sweet spot: [topic] × [content type] × [format]

QUADRANT PROFILE (V2 — requires views data)
- HV+HE (Jackpot): n=[X] posts, mean [X] likes, ceiling [max]
- HV+LE (Distribution-driven): n=[X] posts, mean [X] likes, ceiling [max]
- LV+HE (Conversion-driven): n=[X] posts, mean [X] likes, ceiling [max]
- LV+LE (Underperform): n=[X] posts, mean [X] likes
- Account success mode: [distribution-driven / conversion-driven / balanced]

PERSONA PROFILE
- Positioning tags: [e.g. "hardworking", "technical deep-diver", "direct/provocative"]
- Contrast triggers: [what kind of post would break this positioning]

CONTENT TYPE RANKING (feeds Pattern 1)
1. [Content type] → [avg likes] ([X]× baseline) | avg views [X] | avg ER [X%]
2. [Content type] → [avg likes] ([X]× baseline) | avg views [X] | avg ER [X%]
...

TIMING (feeds prediction Stage 1)
- Best days: [day(s)] (mean [X] likes)
- Worst days: [day(s)] (mean [X] likes)
- Optimal post gap: [range]

THREAD STRUCTURE (feeds Pattern 2)
- Optimal thread count: [range]
- Single vs multi-thread performance ratio: [X]

SERIES DECAY (feeds Pattern 3, if applicable)
- [Series name]: #1 [likes] → #2 [likes] → ... stabilizes at [X]% of #1

FIRST-HAND PREMIUM (feeds Pattern 5)
- First-hand avg: [X]× baseline
- Second-hand avg: [X]× baseline

CONTENT PORTFOLIO MIX (feeds Pattern 7)
- Overall: [X]% core / [Y]% light / [Z]% experimental
- Last 10 posts: [ratio]
- Longest core streak: [N] posts
- Assessment: [healthy / skewed toward core / skewed toward light]

ACCOUNT-SPECIFIC OVERRIDES
- Text length: [longer = better / shorter = better / no effect]
- Quote post penalty: [severity]
- Media type: [IMAGE/TEXT/CAROUSEL — which performs best]

RISK PATTERNS
- [Pattern that consistently underperforms]
- [Topic showing saturation / diminishing returns]

RECOMMENDATIONS
- Next post: [content type] targeting [quadrant]
- Optimization path: [increase distribution / increase conversion / both]
- Avoid: [specific thing to avoid based on data]
```

**If building a personal profile file** (e.g. `cab-late-profile.md`): save the ACCOUNT PROFILE, QUADRANT PROFILE, PERSONA PROFILE, TIMING, and ACCOUNT-SPECIFIC OVERRIDES sections into a dedicated reference file. This allows future predictions to load the profile directly without re-running full historical analysis.
