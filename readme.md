# Repository Guide

One readme only, always lowercase `readme.md`. Never create `README.md`.

## AI entry point

1. `.lovable/memory/what-to-read.md` — routing table: which file to read for what.
2. `.lovable/memory/prompt-library.md` — full prompt storage and formatting rules.
3. `01-general-prompts/01-prompt-library-setup/01-prompt-library-setup.md` — original spec.

## Folder structure

```text
01-general-prompts/             library of all general reusable prompts
  00-folder-structure/          prompts regarding folder layout
  01-prompt-library-setup/      prompts for setting up prompt indexing and architecture
  02-core-workflow/             general lifecycle prompts (initial unified prompt, plan/next steps)
  03-read-write/                canonical Read Memory & Write Memory prompts
  04-coding-standards/          actual master coding guidelines and theming rules
  05-coding-guidelines/         prompts for auditing/executing against guidelines
  06-testing-and-qa/            prompts for unit tests, code coverage, issues
  07-bug-fix/                   prompts for fixing specific issues
  08-dry-code/                  prompts enforcing DRY code
  09-commit-and-multi-agent-code-fix/ prompts for commit fixes and git history cleanups
  10-ui-and-design/             prompts for UI components, SVG, logo creation
  11-content-and-seo/           prompts for README, SEO, social media, jokes
  12-old-plan-prompts/          archive of legacy planning prompts
  13-plan-audit/                prompts for auditing specs and generating strict plans
  14-execute/                   prompts for pending task execution & self-looping agents
  15-prompt-engineering/        prompts for proofreading and prompt creation
  16-ci-cd/                     prompts for CI/CD workflow & script fixes
  17-release-management/        prompts for version bumps and releases
  18-insults/                   consolidated unsoftened stance and enforcement texts
  19-old-execute-prompts/       archive of legacy execution prompts
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
  temp-scripts/                 scratch space for automation scripts (gitignored)
  temp-agents/                  scratch space for active sub-agent states (gitignored)
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
- Read and Write memory prompts belong strictly in `01-general-prompts/03-read-write/`.
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
