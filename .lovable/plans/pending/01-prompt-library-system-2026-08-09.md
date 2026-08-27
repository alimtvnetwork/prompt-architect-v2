# Prompt Library System

Set up a permanent, numbered prompt-archive structure at the repo root, plus the memory files that teach any AI how to use it.

## What gets created

```text
01-prompts/
  01-general/
    01-prompt-library-setup/
      01-prompt-library-setup.md
    .gitkeep
  .gitkeep
readme.md                     (root, lowercase)
.lovable/memory/
  what-to-read.md
  prompt-library.md
```

Rules encoded in the structure:

- Every folder and file is prefixed with a two-digit sequence: `01-`, `02-`, ...
- All names lowercase, hyphen separated. All readme files lowercase (`readme.md`).
- Empty folders are kept with a `.gitkeep` file.
- No project name in the prompt -> goes under `01-general/` in a category subfolder (`01-bug-fix/`, `02-dry-code/`, `03-coding-guidelines/`, ...).
- Project name mentioned -> `02-<project-name>/` at the `01-prompts/` level, with `01-`, `02-` prompt files inside.

## Prompt file format

Each saved prompt file contains, in order:

1. The prompt itself — filler words removed only, exact wording otherwise preserved (proofread only, no rewriting).
2. `## Action Items — Must Follow (Non-Negotiable)` — checklist of every rule discussed in that prompt.
3. `## Folder Structure` — only if a structure was discussed.
4. `## Database` — only if database design was discussed.
5. Standard footer added to every code-related prompt: read spec folders `02`, `03`, `04` (coding guidelines, error management) before writing code; code must be DRY.

## Assets and files handling

- Images/assets given with a prompt -> `assets/` folder.
- Specs -> `spec/`, with app spec inside `spec/21/`.
- If placement is ambiguous, the AI asks instead of guessing.

## Memory

- `.lovable/memory/prompt-library.md` — full rules: naming, sequencing, general vs project routing, prompt file sections, proofread-only policy, "next prompt" / "proofread prompt" behaviour, asset routing, spec folder 02/03/04 requirement, DRY requirement, `.gitkeep` for empty folders.
- `.lovable/memory/what-to-read.md` — short router: which file to read for what, pointing to the prompt library memory and to `01-prompts/`.
- Root `readme.md` — explains the folder structure and points any AI to the memory files and prompt location.

## Seed content

This conversation's instructions become the first archived prompt:
`01-prompts/01-general/01-prompt-library-setup/01-prompt-library-setup.md`, in the exact prompt format above, and referenced from the root readme and from what-to-read.

## Technical notes

- Existing uppercase `README.md` is replaced by lowercase `readme.md` (git-tracked rename).
- No application code or routes are touched.
- Commits are handled by the platform on save; no manual git commands run.
