# Instruction (must follow): Coding Guideline Execution — Error Management & Architecture

Trigger Keywords & Aliases: `cg-error`, `cg-execute error`, `audit error`, `fix error guidelines`, `enforce error management`

```text
N = 100
```

N = total self-loop steps budget for scanning, spec planning, and autonomously resolving all error management guideline violations.

- [ ] /goal First `N/2` steps (Phase 1) are dedicated to scanning the entire codebase for error handling violations, writing the master audit spec into `.lovable/plans/pending/XX-error-management-audit.md`, decomposing into subtasks in `.lovable/plans/subtasks/XX-error-management/`, and verifying/creating the dedicated error linter in `linter-scripts/`.
- [ ] /goal Second `N/2` steps (Phase 2) are dedicated to executing each subtask sequentially, refactoring error handling to adhere to `AppError` context wrapping and universal envelopes, running the error linter, and verifying all local CI gates exit with code 0.
- [ ] /learn Ingest `.lovable/coding-guidelines/coding-guidelines.md`, `spec/03-error-manage/`, `.lovable/strictly-avoid.md`, and `.lovable/memory/issues/` before modifying code.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization.

---

## Phase 0: Antigravity Skill Bootstrap (Memory Optimization)

Before execution, check if `.agents/skills/coding-guidelines/skill.md` exists. If missing, create it with YAML frontmatter (`name: coding-guidelines`, `description: "Audits and enforces cross-language coding standards and error management."`).

---

## Phase 1: Scan, Spec, Subtasks & Linter Verification (Steps 1 to PHASE_1_STEPS)

> [!IMPORTANT]
> **Phase 1 is dedicated to discovery, planning, and tooling setup. Do NOT refactor business code in Phase 1.**

### Step 1: Ingest Error Management Source of Truth

Read and understand the authoritative error management rules from `.lovable/coding-guidelines/coding-guidelines.md` and `spec/03-error-manage/`:

1. **Never Swallow Errors:** Every `catch` block MUST log the operation name and key input variables, then rethrow, return a typed error, or explicitly dispatch to an error handler. Silent `catch {}` or ignored error returns are forbidden.
2. **Contextual Error Wrapping:** Wrap original errors with operation labels and execution context (e.g., `apperror.Wrap(err, "OpName", ctx)` in Go, `throw new AppError(cause, { op, ctx })` in TypeScript, `AppException` in C#/PHP). The original stack trace and root cause must survive.
3. **No Bare Panics / Hard Process Exits:** Never use `panic()`, `os.Exit()`, `process.exit()`, or `die()` inside library or domain logic. All recoverable errors must bubble up through typed return values or exceptions.
4. **Universal Response Envelope:** All backend API handlers and service boundaries must return standard envelopes: `{ "data": T, "errors": [AppError], "meta": Meta }`.
5. **Typed & Registered Error Codes:** Error codes must be stable and registered (e.g. `ErrCodeNotFound`, `INVALID_PAYLOAD`). No ad-hoc string literals at throw sites.

### Step 2: Codebase-Wide Violation Scan

Search all active source files (Go, TypeScript, Python, C#, PHP, Rust) for:

- Empty `catch` blocks or swallowed errors (`_ = err`, `except: pass`).
- Bare error returns without contextual wrapping (`return err` vs `return apperror.Wrap(err, ...)`).
- Hard exits or bare panics (`panic(`, `process.exit(`, `os.Exit(`).
- Missing operation names or omitted contextual input variables in error logs.
- Unregistered, raw string error throws (`throw "error string"`).

### Step 3: Write Master Audit Spec

Save the complete violation inventory to `.lovable/plans/pending/XX-error-management-audit.md`:

- Document exact files, line numbers, failing functions, and the required refactoring pattern.
- Formulate clear Acceptance Criteria for every affected component.
- Register the spec in `.lovable/plans/index.md` and `.lovable/plans/what-to-read.md`.

### Step 4: Decompose into Subtasks

Break down the master plan into granular, microscopic subtasks in `.lovable/plans/subtasks/XX-error-management/`:

- `01-core-wrappers.md` (Domain layer error wrappers)
- `02-api-envelopes.md` (Handler & transport layer response envelopes)
- `03-service-handlers.md` (Service layer error capture and logging)

### Step 5: Linter Verification & CI/CD Connection (Mandatory Checklist)

- [ ] **Check Linter Script Existence:** Check if `linter-scripts/check-mws-error-codes.py` or `linter-scripts/validate-guidelines.py` exists.
- [ ] **Create Linter Script if Missing:** If no error management linter exists, create `linter-scripts/check-error-management.py` that scans for empty catch blocks, un-wrapped error returns, and bare panics/exits, exiting with code `1` upon finding violations.
- [ ] **Local Linter Command:** Verify the linter runs locally with:
  ```bash
  python linter-scripts/check-error-management.py
  ```
- [ ] **CI/CD Integration:** Connect the linter into `.lovable/ai-fix-scripts/03-cicd-local-runner.py` under the `JOBS` dictionary:
  ```python
  JOBS["lint:errors"] = ["python", "linter-scripts/check-error-management.py"]
  ```
  And verify it is present in `.github/workflows/ci.yml` as a mandatory validation step.

---

## Phase 2: Autonomous Subtask Execution Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Sequentially execute each subtask, applying surgical fixes and re-running linters until the codebase is 100% compliant.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Read the next subtask from .lovable/plans/subtasks/XX-error-management/
    2. Apply surgical code fixes adhering to AppError context wrapping and envelope rules.
    3. Run the error management linter:
          python linter-scripts/check-error-management.py
    4. Run the universal guideline autofixer:
          python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
    5. Run the local CI runner:
          python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    6. IF any check fails:
          - Diagnose failure, apply correction, and loop back to step 3 immediately.
       IF all checks pass (exit code 0):
          - Mark subtask completed and proceed to the next subtask.

    7. When all subtasks are finished and local CI is 100% green:
          - BREAK and proceed to End of Tunnel.
```

---

## Authoritative Error Handling Reference

### Go Example

```go
// BAD: Swallowed or unwrapped bare error
func FetchUser(id string) (*User, error) {
    user, err := db.Find(id)
    if err != nil {
        return nil, err // BAD: No operation context, root cause trace lost
    }
    return user, nil
}

// GOOD: Wrapped with operation context and parameters
func FetchUser(ctx context.Context, id string) (*User, error) {
    user, err := db.Find(ctx, id)
    if err != nil {
        return nil, apperror.Wrap(err, "FetchUser", map[string]any{"userId": id})
    }
    
    return user, nil
}
```

### TypeScript Example

```typescript
// BAD: Raw string throw, swallowed error
try {
    await processPayment(cartId);
} catch (e) {
    // BAD: Swallowed error
}

// GOOD: AppError with operation context and universal envelope
try {
    await processPayment(cartId);
} catch (cause) {
    logger.error("PaymentProcessingFailed", { cartId, cause });
    throw new AppError(ErrCodePaymentFailed, "Failed to process payment", { cartId, cause });
}
```

---

## Pre-Reply / Loop Checklist (Must Verify Every Turn)

- [ ] All errors wrapped with operation name, parameters, and causal stack trace.
- [ ] No bare `panic()`, `process.exit()`, or `os.Exit()` in domain logic.
- [ ] Universal response envelope `{ data, errors, meta }` maintained across all API endpoints.
- [ ] Linter script `linter-scripts/check-error-management.py` executed and exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.
- [ ] Completed subtasks marked `[x]` and master plan moved to `.lovable/plans/completed/`.

---

## No Automatic Releases (Strict Policy)

> [!CAUTION]
> This is a development refactoring workflow. You MUST NOT bump versions, update changelogs, or cut a release at the end of this task. Commits must remain standard development commits (e.g. `refactor(errors): enforce AppError wrapping across services`).

---

## End of Tunnel Checklist

- [ ] `python linter-scripts/check-error-management.py` exited with code 0.
- [ ] `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0 (100% green).
- [ ] Master plan moved to `.lovable/plans/completed/XX-error-management-audit.md`.
- [ ] Git status clean, staged, and committed with descriptive message.
- [ ] Pushed commit to current branch.
- [ ] File Change Summary posted in chat detailing all modified files and error refactoring rationale.

---

## Metadata

- slug: cg-error-management
- priority: high
- status: active
