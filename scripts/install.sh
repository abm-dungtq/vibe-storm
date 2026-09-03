#!/usr/bin/env bash
set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}⚡ Installing vibe-storm 5-Skill Business Pipeline Suite...${NC}"

# Detect if executing via curl pipe or local checkout
IS_PIPED=0
if [ -z "${BASH_SOURCE[0]}" ] || [ "${BASH_SOURCE[0]}" = "bash" ] || [ ! -f "${BASH_SOURCE[0]}" ]; then
    IS_PIPED=1
fi

if [ $IS_PIPED -eq 1 ]; then
    TMP_DIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'vibe-storm')
    trap 'rm -rf "$TMP_DIR"' EXIT
    echo -e "${BLUE}Fetching latest release from GitHub...${NC}"
    git clone --depth 1 https://github.com/abm-dungtq/vibe-storm.git "$TMP_DIR" >/dev/null 2>&1
    REPO_DIR="$TMP_DIR"
else
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
fi

SKILLS_DIR="${REPO_DIR}/skills"
SKILLS=("vibe-storm" "vibe-research" "vibe-scout" "vibe-plan" "vibe-cook")
INSTALLED_TARGETS=0

# 1. Install for Claude Code (~/.claude/skills)
CLAUDE_SKILLS_DIR="${HOME}/.claude/skills"
if [ -d "${HOME}/.claude" ] || command -v claude >/dev/null 2>&1; then
    mkdir -p "${CLAUDE_SKILLS_DIR}"
    for skill in "${SKILLS[@]}"; do
        rm -rf "${CLAUDE_SKILLS_DIR}/${skill}"
        cp -r "${SKILLS_DIR}/${skill}" "${CLAUDE_SKILLS_DIR}/${skill}"
    done
    echo -e "${GREEN}✓ [Claude Code] Installed all 5 skills into:${NC} ${CLAUDE_SKILLS_DIR}/"
    INSTALLED_TARGETS=$((INSTALLED_TARGETS + 1))
fi

# 2. Install for Antigravity / Gemini CLI (~/.gemini/config/skills)
GEMINI_SKILLS_DIR="${HOME}/.gemini/config/skills"
if [ -d "${HOME}/.gemini" ]; then
    mkdir -p "${GEMINI_SKILLS_DIR}"
    for skill in "${SKILLS[@]}"; do
        rm -rf "${GEMINI_SKILLS_DIR}/${skill}" "${GEMINI_SKILLS_DIR}/ak-${skill}"
        cp -r "${SKILLS_DIR}/${skill}" "${GEMINI_SKILLS_DIR}/${skill}"
    done
    echo -e "${GREEN}✓ [Antigravity/Gemini] Installed all 5 skills into:${NC} ${GEMINI_SKILLS_DIR}/"
    INSTALLED_TARGETS=$((INSTALLED_TARGETS + 1))
fi

# 3. Install for Cursor (Current Workspace)
if [ "$REPO_DIR" != "$PWD" ] && ([ -d "${PWD}/.cursor" ] || [ -f "${PWD}/.cursorrules" ]); then
    mkdir -p "${PWD}/.cursor/rules"
    cp "${REPO_DIR}/.cursor/rules/"*.mdc "${PWD}/.cursor/rules/"
    echo -e "${GREEN}✓ [Cursor] Installed all 5 rules into workspace:${NC} ${PWD}/.cursor/rules/"
    INSTALLED_TARGETS=$((INSTALLED_TARGETS + 1))
fi

if [ $INSTALLED_TARGETS -eq 0 ]; then
    # Fallback to standard Claude skills path
    mkdir -p "${CLAUDE_SKILLS_DIR}"
    for skill in "${SKILLS[@]}"; do
        rm -rf "${CLAUDE_SKILLS_DIR}/${skill}"
        cp -r "${SKILLS_DIR}/${skill}" "${CLAUDE_SKILLS_DIR}/${skill}"
    done
    echo -e "${YELLOW}⚠️ No active agent directories detected; installed to default path:${NC} ${CLAUDE_SKILLS_DIR}/"
else
    echo -e "\n${GREEN}🎉 All 5 skills installed successfully!${NC}"
fi

echo -e "Available commands in your AI agent:"
echo -e "  1. ${YELLOW}/vibe-storm \"[Idea / Problem]\"${NC} -> Brainstorm & Contract"
echo -e "  2. ${YELLOW}/vibe-research \"[Market / Competitor]\"${NC} -> Deep Market Intelligence"
echo -e "  3. ${YELLOW}/vibe-scout \"[Funnel / Asset]\"${NC} -> Bottleneck & Asset Audit"
echo -e "  4. ${YELLOW}/vibe-plan \"[Initiative]\"${NC} -> Phased Execution Plan"
echo -e "  5. ${YELLOW}/vibe-cook \"[Plan Path / Task]\"${NC} -> Execute Copy, Funnel & Sales\n"
