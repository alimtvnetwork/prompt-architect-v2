# Repository Guide

One readme only, always lowercase `readme.md`. Never create `README.md`.

## AI entry point

1. `.lovable/memory/what-to-read.md` — routing table: which file to read for what.
2. `.lovable/memory/prompt-library.md` — full prompt storage and formatting rules.
3. `01-prompts/01-general/01-prompt-library-setup/01-prompt-library-setup.md` — original spec.

## Folder structure

```text
01-prompts/                  prompt archive
  01-general/                prompts with no project name
    01-prompt-library-setup/01-prompt-library-setup.md
    02-bug-fix/              example category (.gitkeep while empty)
    03-dry-code/
    04-coding-guidelines/
  02-<project-name>/         prompts that name a project
    01-<prompt-slug>.md
assets/                      images and assets supplied with prompts
spec/
  02/  coding guidelines     03/  error management
  04/  mandatory rules       21/  app spec
.lovable/memory/             what-to-read.md, prompt-library.md
readme.md                    this file
src/                         application code
```

## Naming rules

- Two-digit sequence + hyphen + lowercase slug: `01-prompt-library-setup.md`.
- Lowercase and hyphens only — no spaces, uppercase or camelCase.
- All readme files are lowercase `readme.md`, and the root has exactly one.
- Every empty folder keeps a `.gitkeep`.

## Where a prompt goes

- Project name mentioned -> `01-prompts/<NN>-<project-name>/<NN>-<slug>.md`.
- No project name -> `01-prompts/01-general/<NN>-<category>/<NN>-<slug>.md`.
- Use the next free sequence number. Commit after each stored prompt.

## Prompt file format

Proofread only: remove filler words, keep the exact wording. Sections in order:

1. `## Prompt` — the proofread text.
2. `## Action Items — Must Follow (Non-Negotiable)` — checklist of every stated rule.
3. `## Folder Structure` — only if discussed.
4. `## Database` — only if discussed.
5. `## Before Writing Code` — code prompts only: read `spec/02`, `spec/03`, `spec/04`;
   error management must be followed; code must be DRY.

If the user says to keep a prompt as is, store the body verbatim — only the checklist
section may be enhanced (formatting, phase grouping, sharper wording; never drop a rule).

## Supplied files and links

Assets/images -> `assets/`. Specs -> `spec/` (app spec in `spec/21/`). Ask if unclear.

## Application

TanStack Start, TypeScript, React, Tailwind CSS.

```sh
npm i
npm run dev
```
