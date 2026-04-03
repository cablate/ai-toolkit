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

A marketing consultant's account focuses on SEO and AI tools. Their last post (12 hours ago) about "5 AI writing tools" got 800 likes — well above their usual 200. They now want to post this:

**Draft:**
> AI is changing everything about how we do SEO. Here are 3 more tools that will blow your mind and transform your content workflow forever. Trust me, these are game-changers! 🚀🔥
>
> Link: bestaitools.xyz/my-affiliate-list

**Checklist result:**

| # | Check | Rating | Reason |
|---|-------|--------|--------|
| 1 | First Line | FAIL | "AI is changing everything" is a textbook AI-typical opener with zero info density. "Blow your mind" and "game-changers" are clickbait filler. |
| 2 | Semantic Precision | FAIL | Dominated by generic terms ("AI", "SEO", "content workflow"). No domain-specific nouns — which tools? what kind of SEO? Nothing makes the target audience think "this is for me." |
| 3 | Topic Distance | FAIL | Same topic (AI tools) + same angle (listicle) as the post 12 hours ago. Diversity mechanism (US9336553B2) will penalize same-source density. |
| 4 | External Links | FAIL | Unknown domain (bestaitools.xyz), likely affiliate link. Low authority + content relevance unclear. |
| 5 | Thread Structure | WARN | "3 tools" has enough content for threads, but is packed into a single post. Splitting into 1 tool per thread reply would add independent information value per reply. |
| 6 | Timing | FAIL | Last post was 12 hours ago and is still in active diffusion (800 likes = well above baseline). Posting now competes with yourself (US8402094B2). |
| 7 | Post-Viral Strategy | FAIL | Last post went semi-viral. Should be engaging with comments on that post, not rushing a follow-up on the same topic. |

**Result: 1 WARN, 6 FAIL — do not publish.**

**Optimizer recommendations:**
1. **Wait 24-48h.** Let the 800-like post finish its diffusion cycle. Use that time to reply to every comment on it instead.
2. **Change topic.** If the account covers SEO + AI tools, the next post should lean into SEO (different topic, same niche) rather than another AI tools listicle.
3. **Kill the affiliate link.** Either remove it entirely (safest) or replace with a high-authority source that directly supports the content.
4. **Rewrite the opener.** Lead with a specific, counterintuitive finding — not "AI is changing everything."

**Rewritten (after waiting 48h):**
> I used to mass-produce SEO articles with AI — 50 per week. Rankings went up for 2 months, then every single one dropped out of the top 100. Here's what the data showed was killing them, and the 3-step fix that brought 80% back.
>
> [Thread 1] The first signal was... [specific data]
> [Thread 2] The fix that worked...
> [Thread 3] What I'd do differently now...

Changed topic (AI content quality, not tools listicle), led with a counterintuitive first-hand result, removed affiliate link, added thread structure for depth.

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
