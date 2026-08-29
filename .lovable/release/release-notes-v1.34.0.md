# prompt-architect-v2 v1.34.0

## Quick Install (One-Liners)

### Windows (PowerShell 5.1+)

```powershell
irm https://github.com/alimtvnetwork/prompt-architect-v2/releases/download/v1.34.0/install.ps1 | iex
```

### Linux / macOS (Bash)

```bash
curl -fsSL https://github.com/alimtvnetwork/prompt-architect-v2/releases/download/v1.34.0/install.sh | bash
```


## [v1.34.0] 2026-08-29 Autonomous CI/CD Local Runner with Self-Looping, Parallel Execution, and Release Flow

### Install Prompt Architect v1.34.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.34.0/install.sh | bash -s -- ".lovable/prompts" "v1.34.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.34.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.34.0"`

### Added / Changed / Fixed / Removed

- **Added:** Created `01-general-prompts/16-ci-cd/04-ci-cd-fix-with-release.md` combining the autonomous CI/CD fix loop with a formal Phase 3 verification gate and automated Phase 4 release pipeline via `.lovable/release/bump_versions.py`.
- **Added:** Created Antigravity skill `.agents/skills/ci-cd-fix/skill.md` with YAML frontmatter, enabling progressive disclosure and autonomous self-bootstrap across workspaces.
- **Changed:** Overhauled `01-general-prompts/16-ci-cd/01-ci-cd-fix.md` to feature configurable `N` budget at the header, `N/2` split phases, native host Docker command stripping, parallel batch execution with `BATCH_SIZE`, and intelligent timeout detection with auto-increase.
- **Added:** Added bidirectional error enqueuing to CI/CD loops, automatically generating actionable tasks in `.lovable/plans/pending/` and tracking RCAs in `.lovable/cicd-issues/` and `.lovable/memory/issues/`.
- **Added:** Integrated first-class image/screenshot diagnostic processing to extract pipeline and job headers, verify runner coverage, and apply preemptive code fixes before running checks.
- **Fixed:** Eliminated passive waiting and remote CI polling traps from CI/CD prompts; enforced continuous programmatic self-looping until 100% green.
