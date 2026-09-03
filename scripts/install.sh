#!/usr/bin/env bash
set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}⚡ Installing vibe-storm 5-Skill Business Pipeline Suite...${NC}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
SKILLS_DIR="${REPO_DIR}/skills"

SKILLS=("vibe-storm" "vibe-research" "vibe-scout" "vibe-plan" "vibe-cook")

# 1. Install for Claude Code (~/.claude/skills)
CLAUDE_SKILLS_DIR="${HOME}/.claude/skills"
if [ -d "${HOME}/.claude" ] || command -v claude >/dev/null 2>&1; then
    mkdir -p "${CLAUDE_SKILLS_DIR}"
    for skill in "${SKILLS[@]}"; do
        rm -rf "${CLAUDE_SKILLS_DIR}/${skill}"
        cp -r "${SKILLS_DIR}/${skill}" "${CLAUDE_SKILLS_DIR}/${skill}"
        echo -e "${GREEN}✓ [Claude Code] Installed:${NC} ${CLAUDE_SKILLS_DIR}/${skill}"
    done
fi

# 2. Install for Antigravity / Gemini CLI (~/.gemini/config/skills)
GEMINI_SKILLS_DIR="${HOME}/.gemini/config/skills"
if [ -d "${HOME}/.gemini" ]; then
    mkdir -p "${GEMINI_SKILLS_DIR}"
    for skill in "${SKILLS[@]}"; do
        rm -rf "${GEMINI_SKILLS_DIR}/${skill}" "${GEMINI_SKILLS_DIR}/ak-${skill}"
        cp -r "${SKILLS_DIR}/${skill}" "${GEMINI_SKILLS_DIR}/${skill}"
        echo -e "${GREEN}✓ [Antigravity/Gemini] Installed:${NC} ${GEMINI_SKILLS_DIR}/${skill}"
    done
fi

# 3. Install for Cursor (Current Workspace)
if [ "$REPO_DIR" != "$PWD" ] && ([ -d "${PWD}/.cursor" ] || [ -f "${PWD}/.cursorrules" ]); then
    mkdir -p "${PWD}/.cursor/rules"
    cp "${REPO_DIR}/.cursor/rules/"*.mdc "${PWD}/.cursor/rules/"
    echo -e "${GREEN}✓ [Cursor] Installed all 5 rules into current workspace:${NC} ${PWD}/.cursor/rules/"
fi

echo -e "\n${GREEN}🎉 All 5 skills installed successfully!${NC}"
echo -e "Available commands in your AI agent:"
echo -e "  1. ${YELLOW}/vibe-storm \"[Idea / Problem]\"${NC} -> Brainstorm & Contract"
echo -e "  2. ${YELLOW}/vibe-research \"[Market / Competitor]\"${NC} -> Deep Market Intelligence"
echo -e "  3. ${YELLOW}/vibe-scout \"[Funnel / Asset]\"${NC} -> Bottleneck & Asset Audit"
echo -e "  4. ${YELLOW}/vibe-plan \"[Initiative]\"${NC} -> Phased Execution Plan"
echo -e "  5. ${YELLOW}/vibe-cook \"[Plan Path / Task]\"${NC} -> Execute Copy, Funnel & Sales\n"
