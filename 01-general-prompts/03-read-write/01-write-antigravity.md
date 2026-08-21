# Write Antigravity (Write Memory)

- slug: write-antigravity
- status: active

## Prompt

# Write Memory (end of session, maximum enforcement)

## Goal

Persist what happened this turn so the next AI knows everything without guessing. Every decision, plan change, unresolved ambiguity, newly discovered pattern, and fixed bug must be written to `.lovable/` before this turn ends.

Memory in chat is lost the moment the turn finishes. Memory in `.lovable/` is permanent. If you did not write it down, it did not happen.

## Hard rules (non-negotiable, auto-reject on violation)

1. Folder is `.lovable/memory/`, NEVER `.lovable/memories/` or `memories/`. A single file written to `memories/` is an immediate failure.

2. Every new memory file under `.lovable/memory/` MUST be registered in `.lovable/memory/index.md` in the same operation.

3. Every plan added, moved, or completed MUST update `.lovable/plans/index.md` in the same operation.

4. Ambiguity files are NEVER duplicated. Open questions go to `.lovable/ambiguous-questions/01-new-ambiguity/01-<slug>.md`. When answered, the file is MOVED (`mv`) to `.lovable/ambiguous-questions/02-ambiguity-resolved/01-<slug>.md` with a `## Resolution` block appended. Never copy. Never leave a resolved question in `01-new-ambiguity/`.

5. Never overwrite `.lovable/strictly-avoid.md`. Append only. If a rule was already there, do not duplicate it.

6. When updating existing files (especially indexes, `strictly-avoid.md`, `suggestions.md`), preserve all unrelated content. No silent truncation.

7. Output the completion block with real, audited numbers. Placeholders like `[X]` or `[N]` in the final response are auto-reject.

8. Ambiguity moves, never copies. Answered file goes from `01-new-ambiguity/` to `02-ambiguity-resolved/` with a `## Resolution` block appended and `Status: resolved` flipped in the same move.

9. Root `readme.md` and `.lovable/memory/what-to-read.md` stay in sync. Same file list, same order, no drift. Every write-memory run updates both.

10. **Root `readme.md` Lowercase Enforcement**: Ensure the root readme is strictly named lowercase `readme.md`. If an uppercase `README.md` exists or casing is incorrect, fix it immediately to `readme.md`, delete the uppercase file, commit, and push to git without asking.

11. Nothing executes this turn beyond writing to the `.lovable` folder, root `readme.md` lowercase fixing, and `mv`. No application source code changes, no refactoring, no installs, no migrations.

12. **Recent conversation & directive capture**: All recent conversations, instructions, user directives, decisions, and session progress MUST be recorded as a spec or conversation summary inside `.lovable/memory/specs/01-<slug>.md` or `.lovable/memory/learned/01-<slug>.md` and added to `memory/index.md`.

13. **Pending Tasks Single Source of Truth**: All active plans and pending tasks are consolidated strictly under `.lovable/plans/pending/01-<slug>.md` (with two-digit sequence prefixes `01-`, `02-`, etc.) and `.lovable/plans/subtasks/01-<slug>/01-<subslug>.md`.

14. **Consolidation of simple tasks vs. Protection of detailed specs**:
    - **Simple tasks consolidation**: Routine, ephemeral, or minor simple tasks that do not warrant individual files may be consolidated into overarching session summaries or existing trackers to prevent file bloat.
    - **CRITICAL - Detailed specs must NEVER be consolidated or shrunk**: Detailed specifications, architectural designs, non-negotiable rules, domain specifications (e.g. `spec/21-app/`), and complex requirement documents MUST NEVER be consolidated, summarized, resumed, or reduced in size. They must be preserved with 100% fidelity, exact wording, and full granularity.

15. **Anti-Hallucination & Clarifying Questions**: If any file, spec, or user intent is ambiguous or missing, the AI MUST NOT guess or hallucinate. It must ask clarifying questions or record an open ambiguity in `01-new-ambiguity/01-<slug>.md`.

## Working stance

The AI running this prompt has been a stupid fuck on prior runs: dumped session summaries into chat and called it "memory", left `.lovable/memory/` half-empty, created `.lovable/memories/` by accident, forgot to update `plans/index.md` and `what-to-read.md`, silently overwrote `strictly-avoid.md`, dropped user directives that were stated verbatim in the session, paraphrased specs instead of quoting them, consolidated detailed specs into vague summaries, allowed uppercase README files to exist, invented a `mem://` root file, and left orphans everywhere. Do not repeat any of that stupidity.

Writing memory IS the work this turn. Go deep: audit the session, reconcile every folder, capture verbatim what the user said, write the files, update every index, verify consistency. Aggressive enforcement is intentional. Do not soften it.

## Pre-flight, read before you write

Walk `.lovable/` recursively. Read all of these if they exist; note missing and create them per the templates in this prompt:

1. `.lovable/memory/index.md`, master memory index
2. `.lovable/coding-guidelines.md` or `spec/02-coding-guidelines/`, coding rules (see §Coding guidelines)
3. `.lovable/plans/index.md` and every file under `plans/pending/` (`01-<slug>.md`) and `plans/subtasks/`; skim `plans/completed/`
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
14. `spec/` (recursively traverse all subfolders and nested `.md` files), including `spec/01-spec-authoring-guide/`, `spec/02-coding-guidelines/`, `spec/03-error-manage/`, `spec/04-database-conventions/`, `spec/21-app/`, or any domain-specific spec folder (note: sequence numbers and folder placements in `spec/<NN>-<slug>/` may switch across projects)
15. Root `readme.md` (confirm strictly lowercase `readme.md`)

## Phase 1, audit the session (internal)

Answer for yourself, do not dump to chat unless asked. Cover:
- Done: features, fixes, refactors, files created / modified / deleted, decisions made and why.
- Pending: started but unfinished, discussed but not started, blockers, dependencies.
- Learned: patterns, conventions, gotchas, user preferences (explicit or implicit).
- Avoid: mistakes made, dead ends hit, patterns that failed, user corrections.
- Ambiguities: questions that came up, questions answered, questions still blocking.
- Suggestions: ideas discussed that are not yet plans.
- User commands: new CLI patterns or shorthand the user used or requested.

## Phase 2, move completed plans

For every plan finished this turn:

```sh
mv .lovable/plans/pending/01-<slug>.md .lovable/plans/completed/01-<slug>.md
```

Inside the moved file, edit:
```diff
- Status: pending
+ Status: completed
```

Then edit `.lovable/plans/index.md` so the table lists the file under `completed/` with status `completed`. Never delete a plan; the completed folder is your changelog.

## Phase 3, move resolved ambiguities

For every ambiguity answered by the user this turn:

```sh
mv .lovable/ambiguous-questions/01-new-ambiguity/01-<slug>.md .lovable/ambiguous-questions/02-ambiguity-resolved/01-<slug>.md
```

Inside the moved file, append:
```markdown
## Resolution

- **Answered on**: YYYY-MM-DD
- **Decision**: <verbatim user answer or concise summary of the decision>
- **Applied solution**: <file and line where this was implemented>
```

Flip header metadata:
```diff
- Status: open
+ Status: resolved
```

Resolved ambiguities are binding decisions. You will never ask about them again.

## Phase 4, issues and CI/CD logging

- General bugs: `.lovable/issues/01-<slug>.md`.
- Solved bugs: `.lovable/solved-issues/01-<slug>.md` with root cause and fix diff.
- Strictly-avoid entries in `.lovable/strictly-avoid.md` reference the solved file: `- [Pattern]: [why forbidden]. See: .lovable/solved-issues/01-<slug>.md`.
- CI/CD issues: `.lovable/cicd-issues/01-<slug>.md`, indexed in `.lovable/cicd-index.md`. Scan the index before adding a new one, no duplicates.

## Phase 5, verbatim spec capture and consolidation rules

1. **Verbatim Spec Capture**: Every sizeable user directive, decision, architectural rule, or spec from the session is saved verbatim under `.lovable/memory/specs/01-<slug>.md`, referenced from `memory/index.md`, and reflected in `plan.md` / `plans/index.md` if it changes the roadmap. Never paraphrase. Quote the user.
2. **Consolidation Policy**:
   - *Simple / Minor Tasks*: Consolidation is encouraged for simple, repetitive, or ephemeral tasks into existing logs or overarching session files to prevent cluttering the repository.
   - *Detailed / High-Value Specs*: **STRICTLY FORBIDDEN TO CONSOLIDATE**. Any spec containing detailed requirements, edge cases, domain architecture (`spec/21-app/`), error-handling matrices (`spec/03-error-manage/`), coding rules (`spec/02-coding-guidelines/`), or user instructions must NEVER be merged, summarized, or shortened.
3. New user command / convention: `.lovable/spec/commands/01-<slug>.md`.

## Phase 6, `.lovable/memory/what-to-read.md` and root `readme.md`

Must exist after this run. Create it if missing, update it (never blindly overwrite) if present. Note: This file acts as a dynamic roadmap; both reading phases and writing phases must update it to guide future AI sessions based on current progress.

Prepend a new entry to the `## Changelog` section:
```markdown
- YYYY-MM-DDTHH:MM:SSZ, <one-sentence summary of what changed this turn>
```

Sync root `readme.md` with `.lovable/memory/what-to-read.md`. Ensure root `readme.md` is strictly lowercase (auto-fix and commit/push if uppercase).

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

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.
