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
- **Context Diet:** When spawning a subagent, DO NOT paste file contents, memory logs, or the entire plan into its prompt. Give it the absolute minimal instruction (e.g., "Read subtask file `.lovable/plans/subtasks/XX-slug/01-task.md` and execute it"). The subagent MUST read the necessary files itself.

## 2. Non-Negotiable Core Rules (Auto-Reject on Violation)

1. **Continuous & Zero-Failure Execution:** Run autonomously for up to `N` steps. The assigned task MUST be completed from start to finish without a failure. If a step fails, you must forcefully recover, fix the root cause, and push forward. Do not stop.
2. **Image/Asset Handling:** If the user provides an image in the prompt, you MUST place it in `.lovable/assets/<category>/XX-<slug>.<ext>`. NEVER place images in random root directories.
3. **Temporary Scripts:** Any temporary automation scripts (CSJ, python) used to execute mass edits must be placed in `.lovable/temp-scripts/` and explicitly gitignored. NEVER commit them.
4. **Error Management (AppError Rule):** Never throw or return generic base errors (e.g., `Error`, `Exception`). You MUST use a domain-specific `AppError`. For OOP languages (like C#), this MUST be a custom Exception type (e.g., `AppException`, `DomainException`).
5. **Coding Guidelines Integration:** You must treat `spec/02-coding-guidelines/` and `spec/03-error-manage/` as binding law.

## 3. Pre-Commit Verification Checklist (Must Follow)

Before marking the parent task as complete and pushing to the repository, you MUST manually verify every item on this checklist. If a subagent violated one of these rules, you must reject their work and make them fix it.

- [ ] **Anti-Garbage Naming:** No generic garbage names (`comp_100.go`, `temp`, `data`, `obj`, `Input100`) were used anywhere in the codebase.
- [ ] **Semantic Tests:** All unit test names are strictly semantic and behavior-driven (e.g., `TestUpdateUser_RejectsInvalidEmail`). `TestHandleComp100` is an immediate failure.
- [ ] **Boolean Conventions:** All boolean variables begin with `is`, `has`, `can`, or `should` and are NEVER negative (`isNotReady`). Success checks are never inverted (`!response.isSuccess` is banned; use `response.isFail`).
- [ ] **Function Size Constraints:** No function exceeds 15 lines. Long arguments are split across lines (max 100 chars).
- [ ] **Error Handling:** Errors use domain-specific `AppError` or custom `AppException`, not generic base `Error`. EVERY error is propagated and wrapped with context.
- [ ] **Formatting:** Spacing rules are strictly followed (no double blank lines, no padded braces).
- [ ] **Acronyms:** Casing is strictly PascalCase (`SwapIpWindows` not `SwapIPWindows`).
- [ ] **Artifacts:** Any user-provided images are correctly saved in `.lovable/assets/<category>/`.
- [ ] **Git Hygiene:** The Git working tree is completely clean, `.lovable/temp-scripts/` is untracked, and all tests pass locally.
