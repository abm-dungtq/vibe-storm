#!/usr/bin/env bash
set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}⚡ Installing vibe-storm (AI-Native Ideation Engine)...${NC}"

# Detect base directory of repo
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
SKILL_SRC="${REPO_DIR}/skills/vibe-storm"

INSTALLED=0

# 1. Install for Claude Code (~/.claude/skills)
CLAUDE_SKILLS_DIR="${HOME}/.claude/skills"
if [ -d "${HOME}/.claude" ] || command -v claude >/dev/null 2>&1; then
    mkdir -p "${CLAUDE_SKILLS_DIR}"
    rm -rf "${CLAUDE_SKILLS_DIR}/vibe-storm"
    cp -r "${SKILL_SRC}" "${CLAUDE_SKILLS_DIR}/vibe-storm"
    echo -e "${GREEN}✓ Installed into Claude Code:${NC} ${CLAUDE_SKILLS_DIR}/vibe-storm"
    INSTALLED=$((INSTALLED + 1))
fi

# 2. Install for Antigravity / Gemini CLI (~/.gemini/config/skills)
GEMINI_SKILLS_DIR="${HOME}/.gemini/config/skills"
if [ -d "${HOME}/.gemini" ]; then
    mkdir -p "${GEMINI_SKILLS_DIR}"
    rm -rf "${GEMINI_SKILLS_DIR}/ak-vibe-storm" "${GEMINI_SKILLS_DIR}/vibe-storm"
    cp -r "${SKILL_SRC}" "${GEMINI_SKILLS_DIR}/vibe-storm"
    echo -e "${GREEN}✓ Installed into Antigravity/Gemini:${NC} ${GEMINI_SKILLS_DIR}/vibe-storm"
    INSTALLED=$((INSTALLED + 1))
fi

# 3. Install for Cursor (Current Workspace)
if [ "$REPO_DIR" != "$PWD" ] && ([ -d "${PWD}/.cursor" ] || [ -f "${PWD}/.cursorrules" ]); then
    mkdir -p "${PWD}/.cursor/rules"
    cp "${REPO_DIR}/.cursor/rules/vibe-storm.mdc" "${PWD}/.cursor/rules/"
    echo -e "${GREEN}✓ Installed into current Cursor workspace:${NC} ${PWD}/.cursor/rules/vibe-storm.mdc"
    INSTALLED=$((INSTALLED + 1))
fi

if [ $INSTALLED -eq 0 ]; then
    # Fallback to home claude skills
    mkdir -p "${CLAUDE_SKILLS_DIR}"
    cp -r "${SKILL_SRC}" "${CLAUDE_SKILLS_DIR}/vibe-storm"
    echo -e "${GREEN}✓ Installed into standard user skills path:${NC} ${CLAUDE_SKILLS_DIR}/vibe-storm"
fi

echo -e "\n${GREEN}🎉 Installation complete!${NC}"
echo -e "You can now trigger vibe-storm in your AI agent with:"
echo -e "  ${YELLOW}/vibe-storm \"Micro-SaaS for podcast editing\" --full --html${NC}\n"
