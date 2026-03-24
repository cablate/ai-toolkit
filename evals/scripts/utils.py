"""Shared utilities for agent dispatch eval scripts."""

from __future__ import annotations

import json
import re
import yaml
from pathlib import Path


def parse_agent_md(agent_path: Path) -> tuple[str, str, str]:
    """Parse agent markdown file, return (name, description, full_content)."""
    content = agent_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        raise ValueError(f"No YAML frontmatter found in {agent_path}")

    frontmatter = yaml.safe_load(match.group(1))
    name = frontmatter.get("name", agent_path.stem)
    description = frontmatter.get("description", "")
    return name, description, content


def load_eval_set(eval_set_path: Path) -> list[dict]:
    """Load eval set from JSON file."""
    with open(eval_set_path, encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        if "query" not in item:
            raise ValueError(f"Each eval item must have a 'query' field: {item}")
        if "expected_agent" not in item:
            raise ValueError(f"Each eval item must have an 'expected_agent' field: {item}")
    return data


def discover_agents(agents_dir: Path) -> dict[str, dict]:
    """Discover all agent .md files in a directory, return {name: {description, path}}."""
    agents = {}
    for md_file in sorted(agents_dir.glob("*.md")):
        try:
            name, description, _ = parse_agent_md(md_file)
            agents[name] = {"description": description, "path": str(md_file)}
        except ValueError:
            continue
    return agents
