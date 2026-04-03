# Prediction Model

How to predict a post's performance ceiling and recommend optimal content strategy — derived from darkseoking's 80-post dataset cross-referenced with Meta algorithm patent knowledge.

## Prerequisites

Run historical-analysis.md first if the user has their own data. If no personal data, use the patterns below as benchmark.

---

## Pattern 1: Content Type Hierarchy

From darkseoking's data, content types rank by engagement ceiling:

| Content Type | Engagement Range | Example |
|-------------|-----------------|---------|
| **Original research / patent deep-dive** | 10x-250x baseline | Algorithm patent analysis (20k, 15k likes) |
| **Actionable framework (numbered steps, checklist)** | 5x-15x baseline | Post-viral strategy (5 steps), 10 Q&A compilation |
| **Industry exposé / contrarian take** | 3x-7x baseline | "Low-end SEO hunting" series, "perfect SEO is imperfect" |
| **Tool/tech review with personal results** | 2x-5x baseline | AI SEO tool comparisons, open-source tool shares |
| **Personal story with hard numbers** | 2x-4x baseline | "Made 5.4M with AI+SEO, lost 8 figures in crypto" |
| **Series/challenge log (daily updates)** | 0.05x-1x baseline | "AI SEO gambling affiliate Day X" series (4-72 likes) |
| **Meta/admin posts (thanks, intro, announcement)** | Variable | Thanks posts ride prior viral momentum, not intrinsic value |

**Why this hierarchy works (patent basis):**
- Original research has highest semantic precision → better first-batch matching (US10579688B2)
- Frameworks generate deep comments + DM shares → highest MSI weight (US9378529B2)
- Daily logs have low info density per post → low Expected Engagement Value

---

## Pattern 2: Thread Structure × Engagement

| Thread Count | Observed Performance | Conditions |
|-------------|---------------------|------------|
| 5-7 threads | Highest ceiling (top 4 posts all had 6-11 threads) | Each thread adds independent deep value |
| 2-4 threads | Strong mid-range (many 200-800 like posts) | Good for structured arguments |
| 1 thread (single reply) | Variable, slightly above singles | Only if reply adds real value |
| 0 (single post) | Full range, but ceiling limited | Works for short punchy takes |

**Key finding:** All 4 posts above 1,000 likes had 6+ threads. But thread count alone doesn't cause virality — it correlates with content depth. Shallow content split across threads performs worse than a dense single post.

---

## Pattern 3: Series Decay Pattern

Recurring series show predictable decay:

**"Low-end SEO hunting" series:** 526 → 249 → 141 → 133 → 154 likes
- ~50% drop from #1 to #2, then stabilizes around 25-30% of #1
- Occasional recovery when angle shifts significantly (#4 recovered slightly)

**"AI SEO gambling" daily series:** 20 → 17 → 4 → 72 → 51 → 52 → 56 likes
- Daily logs cluster around baseline or below
- Spike at Day 12 (72) = likely introduced new content angle

**Implication:** Series have a natural engagement floor around 25-30% of the first installment. The diversity mechanism (US9336553B2) penalizes same-topic repetition. To sustain: each installment must shift angle, not just continue.

---

## Pattern 4: Post-Viral Sequence

darkseoking's actual viral sequence:
1. Algorithm patents (20,193) — original research
2. Thanks + milestone + test result (1,270) — different topic, mentions prior post lightly
3. Post-viral strategy breakdown (14,943) — related but different angle (meta-analysis of own behavior)
4. 10 Q&A compilation (1,238) — same domain, completely different format

**What worked:** Each post was a different content type within the same niche. Never repeated the same angle. The thanks post explicitly tested the diversity mechanism and confirmed it.

**Post-viral ceiling prediction:**
- If next post is same topic + same angle → expect 30-60% of baseline (diversity penalty)
- If next post is same niche + different angle → expect baseline to 1.5x baseline
- If next post is different niche → expect 0.3-0.7x baseline (Creator Embedding mismatch, US10558714B2)

---

## Pattern 5: First-Hand vs Second-Hand Content

Posts with first-hand data/experience consistently outperform:

| Content Source | Typical Performance |
|---------------|-------------------|
| Own experiment with numbers ("spent $3000 testing KGR") | Above baseline |
| Own mistake/loss ("lost 8 figures in crypto") | Above baseline |
| Original patent/document research | Far above baseline |
| Tool review without personal data | Around baseline |
| Commentary on others' content/news | Around or below baseline |

**Why (patent basis):** First-hand content has higher authenticity signals, generates deeper comments (people ask follow-up questions), and is harder to duplicate — all factors the algorithm rewards.

---

## Ceiling Prediction Method

### Step 1: Identify content type from hierarchy (Pattern 1)
→ Gives base multiplier range

### Step 2: Check thread structure (Pattern 2)
→ Multi-thread deep content raises ceiling; shallow single posts cap it

### Step 3: Check diversity distance from recent posts (Pattern 4)
→ Same angle = severe penalty; different angle within niche = neutral/bonus

### Step 4: Check series position if applicable (Pattern 3)
→ Later installments expect 25-50% of first installment unless angle shifts

### Step 5: Check first-hand vs second-hand (Pattern 5)
→ First-hand raises ceiling; pure commentary caps it

### Step 6: Apply timing (from darkseoking-mindset)
→ <24h after viral = competing with own diffusion; 24-48h+ gap = neutral/bonus

### Combine:
```
Predicted Range = Account Baseline × Content Type Range × Adjustments

Where:
- Account Baseline = user's median engagement (or darkseoking's ~77 likes as benchmark)
- Content Type Range = from Pattern 1 hierarchy
- Adjustments = narrowed by Patterns 2-5

Output as RANGE with reasoning, never a single number.
```

**Without user's historical data:** Use darkseoking's patterns as directional benchmark. Scale by estimated account size ratio (follower count as rough proxy). Emphasize that ceiling prediction is less precise without personal data, but content type hierarchy and diversity rules still apply universally.

---

## Output Format

```
PREDICTION
- Ceiling range: [X]-[Y] likes
- Based on: [content type] + [thread structure] + [diversity distance] + [timing]
- Confidence: High (has personal data + clear pattern match) / Medium (benchmark only or mixed signals) / Low (insufficient data or unusual content)
- Key risk: [biggest factor that could pull performance down]
- Key upside: [factor that could push it higher]

OPTIMIZATION
- [Specific, actionable suggestion to raise ceiling based on patterns]

NEXT POST RECOMMENDATION (if asked)
- Content type: [from hierarchy] × [thread structure] × [angle]
- Why: [which pattern supports this]
- Avoid: [what pattern says NOT to do]
```
