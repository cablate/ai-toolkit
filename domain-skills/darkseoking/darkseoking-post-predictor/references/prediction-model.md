# Prediction Model

How to predict a post's performance ceiling and recommend optimal content strategy.

Two data sources:
- **darkseoking benchmark** (80 posts) — distribution-driven account, useful for content type hierarchy and algorithm rules
- **Personal data** (if available via historical-analysis.md) — account-specific baselines, quadrant profile, persona tags

## Prerequisites

Run historical-analysis.md first if the user has their own data. If no personal data, use darkseoking benchmark patterns below.

**If user has a personal profile** (`personal-profile.md`), load it — it contains account-specific baselines and overrides that take priority over darkseoking benchmark.

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

## Pattern 6: Persona Contrast Effect

A post's value can come from WHO says it in WHAT context, not just the content itself.

**Case study (cab_late, 2026-04-05):**
- Post: "連假看著群組...感到疲憊...決定放下 AI 去吃蝦喝啤酒"
- Predicted as Life/Casual → 0.4x baseline (15-40 likes)
- Actual: 122 likes = 1.8x baseline (6hr mark, still climbing)

**Why it worked:**
- cab_late is positioned as "the hardest-working AI guy" → him saying "I'm tired" = shock value
- Holiday timing: everyone was watching others hustle, collective exhaustion resonated
- Low-friction engagement: no thinking required to like, just emotional agreement

**Classification rule:** Before categorizing a post as Life/Casual, check: does the value come from the content, or from "who said this + when"? If the latter, apply Persona Contrast multiplier instead of Life/Casual multiplier.

**Persona Contrast conditions:**
- Creator has a strong, consistent positioning (e.g. "always working", "hardcore technical")
- Post breaks that positioning in a relatable way
- Audience can project themselves onto the moment
- When all three → expect 1.5x-3x baseline, NOT 0.4x

**Patent basis:** Authenticity signals (US10579688B2) — posts that break pattern generate higher dwell time and deeper emotional engagement, which the algorithm reads as quality signals.

---

## Ceiling Prediction Method (V2: Dual-Stage)

Posts succeed through two independent mechanisms:
- **Distribution** (Views): how many people the algorithm shows this to
- **Conversion** (ER): what percentage of viewers engage

V1 only predicted likes directly, which conflates the two. V2 predicts each stage separately, then combines.

### Stage 1: Predict Views Range

Evaluate these factors to estimate how far the algorithm will push the post:

**1a. Content type distribution potential (Pattern 1)**
→ Original research / actionable frameworks get widest distribution. Series logs / life posts get minimal push.

**1b. Share potential**
→ Will people share/repost this? Actionable content and tool showcases drive shares → shares trigger secondary distribution. Check share/view ratio benchmarks from personal profile if available.

**1c. Creator Embedding match**
→ Is this post in the creator's established niche? On-niche = algorithm has a ready audience to distribute to. Off-niche = algorithm doesn't know who to show it to.

**1d. Diversity distance from recent posts (Pattern 4)**
→ Same angle as recent post = distribution suppressed. Different angle within niche = neutral/bonus.

**1e. Timing factors**
→ Day of week: check personal profile for high/low days.
→ Post gap: check personal profile for optimal interval.
→ Post-viral: <24h after viral = competing with own diffusion.

**1f. Is quote post?**
→ Quote posts get systematically lower distribution. If personal data shows quote penalty, apply it.

**Views estimate**: Combine factors → Low / Baseline / High / Very High distribution range, mapped to actual views numbers from personal profile.

### Stage 2: Predict ER Range

Evaluate these factors to estimate what percentage of viewers will engage:

**2a. Persona Contrast check (Pattern 6) — FIRST**
→ Does value come from "who said this + when" rather than content itself? If yes → high ER expected (1.5-2x normal ER). This overrides content-type ER expectations.

**2b. Content depth / friction**
→ Account-specific: some accounts reward depth (long text = quality signal → higher ER), others penalize it (long text = friction → lower ER). Check personal profile.

**2c. Emotional intensity**
→ Posts with strong emotional markers (vulnerability, anger, excitement) → higher dwell time → higher ER. Especially potent when combined with persona contrast.

**2d. First-hand vs second-hand (Pattern 5)**
→ First-hand content generates deeper engagement (follow-up questions, personal responses) → higher ER.

**2e. Engagement friction**
→ How much effort to engage? One-liner emotional agreement = zero friction = high ER. Technical deep-dive requiring full read = high friction = ER depends on content quality.

**ER estimate**: Combine factors → Below-normal / Normal / Above-normal / High ER range, mapped to actual ER numbers from personal profile.

### Stage 3: Combine + Quadrant Diagnosis

```
Predicted Likes Range = Views Range × ER Range

Then classify into quadrant:

| Quadrant | Views | ER | Meaning | Typical Ceiling |
|----------|-------|----|---------|-----------------|
| HV+HE (Jackpot) | High | High | Algorithm pushes + audience loves it | Highest (use personal profile data) |
| HV+LE (Distribution-driven) | High | Normal/Low | Algorithm pushes hard, moderate conversion | High likes via volume |
| LV+HE (Conversion-driven) | Normal/Low | High | Small audience but very engaged | Ceiling capped by distribution |
| LV+LE (Underperform) | Low | Low | Neither mechanism fires | Below baseline |
```

**Key insight**: LV+HE posts have a hard ceiling determined by how many people see them. The optimization path is different:
- HV+LE → improve content resonance / emotional hook
- LV+HE → increase shareability / distribution triggers to break out of low-views trap

### Fallback (no personal data)

Without views/ER data, fall back to V1 logic: use darkseoking content type hierarchy as directional benchmark. Note that predictions will be less precise and cannot distinguish distribution-driven vs conversion-driven success.

---

## Pattern 7: Content Portfolio Balance

Not every post should target HV+HE. Accounts need a mix of content intensities for long-term health.

**Why low-traffic posts are necessary:**
- **Posting rhythm**: sustains frequency without exhausting high-value material
- **Authenticity signal**: Creator Embedding needs to see a "real person," not a "content machine" — pure optimization looks artificial
- **Diversity reward**: US9336553B2 rewards content variety; all-banger feeds risk same-source density penalties
- **Contrast foundation**: Persona Contrast (Pattern 6) only works when there's a "normal" baseline to break from — if every post is intense, nothing feels different
- **Audience breathing room**: consecutive high-density content causes follower fatigue, depressing ER over time

**Recommended content mix (directional, not rigid):**

| Category | Share | Examples | Purpose |
|----------|-------|---------|---------|
| Core content | 60-70% | Original research, frameworks, tool showcase, personal journey with data | Ceiling-chasing, audience growth |
| Light content | 20-30% | Life/casual, commentary, quick takes, reactions | Rhythm, personality, diversity signal |
| Experimental | ~10% | New topics, new formats, boundary-testing | Creator Embedding expansion, surprise factor |

**How this affects prediction:**
- A Life/Casual post predicted at LV+LE is not a "bad post" if the account's recent 5 posts were all core content — it's a portfolio-balancing move
- Recommendation should consider recent content mix, not just maximize the next post's ceiling
- If a user asks "what should I post next?" and their last 3+ posts were all high-intensity, recommend a lighter post even though its predicted ceiling is lower

---

## Output Format

```
PREDICTION
- Quadrant: [HV+HE / HV+LE / LV+HE / LV+LE] — [one-line meaning]
- Views range: [X]-[Y] (based on: [key distribution factors])
- ER range: [X%]-[Y%] (based on: [key conversion factors])
- Likes range: [X]-[Y]
- Confidence: High / Medium / Low
- Key risk: [biggest factor that could pull performance down]
- Key upside: [factor that could push it higher]

OPTIMIZATION (tailored to predicted quadrant)
- If HV+LE: [how to increase ER — emotional hook, persona contrast, reduce friction]
- If LV+HE: [how to increase views — shareability, thread structure, timing]
- If LV+LE: [fundamental content/angle change needed]
- If HV+HE: [maintain — what's working and don't change]

PORTFOLIO CONTEXT (Pattern 7)
- Recent content mix: [last 5 posts: X core / Y light / Z experimental]
- Portfolio balance: [healthy / skewed toward core / skewed toward light]
- This post's role: [ceiling-chasing / rhythm maintenance / experiment]

NEXT POST RECOMMENDATION (if asked)
- Target quadrant: [which quadrant to aim for]
- Content type: [from hierarchy] × [angle] × [timing]
- Portfolio rationale: [why this type now — ceiling opportunity / diversity needed / contrast setup]
- Avoid: [what would pull it to a worse quadrant]
```
