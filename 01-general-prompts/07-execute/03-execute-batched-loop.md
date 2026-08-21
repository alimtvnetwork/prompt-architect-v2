# Execute Batched Loop (3 Agents, Chunked Commits)

- slug: execute-batched-loop
- status: active

Run if again if said: go, continue, or next

## Prompt

# Execute Batched Loop (3 Agents, Chunked Commits)

## Goal

Your objective is to execute pending tasks from `.lovable/plans/pending/` using a strictly batched multi-agent loop. You must use exactly 3 sub-agents, assign small micro-task chunks per agent, enforce file collision safety through a locking matrix, sanitize artifacts before commits, handle crashes via the `.lovable/temp/` folder, and push chunked commits to Git without failure. At the end of every loop, you must explicitly list task statistics in your output window.

## Phase 1: Pre-Flight & Gitignore Enforcement (Non-Negotiable)

1. **Check Git Status & Casing:** The working tree must be clean. Confirm root readme is strictly lowercase `readme.md`.
2. **Enforce Gitignore:** Verify that `.lovable/temp/` is explicitly added to `.gitignore`. This folder is for crash identification and lockfiles and must never be committed.
3. **Garbage Collection:** Wipe any orphaned state files in `.lovable/temp/` from previous runs.
4. **Execution Waves:** Group pending tasks into Execution Waves (Wave 1: DB schemas & query wrappers; Wave 2: Business logic & services; Wave 3: UI & docs).

## Phase 2: Allocation & Execution (Strict 3x3 Rule & Locking Matrix)

1. **Strict Limits:** Spawn up to 3 sub-agents to run in parallel.
2. **Chunking Micro-Tasks:** Each agent is assigned a chunk of simple, small micro-tasks (under 15 lines per function) to complete sequentially in its own context. Tasks exceeding 7 steps must be decomposed into subtasks.
3. **File Collision Locking Matrix (`active-locks.json`):**
   - Register active target files in `.lovable/temp/active-locks.json`.
   - Ensure parallel tasks touch completely disjoint files to prevent Git merge conflicts.
4. **Temp Folder Logging & Specific Titling (Mandatory):** Before an agent starts, you must:
   - Spawn the sub-agent with a highly specific title reflecting its exact task (e.g., `Refactoring Auth Service` or `Fixing DB Query Wrapper`). Do not use generic names. If an agent switches chunks, its title must change.
   - Log its assigned chunk of tasks to `.lovable/temp/XX-agent-state.md`.
5. **Crash Identification & 3-Strike Rollback:**
   - If an agent fails or crashes, inspect its state in `.lovable/temp/`.
   - If an agent fails 3 times, automatically revert dirty changes (`git checkout -- <files>`), log root cause to `.lovable/memory/last-failure.md` and `.lovable/issues/`, and restart a new agent for the next disjoint chunk.

## Phase 3: Code Quality (Non-Negotiable)

While executing tasks, you and your agents MUST adhere to these strict coding guidelines:
- Follow guidelines in `spec/02-coding-guidelines/`, `spec/03-error-manage/`, and `spec/04-database-conventions/`.
- **No Magic Strings/Numbers:** Do not introduce any magic strings or numbers anywhere unless explicitly for the logger.
- **TypeScript Enums:** Never use string union types (e.g., `"pass" | "fail"`). You must use Enums ending with the suffix `Type` (e.g., `StatusType`).
- **Explicit Booleans:** Always use explicit boolean state checks (e.g., `response.isFail`). Never invert success booleans (e.g., `!response.isSuccess`).
- **DRY Code:** Code must be DRY. Reuse constants and wrappers.

## Phase 4: Chunked Delivery, Artifact Purge & File Moving

When a chunk of tasks is completed by the agents, do the following before starting the next loop iteration:
1. **Move Files:** `mv` the completed task files from `.lovable/plans/pending/` to `.lovable/plans/completed/`.
2. **Status Flip:** Open the moved files and change `Status: pending` to `Status: completed`.
3. **Update Indexes:** Update `.lovable/plans/index.md` to reflect the new file locations.
4. **Artifact Sanitizer:** Audit staged files. Purge unapproved artifact zip archives, temporary scratch files, or test outputs before committing.
5. **Lovable Git History Guard:** Run local tests (no live API calls). Commit code with a clear descriptive message. Never rewrite published git history (no force push, no rebasing, no squash). Push to git cleanly without failure.

## Phase 5: Output Window Stats (Mandatory)

Every time you return a response or complete a loop iteration, explicitly output the following statistics:
- **Tasks Done (This Chunk):** [Number of tasks completed]
- **Total Completed:** [Total number of tasks in `.lovable/plans/completed/`]
- **Total Pending:** [Number of tasks remaining in `.lovable/plans/pending/`]
- **Remaining Tasks List:** [List the specific filenames/slugs of the tasks remaining]

---

## Pre-Reply / Loop Checklist (Must verify every loop iteration)

- [ ] `.gitignore` verified to exclude `.lovable/temp/` and garbage collection executed.
- [ ] Strictly up to 3 agents spawned, each assigned disjoint files tracked in `.lovable/temp/active-locks.json`.
- [ ] Pre-flight state written to `.lovable/temp/` for every agent.
- [ ] 3-Strike rollback honored with `git checkout` and logged to `last-failure.md`.
- [ ] Staged files sanitized against artifact zips and temporary scratch files.
- [ ] No end-to-end live API tests executed.
- [ ] Completed task files `mv`'d and `plans/index.md` updated.
- [ ] Fast-forward commit created and pushed without rewriting Git history.
- [ ] Output window explicitly lists "Done", "Pending", and remaining task names.

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.
