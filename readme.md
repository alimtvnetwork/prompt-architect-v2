# Repository Guide

One readme only, always lowercase `readme.md`. Never create `README.md`.

## AI entry point

1. `.lovable/memory/what-to-read.md` — routing table: which file to read for what.
2. `.lovable/memory/prompt-library.md` — full prompt storage and formatting rules.
3. `01-general-prompts/01-prompt-library-setup/01-prompt-library-setup.md` — original spec.

## Folder structure

```text
01-general-prompts/             library of all general reusable prompts
  01-core-workflow/             prompts for memory, planning, task management
  02-coding-standards/          prompts for coding guidelines and theming
  03-release-management/        prompts for version bumps and releases
  04-testing-and-qa/            prompts for unit tests, code coverage, issues
  05-commit-and-multi-agent-code-fix/ prompts for code fix, wrappers, artifact purge
  05-ui-and-design/             prompts for UI components, SVG, logo creation
  06-content-and-seo/           prompts for README, SEO, social media, jokes
  07-prompt-engineering/        prompts for proofreading and prompt creation
  08-ci-cd/                     prompts for CI/CD workflow & script fixes
  09-insults/                   consolidated unsoftened stance and enforcement texts
02-pwsh-prompts/                PowerShell specific prompts
<project-name>-prompts/         prompts that name a project
  01-<prompt-slug>.md
assets/                         images and assets supplied with prompts
spec/                           specifications (hyphenated: spec/<NN>-<slug>/)
  01-spec-authoring-guide/      spec authoring standards
  02-coding-guidelines/         coding standards & rules
  03-error-manage/              error management conventions
  04-database-conventions/      database schema & query rules
  21-app/                       app domain specifications & routes
.lovable/                       configuration, memory, and indexes
  memory/                       what-to-read.md, prompt-library.md
  prompts.md                    canonical index of all saved prompts
readme.md                       this file
src/                            application code
```

*(Note: Spec folder sequence numbers and placements follow `spec/<NN>-<slug>/` but can switch between projects; AI agents dynamically discover and read all nested markdown files).*

## Naming rules

- Two-digit sequence + hyphen + lowercase slug: `01-prompt-library-setup.md`.
- Lowercase and hyphens only — no spaces, uppercase or camelCase.
- All readme files are lowercase `readme.md`, and the root has exactly one.
- Every empty folder keeps a `.gitkeep`.

## Where a prompt goes

- Project name mentioned -> `<project-name>-prompts/<NN>-<slug>.md`.
- General reusable prompt -> `01-general-prompts/<NN>-<category>/<slug>.md`.
- Use the next free sequence number when generating a new category or new project folder.
- All prompts must be indexed in `.lovable/prompts.md` per the canonical prompt architecture.

## Prompt file format

Proofread only: remove filler words, keep the exact wording. Sections in order:

1. `## Prompt` — the proofread text.
2. `## Action Items — Must Follow (Non-Negotiable)` — checklist of every stated rule.
3. `## Folder Structure` — only if discussed.
4. `## Database` — only if discussed.
5. `## Before Writing Code` — code prompts only: read `spec/02-coding-guidelines/`, `spec/03-error-manage/`, `spec/04-database-conventions/`; error management must be followed; code must be DRY.

If the user says to keep a prompt as is, store the body verbatim — only the checklist
section may be enhanced (formatting, phase grouping, sharper wording; never drop a rule).

## Supplied files and links

Assets/images -> `assets/`. Specs -> `spec/` (app spec in `spec/21-app/`). Ask if unclear.

## Application

TanStack Start, TypeScript, React, Tailwind CSS.

```sh
npm i
npm run dev
```
