#!/usr/bin/env python3
"""
Agent Dispatch Eval — tests whether Claude routes queries to the correct agent.

Adapted from Anthropic's official skill-creator eval system for agent dispatch testing.

Usage:
    python -m scripts.run_eval \
        --eval-set ../eval-sets/dispatch-agents.json \
        --agents-dir ../../agents/dispatch \
        [--runs-per-query 3] \
        [--num-workers 5] \
        [--timeout 30] \
        [--threshold 0.5] \
        [--verbose]
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import shutil
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from .utils import load_eval_set, discover_agents


def run_single_query(
    query: str,
    working_dir: str,
    timeout: int = 30,
    verbose: bool = False,
) -> str | None:
    """Run a single query through Claude and detect which agent is dispatched.

    Returns the agent name if an Agent tool call is detected, None otherwise.
    """
    env = os.environ.copy()
    # Remove CLAUDECODE to allow nesting inside a Claude Code session
    env.pop("CLAUDECODE", None)

    cmd = [
        "claude",
        "-p", query,
        "--output-format", "stream-json",
        "--verbose",
    ]

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE if not verbose else None,
            cwd=working_dir,
            env=env,
        )

        dispatched_agent = None
        buffer = ""

        for line in proc.stdout:
            decoded = line.decode("utf-8", errors="replace").strip()
            if not decoded:
                continue

            try:
                event = json.loads(decoded)
            except json.JSONDecodeError:
                buffer += decoded
                try:
                    event = json.loads(buffer)
                    buffer = ""
                except json.JSONDecodeError:
                    continue

            # Detect Agent tool call in the stream
            # Claude emits content_block_start with type: tool_use
            if event.get("type") == "content_block_start":
                content_block = event.get("content_block", {})
                if content_block.get("type") == "tool_use":
                    tool_name = content_block.get("name", "")
                    # Agent tool (or legacy Task tool)
                    if tool_name in ("Agent", "Task"):
                        # We need to accumulate the input to get the agent type
                        pass

            # Accumulate tool input delta to extract agent name
            if event.get("type") == "content_block_delta":
                delta = event.get("delta", {})
                if delta.get("type") == "input_json_delta":
                    partial = delta.get("partial_json", "")
                    buffer += partial

            # When a tool use block stops, check if it was an Agent call
            if event.get("type") == "content_block_stop":
                if buffer:
                    try:
                        tool_input = json.loads(buffer)
                        # Check for agent dispatch fields
                        agent_name = (
                            tool_input.get("subagent_type")
                            or tool_input.get("description", "")
                        )
                        if agent_name:
                            dispatched_agent = agent_name
                            break
                    except json.JSONDecodeError:
                        pass
                    buffer = ""

        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()

        return dispatched_agent

    except subprocess.TimeoutExpired:
        proc.kill()
        return None
    except Exception as e:
        if verbose:
            print(f"Error running query: {e}", file=sys.stderr)
        return None


def classify_dispatch(dispatched: str | None, agents: dict) -> str | None:
    """Classify a dispatch result to a known agent name.

    The Agent tool may use subagent_type (exact name) or description (fuzzy).
    Returns the matched agent name or None.
    """
    if dispatched is None:
        return None

    dispatched_lower = dispatched.lower().strip()

    # Exact match on agent name
    for name in agents:
        if dispatched_lower == name.lower():
            return name

    # Fuzzy match: check if agent name appears in the description
    for name in agents:
        if name.lower() in dispatched_lower:
            return name

    return dispatched  # Return raw value for debugging


def run_eval(
    eval_set_path: Path,
    agents_dir: Path,
    working_dir: Path | None = None,
    runs_per_query: int = 3,
    num_workers: int = 5,
    timeout: int = 30,
    threshold: float = 0.5,
    verbose: bool = False,
) -> dict:
    """Run the full dispatch eval.

    Returns results dict with per-query results and summary.
    """
    eval_set = load_eval_set(eval_set_path)
    agents = discover_agents(agents_dir)

    if not agents:
        raise ValueError(f"No agents found in {agents_dir}")

    # Set up working directory with agents
    if working_dir is None:
        working_dir = Path(tempfile.mkdtemp(prefix="dispatch-eval-"))
        cleanup_working_dir = True
    else:
        cleanup_working_dir = False

    # Ensure .claude/agents/ exists in working dir with our agents
    target_agents_dir = working_dir / ".claude" / "agents"
    target_agents_dir.mkdir(parents=True, exist_ok=True)

    for md_file in agents_dir.glob("*.md"):
        shutil.copy2(md_file, target_agents_dir / md_file.name)

    if verbose:
        print(f"Agents discovered: {list(agents.keys())}")
        print(f"Working dir: {working_dir}")
        print(f"Eval set: {len(eval_set)} queries, {runs_per_query} runs each")
        print()

    results = []

    def run_query_batch(item: dict) -> dict:
        query = item["query"]
        expected = item["expected_agent"]
        dispatches = []

        for run_idx in range(runs_per_query):
            dispatched_raw = run_single_query(
                query=query,
                working_dir=str(working_dir),
                timeout=timeout,
                verbose=verbose,
            )
            dispatched = classify_dispatch(dispatched_raw, agents)
            dispatches.append(dispatched)

            if verbose:
                status = "✓" if dispatched == expected else "✗"
                print(f"  [{run_idx+1}/{runs_per_query}] {status} query={query[:50]}... → {dispatched} (expected: {expected})")

        correct_count = sum(1 for d in dispatches if d == expected)
        accuracy = correct_count / runs_per_query

        return {
            "query": query,
            "expected_agent": expected,
            "dispatches": dispatches,
            "correct_count": correct_count,
            "accuracy": accuracy,
            "pass": accuracy >= threshold,
        }

    # Run queries (sequential for now — each query does multiple runs)
    for i, item in enumerate(eval_set):
        if verbose:
            print(f"[{i+1}/{len(eval_set)}] Testing: {item['query'][:60]}...")

        result = run_query_batch(item)
        results.append(result)

    # Cleanup
    if cleanup_working_dir:
        shutil.rmtree(working_dir, ignore_errors=True)

    # Summary
    passed = sum(1 for r in results if r["pass"])
    failed = len(results) - passed

    # Per-agent accuracy
    agent_stats = {}
    for r in results:
        agent = r["expected_agent"]
        if agent not in agent_stats:
            agent_stats[agent] = {"total": 0, "passed": 0}
        agent_stats[agent]["total"] += 1
        if r["pass"]:
            agent_stats[agent]["passed"] += 1

    # Confusion matrix
    confusion = {}
    for r in results:
        expected = r["expected_agent"]
        for dispatched in r["dispatches"]:
            key = f"{expected} → {dispatched or 'none'}"
            confusion[key] = confusion.get(key, 0) + 1

    output = {
        "agents": list(agents.keys()),
        "eval_set": str(eval_set_path),
        "runs_per_query": runs_per_query,
        "threshold": threshold,
        "results": results,
        "summary": {
            "total": len(results),
            "passed": passed,
            "failed": failed,
            "pass_rate": passed / len(results) if results else 0,
        },
        "agent_stats": agent_stats,
        "confusion": confusion,
    }

    return output


def main():
    parser = argparse.ArgumentParser(description="Agent Dispatch Eval")
    parser.add_argument("--eval-set", required=True, help="Path to eval set JSON")
    parser.add_argument("--agents-dir", required=True, help="Path to agents directory")
    parser.add_argument("--working-dir", default=None, help="Working directory for Claude (temp if not specified)")
    parser.add_argument("--runs-per-query", type=int, default=3)
    parser.add_argument("--num-workers", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--output", "-o", default=None, help="Output JSON path")

    args = parser.parse_args()

    results = run_eval(
        eval_set_path=Path(args.eval_set),
        agents_dir=Path(args.agents_dir),
        working_dir=Path(args.working_dir) if args.working_dir else None,
        runs_per_query=args.runs_per_query,
        num_workers=args.num_workers,
        timeout=args.timeout,
        threshold=args.threshold,
        verbose=args.verbose,
    )

    output_json = json.dumps(results, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(output_json, encoding="utf-8")
        print(f"Results written to {args.output}")
    else:
        print(output_json)

    # Print summary
    s = results["summary"]
    print(f"\n{'='*50}", file=sys.stderr)
    print(f"Pass rate: {s['passed']}/{s['total']} ({s['pass_rate']:.0%})", file=sys.stderr)
    for agent, stats in results["agent_stats"].items():
        print(f"  {agent}: {stats['passed']}/{stats['total']}", file=sys.stderr)
    if results["confusion"]:
        print(f"\nConfusion (expected → actual):", file=sys.stderr)
        for route, count in sorted(results["confusion"].items()):
            print(f"  {route}: {count}", file=sys.stderr)


if __name__ == "__main__":
    main()
