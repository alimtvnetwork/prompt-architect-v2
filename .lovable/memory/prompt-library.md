# Prompt Library — Memory

This file defines how prompts are archived in this repository. Any AI working in this
repo must follow it exactly.

## 1. Location and naming

- All prompts live under `<category>_prompts/` at the repo root (e.g. `01_general_prompts`, `pwsh_prompts`).
- Root prompt folders use underscores (e.g., `01_general_prompts`). Folders and files inside them use: two-digit sequence, hyphen, lowercase slug.
  Examples: `01-prompt-library-setup.md`, `03-fix-login-redirect.md`.
- Lowercase and hyphens only. No spaces, no camelCase, no uppercase.
- All readme files are lowercase: `readme.md`.
- Every empty folder contains a `.gitkeep` file so it is tracked by git.

## 2. Routing a new prompt

1. Does the prompt mention a project name?
   - Yes -> store under `<project-name>_prompts/` (create the folder if it does not exist). Inside, the file is
     `<NN>-<prompt-slug>.md` using the next free sequence in that folder.
   - No -> it is a general prompt. Store under `01_general_prompts/` inside the
     matching category folder (see below).
2. General categories are themselves numbered folders, e.g.
   `01-prompt-library-setup`, `02-bug-fix`, `03-dry-code`, `04-coding-guidelines`.
   Create a new category folder (next free number) when none fits.
3. Derive the slug from the prompt's intent — short, lowercase, hyphenated.
4. Commit after storing the prompt.

## 3. How to write the prompt file

Proofread only. Remove filler words ("uh", "um", "I mean", "okay?", "you know").
Keep the exact wording otherwise. Never rewrite, summarise, reorder or "improve" it.

Sections, in this order:

1. `# <Title>`
2. `## Prompt` — the proofread prompt text.
3. `## Action Items — Must Follow (Non-Negotiable)` — a markdown checklist of every
   rule, constraint and requirement stated in the prompt.
4. `## Folder Structure` — only if a folder structure was defined or discussed. Skip otherwise.
5. `## Database` — only if a database segment or schema design was discussed. Skip otherwise.
6. `## Before Writing Code` — for any code-related prompt, append the standard footer:
   read spec folders `02`, `03` and `04` before writing code; error management must be
   followed; code must be DRY.

## 4. Trigger phrases

- "proofread prompt" / "next prompt" / any new prompt given for storage:
  apply sections 2 and 3 above, save the file, commit. Do not implement the prompt
  unless the user also asks for implementation.
- If the user asks for implementation as well, store the prompt first, then implement.

## 5. Files and links supplied with a prompt

- Images and other assets -> `assets/`.
- Specs -> `spec/`. The app spec goes in `spec/21/`.
- Spec folders `02` (coding guidelines), `03` (error management) and `04` (additional
  mandatory rules) must be read before writing any code.
- If the correct destination is unclear, ask the user instead of guessing.

## 6. Code rules referenced by every code prompt

- Read and understand `spec/02`, `spec/03`, `spec/04` before writing code.
- Error management must be followed.
- Code must be DRY.

## 7. Readme casing — root cause and standing rule

Root cause: the root readme was renamed `README.md` -> `readme.md`. Git tracks case,
but macOS/Windows filesystems and editor tabs do not, so both spellings appeared to
exist at once and the stale entry kept resurfacing.

Standing rule (non-negotiable):
- Exactly ONE readme at the repo root, named lowercase `readme.md`.
- Never create `README.md`, never keep both, never reintroduce an uppercase readme
  anywhere in the repo (including `src/routes/readme.md`).
- Any readme content additions are merged into the existing lowercase file, kept compact.
- If a duplicate ever reappears, delete the uppercase file and reopen the editor tab —
  it is a stale reference, not a real second file.

## 8. "Keep as is" prompts

When the user says to keep a prompt as is (no proofread, do not change anything):
- Store the prompt body VERBATIM under `## Prompt` — no filler-word removal, no rewording,
  no reordering, nothing added or removed.
- Only the "Actionable Items & Checklist and non-negotiable must follow" section may be
  enhanced: format as a markdown checklist, group into execution phases, sharpen wording
  into unambiguous instructions, drop literal duplicates. Never drop or invent a rule.
