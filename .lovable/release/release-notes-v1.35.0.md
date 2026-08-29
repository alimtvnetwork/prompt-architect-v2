# prompt-architect-v2 v1.35.0

## Quick Install (One-Liners)

### Windows (PowerShell 5.1+)

```powershell
irm https://github.com/alimtvnetwork/prompt-architect-v2/releases/download/v1.35.0/install.ps1 | iex
```

### Linux / macOS (Bash)

```bash
curl -fsSL https://github.com/alimtvnetwork/prompt-architect-v2/releases/download/v1.35.0/install.sh | bash
```

## [v1.35.0] 2026-08-29 Sequenced Coding Guideline Execution Suite (cg-execute) with Prioritized Error-First Routing, Relative Spec Checklists, and Linter Hooks

### Install Prompt Architect v1.35.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.35.0/install.sh | bash -s -- ".lovable/prompts" "v1.35.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.35.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.35.0"`

### Added / Changed / Fixed / Removed

- **Added:** Created the comprehensive Coding Guideline Execution Suite (`cg-execute`) in `01-general-prompts/15-cg-execute/` and mirrored to `.lovable/prompts/cg-execute/`.
- **Changed:** Sequenced prompts strictly by priority: `01-index.md`, `02-error-management.md` (highest priority), `03-boolean-and-naming.md`, `04-data-and-schema.md`, `05-react-frontend-guidelines.md`, `06-code-hygiene.md`, and `07-style-guidelines.md` (moved to the end).
- **Added:** Implemented non-negotiable relative specification checklists mapping every single file across `spec/03-error-manage/`, `spec/02-coding-guidelines/`, `spec/04-database-conventions/`, and `spec/07-design-system/` with concrete "Why" and "How" mandates.
- **Added:** Standardized configurable `N = 200` budget positioned as the primary variable on top of each prompt, with `N/2` split phases for deep AST scanning and autonomous execution loops.
- **Added:** Embedded native Antigravity skill bootstrapping (`Phase 0`) into every execution prompt, auto-generating `.agents/skills/<slug>/skill.md` for progressive disclosure.
- **Added:** Embedded mandatory Linter & CI/CD Connection checklists requiring the verification or automatic generation of dedicated linters in `linter-scripts/` and wiring them to `.lovable/ai-fix-scripts/03-cicd-local-runner.py`.
- **Fixed:** Re-sequenced downstream general prompt directories (`16-prompt-engineering` through `22-ai-fix-script-prompts`), resolving sequence collisions and updating the master repository tree.
- **Fixed:** Stripped all absolute `file:///` paths across prompt files, strictly enforcing portable relative markdown paths and checklists.
