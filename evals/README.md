# Agent Dispatch Evals

Test whether Claude routes queries to the correct dispatch agent.

Adapted from [Anthropic's official skill-creator eval system](https://github.com/anthropics/skills/tree/main/skills/skill-creator/scripts).

## Quick Start

```bash
cd evals

# Run dispatch eval (tests all 5 agents)
python -m scripts.run_eval \
  --eval-set eval-sets/dispatch-agents.json \
  --agents-dir ../agents/dispatch \
  --verbose

# Optimize a specific agent's description
python -m scripts.run_loop \
  --eval-set eval-sets/dispatch-agents.json \
  --agents-dir ../agents/dispatch \
  --target-agent investigator \
  --report report.html \
  --verbose
```

## How It Works

### Dispatch Eval (`run_eval.py`)

1. Copies agents to a temp `.claude/agents/` directory
2. Runs `claude -p <query> --output-format stream-json` for each query
3. Detects `Agent` tool calls in the stream and checks `subagent_type`
4. Each query runs N times (default 3) to account for non-determinism
5. Pass = accuracy ≥ threshold (default 50%)

Output: JSON with per-query results, per-agent accuracy, and confusion matrix.

### Optimization Loop (`run_loop.py`)

1. Splits eval set 60/40 train/test (stratified, seeded)
2. Runs eval → finds failures → uses Claude to rewrite description
3. Test scores are hidden from the improver (prevents overfitting)
4. Selects best description by test score
5. Generates live-updating HTML report

### Eval Set Format

```json
[
  {"query": "find all usages of handleAuth", "expected_agent": "investigator"},
  {"query": "implement rate limiting", "expected_agent": "builder"}
]
```

Queries should be realistic and varied — include context, file names, slang. Avoid trivially simple 3-word queries.

## Scripts

| Script | Purpose |
|--------|---------|
| `run_eval.py` | Run dispatch accuracy test |
| `run_loop.py` | Iteratively optimize an agent's description |
| `improve_description.py` | LLM-powered description rewriter |
| `generate_report.py` | HTML report generator |
| `utils.py` | Shared utilities (frontmatter parsing, agent discovery) |

## Cost

Each query costs one `claude -p` API call. With 32 queries × 3 runs = ~96 calls per eval run. Budget accordingly.

## Requirements

- Python 3.10+
- `claude` CLI installed and authenticated
- `pyyaml` (`pip install pyyaml`)
