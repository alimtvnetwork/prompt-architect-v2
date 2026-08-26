# Prompt Architect Versioning & Import Scripts

The Prompt Architect system uses a sophisticated import/export mechanism mimicking our coding guidelines architecture. This allows any repository to pull the exact versions of the prompts needed for their AI workflows.

## Prompt Version Tracking

Whenever the import scripts (`install.ps1` or `install.sh`) are executed, they write a tracking file:
`prompt-version.json` (inside the target directory, typically `.lovable/prompts/`).

This file contains the Git version tag and timestamp. AI Agents must read this file to understand the capabilities and prompt versions available to them in the target repo.

## The Import Scripts

Located in the root of the `prompt-architect` repository:
- `install.ps1` (For Windows/PowerShell users)
- `install.sh` (For macOS/Linux users)

These scripts accept two arguments:
1. `TargetDir` (e.g. `.lovable/prompts`)
2. `Version` (e.g. `main` or a pinned tag like `v1.2.0`)

They safely remove the old prompts matching the previous tracking stamp, clone the new version via git sparse extraction, and install the new library seamlessly.

## Coding Guidelines Integration

The master coding guidelines file (`.lovable/coding-guidelines/coding-guidelines.md`) has been updated to explicitly enforce this Prompt Architecture. When users import the coding guidelines, they are explicitly instructed to also import the Prompt Architect using these scripts to ensure the AI has the mandatory Execution Prompts (`02-execute-parent-task-with-n-steps.md` and `03-execute-batched-loop.md`).
