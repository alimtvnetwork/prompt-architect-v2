# Changelog

## [v1.11.0] 2026-08-27 Dynamic Git Install Script Detection

### Install Prompt Architect v1.11.0
To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.11.0/install.sh | bash -s -- ".lovable/prompts" "v1.11.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.11.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.11.0"`

### Added / Changed / Fixed / Removed

- **Fixed:** Removed the hardcoded "Prompt Architect" repository URL from all generic release prompts (`01-general-prompts/17-release-management/*`).
- **Added:** Added explicit instructions to the release prompts requiring AI agents to dynamically construct the raw `install.sh`/`install.ps1` URL by running `git config --get remote.origin.url` and parsing the `<owner>/<repo>`.
- **Added:** Formalized the dynamic Git config extraction rule inside the `16-generic-release/03-install-scripts.md` and `14-update/18-install-scripts.md` coding guidelines.


## [v1.10.0] 2026-08-27 Checklist-Driven Anti-Hallucination

### Install Prompt Architect v1.10.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.10.0/install.sh | bash -s -- ".lovable/prompts" "v1.10.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.10.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.10.0"`

### Added / Changed / Fixed / Removed

- **Fixed:** Corrected a critical placement error in execution prompts where `N=20` and `/goal` instructions were being pushed down by top-level anti-hallucination blocks. These variables are now firmly back at the absolute top of the file.
- **Changed:** Refactored the anti-hallucination stance to be exclusively checklist-driven. The aggressive warnings are now embedded directly within the End of Tunnel Release and Action Summary Checklists, targeting specific points of failure (e.g. "To prevent this hallucination... physically check off these items").


## [v1.9.0] 2026-08-27 Execution Architecture Improvements

### Install Prompt Architect v1.9.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.9.0/install.sh | bash -s -- ".lovable/prompts" "v1.9.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.9.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.9.0"`

### Added / Changed / Fixed / Removed

- **Added:** `04-execute-ai-instruction-writer.md` prompt for generating generic, anti-hallucination spec instructions.
- **Changed:** Injected aggressive Anti-Hallucination ("Insult") stance into all execution prompts to strictly enforce code quality and zero-sloppiness.
- **Changed:** Refactored the End of Tunnel Release block in all execution prompts into a strict Markdown checklist (`- [ ]`), explicitly forcing verification of Root README pinning.
- **Changed:** Expanded the `Execution Reporting` format to enforce an Action Summary Checklist summarizing all completed tasks.


## [v1.8.0] 2026-08-27 Strict Readme Pinning & Markdown Unbolding

### Install Prompt Architect v1.8.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.8.0/install.sh | bash -s -- ".lovable/prompts" "v1.8.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.8.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.8.0"`

### Added / Changed / Fixed / Removed

- Stripped all `**` bold formatting from all recently injected execution and CI/CD checklists to comply with repository Markdown standards.
- Injected explicit Root README Pinning instructions (labeled FATAL) directly into the End of Tunnel Release blocks of all `14-execute`, `16-ci-cd`, and `09-commit-and-multi-agent-code-fix` prompts.
- Added explicit README pinning checklists to all release prompts so agents cannot skip the step.


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






