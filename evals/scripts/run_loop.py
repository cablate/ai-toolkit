#!/usr/bin/env python3
"""
Agent Dispatch Optimization Loop — iteratively improves agent descriptions
to maximize routing accuracy.

Adapted from Anthropic's official skill-creator run_loop.py.

Usage:
    python -m scripts.run_loop \
        --eval-set ../eval-sets/dispatch-agents.json \
        --agents-dir ../../agents/dispatch \
        --target-agent investigator \
        [--max-iterations 5] \
        [--holdout 0.4] \
        [--runs-per-query 3] \
        [--verbose]
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

from .run_eval import run_eval
from .improve_description import improve_agent_description
from .generate_report import generate_html
from .utils import parse_agent_md


def split_eval_set(
    eval_set: list[dict],
    target_agent: str,
    holdout: float = 0.4,
    seed: int = 42,
) -> tuple[list[dict], list[dict]]:
    """Split eval set into train/test, stratified by whether query targets this agent."""

    targets = [q for q in eval_set if q["expected_agent"] == target_agent]
    others = [q for q in eval_set if q["expected_agent"] != target_agent]

    rng = random.Random(seed)
    rng.shuffle(targets)
    rng.shuffle(others)

    split_t = max(1, int(len(targets) * (1 - holdout)))
    split_o = max(1, int(len(others) * (1 - holdout)))

    train = targets[:split_t] + others[:split_o]
    test = targets[split_t:] + others[split_o:]

    rng.shuffle(train)
    rng.shuffle(test)

    return train, test


def run_loop(
    eval_set_path: Path,
    agents_dir: Path,
    target_agent: str,
    max_iterations: int = 5,
    holdout: float = 0.4,
    runs_per_query: int = 3,
    threshold: float = 0.5,
    timeout: int = 30,
    verbose: bool = False,
    report_path: Path | None = None,
) -> dict:
    """Run the optimization loop for a single agent's description."""

    eval_set = json.loads(eval_set_path.read_text(encoding="utf-8"))
    train_set, test_set = split_eval_set(eval_set, target_agent, holdout)

    agent_path = agents_dir / f"{target_agent}.md"
    if not agent_path.exists():
        raise FileNotFoundError(f"Agent file not found: {agent_path}")

    name, current_description, full_content = parse_agent_md(agent_path)

    if verbose:
        print(f"Target agent: {target_agent}")
        print(f"Train: {len(train_set)} queries, Test: {len(test_set)} queries")
        print(f"Current description: {current_description[:80]}...")
        print()

    history = []
    best_description = current_description
    best_test_score = 0.0

    for iteration in range(1, max_iterations + 1):
        if verbose:
            print(f"{'='*50}")
            print(f"Iteration {iteration}/{max_iterations}")
            print(f"Description: {current_description[:80]}...")
            print()

        # Write current description to agent file
        _update_agent_description(agent_path, current_description)

        # Run eval on full set (train + test)
        full_eval_path = _write_temp_eval_set(train_set + test_set)
        results = run_eval(
            eval_set_path=full_eval_path,
            agents_dir=agents_dir,
            runs_per_query=runs_per_query,
            threshold=threshold,
            timeout=timeout,
            verbose=verbose,
        )
        full_eval_path.unlink()

        # Split results back
        train_queries = {q["query"] for q in train_set}
        train_results = [r for r in results["results"] if r["query"] in train_queries]
        test_results = [r for r in results["results"] if r["query"] not in train_queries]

        train_pass = sum(1 for r in train_results if r["pass"])
        test_pass = sum(1 for r in test_results if r["pass"])
        train_score = train_pass / len(train_results) if train_results else 0
        test_score = test_pass / len(test_results) if test_results else 0

        if verbose:
            print(f"\nTrain: {train_pass}/{len(train_results)} ({train_score:.0%})")
            print(f"Test:  {test_pass}/{len(test_results)} ({test_score:.0%})")

        # Track best by TEST score (prevents overfitting)
        if test_score > best_test_score:
            best_test_score = test_score
            best_description = current_description

        # Record history (hide test scores from improver)
        history.append({
            "iteration": iteration,
            "description": current_description,
            "train_score": train_score,
            "test_score": test_score,  # kept for report, hidden from improver
            "train_failures": [r for r in train_results if not r["pass"]],
        })

        # Generate report
        if report_path:
            html = generate_html(history, target_agent, auto_refresh=(iteration < max_iterations))
            report_path.write_text(html, encoding="utf-8")

        # Exit early if train is perfect
        if train_score == 1.0:
            if verbose:
                print(f"\nAll train queries passed. Stopping early.")
            break

        # Improve description (only sees train failures, not test scores)
        train_failures = [r for r in train_results if not r["pass"]]
        blinded_history = [
            {"iteration": h["iteration"], "description": h["description"], "train_score": h["train_score"]}
            for h in history
        ]

        new_description = improve_agent_description(
            agent_name=target_agent,
            current_description=current_description,
            agent_content=full_content,
            train_failures=train_failures,
            history=blinded_history,
            all_agents={a.stem: parse_agent_md(a)[1] for a in agents_dir.glob("*.md")},
            verbose=verbose,
        )

        if new_description and new_description != current_description:
            current_description = new_description
        else:
            if verbose:
                print("No improvement suggested. Stopping.")
            break

    # Restore best description
    _update_agent_description(agent_path, best_description)

    return {
        "target_agent": target_agent,
        "best_description": best_description,
        "best_test_score": best_test_score,
        "iterations": len(history),
        "history": history,
    }


def _update_agent_description(agent_path: Path, new_description: str):
    """Update the description in an agent's YAML frontmatter."""
    import re
    content = agent_path.read_text(encoding="utf-8")
    # Replace description line in frontmatter
    content = re.sub(
        r'(description:\s*)"[^"]*"',
        f'\\1"{new_description}"',
        content,
        count=1,
    )
    agent_path.write_text(content, encoding="utf-8")


def _write_temp_eval_set(items: list[dict]) -> Path:
    """Write eval items to a temp JSON file."""
    import tempfile
    tmp = Path(tempfile.mktemp(suffix=".json"))
    tmp.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    return tmp


def main():
    parser = argparse.ArgumentParser(description="Agent Dispatch Optimization Loop")
    parser.add_argument("--eval-set", required=True)
    parser.add_argument("--agents-dir", required=True)
    parser.add_argument("--target-agent", required=True, help="Which agent's description to optimize")
    parser.add_argument("--max-iterations", type=int, default=5)
    parser.add_argument("--holdout", type=float, default=0.4)
    parser.add_argument("--runs-per-query", type=int, default=3)
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--report", default=None, help="HTML report output path")
    parser.add_argument("--output", "-o", default=None)

    args = parser.parse_args()

    results = run_loop(
        eval_set_path=Path(args.eval_set),
        agents_dir=Path(args.agents_dir),
        target_agent=args.target_agent,
        max_iterations=args.max_iterations,
        holdout=args.holdout,
        runs_per_query=args.runs_per_query,
        threshold=args.threshold,
        timeout=args.timeout,
        verbose=args.verbose,
        report_path=Path(args.report) if args.report else None,
    )

    output_json = json.dumps(results, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(output_json, encoding="utf-8")
    else:
        print(output_json)

    print(f"\nBest description (test score: {results['best_test_score']:.0%}):", file=sys.stderr)
    print(f"  {results['best_description']}", file=sys.stderr)


if __name__ == "__main__":
    main()
