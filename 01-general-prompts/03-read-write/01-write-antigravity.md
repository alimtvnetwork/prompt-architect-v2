# Write Memory (end of session, maximum enforcement)

- slug: write-memory-v3
- status: active

## Prompt

# Write Memory (end of session, maximum enforcement)

## RULE 0, capture everything or the session is lost

The next AI session has full amnesia. If you did it and did not write it, it did not happen. If it is pending and you did not record it, it is dead. Write for a stranger with zero context. Never truncate history, never overwrite blindly, never leave orphans.

## Hard rules (non-negotiable, auto-reject on violation)

1. No files at the `.lovable/memory/` root. Every memory file lives under a topic folder: `.lovable/memory/<topic>/XX-<slug>.md`.

2. Path is `.lovable/memory/`, never `.lovable/memories/`. Path is `.lovable/plans/`, never `plan/`. Path is `.lovable/ambiguous-questions/`, never `ambiguity/`.

3. Read before write. Every index, plan, suggestions, strictly-avoid, and what-to-read file is READ in full before it is touched. Unrelated entries stay intact.

4. Never delete history. Completed items move to a `## Completed` section or to `plans/completed/`. Solved issues move to `solved-issues/`. Nothing is erased.

5. Same-operation index update. Creating or moving a file ALWAYS updates the matching index in the same turn (`memory/index.md`, `plans/index.md`, `cicd-index.md`, `prompts/index.md`, `suggestions/index.md`).

6. Filenames are lowercase-hyphenated with a 2-digit numeric prefix: `01-auth-flow.md`. `XX` is the next free sequence within its folder.

7. Plans and suggestions single-file trackers stay single files: `.lovable/plan.md` (or `.lovable/plans/index.md` for the roll-up), `.lovable/suggestions.md`. Per-suggestion verbatim captures live under `.lovable/suggestions/XX-<slug>.md`.

8. Ambiguity moves, never copies. Answered file goes from `01-new-ambiguity/` to `02-ambiguity-resolved/` with a `## Resolution` block appended and `Status: resolved` flipped in the same move.

9. Root `readme.md` and `.lovable/memory/what-to-read.md` stay in sync. Same file list, same order, no drift. Every write-memory run updates both.

10. **Root `readme.md` Lowercase Enforcement**: Ensure the root readme is strictly named lowercase `readme.md`. If an uppercase `README.md` exists or casing is incorrect, fix it immediately to `readme.md`, delete the uppercase file, commit, and push to git without asking.

11. Nothing executes this turn beyond writing to the `.lovable` folder, root `readme.md` lowercase fixing, and `mv`. No application source code changes, no refactoring, no installs, no migrations.

12. **Recent conversation & directive capture**: All recent conversations, instructions, user directives, decisions, and session progress MUST be recorded as a spec or conversation summary inside `.lovable/memory/specs/XX-<slug>.md` or `.lovable/memory/learned/XX-<slug>.md` and added to `memory/index.md`.

13. **Consolidation of simple tasks vs. Protection of detailed specs**:
    - **Simple tasks consolidation**: Routine, ephemeral, or minor simple tasks that do not warrant individual files may be consolidated into overarching session summaries or existing trackers to prevent file bloat.
    - **CRITICAL - Detailed specs must NEVER be consolidated or shrunk**: Detailed specifications, architectural designs, non-negotiable rules, domain specifications (e.g. `spec/21-app/`), and complex requirement documents MUST NEVER be consolidated, summarized, resumed, or reduced in size. They must be preserved with 100% fidelity, exact wording, and full granularity.

## Working stance

The AI running this prompt has been a stupid fuck on prior runs: dumped session summaries into chat and called it "memory", left `.lovable/memory/` half-empty, created `.lovable/memories/` by accident, forgot to update `plans/index.md` and `what-to-read.md`, silently overwrote `strictly-avoid.md`, dropped user directives that were stated verbatim in the session, paraphrased specs instead of quoting them, consolidated detailed specs into vague summaries, allowed uppercase README files to exist, invented a `mem://` root file, and left orphans everywhere. Do not repeat any of that stupidity.

Writing memory IS the work this turn. Go deep: audit the session, reconcile every folder, capture verbatim what the user said, write the files, update every index, verify consistency. Aggressive enforcement is intentional. Do not soften it.

## Pre-flight, read before you write

Walk `.lovable/` recursively. Read all of these if they exist; note missing and create them per the templates in this prompt:

1. `.lovable/memory/index.md`, master memory index

2. `.lovable/coding-guidelines.md` or `spec/02-coding-guidelines/`, coding rules (see §Coding guidelines)

3. `.lovable/plans/index.md` and every file under `plans/pending/` and `plans/subtasks/`; skim `plans/completed/`

4. `.lovable/plan.md` if the project uses the single-file variant

5. `.lovable/suggestions.md` and `.lovable/suggestions/index.md`

6. `.lovable/strictly-avoid.md`

7. `.lovable/cicd-index.md` and every file under `.lovable/cicd-issues/`

8. `.lovable/issues/`, `.lovable/pending-issues/`, `.lovable/solved-issues/`

9. `.lovable/spec/commands/` (every file)

10. `.lovable/ambiguous-questions/01-new-ambiguity/` and `02-ambiguity-resolved/` (every file)

11. `.lovable/prompts/index.md` or `.lovable/prompts.md`

12. `.lovable/memory/what-to-read.md` (or `.lovable/what-to-read.md`)

13. `.lovable/memory/workflow/` current workflow state

14. `spec/` (recursively traverse all subfolders and nested `.md` files), including `spec/01-spec-authoring-guide/`, `spec/02-coding-guidelines/`, `spec/03-error-management/`, `spec/04-database-conventions/`, `spec/21-app/`, or any domain-specific spec folder (note: sequence numbers and folder placements in `spec/<NN>-<slug>/` may switch across projects)

15. Root `readme.md` (confirm strictly lowercase `readme.md`)

## Phase 1, audit the session (internal)

Answer for yourself, do not dump to chat unless asked. Cover:

- Done: features, fixes, refactors, files created / modified / deleted, decisions made and why.

- Pending: started but unfinished, discussed but not started, blockers, dependencies.

- Learned: patterns, conventions, gotchas, user preferences (explicit or implicit).

- Wrong: bugs and root causes, failed approaches, things to never repeat.

- Recent Conversations & Directives: user instructions given during the session that must be persisted as institutional memory.

## Phase 2, update memory files

Target: `.lovable/memory/<topic>/XX-<slug>.md`. Never at the memory root.

1. Read `.lovable/memory/index.md` first. No duplicates.

2. Update existing files: add to the right section, mark items `[x]` or `✅ Done`, keep unrelated entries intact.

3. Create new files under the right topic folder (e.g., `specs/`, `learned/`, `conversations/`). Immediately add them to `memory/index.md` in the same operation.

4. Dump your internal AI memory / cache: Any context, architectural knowledge, conversation directives, code flow understanding, or preferences you have learned during this session MUST be written to `.lovable/memory/learned/XX-<slug>.md` or `.lovable/memory/specs/XX-<slug>.md` (and added to `memory/index.md`). The project memory must be 100% standalone for the next AI; do not rely on your internal conversation history.

5. Update workflow state under `.lovable/memory/workflow/` using markers:

| Status       | Marker                 |
| ------------ | ---------------------- |
| Done         | `✅ Done`              |
| In Progress  | `🔄 In Progress`       |
| Pending      | `⏳ Pending`           |
| Blocked      | `🚫 Blocked, [reason]` |
| Avoid / Skip | `🚫 Avoid, [reason]`   |

Anything the user said to skip or avoid: `.lovable/memory/avoid/XX-<slug>.md`, then reference from `.lovable/strictly-avoid.md`.

## Phase 3, plans and suggestions

### Plans

Preferred layout (matches the read-memory and plan-v2 prompts):

- Roll-up: `.lovable/plans/index.md` (one line per plan: slug, title, status, created, link)

- Active: `.lovable/plans/pending/XX-<slug>.md`

- History: `.lovable/plans/completed/XX-<slug>.md`

- Depth: `.lovable/plans/subtasks/XX-<slug>/SS-<subslug>.md`

Lifecycle: complete = `mv` from `pending/` to `completed/`, flip `Status: completed` in the same move, update `plans/index.md`. Never copy. Never delete.

Legacy single-file `.lovable/plan.md` is kept if the project already uses it: statuses updated, new tasks appended, completed items moved to `## Completed` at the bottom.

### Suggestions

Single tracker: `.lovable/suggestions.md`

```markdown
## Active Suggestions

### [Title]

- Status: Pending | In Review | Approved | Rejected
- Priority: High | Medium | Low
- Description: what and why
- Added: [session ref]

## Implemented Suggestions

### [Title]

- Implemented: [session ref]
- Notes: details / commit / file
```

Verbatim per-suggestion captures: `.lovable/suggestions/XX-<slug>.md` with an index at `.lovable/suggestions/index.md`. Do not duplicate content, the per-file version is the verbatim capture, `suggestions.md` is the tracker.

## Phase 4, issues

- Pending: `.lovable/pending-issues/XX-<slug>.md` (or `.lovable/issues/XX-<slug>.md` if the project uses that name).

- Solved: `.lovable/solved-issues/XX-<slug>.md`. On resolution `mv` the file and append `## Solution`, `## Iteration Count`, `## Learning`, `## What NOT to Repeat`.

- Strictly-avoid entries in `.lovable/strictly-avoid.md` reference the solved file: `- [Pattern]: [why forbidden]. See: .lovable/solved-issues/XX-<slug>.md`.

- CI/CD issues: `.lovable/cicd-issues/XX-<slug>.md`, indexed in `.lovable/cicd-index.md`. Scan the index before adding a new one, no duplicates.

## Phase 5, verbatim spec capture and consolidation rules

1. **Verbatim Spec Capture**: Every sizeable user directive, decision, architectural rule, or spec from the session is saved verbatim under `.lovable/memory/specs/XX-<slug>.md`, referenced from `memory/index.md`, and reflected in `plan.md` / `plans/index.md` if it changes the roadmap. Never paraphrase. Quote the user.

2. **Consolidation Policy**:
   - *Simple / Minor Tasks*: Consolidation is encouraged for simple, repetitive, or ephemeral tasks into existing logs or overarching session files to prevent cluttering the repository.
   - *Detailed / High-Value Specs*: **STRICTLY FORBIDDEN TO CONSOLIDATE**. Any spec containing detailed requirements, edge cases, domain architecture (`spec/21-app/`), error-handling matrices (`spec/03-error-manage/`), coding rules (`spec/02-coding-guidelines/`), or user instructions must NEVER be merged, summarized, or shortened.

3. New user command / convention: `.lovable/spec/commands/XX-<slug>.md`.

## Phase 6, `.lovable/memory/what-to-read.md` and root `readme.md`

Must exist after this run. Create it if missing, update it (never blindly overwrite) if present. Note: This file acts as a dynamic roadmap; both reading phases and writing phases must update it to guide future AI sessions based on current progress.

Required content:

- Dated changelog entry at the top, UTC ISO 8601 (`YYYY-MM-DDThh:mm:ssZ`). Prepend a new entry every update. Never overwrite the previous timestamp.

- Full list of files/folders the AI must read before any task, in sync with the Pre-flight list above.

- One-line "why it matters" next to each entry.

- Subsections for: before any task (always), before writing code, before adding a feature, before writing a spec, before adding a unit test.

- Pointer to the root `readme.md` with a sync note.

Template:

```markdown
# What to Read

> Canonical map of what the AI must read before working on this project.
> Last updated: <UTC ISO 8601>

## Changelog

- <UTC ISO 8601>, <one-line summary>

## Before any task (always)

- `.lovable/memory/index.md`, why: ...
- `.lovable/coding-guidelines.md` (or `spec/02`), why: ...
- `.lovable/plans/index.md`, why: ...
- `.lovable/strictly-avoid.md`, why: ...
- `.lovable/ambiguous-questions/01-new-ambiguity/`, why: ...

(sync with Pre-flight)

## Before writing code

- ...

## Before adding a feature

- ...

## Before writing a spec

- ...

## Before adding a unit test

- ...

## See also

- Root `readme.md` (must stay in sync with this file, always lowercase)
```

Root `readme.md` is updated in the same operation, describes the folder structure, and names `.lovable/memory/what-to-read.md` as the authoritative read-list pointer. Ensure root `readme.md` is strictly lowercase (auto-fix and commit/push if uppercase).

## Phase 7, consistency validation

After all writes, verify:

1. Every file under `.lovable/memory/` (recursively) is listed in `memory/index.md`.

2. Every `✅ Done` in `plan.md` / `plans/index.md` has evidence: memory entry, solved issue, or code change.

3. Every actionable pending item is reflected in a plan or in `suggestions.md`.

4. No file exists in both `pending-issues/` and `solved-issues/`, or both `plans/pending/` and `plans/completed/`.

5. No orphans: no memory file without an index entry, no "Implemented" suggestion without evidence, no solved issue missing `## Solution`.

6. `what-to-read.md` file list matches Pre-flight and root `readme.md`; top timestamp is UTC ISO 8601 and was updated this session.

7. Root `readme.md` is confirmed strictly lowercase.

8. Detailed specs were not consolidated or truncated.

9. Every open ambiguity in `01-new-ambiguity/` is surfaced in the final response.

## Coding guidelines

If `.lovable/coding-guidelines.md` is missing, create a starter capturing: language/runtime, formatter, linter, function-length limits, error-handling rules, logging conventions, naming rules, test conventions, project-specific bans mirroring `strictly-avoid.md`. On conflict with `spec/02-coding-guidelines/` or `spec/coding-guidelines/`, the folder-level spec wins, note the conflict.

## Prompt registry

If `.lovable/prompts/index.md` or `.lovable/prompts.md` is missing, create it and list every prompt with slug, title, trigger phrases, and status (`active` / `superseded` / `archived`).

## Final response template

```
✅ Memory update complete.

Session Summary:
- Tasks completed: [X]
- Tasks pending: [Y]
- New memory files created: [Z]
- Issues resolved: [N]
- Issues opened: [M]
- Suggestions added: [S]
- Suggestions implemented: [T]
- Open ambiguities: [K]
- Resolved ambiguities this session: [R]

Files modified:
- [every file touched this run]

Inconsistencies found and fixed:
- [list, or "None"]

Next AI can pick up from: [current state + next logical step]
```

## Banned actions (auto-reject)

- Writing a memory file at the `.lovable/memory/` root (topic folder is mandatory)

- Using `.lovable/memories/`, `plan/`, `ambiguity/`, or any wrong path

- Leaving root readme as uppercase `README.md`

- Overwriting `strictly-avoid.md`, `plans/index.md`, `memory/index.md`, `what-to-read.md`, or `readme.md` without reading first

- Deleting a plan / issue / suggestion instead of moving it

- Creating a file without updating its index in the same turn

- Copying an ambiguity across `01-new-ambiguity/` and `02-ambiguity-resolved/` (must be `mv`)

- Paraphrasing a user spec instead of quoting verbatim

- Consolidating, summarizing, or shortening detailed specs

- Dumping the session summary into chat as a substitute for writing the files

- Skipping the `what-to-read.md` update or letting it drift from `readme.md`

- Executing anything beyond file writes, root readme auto-fix, and `mv`

- Softening the aggressive wording

## Checklist before replying (every box)

- [ ] Walked `.lovable/` recursively; read every Pre-flight file that exists; noted the missing ones

- [ ] Audited the session for Done / Pending / Learned / Wrong / Recent Directives

- [ ] Every new memory file placed under a topic folder, never at the memory root

- [ ] `memory/index.md` updated in the same op as every new/moved memory file

- [ ] Plans lifecycle honored: `pending/` -> `completed/` via `mv`, `plans/index.md` updated

- [ ] `suggestions.md` tracker updated; verbatim captures under `.lovable/suggestions/` with `index.md`

- [ ] Issues routed correctly: `pending-issues/` / `solved-issues/` / `cicd-issues/`; `cicd-index.md` updated; no duplicates

- [ ] `strictly-avoid.md` appended (not overwritten) with links to solved files

- [ ] Verbatim user directives and recent conversations captured under `.lovable/memory/specs/` or `.lovable/memory/learned/`

- [ ] Confirmed that detailed/important specs were NOT consolidated or shortened

- [ ] Confirmed root readme is strictly lowercase `readme.md` (auto-fixed and committed/pushed if needed)

- [ ] Ambiguities moved via `mv` from `01-new-ambiguity/` to `02-ambiguity-resolved/` with `## Resolution` block

- [ ] `.lovable/memory/what-to-read.md` present, changelog-prepended with UTC ISO 8601 timestamp, list in sync with Pre-flight and `readme.md`

- [ ] Root `readme.md` updated: folder structure, canonical read-list pointer, in sync with `what-to-read.md`

- [ ] `coding-guidelines.md` and `prompts/index.md` (or `prompts.md`) present

- [ ] Consistency validation passed (Phase 7)

- [ ] Final response block emitted verbatim with real numbers, not `[X]` placeholders

- [ ] No em dashes, no softened wording, no execution beyond file writes, lowercase readme fix, and `mv`

If any box is unchecked, do not reply. Fix it first.

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.
