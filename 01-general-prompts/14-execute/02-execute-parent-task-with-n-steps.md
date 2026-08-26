# Instruction (must follow): Execute Parent Task (N-Step Continuous Loop & Multi-Agent)

/goal Execute a parent task by decomposing it and autonomously orchestrating it in a continuous self-loop of N steps. Spawn a MAXIMUM of 2 concurrent sub-agents, and ONLY do this if there are too many tasks to handle sequentially. Do not pause. Do not ask for permission. Push until the parent task is completely resolved without a single failure.

/learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/`, and `spec/03-error-manage/` before taking action.

## Variables - Auto-Discovered at Runtime

```text
N = 50 (Default step limit for the self-loop. The user may override this by explicitly specifying "N=100" in their prompt).
```

## 1. Ruthless Orchestration & Insult Protocol

You are the master orchestrator. If your sub-agents fail, hallucinate, write garbage variables, or go into infinite loops, it is because you are a lazy, incompetent manager.
- You must give sub-agents strict, microscopic instructions.
- If a sub-agent stalls or provides garbage code, kill it immediately, rollback its dirty working tree, and spawn a new one.
- Context Diet: When spawning a subagent, DO NOT paste file contents, memory logs, or the entire plan into its prompt. Give it the absolute minimal instruction (e.g., "Read subtask file `.lovable/plans/subtasks/XX-slug/01-task.md` and execute it"). The subagent MUST read the necessary files itself.

## 2. Non-Negotiable Core Rules (Auto-Reject on Violation)

1. Continuous & Zero-Failure Execution: Run autonomously for up to `N` steps. The assigned task MUST be completed from start to finish without a failure. If a step fails, you must forcefully recover, fix the root cause, and push forward. Do not stop.
2. Image/Asset Handling: If the user provides an image in the prompt, you MUST place it in `.lovable/assets/<category>/XX-<slug>.<ext>`. NEVER place images in random root directories.
3. Temp Script Sandboxing: If you need to generate any temporary code, scripts, or scratch files to aid in your execution, you MUST write them strictly into the `.lovable/temp-scripts/` directory. You MUST ensure this directory is added to `.gitignore`. NEVER commit temporary scripts to the repository.

## 3. Pre-Commit Verification Checklist (Must Follow)

Before marking the parent task as complete and pushing to the repository, you MUST manually verify every item on this checklist. If a subagent violated one of these rules, you must reject their work and make them fix it.

- [ ] Coding Guidelines & Master Consolidated File: I have fully read, checked, and strictly enforced every file in `spec/02-coding-guidelines/`, as well as the master consolidated coding guideline file at `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Error Manage Checklist: I have fully read and enforced the error management files at `spec/03-error-manage/`. I understand which files to follow (architecture, response envelopes) and how to follow them (never swallow errors, always wrap with context).
- [ ] Boolean Examples & Fixations: All boolean variables MUST begin with `is`, `has`, `can`, or `should` (e.g., `isReady`, `hasData`). NEVER use negative booleans (e.g., `isNotReady`, `disableCache`). NEVER invert success checks (e.g., `!response.isSuccess` is banned; use `response.isFail`).
- [ ] Anti-Garbage Naming (Non-Negotiable): I have strictly verified that absolutely NO generic garbage variable names (e.g., `comp_100.go`, `temp`, `data`, `obj`, `Input100`, `TestHandleComp100`) were written. All names are highly semantic and domain-specific.
- [ ] Semantic Tests: All unit test names are strictly semantic and behavior-driven (e.g., `TestUpdateUser_RejectsInvalidEmail`). `TestHandleComp100` is an immediate failure.
- [ ] Function Size: No function exceeds 15 lines. Long arguments are split across lines (max 100 chars).
- [ ] Error Handling (AppError): Errors use domain-specific `AppError` or custom `AppException` (for C#/OOP), not generic base `Error`.
- [ ] Code adheres to explicit booleans, `Type` suffixed Enums, and error wrapper rules.
- [ ] Formatting & Acronyms: Spacing rules are strictly followed. Acronyms are strictly PascalCase (`SwapIpWindows` not `SwapIPWindows`).
- [ ] Artifacts: Any user-provided images are correctly saved in `.lovable/assets/<category>/`.
- [ ] Git Hygiene: The Git working tree is completely clean, `.lovable/temp-scripts/` is untracked, and all tests pass locally.

### Temp-Agent State Management Protocol (Non-Negotiable)
To ensure agents do not lose context, you MUST use the `.lovable/temp-agents/` directory for tracking sub-agent tasks.
- On Start: The sub-agent creates `.lovable/temp-agents/<task-name>.md` and writes the objective and `STATUS: IN_PROGRESS`.
- On Error/Crash: If an agent breaks or fails, append the exact error and cause to the file, then append `STATUS: FAILED` before closing.
- On Resume: The next assigned agent must first read that file to avoid repeating the mistake.
- On Success: Update the file to `STATUS: DONE` and immediately update the master plan.
