# Scenario: Understanding / Researching Algorithms

> When you want to understand a platform's algorithm, don't rely on second-hand interpretations from KOLs — go straight to primary sources: patent filings and litigation documents.

## Approach: Don't Guess — Find Primary Sources

### How to Research Algorithms Using Patents

- Sources: Google Patents, USPTO
- Patents must be 100% accurate (filing requires describing the real mechanism)
- Litigation documents are even stronger (executives testify in person; evidence cannot be fabricated)

---

## Meta/Threads Algorithm — The Underlying Pipeline Derived from Patents

Every point below is backed by a patent number. That is the core value of this approach — grounded in evidence, not speculation.

1. **Semantic vector matching for the initial audience** — After content is posted, the system uses semantic vectors to find the nearest-matching group of users to push it to (US10579688B2)

2. **Small-scale diffusion scoring** — A composite score of relationship strength + content features + behavioral data determines whether the content spreads (US20190095961A1)

3. **Sensational opening = low signal** — If the post uses a clickbait-style opening, it is likely flagged as a low-quality signal. AI-generated content frequently triggers this.

4. **Creator Embedding clusters** — Accounts are clustered based on the nature of their viral posts (US10558714B2). Relevant content gets distribution; unrelated content does not. This is the algorithmic representation of your "account identity."

5. **Social graph diffusion** — Interactions with authoritative KOLs in the same niche trigger social graph diffusion (US9582786B2)

6. **External links do not automatically suppress reach** — Adding an external link does not inherently limit distribution. The system evaluates domain authority and content relevance (EP2977948A1, US10268763B2)

7. **Content diversity mechanism** — The system actively controls same-source density (US9336553B2). Posting highly similar content consecutively will suppress distribution.

8. **Audience Affinity scoring** — Affinity between you and each user is calculated based on interaction frequency, interaction type, time decay, and bidirectionality (US8402094B2)

9. **Expected Engagement Value** — The system predicts how much engagement value each piece of content will generate and uses that to determine distribution volume (US9378529B2)

10. **Engagement signal weights** — DM shares >> deep comments (30 pts) >> likes (1 pt). Source: publicly confirmed by Mosseri + FB Papers MSI scoring system

11. **New account honeymoon period** — New accounts benefit from an exploration vs. exploitation mechanism (US20140172877A1) that grants extra exposure. Low-quality content still sinks, however (US9959412B2)

12. **Second-chance mechanism** — The system automatically gives underperforming content a second chance. This is system-triggered — deleting and reposting does not activate it (US10635732B2)

---

## Google Algorithm — Derived from Litigation Documents

Source: Case No. 1:20-cv-03010-APM

1. **Navboost** — Records user click behavior for up to 13 months. Long clicks and short clicks are tracked separately; mobile and desktop are tracked separately. This is the most direct user behavior signal influencing rankings.

2. **Chrome data** — Browsing behavior is fed directly into the ranking system. Dwell time, scroll depth, text zoom… all reported back to Google. Chrome is not just a browser — it is a data collection instrument.

3. **IS4 (Search Quality Raters)** — Human employees manually score results, with particular focus on YMYL (Your Money Your Life) queries. Some keywords are effectively impossible to rank for via black-hat methods because you are facing human review, not an algorithm.

---

## Cross-Platform Common Logic

- The Threads algorithm is ~80% similar to Google SEO (semantic vectors, clustering, external link authority)
- Google's semantic clusters ≈ Threads' Creator Embedding
- At the core, both do the same thing: use different parameter codes to surface content users are most likely to engage with
- Once you deeply understand one platform's logic, migrating that understanding to another platform costs very little
