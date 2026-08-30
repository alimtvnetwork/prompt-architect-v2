# prompt-architect-v2 v1.36.0

## Quick Install (One-Liners)

### Windows (PowerShell 5.1+)

```powershell
irm https://github.com/alimtvnetwork/prompt-architect-v2/releases/download/v1.36.0/install.ps1 | iex
```

### Linux / macOS (Bash)

```bash
curl -fsSL https://github.com/alimtvnetwork/prompt-architect-v2/releases/download/v1.36.0/install.sh | bash
```

## [v1.36.0] 2026-08-30 Final Prompt Architect Release & Migration to Coding Guidelines

### Install Prompt Architect v1.36.0

To pin your repository to this exact version, run the following one-liner:
**Unix/Bash:** `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.36.0/install.sh | bash -s -- ".lovable/prompts" "v1.36.0"`
**PowerShell:** `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/v1.36.0/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.36.0"`

### Added / Changed / Fixed / Removed

- **Added:** Created `18-function-argument-reduction-and-params.md` enforcing parameter structs (`*Params`), value-based struct passing in Go, and mandatory `*apperror.AppError` returns (eliminating bare "void" functions in Go).
- **Added:** Upgraded `14-function-signatures-and-return-types.md` with complete, production-ready `Result[T]` struct and method suite (`IsSuccess`, `IsFailed`, `IsInvalid`, `HasError`, `HasNoError`, `HasValidError`, `Unwrap`, `UnwrapOr`), `*AppError` comparison methods, and multi-language wrappers.
- **Changed:** Upgraded `10-style-guidelines.md` with Rule 2c and Rule 2d enforcing mandatory vertical line gaps around multiline collection literals, struct instantiations, sequential function invocations, and extracted affirmative boolean guards.
- **Added:** Implemented bounded micro-tasking protocol (5–8 files per batch) and AI diagnostic guide in `10-style-guidelines.md` to prevent premature completion hallucinations.
- **Changed:** Standardized boolean naming across 38 files to strictly allow ONLY `is` or `has` prefixes (`is, has as prefix is only acceptable and nothing else acceptable including but not limited to can, should etc`).
- **Changed:** Formatted all 98 prompts with clean numbered checklists (`1. [ ]`) with zero hyphens after numbers.
- **Changed:** Standardized all prompt titles to begin with unique topic-first descriptive words with zero repeated leading prefixes.
- **Added:** Integrated continuous 2-agent auto-looping concurrency architecture (max 2 threads each) and failure memory recovery into `.lovable/plans/last-failure.md` across all execution and CI/CD prompts.
- **Changed:** Added repository deprecation and transition notice in `readme.md` directing future development to `coding-guidelines`.
