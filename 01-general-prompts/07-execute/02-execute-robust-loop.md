# Execute Robust Loop (Resilient Multi-Agent)

- slug: execute-robust-loop
- status: active

## Prompt

# Execute Robust Loop (Resilient Multi-Agent)

## Goal

Your objective is to read pending tasks from the `.lovable/` folder, allocate small micro-portions of work to sub-agents, and execute them in a continuous self-loop. You must manage sub-agent crashes gracefully, strictly restrict concurrent agents to a maximum of 3, enforce file collision safety through a locking matrix, sanitize artifacts before commits, and ensure continuous execution without halting the pipeline. Avoid running any end-to-end tests that make live API calls.

## Phase 1: Load, Clean, & Prepare Tasks

1. **Check Git Status & Casing:** Fix git status first. The working tree must be clean. Confirm root readme is strictly lowercase `readme.md`.
2. **Git Ignore Temp:** Ensure `.lovable/temp/` is added to your project's `.gitignore` file.
3. **Garbage Collection:** Wipe any old, orphaned state files in `.lovable/temp/` from previous incomplete runs before starting fresh.
4. **Read the Queue & Waves:** Read `.lovable/plans/index.md` and load tasks from `.lovable/plans/pending/XX-<slug>.md`. Sequence them into Execution Waves (Wave 1: Schemas/DB/wrappers; Wave 2: Core logic; Wave 3: UI/docs).
5. **Dependency Check:** Do not start a task if its prerequisite tasks are not marked `Status: completed`.
6. **Micro-Tasking:** Break tasks down so each agent handles a simple, small micro-task (under 15 lines per function). Monolithic tasks with >7 steps must be decomposed into `.lovable/plans/subtasks/XX-<slug>/`.

## Phase 2: Resilient Allocation & Execution Loop

1. **Agent Limit (Strict):** Spawn a maximum of 2 to 3 sub-agents concurrently. Never exceed this limit.
2. **File Collision Locking Matrix (`active-locks.json`):**
   - Register active target files in `.lovable/temp/active-locks.json` before spawning an agent.
   - When assigning tasks in parallel, ensure the tasks touch **completely different files or components**. If two tasks share a dependency or file, sequence them sequentially to eliminate git merge conflicts.
3. **Pre-Flight Logging & Specific Titling:** Before spawning a sub-agent, you must:
   - Assign the sub-agent a highly specific title reflecting its exact task (e.g., `Refactoring Auth Service` or `Fixing DB Query Wrapper`). Do not use generic names. If an agent switches tasks, its title must change.
   - Write `.lovable/temp/XX-agent-state.md` documenting which sub-agent is running, its assigned micro-task, and instructions.
4. **Continuous Self-Looping:** Loop yourself to monitor sub-agent progress.
5. **Crash Recovery, Deadlocks & The 3-Strike Rollback Rule:**
   - **Deadlocks:** If an agent hangs without updating its state for an extended period, terminate it and retry.
   - **Revamp & Restart:** If an agent crashes, read its state from `.lovable/temp/`. Reason about the failure, fix the issue, and restart.
   - **3-Strike Rule & Automatic Rollback:** If a specific micro-task fails unit tests or crashes 3 times, **STOP retrying**. Automatically rollback the dirty files (`git checkout -- <modified_files>`), mark the task as `Status: blocked` in `plans/pending/`, and proceed to the next disjoint task.
   - **Persistent Failure Log:** Whenever a task hits 3 strikes, write the exact failure context, stack traces, and attempted fixes to `.lovable/memory/last-failure.md` and `.lovable/issues/`. When the user later says "continue", read this file first to resume recovery.
6. **End-to-End Tests Ban:** Do not run end-to-end tests that make live API calls. Only run local, isolated unit tests.

## Phase 3: Code Quality & Commit Fix (Non-Negotiable)

While executing tasks, you and your agents MUST adhere to these strict coding guidelines:
- **Code Review & Logging:** Follow guidelines in `spec/02-coding-guidelines/`, `spec/03-error-manage/`, and `spec/04-database-conventions/`. Use automated query wrappers for failure logging.
- **No Magic Strings/Numbers:** Do not introduce any magic strings or numbers anywhere unless explicitly for the logger.
- **TypeScript Enums:** Never use string union types (e.g., `"pass" | "fail"`). You must use Enums ending with the suffix `Type` (e.g., `StatusType`).
- **Explicit Booleans:** Always use explicit boolean state checks (e.g., `response.isFail`). Never invert success booleans (e.g., `!response.isSuccess`).
- **DRY Code:** Code must be DRY. Reuse constants and wrappers.

## Phase 4: Memory Update & File Moving

As tasks are completed, you must update the memory structure:
1. **Move on Success:** When a task completes successfully, use `mv` to move the file from `.lovable/plans/pending/` to `.lovable/plans/completed/`.
2. **Status Flip:** Flip `Status: pending` to `Status: completed` inside the moved file.
3. **Update Indexes:** Immediately update `.lovable/plans/index.md` to reflect the completed status and the new file location.
4. **Clear Temp & Locks:** Once an agent successfully finishes its task and you have verified it, remove its entry from `.lovable/temp/active-locks.json` and delete its state file from `.lovable/temp/`.

## Phase 5: End-of-Loop Commit Fix, Artifact Purge & Delivery

At the end of *every single iteration* of your execution loop (when a batch of tasks completes), execute this Commit Fix before continuing:
1. **Artifact Sanitizer:** Audit staged files and working tree. Purge unapproved artifact zip archives, temporary scratch files, or test outputs before committing.
2. **Run Tests:** Run local unit tests (NO live API end-to-end tests). Fix failures before proceeding.
3. **Lovable Git History Guard:** Group similar code changes into a single commit with a clear, descriptive message. Never rewrite published git history (no force push, no rebasing, no squash) to protect Lovable synchronization.
4. **Push:** Push to the remote Git repository.
5. **List Completed Tasks:** Explicitly list out all the tasks that were successfully completed during that run.

---

## Pre-Reply / Loop Checklist (Must verify every loop iteration)

- [ ] `.lovable/temp/` verified in `.gitignore` and orphaned state garbage-collected.
- [ ] Dependencies and prerequisites verified before starting tasks.
- [ ] Parallel assignments verified disjoint using `.lovable/temp/active-locks.json`.
- [ ] Maximum of 2-3 sub-agents spawned concurrently with specific titling.
- [ ] Pre-flight state written to `.lovable/temp/` for every agent before it started.
- [ ] 3-Strike rollback honored: failed changes reverted via `git checkout` and logged to `last-failure.md`.
- [ ] Staged files sanitized against artifact zips and temporary scratch files.
- [ ] No live-API end-to-end tests executed.
- [ ] Completed tasks `mv`'d to `plans/completed/` and `.lovable/plans/index.md` updated.
- [ ] Code adheres to explicit booleans, `Type` suffixed Enums, and error wrapper rules.
- [ ] Fast-forward commits created and pushed without rewriting Git history.
- [ ] Completed tasks listed out explicitly in the response.

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.
