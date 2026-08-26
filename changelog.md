# Changelog

## [v1.7.0] 2026-08-26 Consolidated Master Release Prompt Updates

### Install Prompt Architect v1.7.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.7.0/install.sh | bash -s -- ".lovable/prompts" "v1.7.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.7.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.7.0"`

### Added / Changed / Fixed / Removed

- Saved user's master release prompt text to `.lovable/prompts/01-release.md`.
- Executed strict 1.7.0 lock-step version bump across all codebase files, including root README.


## [v1.6.0] 2026-08-26 Minor bump and release process updates

### Install Prompt Architect v1.6.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.6.0/install.sh | bash -s -- ".lovable/prompts" "v1.6.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.6.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.6.0"`

### Added / Changed / Fixed / Removed

- Added `version.json` dynamic changelog format block to `prompt-version.template.json` and install scripts.
- Implemented `MD022` markdown linter rule across the entire repository.
- Upgraded release prompts to dynamically ban test files from version scanning.
- Formalized `.lovable/memory/version-json-architecture.md` as Single Source of Truth architecture memory.


