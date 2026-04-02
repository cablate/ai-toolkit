# Scenario: Running a Threads Account

> Understand how the recommendation pipeline works at each stage — do the right thing at the right time, instead of blindly chasing impressions.

## Approach: Understand the Recommendation Pipeline and Act Correctly at Each Stage

---

## The Four Stages of the Recommendation Pipeline

1. **Initial matching** — The system first pushes to a small group with the closest vector distance (roughly a few hundred people)
2. **Quality judgment** — Diffusion is decided based on engagement quality in the first 1–3 hours. Deep comments of 5+ words and DM shares matter most.
3. **Gradual diffusion** — Strong engagement → content spreads progressively to a wider audience
4. **Make or break** — If the first wave fails, the post is effectively dead

---

## Before Posting

**Semantic precision > audience breadth**: Use specific domain terminology → match the right people → strong engagement → positive feedback loop

- Avoid vague generic phrases ("AI is amazing" → bad; "MCP architecture in Claude Code" → good)
- The first line is life or death — it must make people want to keep reading, but cannot be clickbait (AI loves clickbait → system flags it as low signal)

---

## After Posting

- Reply to every comment within 0–30 minutes; ask follow-up questions to generate back-and-forth
- **Reply quality triggers second-wave distribution**: When your replies contain substantive content (not just "thanks!"), the system treats them as new engagement signals and re-enters the post into the distribution pipeline. darkseoking tested this on Post #1 (20k likes) — aggressively replying to every algorithm discussion comment with real advice visibly extended the viral window beyond the typical 24-hour decay. The mechanism: high-quality replies generate their own engagement chains, which feed back into the post's Expected Engagement Value (US9378529B2)
- Leave 5–10 substantive replies on accounts in the same niche
- Do not prompt people to like, follow, or share

---

## 5 Steps After a Viral Post to Break Through the Reach Wall

### 1. Do Not Post Highly Similar Follow-Up Content

The diversity mechanism (US9336553B2) penalizes high same-source density. The right approach: weakly related semantics, different angle. Address the same audience but switch topics.

### 2. Maximize Engagement on the Current Viral Post

Boost Expected Engagement Value (US9378529B2) so the system views your account as having high overall engagement value — your next post benefits too.

### 3. Force a 24–48 Hour Rest

Avoid colliding with your own diffusion cycle (US8402094B2, US10565267B1). Pausing for a few days can actually move you into the priority distribution pool (US20140172877A1).

### 4. Leave Comments Before Posting to Test the Temperature

Check whether Audience Affinity is still at a high point. Posting when it is peaks the hit rate significantly.

### 5. Do Not Piggyback on Unrelated Trending Topics

Disrupting your Creator Embedding → the system loses track of who you are → account-level recommendation collapses.

---

## Quick Reference: 10 Common Questions

| Question | Conclusion |
|----------|------------|
| Does comment-touring help? | Yes, but quality is the core. Leave a few substantive comments in the same niche 1–2 hours before posting. Touring aggressively for three hours has terrible ROI. |
| Does posting time matter? | Overrated. What matters is when your audience is online, not which time slot is "best." |
| What if someone copies my content? | Creator Embedding cannot be copied. Consistent output is the better play. |
| Comment didn't go viral but a post did? | Different audience pools. Take a good comment and expand it into a post. |
| Do comments eat post impressions? | Not directly. But long-term commenting without posting gets you classified as an "engager," not a "creator." |
| Weight of likes / comments / shares? | Sends >> deep comments (30 pts) >> likes (1 pt) |
| Do new accounts get a boost? | Yes (honeymoon period), but low-quality content still sinks. |
| Does deleting and reposting work? | 99% of the time it makes things worse — all engagement signals reset to zero. Use the edit function instead. |
| Posting multiple times a day? | Bad. Engagement gets diluted and no individual post crosses the threshold. |
| Does a high follower count mean better reach? | Often the opposite. A mismatched follower structure drags down your initial engagement rate. |
