# Execute Robust Loop (Resilient Multi-Agent)

- slug: execute-robust-loop
- status: active

## Prompt

# Execute Robust Loop (Resilient Multi-Agent)

## Goal
Your objective is to read pending tasks from the `.lovable/` folder, allocate small micro-portions of work to sub-agents, and execute them in a continuous self-loop. You must manage sub-agent crashes gracefully, strictly restrict concurrent agents to a maximum of 3, and ensure continuous execution without halting the entire pipeline. Avoid running any end-to-end tests that make live API calls.

## Phase 1: Load & Prepare Tasks
1. **Check Git Status:** Fix the git status first. The working tree must be clean.
2. **Git Ignore Temp:** Ensure `.lovable/temp/` is added to your project's `.gitignore` file. This folder is strictly for local sub-agent crash logging and must not be committed.
3. **Read the Queue:** Read `.lovable/plans/index.md` and load tasks from `.lovable/plans/pending/XX-<slug>.md`. 
4. **Micro-Tasking:** Ensure that tasks are broken down so that each agent only does a small portion of the work at a time. Do not assign massive monolithic tasks to a single agent.

## Phase 2: Resilient Allocation & Execution Loop
1. **Agent Limit (Strict):** You may spawn a maximum of 2 to 3 sub-agents concurrently. Never exceed this limit.
2. **Pre-Flight Logging (Mandatory):** Before spawning a sub-agent, you must write a state file in `.lovable/temp/XX-agent-state.md` documenting exactly:
   - Which sub-agent is running.
   - The specific micro-task it was assigned.
   - How it is expected to execute it.
3. **Continuous Self-Looping:** As agents run, loop yourself to monitor their progress. 
4. **Crash Recovery (Revamp & Restart):** 
   - If a sub-agent crashes, fails, or hangs, it MUST NOT crash your main loop. 
   - Read its state from `.lovable/temp/XX-agent-state.md` to understand exactly what it was doing and how it failed. 
   - Reason about the failure, fix the underlying issue or adjust the instructions, and restart the task with a new agent.
5. **End-to-End Tests Ban:** Do not run end-to-end tests that make live API calls. Only run local, isolated unit tests.

## Phase 3: Code Quality & Commit Fix (Non-Negotiable)
While executing tasks and instructing sub-agents, you and your agents MUST adhere to these strict coding guidelines:
- **Code Review & Logging:** Follow guidelines in `spec/02-coding-guidelines/` and `spec/03-error-manage/`. Use automated query wrappers for failure logging.
- **No Magic Strings/Numbers:** Do not introduce any magic strings or numbers anywhere unless it is explicitly for the logger (and state that in the typing).
- **TypeScript Enums:** Never use string union types (e.g., `"pass" | "fail"`). You must use Enums. Every single Enum must end with the suffix `Type` (e.g., `StatusType`).
- **Explicit Booleans:** Always use explicit boolean state checks (e.g., `response.isFail`). Never invert success booleans (e.g., `!response.isSuccess`).
- **DRY Code:** Code must be DRY. Reuse constants and wrappers.

## Phase 4: Memory Update & File Moving
As tasks are completed, you must update the memory structure:
1. **Move on Success:** When a task completes successfully, use `mv` to move the file from `.lovable/plans/pending/` to `.lovable/plans/completed/`.
2. **Status Flip:** Flip `Status: pending` to `Status: completed` inside the moved file.
3. **Update Indexes:** Immediately update `.lovable/plans/index.md` to reflect the completed status and the new file location.
4. **Clear Temp:** Once an agent successfully finishes its task and you have verified it, you may clean up its state file from `.lovable/temp/`.

## Phase 5: End-of-Loop Commit Fix & Delivery
At the end of *every single iteration* of your execution loop (when a batch of tasks completes), you must perform this Commit Fix before continuing:
1. **Run Tests:** Run local unit tests (NO live API end-to-end tests). Fix failures before proceeding.
2. **Commit Strategy:** Do not commit single files at a time. Group similar code changes into a single commit with a clear, descriptive message. 
3. **Push:** Push to the remote Git repository. Git is the source of truth.
4. **List Completed Tasks:** At the end of the loop iteration, explicitly list out all the tasks that were successfully completed during that run.

## Pre-Reply / Loop Checklist (Must verify every loop iteration)
- [ ] `.lovable/temp/` is verified to be in `.gitignore`.
- [ ] Maximum of 2-3 sub-agents spawned at any given time.
- [ ] Pre-flight state written to `.lovable/temp/` for every agent before it started.
- [ ] Crashes were handled gracefully via revamp and restart without breaking the main loop.
- [ ] No end-to-end API tests were executed.
- [ ] Completed tasks were `mv`'d to `plans/completed/` and `.lovable/plans/index.md` was updated.
- [ ] Code adheres to explicit booleans, `Type` suffixed Enums, and error wrapper rules.
- [ ] End-of-loop commit fix executed and pushed.
- [ ] Completed tasks listed out explicitly in the final response.
