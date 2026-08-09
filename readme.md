# Repository Guide

This repository keeps a structured **prompt library** alongside the application code.
Any AI or contributor working here must follow the conventions below.

## Read this first (AI entry point)

1. `.lovable/memory/what-to-read.md` — routing table: which file to read for what.
2. `.lovable/memory/prompt-library.md` — full rules for storing and formatting prompts.
3. `01-prompts/01-general/01-prompt-library-setup/01-prompt-library-setup.md` — the
   original specification of this system.

## Folder structure

```text
01-prompts/                  prompt archive (root of all stored prompts)
  01-general/                prompts with no project name
    01-prompt-library-setup/
      01-prompt-library-setup.md
    02-bug-fix/              example category (.gitkeep while empty)
    03-dry-code/             example category (.gitkeep while empty)
    04-coding-guidelines/    example category (.gitkeep while empty)
  02-<project-name>/         prompts that name a project
    01-<prompt-slug>.md
    02-<prompt-slug>.md
assets/                      images and other assets supplied with prompts
spec/
  02/                        coding guidelines
  03/                        error management
  04/                        additional mandatory rules
  21/                        app spec
.lovable/memory/             AI memory files
  what-to-read.md
  prompt-library.md
readme.md                    this file
src/                         application code
```

## Naming rules

- Two-digit sequence prefix, hyphen, lowercase slug: `01-prompt-library-setup.md`.
- Lowercase and hyphens only — no spaces, no uppercase, no camelCase.
- All readme files are lowercase `readme.md`.
- Every empty folder contains a `.gitkeep` so git tracks it.

## Where a prompt goes

- Prompt mentions a project name -> `01-prompts/<NN>-<project-name>/<NN>-<slug>.md`.
- No project name -> `01-prompts/01-general/<NN>-<category>/<NN>-<slug>.md`.
- Create the next free sequence number when adding a folder or file.
- Commit after each stored prompt.

## How a prompt file is written

Proofread only: remove filler words, keep the exact wording. Then:

1. `## Prompt` — the proofread text.
2. `## Action Items — Must Follow (Non-Negotiable)` — checklist of every stated rule.
3. `## Folder Structure` — only if discussed.
4. `## Database` — only if discussed.
5. `## Before Writing Code` — for code prompts: read `spec/02`, `spec/03`, `spec/04`;
   error management must be followed; code must be DRY.

## Supplied files and links

Assets/images -> `assets/`. Specs -> `spec/` (app spec in `spec/21/`). Ask if unclear.

## Application

Built with TanStack Start, TypeScript, React and Tailwind CSS.

```sh
npm i
npm run dev
```
