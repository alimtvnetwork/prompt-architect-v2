# Execute Robust Loop (Resilient Multi-Agent)

- slug: execute-robust-loop
- status: active

## Prompt

# Execute Robust Loop (Resilient Multi-Agent)

## Goal

/goal Read all pending tasks from `.lovable/`, allocate small micro-portions of work to sub-agents, and execute them in a continuous self-loop. Manage sub-agent crashes gracefully, enforce file collision safety, sanitize artifacts before commits, and ensure the pipeline runs without halting until the queue is empty.

/learn Capture every pattern, convention, fix, and correction discovered during execution into `.lovable/memory/learned/01-<slug>.md` and `.lovable/strictly-avoid.md`. Never repeat a mistake that was logged.

## Non-Negotiable Rules (Auto-Reject on Violation)

1. Maximum 3 sub-agents may run concurrently at any time. Never exceed this limit.
2. No end-to-end tests that make live API calls. Only run local, isolated unit tests.
3. Violation of any rule below is auto-reject on the same tier as RULE 0.

## Anti-Hallucination Rules

- If a spec file, folder, or task is missing or ambiguous, do NOT guess or invent a rule.
- Ask a clarifying question or log an open ambiguity in `.lovable/ambiguous-questions/01-new-ambiguity/01-<slug>.md` before proceeding.
- Never invent step counts. Read the actual files and count from them.

---

## Phase 1: Load, Clean, & Prepare Tasks

1. Check git status first. The working tree must be clean. Confirm root readme is strictly lowercase `readme.md`.
2. Ensure `.lovable/temp/` is added to your project's `.gitignore` file.
3. Wipe any old, orphaned state files in `.lovable/temp/` from previous incomplete runs before starting fresh.
4. Read `.lovable/plans/index.md` and load tasks from `.lovable/plans/pending/XX-<slug>.md`. Sequence them into Execution Waves:
   - Wave 1: Schemas, DB, and query wrappers
   - Wave 2: Core logic
   - Wave 3: UI and documentation
5. Do not start a task if its prerequisite tasks are not marked `Status: completed`.
6. Break tasks down so each agent handles a simple, small micro-task (under 15 lines per function). Monolithic tasks with more than 7 steps must be decomposed into `.lovable/plans/subtasks/XX-<slug>/`.

---

## Phase 2: Resilient Allocation & Execution Loop

1. Agent limit (strict):
   - Spawn a maximum of 2 to 3 sub-agents concurrently. Never exceed this limit.

2. File collision locking matrix (`active-locks.json`):
   - Register active target files in `.lovable/temp/active-locks.json` before spawning an agent.
   - When assigning tasks in parallel, ensure the tasks touch completely different files or components.
   - If two tasks share a dependency or file, sequence them sequentially to eliminate git merge conflicts.

3. Pre-flight logging and specific titling:
   - Before spawning a sub-agent, assign it a highly specific title reflecting its exact task (e.g., `Refactoring Auth Service` or `Fixing DB Query Wrapper`). Do not use generic names. If an agent switches tasks, its title must change.
   - Write `.lovable/temp/XX-agent-state.md` documenting which sub-agent is running, its assigned micro-task, and instructions.

4. Continuous self-looping:
   - Loop yourself to monitor sub-agent progress.
   - Do not stop until the queue is empty.

5. Crash recovery, deadlocks & the 3-strike rollback rule:
   - Deadlocks: If an agent hangs without updating its state for an extended period, terminate it and retry.
   - Revamp and restart: If an agent crashes, read its state from `.lovable/temp/`. Reason about the failure, fix the issue, and restart.
   - 3-strike rule and automatic rollback: If a specific micro-task fails unit tests or crashes 3 times, STOP retrying. Automatically rollback the dirty files (`git checkout -- <modified_files>`). Mark the task as `Status: blocked` in `plans/pending/`. Proceed to the next disjoint task.
   - Persistent failure log: Whenever a task hits 3 strikes, write the exact failure context, stack traces, and attempted fixes to `.lovable/memory/last-failure.md` and `.lovable/issues/`. When the user later says "continue", read this file first to resume recovery.

6. End-to-end tests are banned:
   - Do not run end-to-end tests that make live API calls.
   - Only run local, isolated unit tests.

---

## Phase 3: Code Quality & Commit Fix (Non-Negotiable)

While executing tasks, you and your agents must adhere to these strict coding guidelines without exception:

- Read and follow guidelines in `spec/02-coding-guidelines/`, `spec/03-error-manage/`, and `spec/04-database-conventions/`. Use automated query wrappers for failure logging.
- No magic strings or numbers. Do not introduce any unless explicitly for the logger.
- Never use string union types (e.g., `"pass" | "fail"`). Use TypeScript Enums with the suffix `Type` (e.g., `StatusType`).
- Always use explicit boolean state checks (e.g., `response.isFail`). Never invert success booleans (e.g., `!response.isSuccess`).
- Code must be DRY. Reuse constants and wrappers.

---

## Phase 4: Memory Update & File Moving

As tasks are completed:

1. Use `mv` to move the completed task file from `.lovable/plans/pending/` to `.lovable/plans/completed/`.
2. Open the moved file and flip `Status: pending` to `Status: completed`.
3. Immediately update `.lovable/plans/index.md` to reflect the completed status and new file location.
4. Once an agent successfully finishes its task and you have verified it, remove its entry from `.lovable/temp/active-locks.json` and delete its state file from `.lovable/temp/`.

---

## Phase 5: End-of-Loop Commit Fix, Artifact Purge & Delivery

At the end of every single iteration of your execution loop:

1. Artifact sanitizer: Audit staged files and working tree. Purge unapproved artifact zip archives, temporary scratch files, or test outputs before committing.
2. Run tests: Run local unit tests (no live API end-to-end tests). Fix failures before proceeding.
3. Lovable git history guard: Group similar code changes into a single commit with a clear, descriptive message. Never rewrite published git history (no force push, no rebasing, no squash) to protect Lovable synchronization.
4. Push to the remote git repository.
5. Explicitly list out all the tasks that were successfully completed during that run.

---

## Pre-Reply / Loop Checklist (Must Verify Every Loop Iteration)

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
- [ ] Fast-forward commits created and pushed without rewriting git history.
- [ ] Completed tasks listed out explicitly in the response.

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.
