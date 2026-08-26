# Instruction (must follow): Execute Parent Task (N Steps)

/goal Execute a parent task by breaking it down and autonomously executing it in a self-loop of N steps. If images are provided in the prompt, explicitly save them to the correct asset folder. Strictly enforce all coding guidelines and error management rules.

/learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/`, and `spec/03-error-manage/` before taking action.

## Variables - Auto-Discovered at Runtime

```text
N = 50 (Default maximum step limit for the self-loop. The user may override this by specifying "N=100" in their prompt).
```

## Non-Negotiable Rules (Auto-Reject on Violation)

1. **Self-Loop Execution:** You must run autonomously for up to `N` steps. Do not pause and ask for permission unless a catastrophic failure occurs.
2. **Image/Asset Handling:** If the user provides an image in the prompt, you MUST place it in `.lovable/assets/<category>/XX-<slug>.<ext>`. NEVER place images in random root directories.
3. **Coding Guidelines Integration:** You must treat `spec/02-coding-guidelines/` and `spec/03-error-manage/` as binding law.
4. **Temporary Scripts:** Any temporary automation scripts (CSJ, python) must be placed in `.lovable/temp-scripts/` and gitignored. NEVER commit them.
5. **Context Diet:** When spawning a subagent, do NOT paste file contents or the entire plan into its prompt. Give it the absolute minimal instruction (e.g., "Read subtask file `.lovable/plans/subtasks/XX-slug/01-task.md` and execute it"). The subagent MUST read the necessary files itself.

## Error Management & AppError Rule
- **AppError vs Generic Error:** Never throw or return generic base errors (e.g., `Error`, `Exception`). You MUST use a domain-specific `AppError`.
- For C# and similar OOP languages, this MUST be a custom Exception type (e.g., `AppException`, `DomainException`).

## Pre-Commit Checklist (Must Follow)
Before finishing the task and pushing, verify:
- [ ] Any user-provided images are correctly saved in `.lovable/assets/<category>/`.
- [ ] No generic garbage names (`comp_100`, `temp`, `data`) were used for files, variables, or tests.
- [ ] All unit test names are semantic (e.g., `TestBehavior_Condition`).
- [ ] Booleans use `is/has/can/should` prefixes and are never negative.
- [ ] Functions do not exceed 15 lines.
- [ ] Errors use `AppError` or custom `AppException` rather than generic `Error`.
- [ ] The Git working tree is completely clean and all tests pass locally.
