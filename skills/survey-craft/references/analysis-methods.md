# Survey Analysis Methods

> Detailed reference for the Analysis Framework in SKILL.md. Load when performing survey data analysis or building analysis pipelines.

---

## Data Cleaning Checklist

Before any analysis, clean the data:

| Check | Rule | Action |
|-------|------|--------|
| Speed-through | Completion time < 30 seconds | Flag as invalid |
| Straight-lining | Same answer for all Likert questions | Flag as invalid |
| Missing values | > 50% questions unanswered | Exclude from analysis |
| Outliers | Extreme values on numeric questions | Investigate, don't auto-remove |
| Duplicates | Same respondent ID or IP | Keep first response only |

**Target**: Invalid response rate < 20%. If higher, suspect survey design issues (too long, confusing questions).

---

## Cross-Tabulation (Cross-Tab) Detailed Guide

### What It Is

Cross two or more categorical variables in a matrix to reveal sub-group differences invisible in aggregate stats.

### Example

```
              Satisfaction
              High   Med    Low    Total
Tenure  <3yr  20%    50%    30%    100%
        3-5yr 35%    45%    20%    100%
        >5yr  50%    35%    15%    100%
```

**Insight**: Tenure strongly correlates with satisfaction — but the overall average (35%) masks this.

### When to Cross-Tab

- When an overall metric seems "okay" but you suspect hidden segments
- When you have a clear hypothesis: "Does [Variable A] affect [Variable B]?"
- When stakeholders ask "but what about [segment]?"

### How to Execute

1. **Pick variables**: One independent (e.g., tenure, role, device) x one dependent (e.g., satisfaction, completion)
2. **Build the matrix**: Count or percentage per cell
3. **Test significance**: Chi-square test (p < 0.05 = significant)
4. **Interpret**: Look for cells that deviate from the overall average
5. **Report**: "Among [sub-group], [metric] is [X]% vs [Y]% overall — this suggests [insight]"

### Common Cross-Tab Pairs for Surveys

| Independent | Dependent | What You Learn |
|-------------|-----------|---------------|
| Device (mobile/desktop) | Completion rate | Mobile UX problems |
| Demographic (age, role) | Key attitude question | Segment-specific needs |
| Acquisition channel | Response quality | Channel effectiveness |
| Survey version (A/B) | Completion rate | Which version wins |
| Question reached | Drop-off rate | Problem questions |

---

## Root Cause Analysis (RCA) Frameworks

### Framework 1: 5 Whys

Start with the observed problem, ask "why?" five times to drill to the root.

**Example**:
```
Problem: Survey completion rate is 18% (target: 30%)
Why 1: 45% of respondents drop off at Q7
Why 2: Q7 is a ranking question with 8 options
Why 3: On mobile, ranking 8 options requires excessive scrolling
Why 4: The question was designed for desktop without mobile testing
Why 5: No mobile pre-test step in our launch checklist
→ Root cause: Missing mobile pre-test in process
→ Fix: Add mandatory mobile test to launch checklist + redesign Q7 as top-3 selection
```

### Framework 2: Fishbone Diagram (Ishikawa)

Organize possible causes into categories:

```
                    ┌─ Design: Too many questions, complex types
                    ├─ Technical: Slow loading, broken on mobile
Problem ←───────────├─ Distribution: Wrong timing, wrong channel
(low completion)    ├─ Audience: Survey fatigue, low motivation
                    └─ Incentive: No reward, delayed reward
```

### Framework 3: Three-Module Analysis (for complex issues)

```
Module 1: Problem Identification
├─ Anomaly detection: What metric is off?
├─ Trend analysis: Is it getting worse over time?
└─ Comparative analysis: Which segment is worst?

Module 2: Root Cause Discovery
├─ Causal learning: What correlates with the problem?
├─ Association rules: What patterns co-occur?
└─ Pattern recognition: Are there recurring failure modes?

Module 3: Solution Development
├─ Prioritization: Impact vs effort matrix
├─ Impact assessment: Expected improvement per fix
└─ Action planning: Who does what by when
```

---

## Analysis Workflow (6 Steps)

```
Step 1: Data Cleaning
  └─ Apply checklist above, document exclusions

Step 2: Descriptive Statistics
  ├─ Mean, median, mode for numeric questions
  ├─ Frequency distributions for categorical questions
  └─ Visualize: bar charts, pie charts

Step 3: Cross-Tabulation
  ├─ Cross key demographics x key outcome variables
  └─ Chi-square test for significance

Step 4: Deep Analysis (if warranted)
  ├─ Correlation analysis between variables
  └─ Regression if predicting outcomes

Step 5: Insight Extraction
  ├─ "So What?" — What does this finding mean?
  └─ "Now What?" — What should we do about it?

Step 6: Action Recommendations
  └─ Convert insights to specific, prioritized actions
```

---

## Sources

- Cross-Tabulation: SurveySensum 2025, Qualtrics
- RCA: Tableau, IR, ScienceDirect (102 citations)
- Analysis workflow: AskAttest Nov 2025
- Three-module framework: ScienceDirect Big Data-Driven RCA System
