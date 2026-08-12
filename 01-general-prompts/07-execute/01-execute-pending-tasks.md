# Execute Pending Tasks (Continuous Loop & Multi-Agent)

- slug: execute-pending-tasks
- status: active

## Prompt

# Execute Pending Tasks (Continuous Loop & Multi-Agent)

## Goal
Your objective is to read all pending tasks from the `.lovable/` folder, allocate them to sub-agents, and execute them in a continuous self-loop until the entire queue is empty. You must strictly follow the project's folder structure, memory update protocols, and code quality guidelines (Commit Fix rules). 

**CRITICAL:** You must NEVER stop by yourself as long as there are pending tasks. You must self-loop continuously. If something breaks or a catastrophic failure occurs, halt and ask the user to type "continue" to resume the loop. Do not quit.

## Phase 1: Load Pending Tasks & Project State
1. **Check Git Status:** Fix the git status first. The working tree must be clean and committed before you start executing anything.
2. **Read the Indexes:** Read `.lovable/memory/index.md` and `.lovable/what-to-read.md`.
3. **Load the Queue:** Read `.lovable/plans/index.md`. Then read every file in `.lovable/plans/pending/XX-<slug>.md` and all associated subtasks in `.lovable/plans/subtasks/XX-<slug>/`.
4. **Identify Work:** Compile the list of pending tasks that need execution. 

## Phase 2: Allocate & Execute (Continuous Loop)
1. **Spawn Sub-Agents:** Assign sub-tasks to multiple sub-agents and run them in parallel to speed up the work. Give them explicit instructions based on the subtask `.md` files.
   - **Specific Titling:** You must spawn each sub-agent with a highly specific title reflecting its exact task (e.g., `Refactoring Auth` or `Fixing DB Connection`). Do not use generic names like `Frontend Agent`. If an agent switches tasks, its title must change to reflect the new task.
   - **Micro-Tasking:** Ensure agents are assigned simple, small tasks rather than larger monolithic ones.
2. **Continuous Self-Looping:** As sub-agents complete their work, you must loop yourself to review their progress, update the plan trackers, and spawn new agents for the next tasks. Do not stop until every task in `.lovable/plans/pending/` is complete. **Crucially, at the end of every while loop iteration, you must execute the Commit Fix (Phase 5) before spinning up the next loop.**
3. **Error Handling:** If a sub-agent fails or a build breaks, find the root cause, write it into memory (`.lovable/issues/`), and fix it. If the pipeline completely halts, pause and explicitly ask the user to say "continue" to resume the loop.

## Phase 3: Code Quality & Commit Fix (Non-Negotiable)
While executing tasks and instructing sub-agents, you and your agents MUST adhere to these strict coding guidelines:
- **Code Review:** Follow the code review guidelines from `spec/02-coding-guidelines/` and `spec/03-error-manage/`.
- **Error Logging:** All caught errors must be explicitly logged. Use or create a query wrapper for PHP/Python/TS that automatically logs failures to reduce scattered logging code.
- **No Magic Strings/Numbers:** Do not introduce any magic strings or numbers anywhere unless it is explicitly for the logger (and state that in the typing).
- **TypeScript Enums:** Never use string union types (e.g., `"pass" | "fail"`). You must use Enums. Every single Enum must end with the suffix `Type` (e.g., `StatusType`).
- **Explicit Booleans:** Always use explicit boolean state checks (e.g., `response.isFail`). Never invert success booleans (e.g., `!response.isSuccess`).
- **DRY Code:** Code must be DRY. Reuse constants and wrappers.

## Phase 4: Memory Update & File Moving
As tasks are completed, you must update the memory structure exactly as follows:
1. **Move, Don't Delete:** When a pending task or subtask is fully complete, use `mv` to move the file from `.lovable/plans/pending/` to `.lovable/plans/completed/`.
2. **Status Flip:** Open the moved file and flip `Status: pending` to `Status: completed`.
3. **Update Indexes:** Immediately update `.lovable/plans/index.md` to reflect the completed status and the new file location.
4. **Memory Writes:** If you or your sub-agents learn new architectural patterns, discover bugs, or establish new conventions, write them to `.lovable/memory/<topic>/XX-<slug>.md` and update `memory/index.md`.

## Phase 5: End-of-Loop Commit Fix & Delivery
At the end of *every single iteration* of your execution loop (when a batch of tasks completes), you must perform this Commit Fix before continuing:
1. **Run Tests:** Make sure the code runs standalone locally and in CI/CD. Run builds and unit tests. If any fail, fix them before proceeding.
2. **Commit Strategy:** Do not commit single files at a time. Group similar code changes into a single commit with a clear, descriptive commit message. Commit frequently after logical milestones.
3. **Push:** Make sure every commit is pushed to the remote Git repository without failure. Git is the source of truth.
4. **Final Check:** When the loop finally ends (the pending queue is empty), bump the minor release version following the repository's release guidelines.

## Pre-Reply / Loop Checklist (Must verify every loop iteration)
- [ ] Git working tree is clean before new code changes.
- [ ] Sub-agents are actively working on remaining tasks.
- [ ] Completed tasks were `mv`'d to `plans/completed/` and `plans/index.md` was updated.
- [ ] Code adheres to explicit booleans, `Type` suffixed Enums, and error wrapper rules.
- [ ] Commits are grouped logically and pushed to the remote.
- [ ] Continuous loop maintained; only pausing to ask for "continue" on critical failures.
