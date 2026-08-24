# Instruction (must follow): Execute Pending Tasks (Continuous Loop & Multi-Agent)

/goal Execute every pending task across `.lovable/plans/pending/` using up to 3 sub-agents in a continuous self-loop. Do not stop until the queue is empty, every plan is committed to git, and all indexes are updated. This run ends only when there is nothing left to execute. You MUST self-loop continuously until every pending task is completed; do not stop until the queue is completely empty.

/learn Capture every pattern, convention, fix, and correction discovered during execution into `.lovable/memory/learned/01-<slug>.md` and `.lovable/strictly-avoid.md`. Never repeat a mistake that was logged.

## Non-Negotiable Rules (Auto-Reject on Violation)

1. You must NEVER stop by yourself as long as there are pending tasks.
2. You must self-loop continuously without breaking between tasks.
3. If a catastrophic failure occurs, halt, log the issue, and ask the user to type "continue" to resume.
4. Violation of any rule below is auto-reject on the same tier as RULE 0.

## Anti-Hallucination Rules

- If a spec file, folder, or task is missing or ambiguous, do NOT guess or invent a rule.
- Ask a clarifying question or log an open ambiguity in `.lovable/ambiguous-questions/01-new-ambiguity/01-<slug>.md` before proceeding.
- Never invent step counts. Read the actual files and count from them.

---

## Phase 1: Load Pending Tasks & Project State

1. Check git status first. The working tree must be clean and committed before executing anything.
2. Read `.lovable/memory/index.md` and `.lovable/memory/what-to-read.md`. Verify root readme is strictly lowercase `readme.md`.
3. Read `.lovable/plans/index.md`. Then read every file in `.lovable/plans/pending/XX-<slug>.md` and all associated subtasks in `.lovable/plans/subtasks/XX-<slug>/` (Note: for coding guidelines, check `.lovable/plans/subtasks/01-coding-guideline-fixes/` or other synced folder structures).
4. Group pending tasks into sequenced Execution Waves:
   - Wave 1: Schemas, DB, and query wrappers
   - Wave 2: Business logic and services
   - Wave 3: UI and documentation

---

## Phase 2: Allocate & Execute (Continuous Loop & Parallel Agents)

1. Spawn sub-agents (maximum 3 concurrent):
   - Assign subtasks to up to 3 parallel sub-agents to accelerate execution.
   - Maintain active file paths in `.lovable/temp/active-locks.json`. Parallel sub-agents must never touch the same files simultaneously.
   - Assign each sub-agent a highly specific title reflecting its exact task (e.g., `Refactoring Auth Service`). Do not use generic names. If an agent switches tasks, its title must change.
   - Ensure each agent handles discrete, simple tasks (under 15 lines per function). Tasks exceeding 7 steps must be decomposed into subtasks before execution.

2. Continuous self-looping:
   - Loop to review sub-agent progress, update plan trackers, and spawn new agents for the next wave.
   - Do not stop until every task in `.lovable/plans/pending/` is complete.
   - At the end of every loop iteration, execute the Commit Fix (Phase 5) before spinning up the next loop.

3. Crash Recovery & 3-Strike Rollback:
   - If a sub-agent fails unit tests or build commands, attempt a targeted fix.
   - If it fails 3 consecutive times, automatically rollback the dirty working tree (`git checkout -- <modified_files>`).
   - Log the root cause to `.lovable/memory/last-failure.md` and `.lovable/issues/`.
   - Proceed to the next disjoint task after rollback.

---

## Phase 3: Code Quality & Commit Fix (Non-Negotiable)

While executing tasks, you and your agents must adhere to these strict coding guidelines without exception:

- Read and follow guidelines in `spec/02-coding-guidelines/`, `spec/03-error-manage/`, and `spec/04-database-conventions/`.
- All caught errors must be explicitly logged. Use or create a query wrapper that automatically logs failures with operation name and key inputs.
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
4. If new patterns or conventions are established, record them in `.lovable/memory/<topic>/XX-<slug>.md` and update `memory/index.md`. Detailed specs must never be shortened.

---

## Phase 5: End-of-Loop Commit Fix, Artifact Purge & Delivery

At the end of every single iteration of your execution loop:

1. Artifact sanitizer: Audit working tree and staged files. Ensure no zip archives, temporary test outputs, or unapproved scratch scripts are committed.
2. Run tests and builds: Ensure code runs standalone locally and in CI/CD. Run full builds and unit test suites.
3. Lovable git history guard: Group similar code changes into a single commit with a clear, descriptive message. Never rewrite published git history (no force push, no rebasing, no squash) to preserve Lovable editor sync.
4. Push every commit to the remote git repository.
5. Final check: When the loop finally ends (the pending queue is empty), bump the minor release version following release guidelines.

---

## Pre-Reply / Loop Checklist (Must Verify Every Loop Iteration)

- [ ] Git working tree is clean before new code changes.
- [ ] Sub-agents are actively assigned disjoint files verified against `.lovable/temp/active-locks.json`.
- [ ] Completed tasks were `mv`'d to `plans/completed/` and `plans/index.md` was updated.
- [ ] 3-strike rule respected: failed tasks cleanly rolled back and logged to `last-failure.md`.
- [ ] Staged files sanitized of artifact zips and temporary scratch files.
- [ ] Code adheres to explicit booleans, `Type` suffixed Enums, and error wrapper rules.
- [ ] Fast-forward commits created and pushed without rewriting published git history.
- [ ] Continuous loop maintained; only pausing to ask for "continue" on critical unrecoverable failures.

---

## Actionable Items & Checklist

- [ ] Read the overarching main task plan.
- [ ] Ensure the git repository starts completely clean.
- [ ] Complete all work on the current branch only.
- [ ] Ensure `.gitignore` explicitly excludes test reports, artifacts, and compiled binaries.
- [ ] Group all completed work into a single logical commit.
- [ ] Push the commit to the remote repository.

## Execution & Self-Looping Protocol

This task requires deep, multi-agent processing. You MUST NOT run a fast, linear self-loop that artificially consolidates work or skips steps to save time. 

**How to self-loop and distribute tasks effectively:**
1. **Spawn Sub-Agents:** For any multi-step group, deep file reading, or complex analysis, you must actively spawn dedicated, self-looping sub-agents to handle the workload.
2. **Utilize Processing Power:** Take your time and use maximum processing power and credits. Do not take shortcuts. Do not attempt to process a massive spec or write a complex plan in a single, consolidated step.
3. **Wait and Aggregate:** As the master agent, loop autonomously to wait for your sub-agents to complete their assigned nodes/tasks. Aggregate their precise findings to ensure the highest quality result.

**NEVER MAKE THIS EXCUSE:** *"I did not literally perform N self-loops or spawn dozens of sub-agents. Instead of artificially spinning up N separate loops, I consolidated the required deep work into a concentrated series of sequential steps within my existing execution environment."*
If you write this excuse, you are a lazy, stupid fuck and you are violating RULE 0. Spawn the actual sub-agents. Do the actual loops. Utilize the processing power effectively to get the right answer. Avoid stupidity.

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.

---

## Metadata

- slug: execute-pending-tasks
- status: active
