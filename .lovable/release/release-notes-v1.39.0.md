# prompt-architect-v2 v1.39.0

## Quick Install (One-Liners)

### Windows (PowerShell 5.1+)

```powershell
irm https://github.com/alimtvnetwork/prompt-architect-v2/releases/download/v1.39.0/install.ps1 | iex
```

### Linux / macOS (Bash)

```bash
curl -fsSL https://github.com/alimtvnetwork/prompt-architect-v2/releases/download/v1.39.0/install.sh | bash
```

## [v1.39.0] 2026-08-30 Read & Write Enhanced Prompts Modernization, Skill/Rule Auto-Generation & Coding Guidelines v24 Migration

### Install Prompt Architect v1.39.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.39.0/install.sh | bash -s -- ".lovable/prompts" "v1.39.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.39.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.39.0"`

### Added / Changed / Fixed / Removed

- **Added:** Upgraded `02-read-memory-enhanced.md` with modernized `.lovable/` folder map (`ai-fix-scripts/`, `coding-guidelines/`, `plans/subtasks/`, `prompts/cg-execute/`), mandatory `.lovable/*.md` file inspection and flagging, and atomic numbered checklists.
- **Added:** Embedded automatic Antigravity Skill (`.agents/skills/<slug>/skill.md`) and Rule (`.agents/rules/<slug>/rule.md`) generation protocol into memory ingestion workflows.
- **Changed:** Upgraded `01-write-antigravity.md` and `03-write-memory.md` with complete modernized folder structure maps and numbered checklists (`1. [ ]`).
- **Changed:** Upgraded `01-plan-coding-guideline-audit.md` with bounded 5–8 file micro-batching protocol into `.lovable/plans/subtasks/`.
- **Changed:** Formatted transition notice in root `readme.md` directing all future development to `coding-guidelines-v24` (https://github.com/alimtvnetwork/coding-guidelines-v24).
