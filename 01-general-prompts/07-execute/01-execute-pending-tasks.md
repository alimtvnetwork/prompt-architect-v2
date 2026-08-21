# Execute Pending Tasks (Continuous Loop & Multi-Agent)

- slug: execute-pending-tasks
- status: active

## Prompt

# Execute Pending Tasks (Continuous Loop & Multi-Agent)

## Goal

Your objective is to read all pending tasks from the `.lovable/` folder, allocate them across up to 3 sub-agents, and execute them in a continuous self-loop until the entire queue is empty. You must strictly follow the project's folder structure, memory update protocols, code quality guidelines, artifact sanitation, and file-collision safety rules.

**CRITICAL:** You must NEVER stop by yourself as long as there are pending tasks. You must self-loop continuously. If something breaks or a catastrophic failure occurs, halt, log the issue, and ask the user to type "continue" to resume the loop. Do not quit.

## Phase 1: Load Pending Tasks & Project State

1. **Check Git Status:** Fix the git status first. The working tree must be clean and committed before you start executing anything.
2. **Read the Indexes & Casing Check:** Read `.lovable/memory/index.md` and `.lovable/memory/what-to-read.md`. Verify root readme is strictly lowercase `readme.md`.
3. **Load the Queue:** Read `.lovable/plans/index.md`. Then read every file in `.lovable/plans/pending/XX-<slug>.md` and all associated subtasks in `.lovable/plans/subtasks/XX-<slug>/`.
4. **Identify Work & Execution Waves:** Group pending tasks into sequenced Execution Waves (Wave 1: Schemas/DB/wrappers; Wave 2: Business logic & services; Wave 3: UI & docs).

## Phase 2: Allocate & Execute (Continuous Loop & Parallel Agents)

1. **Spawn Sub-Agents (Max 3 Concurrent):** Assign subtasks to up to 3 parallel sub-agents to accelerate execution.
   - **File Collision Locking Matrix (`active-locks.json`):** Maintain active file paths in `.lovable/temp/active-locks.json`. Parallel subagents must never touch the same files simultaneously.
   - **Specific Titling:** You must spawn each sub-agent with a highly specific title reflecting its exact task (e.g., `Refactoring Auth Service` or `Fixing DB Connection`). Do not use generic names. If an agent switches tasks, its title must change.
   - **Micro-Tasking:** Ensure agents are assigned discrete, simple tasks (under 15 lines per function). Tasks exceeding 7 steps must be decomposed into subtasks first.
2. **Continuous Self-Looping:** As sub-agents complete their work, loop to review their progress, update the plan trackers, and spawn new agents for the next wave. Do not stop until every task in `.lovable/plans/pending/` is complete. **At the end of every while loop iteration, execute the Commit Fix (Phase 5) before spinning up the next loop.**
3. **Crash Recovery & 3-Strike Rollback:**
   - If a sub-agent fails unit tests or build commands, attempt targeted fix.
   - If it fails 3 consecutive times, automatically rollback dirty working tree (`git checkout -- <modified_files>`), log root cause to `.lovable/memory/last-failure.md` and `.lovable/issues/`, and proceed to the next disjoint task.

## Phase 3: Code Quality & Commit Fix (Non-Negotiable)

While executing tasks and instructing sub-agents, you and your agents MUST adhere to these strict coding guidelines:
- **Code Review:** Follow guidelines from `spec/02-coding-guidelines/`, `spec/03-error-manage/`, and `spec/04-database-conventions/`.
- **Error Logging:** All caught errors must be explicitly logged. Use or create a query wrapper that automatically logs failures with operation name and key inputs.
- **No Magic Strings/Numbers:** Do not introduce any magic strings or numbers anywhere unless explicitly for the logger.
- **TypeScript Enums:** Never use string union types (e.g., `"pass" | "fail"`). You must use Enums ending with the suffix `Type` (e.g., `StatusType`).
- **Explicit Booleans:** Always use explicit boolean state checks (e.g., `response.isFail`). Never invert success booleans (e.g., `!response.isSuccess`).
- **DRY Code:** Code must be DRY. Reuse constants and wrappers.

## Phase 4: Memory Update & File Moving

As tasks are completed, you must update the memory structure exactly as follows:
1. **Move, Don't Delete:** When a pending task or subtask is fully complete, use `mv` to move the file from `.lovable/plans/pending/` to `.lovable/plans/completed/`.
2. **Status Flip:** Open the moved file and flip `Status: pending` to `Status: completed`.
3. **Update Indexes:** Immediately update `.lovable/plans/index.md` to reflect the completed status and the new file location.
4. **Memory Writes & Spec Preservation:** If new patterns or conventions are established, record them in `.lovable/memory/<topic>/XX-<slug>.md` and update `memory/index.md`. Detailed specs must never be shortened.

## Phase 5: End-of-Loop Commit Fix, Artifact Purge & Delivery

At the end of *every single iteration* of your execution loop (when a batch of tasks completes), execute this Commit Fix before continuing:
1. **Artifact Sanitizer:** Audit working tree and staged files. Ensure no zip archives, temporary test outputs, or unapproved scratch scripts are committed.
2. **Run Tests & Builds:** Ensure code runs standalone locally and in CI/CD. Run full builds and unit test suites.
3. **Lovable Git History Guard:** Group similar code changes into a single commit with a clear, descriptive message. Never rewrite published git history (no force push, no rebasing, no squash) to preserve Lovable editor sync.
4. **Push:** Push every commit to the remote Git repository.
5. **Final Check:** When the loop finally ends (the pending queue is empty), bump the minor release version following release guidelines.

---

## Pre-Reply / Loop Checklist (Must verify every loop iteration)

- [ ] Git working tree is clean before new code changes.
- [ ] Sub-agents are actively assigned disjoint files verified against `.lovable/temp/active-locks.json`.
- [ ] Completed tasks were `mv`'d to `plans/completed/` and `plans/index.md` was updated.
- [ ] 3-strike rule respected: failed tasks cleanly rolled back and logged to `last-failure.md`.
- [ ] Staged files sanitized of artifact zips and temporary scratch files.
- [ ] Code adheres to explicit booleans, `Type` suffixed Enums, and error wrapper rules.
- [ ] Fast-forward commits created and pushed without rewriting published Git history.
- [ ] Continuous loop maintained; only pausing to ask for "continue" on critical unrecoverable failures.

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.
