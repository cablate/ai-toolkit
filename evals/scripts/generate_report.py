#!/usr/bin/env python3
"""Generate HTML report from dispatch eval results."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def generate_html(
    history: list[dict],
    target_agent: str,
    auto_refresh: bool = False,
) -> str:
    """Generate an HTML report from optimization loop history."""

    refresh_tag = '<meta http-equiv="refresh" content="5">' if auto_refresh else ""

    # Find best iteration by test score
    best_iter = max(range(len(history)), key=lambda i: history[i].get("test_score", 0)) if history else -1

    rows = ""
    for i, h in enumerate(history):
        is_best = i == best_iter
        row_class = ' class="best-row"' if is_best else ""
        badge = " ★" if is_best else ""

        train_pct = f"{h['train_score']:.0%}"
        test_pct = f"{h.get('test_score', 0):.0%}"
        desc_short = h["description"][:100] + ("..." if len(h["description"]) > 100 else "")

        failures = ""
        for f in h.get("train_failures", []):
            failures += f'<div class="failure">✗ {_esc(f["query"][:60])} → {f["dispatches"]}</div>'

        rows += f"""
        <tr{row_class}>
            <td>{h['iteration']}{badge}</td>
            <td class="score">{train_pct}</td>
            <td class="score">{test_pct}</td>
            <td class="desc">{_esc(desc_short)}</td>
            <td>{failures or '<span class="pass">All passed</span>'}</td>
        </tr>"""

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    {refresh_tag}
    <title>Dispatch Eval: {_esc(target_agent)}</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; margin: 2rem; background: #f5f5f5; }}
        h1 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; background: white; box-shadow: 0 1px 3px rgba(0,0,0,.1); }}
        th, td {{ padding: 8px 12px; text-align: left; border-bottom: 1px solid #eee; }}
        th {{ background: #f8f8f8; font-weight: 600; }}
        .score {{ font-family: monospace; font-size: 1.1em; }}
        .desc {{ font-size: 0.85em; color: #666; max-width: 400px; }}
        .failure {{ font-size: 0.8em; color: #c33; margin: 2px 0; }}
        .pass {{ color: #3a3; }}
        .best-row {{ background: #f0fff0; }}
        .best-row td {{ font-weight: 600; }}
    </style>
</head>
<body>
    <h1>Dispatch Eval: {_esc(target_agent)}</h1>
    <table>
        <tr>
            <th>Iter</th>
            <th>Train</th>
            <th>Test</th>
            <th>Description</th>
            <th>Failures</th>
        </tr>
        {rows}
    </table>
</body>
</html>"""


def _esc(text: str) -> str:
    """HTML escape."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def generate_eval_report(results: dict) -> str:
    """Generate an HTML report from a single run_eval result."""
    summary = results["summary"]
    agent_stats = results.get("agent_stats", {})
    confusion = results.get("confusion", {})

    agent_rows = ""
    for agent, stats in agent_stats.items():
        pct = stats["passed"] / stats["total"] if stats["total"] else 0
        color = "#3a3" if pct >= 0.8 else "#c93" if pct >= 0.5 else "#c33"
        agent_rows += f'<tr><td>{_esc(agent)}</td><td style="color:{color}">{stats["passed"]}/{stats["total"]} ({pct:.0%})</td></tr>'

    result_rows = ""
    for r in results["results"]:
        status = "✓" if r["pass"] else "✗"
        color = "#3a3" if r["pass"] else "#c33"
        dispatches = ", ".join(str(d) for d in r["dispatches"])
        result_rows += f"""
        <tr>
            <td style="color:{color}">{status}</td>
            <td>{_esc(r['query'][:80])}</td>
            <td>{_esc(r['expected_agent'])}</td>
            <td>{_esc(dispatches)}</td>
            <td>{r['accuracy']:.0%}</td>
        </tr>"""

    confusion_rows = ""
    for route, count in sorted(confusion.items(), key=lambda x: -x[1]):
        confusion_rows += f"<tr><td>{_esc(route)}</td><td>{count}</td></tr>"

    pass_rate = summary["pass_rate"]
    rate_color = "#3a3" if pass_rate >= 0.8 else "#c93" if pass_rate >= 0.5 else "#c33"

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Dispatch Eval Report</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; margin: 2rem; background: #f5f5f5; }}
        h1, h2 {{ color: #333; }}
        .big-number {{ font-size: 3em; color: {rate_color}; font-weight: bold; }}
        table {{ border-collapse: collapse; width: 100%; background: white; box-shadow: 0 1px 3px rgba(0,0,0,.1); margin: 1rem 0; }}
        th, td {{ padding: 8px 12px; text-align: left; border-bottom: 1px solid #eee; }}
        th {{ background: #f8f8f8; }}
        .section {{ margin: 2rem 0; }}
    </style>
</head>
<body>
    <h1>Agent Dispatch Eval Report</h1>
    <div class="big-number">{pass_rate:.0%}</div>
    <p>{summary['passed']}/{summary['total']} queries routed correctly</p>

    <div class="section">
        <h2>Per-Agent Accuracy</h2>
        <table><tr><th>Agent</th><th>Score</th></tr>{agent_rows}</table>
    </div>

    <div class="section">
        <h2>Query Results</h2>
        <table>
            <tr><th></th><th>Query</th><th>Expected</th><th>Dispatched</th><th>Accuracy</th></tr>
            {result_rows}
        </table>
    </div>

    <div class="section">
        <h2>Confusion Matrix</h2>
        <table><tr><th>Route</th><th>Count</th></tr>{confusion_rows}</table>
    </div>
</body>
</html>"""


def main():
    """Generate report from JSON input."""
    if len(sys.argv) > 1:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    else:
        data = json.load(sys.stdin)

    output_path = sys.argv[2] if len(sys.argv) > 2 else "report.html"

    if "history" in data:
        html = generate_html(data["history"], data.get("target_agent", "unknown"))
    else:
        html = generate_eval_report(data)

    Path(output_path).write_text(html, encoding="utf-8")
    print(f"Report written to {output_path}")


if __name__ == "__main__":
    main()
