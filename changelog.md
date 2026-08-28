# Changelog

## [v1.24.0] 2026-08-28 Encoding Verification & Line Ending Normalization

### Install Prompt Architect v1.24.0
To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.24.0/install.sh | bash -s -- ".lovable/prompts" "v1.24.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.24.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.24.0"`

### Added / Changed / Fixed / Removed

- **Fixed:** Conducted a repository-wide byte-level audit of all 787 `.md` files. Confirmed zero files were suffering from UTF-8 BOM or UTF-16 corruption. 
- **Changed:** Normalized CRLF (Windows) line endings to LF (Unix) across 784 markdown files to permanently eliminate Git `LF will be replaced by CRLF` warnings and ensure perfect cross-platform rendering.


## [v1.23.0] 2026-08-28 Execution Prompts Consolidation & Rule Sets

### Install Prompt Architect v1.23.0
To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.23.0/install.sh | bash -s -- ".lovable/prompts" "v1.23.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.23.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.23.0"`

### Added / Changed / Fixed / Removed

- **Changed:** Refactored all Execution prompts (`14-execute/*` and `09-commit*`) to place an explicit, overarching `/goal` defining the N-step continuous loop immediately below the document title.
- **Added:** Injected a strict `Task-Specific Rule Set` directive during Phase 1 (Spec Writing) that forces the AI to analyze the task domain and generate 3-5 explicit custom rules before it is allowed to start coding, preventing domain-specific regressions.
- **Changed:** Consolidated and aggressively stripped minor repetitive instructions from the core orchestration loops while rigorously preserving the Coding Guidelines and Anti-Hallucination checklists.


## [v1.22.0] 2026-08-28 Write Memory Prompt Restructuring

### Install Prompt Architect v1.22.0
To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.22.0/install.sh | bash -s -- ".lovable/prompts" "v1.22.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.22.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.22.0"`

### Added / Changed / Fixed / Removed

- **Changed:** Manually replaced the `01-general-prompts/03-read-write/03-write-memory.md` payload with the user's provided block to precisely align the "Actionable Items & Checklist" and "MUST FOLLOW NON-NEGOTIABLE" insult sections at the bottom of the execution file.


## [v1.21.0] 2026-08-28 Folder Structure Docs & 4-Step Release Fallback

### Install Prompt Architect v1.21.0
To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.21.0/install.sh | bash -s -- ".lovable/prompts" "v1.21.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.21.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.21.0"`

### Added / Changed / Fixed / Removed

- **Added:** Created `.lovable/lovable-folder-structure.md` and `spec/spec-folder-structure.md` to serve as the absolute source of truth for the `XX-<slug>` directory structure and sequential prefixing system.
- **Added:** Introduced a strict 4-Step Fallback Chain for version bumping into all execution and release prompts:
  1. Rely on `.lovable/release/bump_versions.py`
  2. Fallback to `.lovable/release/release-method.md` to learn pin sites and generate the Python script.
  3. Fallback to a high-performance, OS-agnostic Python `os.walk` search (banning `rg`) to generate the method doc and script.
  4. Fallback to stopping and asking the user if utterly stuck.


## [v1.20.0] 2026-08-27 Ripgrep Global Search Ban & Performance Optimization

### Install Prompt Architect v1.20.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.20.0/install.sh | bash -s -- ".lovable/prompts" "v1.20.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.20.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.20.0"`

### Added / Changed / Fixed / Removed

- **Added:** Injected a `CRITICAL PERFORMANCE RULE` into all Release and Execution prompts that strictly forbids the AI from running slow global ripgrep (`rg`) or `find` searches across the repository.
- **Fixed:** Removed the hardcoded `rg -n " <PREV_VERSION> " -g '!node_modules'` command from the Auto-Bumper Bootstrap phase. Agents are now forced to use the high-performance Python script (`bump_versions.py`) targeting explicitly known files, vastly improving release pipeline speed.


## [v1.19.0] 2026-08-27 Aggressive Insult Block Expansion

### Install Prompt Architect v1.19.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.19.0/install.sh | bash -s -- ".lovable/prompts" "v1.19.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.19.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.19.0"`

### Added / Changed / Fixed / Removed

- **Added:** Aggressively expanded the `MUST FOLLOW NON-NEGOTIABLE` insult block to **20 additional prompts**, covering every single actionable file in the repository.
- **Added:** The insult block is now forcefully embedded in Spec Writing, UI/Design generation, Content/SEO workflows, Prompt Engineering proofreading, and Release Management/Version Bumping scripts.


## [v1.18.0] 2026-08-27 Mandatory Anti-Hallucination Checklist Integrations

### Install Prompt Architect v1.18.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.18.0/install.sh | bash -s -- ".lovable/prompts" "v1.18.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.18.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.18.0"`

### Added / Changed / Fixed / Removed

- **Added:** Implemented the 5 user-approved Anti-Hallucination rules directly into the core `execute` and `commit` prompts (`02-execute-parent-task-with-n-steps.md`, `04-execute-ai-instruction-writer.md`, etc.).
- **Added:** Created a new mandatory `Anti-Hallucination & Blast Radius Checklist` that forces the AI to output git status diff proofs, grep for `TODO` placeholders, globally search before renaming, and explicitly sync created files with `what-to-read.md`.


## [v1.17.0] 2026-08-27 Global Insult Injection & Anti-Hallucination Overhaul

### Install Prompt Architect v1.17.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.17.0/install.sh | bash -s -- ".lovable/prompts" "v1.17.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.17.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.17.0"`

### Added / Changed / Fixed / Removed

- **Added:** Scanned all actionable prompts in `01-general-prompts/` and injected the mandatory `## MUST FOLLOW NON-NEGOTIABLE` insult block into 9 files that were missing it.
- **Fixed:** Ensured the insult block is placed aggressively at the top of the execution flow in `02-execute-parent-task-with-n-steps.md`, `04-execute-ai-instruction-writer.md`, `01-plan-coding-guideline-audit.md`, and all CI/QA prompts to forcefully jolt the AI into compliance before it processes variables.


## [v1.16.0] 2026-08-27 Goal Re-Alignment & Audit Plan De-Duplication

### Install Prompt Architect v1.16.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.16.0/install.sh | bash -s -- ".lovable/prompts" "v1.16.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.16.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.16.0"`

### Added / Changed / Fixed / Removed

- **Fixed:** Resolved a regression where `01-coding-guidelines.md` was inadvertently reverted back to its bloated state. I have re-applied the condensed, highly effective Antigravity structure with exactly two cross-language code examples.
- **Changed:** Lifted all `/goal` directives in `01-plan-coding-guideline-audit.md` and `02-execute-coding-guideline-fix.md` to sit at the absolute top level of the prompt (immediately following the H1 title) so Antigravity properly prioritizes the action.
- **Removed:** Nuked an entire 20KB duplicated block of "Compiled Simple Coding Guidelines" from the bottom of `01-plan-coding-guideline-audit.md`.
- **Added:** Replaced the duplicated text in the audit plan with a strict `/learn` command pointing directly to `01-coding-guidelines.md` to enforce a Single Source of Truth architecture for guidelines.


## [v1.15.1] 2026-08-27 Coding Guidelines: Restored Language-Specific Rules

### Install Prompt Architect v1.15.1

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.15.1/install.sh | bash -s -- ".lovable/prompts" "v1.15.1"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.15.1/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.15.1"`

### Added / Changed / Fixed / Removed

- **Added:** Injected the missing `## Language-Specific Rules` section back into `01-coding-guidelines.md`.
- **Added:** Formatted the language-specific rules to heavily utilize the `/learn` command, instructing the Antigravity agent on exactly which sub-folders to ingest for React/TypeScript, Go, Python, C#, and PHP standards.


## [v1.15.0] 2026-08-27 Coding Guidelines Consolidation & Antigravity Optimization

### Install Prompt Architect v1.15.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.15.0/install.sh | bash -s -- ".lovable/prompts" "v1.15.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.15.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.15.0"`

### Added / Changed / Fixed / Removed

- **Changed:** Massively overhauled and consolidated `01-coding-guidelines.md`. Removed all repeated sections, verbose auto-generated boilerplate blocks, and excessive multi-language code snippets.
- **Added:** Optimized the file strictly for the Antigravity multi-agent architecture. The `/goal` and `/learn` commands are now heavily focused at the very top of the file to guarantee agents internalize the rules before executing.
- **Changed:** Reduced the coding examples to exactly two highly effective snippets (one Bad, one Good) that succinctly demonstrate Parameter Structs, PascalCase Acronyms, Positive Booleans, and Whitespace spacing rules across languages.
- **Added:** Added a rigid "Antigravity Verification Checklist" to the bottom of the prompt to ensure agents mechanically verify their compliance with the rules before ending their turn.


## [v1.14.0] 2026-08-27 Execute Prompts Checklist Consolidation & Spec Phase

### Install Prompt Architect v1.14.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.14.0/install.sh | bash -s -- ".lovable/prompts" "v1.14.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.14.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.14.0"`

### Added / Changed / Fixed / Removed

- **Changed:** Restructured the `02-execute-parent-task-with-n-steps.md` and `04-execute-ai-instruction-writer.md` prompts to explicitly force a "Phase 1: Write Spec" step. Agents MUST write a detailed spec to `.lovable/plans/pending/XX-<slug>.md` before writing code.
- **Changed:** Differentiated the goals of the two execution prompts. `02` focuses on writing subtasks (`.lovable/plans/subtasks/`) for multi-agent execution, while `04` focuses on writing a generic AI instruction spec and outputting it to the chat window for cross-library sharing.
- **Fixed:** Consolidated the messy, scattered checklists in the execution prompts into exactly two unified blocks: **Non-Negotiable Coding Guidelines Checklist** (which now heavily focuses on MD022, MD032, Boolean logic, and error envelopes) and the **End of Tunnel Release Checklist**.
- **Removed:** Stripped out the "status task" (Temp-Agent State Management Protocol) checklists to reduce noise and prevent AI hallucination.


## [v1.13.1] 2026-08-27 File Encoding / Null Byte Fixes

### Install Prompt Architect v1.13.1

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.13.1/install.sh | bash -s -- ".lovable/prompts" "v1.13.1"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.13.1/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.13.1"`

### Added / Changed / Fixed / Removed

- **Fixed:** Stripped accidental null bytes (`\x00`) from `03-commit-fix-v2.md` and several other Markdown files. A bad regex evaluation during a previous injection caused folder references like `01-` to be written as an octal null byte escape sequence (`\01-`). This resolves the issue where GitHub Desktop incorrectly identified these Markdown files as binary.


## [v1.13.0] 2026-08-27 Python Auto-Bumper & Install Snippet Propagation

### Install Prompt Architect v1.13.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.13.0/install.sh | bash -s -- ".lovable/prompts" "v1.13.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.13.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.13.0"`

### Added / Changed / Fixed / Removed

- **Added:** Replaced the rigid `rg` global search in the release prompts with a new **Python Auto-Bumper Bootstrap** phase. On the first release, the AI will scan the repository and auto-generate `.lovable/release/bump_versions.py` and a `.lovable/memory/release-architecture.md` brain file to explicitly map and handle all future version replacements without breaking context limits.
- **Added:** Supplied a rich, functional Python skeleton for the Auto-Bumper script within the release prompts to ensure AIs generate robust bumping logic.
- **Changed:** Propagated the non-negotiable **Install Snippet (Dynamic URL Discovery)** section to ALL remaining release scripts (`01`, `02`, `03`) and ALL execution/CI/CD/bug scripts (`09` and `14` series).
- **Added:** Injected a strict rule into all Execution and CI/CD scripts commanding the AI to execute `bump_versions.py --type <tier>` for releases instead of manually trying to search and replace versions.


## [v1.12.0] 2026-08-27 Collapse Markdown Checklist Gaps

### Install Prompt Architect v1.12.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.12.0/install.sh | bash -s -- ".lovable/prompts" "v1.12.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.12.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.12.0"`

### Added / Changed / Fixed / Removed

- **Fixed:** Executed a repository-wide regex sweep to collapse all "loose" markdown checklists. Every `- [ ]` checklist item that was previously separated by an ugly empty blank line has been tightly condensed to improve visual readability across all `01-general-prompts`, `.lovable/prompts`, and `spec` files.


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












