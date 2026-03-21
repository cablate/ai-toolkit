#!/bin/bash
# Sync from ~/.claude/ to this repo
# Usage: bash sync.sh [&& git add -A && git commit && git push]

set -e

CLAUDE_DIR="$HOME/.claude"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Skills to sync (add new entries here)
SKILLS=(
  handoff
  thorough
  agentskill-expertise
  collaboration-style
)

echo "Syncing from $CLAUDE_DIR → $SCRIPT_DIR"

# Sync skills
for skill in "${SKILLS[@]}"; do
  src="$CLAUDE_DIR/skills/$skill"
  dst="$SCRIPT_DIR/skills/$skill"
  if [ -d "$src" ]; then
    rsync -av --delete "$src/" "$dst/"
    echo "  ✓ $skill"
  else
    echo "  ✗ $skill (not found in ~/.claude/skills/)"
  fi
done

# Sync statusline
if [ -f "$CLAUDE_DIR/statusline.ps1" ]; then
  cp "$CLAUDE_DIR/statusline.ps1" "$SCRIPT_DIR/statusline/"
  echo "  ✓ statusline.ps1"
fi

echo ""
echo "Done. Review changes with: git diff"
echo "Then: git add -A && git commit -m 'Sync from ~/.claude' && git push"
