#!/usr/bin/env python3
"""
Improve an agent's description based on dispatch eval failures.

Uses Claude to rewrite the description to better capture the agent's
dispatch triggers while staying distinct from other agents.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def improve_agent_description(
    agent_name: str,
    current_description: str,
    agent_content: str,
    train_failures: list[dict],
    history: list[dict],
    all_agents: dict[str, str],
    verbose: bool = False,
) -> str | None:
    """Use Claude to improve an agent's description based on failures.

    Args:
        agent_name: Name of the agent being optimized
        current_description: Current description text
        agent_content: Full SKILL.md/agent.md content
        train_failures: List of failed eval results
        history: Previous iteration attempts (train scores only, no test)
        all_agents: Dict of {name: description} for all agents
        verbose: Print debug info

    Returns:
        New description string, or None if improvement failed.
    """
    # Build the prompt
    other_agents = "\n".join(
        f"- {name}: {desc}"
        for name, desc in all_agents.items()
        if name != agent_name
    )

    missed_queries = "\n".join(
        f"- \"{r['query']}\" (dispatched to: {r['dispatches']})"
        for r in train_failures
        if r["expected_agent"] == agent_name and not r["pass"]
    )

    false_dispatches = "\n".join(
        f"- \"{r['query']}\" (expected: {r['expected_agent']}, got: {r['dispatches']})"
        for r in train_failures
        if r["expected_agent"] != agent_name and not r["pass"]
    )

    history_text = "\n".join(
        f"Iteration {h['iteration']}: score={h['train_score']:.0%} desc=\"{h['description'][:80]}...\""
        for h in history
    ) if history else "No previous attempts."

    prompt = f"""You are optimizing the description of a Claude Code agent named "{agent_name}".

The description is what Claude reads to decide which agent to dispatch for a given task.
Your goal: maximize correct dispatch (route the right queries to this agent, avoid stealing others' queries).

## Current Description
{current_description}

## Other Agents (must stay distinct from these)
{other_agents}

## Queries That SHOULD Have Dispatched to {agent_name} But Didn't
{missed_queries or "None — all target queries triggered correctly."}

## Queries That Were INCORRECTLY Dispatched to {agent_name}
{false_dispatches or "None — no false dispatches."}

## Previous Attempts
{history_text}

## Full Agent Content (for context)
{agent_content[:2000]}

## Constraints
- Max 200 words, hard limit 1024 characters
- Use imperative form ("Use when: ...")
- Focus on dispatch TRIGGERS — what kind of user intent should route here
- Stay distinct from other agents — don't steal their queries
- Include "Use when:" with specific trigger phrases
- Generalize from failures rather than listing specific query keywords

## Output
Write ONLY the new description text (no quotes, no explanation).
<new_description>
YOUR IMPROVED DESCRIPTION HERE
</new_description>"""

    env = os.environ.copy()
    env.pop("CLAUDECODE", None)

    cmd = ["claude", "-p", prompt, "--output-format", "text"]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
            env=env,
        )

        output = result.stdout.strip()

        if verbose:
            print(f"Improve output: {output[:200]}...", file=sys.stderr)

        # Extract from tags
        import re
        match = re.search(r"<new_description>\s*(.*?)\s*</new_description>", output, re.DOTALL)
        if match:
            new_desc = match.group(1).strip()
        else:
            # Try using the whole output if no tags
            new_desc = output.strip()

        # Enforce hard limit
        if len(new_desc) > 1024:
            new_desc = new_desc[:1021] + "..."

        if not new_desc or new_desc == current_description:
            return None

        return new_desc

    except (subprocess.TimeoutExpired, Exception) as e:
        if verbose:
            print(f"Error improving description: {e}", file=sys.stderr)
        return None
