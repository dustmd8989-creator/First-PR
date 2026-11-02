#!/bin/bash
set -euo pipefail

# Cloud sessions only
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"
export PATH="$HOME/.local/bin:$PATH"

# Python deps (system Python, so no hash check; pip is a no-op when satisfied)
pip install --quiet -r heritage-report-gen/requirements.txt

# graphify CLI (used by the PreToolUse hooks) and a fresh AST-only graph
if ! command -v graphify >/dev/null 2>&1; then
  uv tool install graphifyy
fi
graphify update . >/dev/null

# Make graphify visible in later Bash calls
echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$CLAUDE_ENV_FILE"
