# Execute Pending Tasks (Self-Loop & Commit)

- slug: execute-pending-tasks
- status: active

## Prompt

# Execute Pending Tasks (Autonomous Execution)

## 1. Initial State: Audit and Re-Sequence Pending Tasks

Before starting execution, you must ensure the queue of pending tasks is properly ordered and named.

- Read the `.lovable/plans/pending/` directory and `.lovable/plans/index.md`.
- Count exactly how many pending tasks exist.
- **Naming Correction**: Check if the pending task files are correctly sequenced with a 2-digit numerical prefix (e.g., `01-<slug>.md`, `02-<slug>.md`). 
- If the naming is incorrect or missing prefixes, **fix it immediately**. Rename the files to follow the sequential `01-`, `02-`, `03-` format and update `.lovable/plans/index.md` to match the new filenames in the same operation.

## 2. Uninterrupted Autonomous Execution (Self-Looping)

You are the sole orchestrator. Your job is to complete ALL pending tasks without stopping.

- **Make a Great Plan**: Analyze all pending tasks and devise a comprehensive execution plan. 
- **Do NOT Ask Questions**: Do not stop to ask the user for permission. Do not stop to ask clarifying questions. 
- **Self-Loop**: You must self-loop continuously until every single pending task in the queue is verifiably completed.
- Ensure everything gets done properly and deeply. If you are not going deep, you are not doing the job.

## 3. High-Stakes Code Standards & Root Cause Analysis

While executing the pending tasks, you must adhere strictly to the project's code standards and root cause protocols:

- **Root Cause First**: Find the root cause of every problem before applying any fix. Record the root cause into the `.lovable` memory before touching code.
- **Error Management**: All caught errors must be explicitly logged following the guidelines in the `spec/03-error-manage/` folder. Use the established query wrapper for PHP/Python/TS that automatically logs failures.
- **No Magic Values**: Do not introduce any magic strings or magic numbers anywhere unless it is explicitly for the logger (and state that exception in the typing).
- **Enums Over Unions**: Replace TypeScript string union types (e.g., `"pass" | "fail"`) with Enums.
- **Enum Naming**: Every Enum name must end with the `Type` suffix (e.g., `StatusType`). Enum values must use `PascalCase` (e.g., `ActiveState`).
- **Boolean State Checks**: Always use explicit boolean state checks like `response.isFail`. NEVER use inverted success booleans like `!response.isSuccess`.
- **DRY Code**: Reuse constants; never duplicate them.

## 4. Sub-Agent Orchestration

To speed up the work, you may spawn sub-agents to handle independent chunks of the pending tasks.

- Spawn a maximum of 2 sub-agents concurrently to avoid RAM and caching issues.
- Give sub-agents highly specific titles (e.g., `Refactoring Auth`, `Fixing DB Connection`).
- Enforce the sub-agent lifecycle: they must read their subtask file, mark it `🔄 In Progress`, do the work (max 2-3 async operations), and mark it `✅ Done` with a summary of changed files.
- Sub-agents only write to the file system; they NEVER commit to Git.
- Track queue state by counting total subtasks spawned vs. total `✅ Done` entries.

## 5. End-of-Loop Final Verification & Commit

Once ALL pending tasks have been completed and marked `✅ Done`:

- **Final Verification**: Check the full build, run all unit tests, and check the CI/CD status. Fix any build failures or failing tests immediately. You may only finish the job when everything is green and fully verified.
- **No Test Artifacts**: Check `.gitignore` to explicitly exclude test reports, test data, artifacts, and compiled binaries. Ensure absolutely NO test results or binaries are staged.
- **Commit**: Group all completed work into a single, logical Git commit with a clear, descriptive message summarizing the executed tasks.
- **Push**: You MUST push the commit to the remote GitHub repository. Pushing after the commit is non-negotiable.

## Actionable Items & Checklist (All Must Be True)

- [ ] Audited `.lovable/plans/pending/` and re-sequenced task filenames to `01-`, `02-`, etc., if they were named incorrectly.
- [ ] Devised a comprehensive execution plan for all pending tasks.
- [ ] Executed autonomously via continuous self-looping without stopping to ask the user questions.
- [ ] Followed all high-stakes code standards (Enums, `Type` suffixes, `PascalCase` values, explicit `isFail` checks, no magic strings, DRY code).
- [ ] Root causes were identified and logged in `.lovable/` before code was patched.
- [ ] Sub-agents followed the strict status lifecycle and never exceeded 2 concurrent instances.
- [ ] End-of-loop verification passed: build is green, tests pass, CI/CD is clear.
- [ ] Test data and binaries were explicitly excluded and not staged.
- [ ] All completed pending tasks were grouped into a single commit and pushed to GitHub.
