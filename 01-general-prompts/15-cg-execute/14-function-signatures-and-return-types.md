# Instruction (must follow): Execute Coding Guidelines — Function Naming, Single Return Types & Result Envelope Architecture

Trigger Keywords & Aliases: `cg-functions`, `cg-signatures`, `cg-return-types`, `cg-execute functions`, `audit function naming`, `fix return types`, `enforce apperror`, `enforce result envelope`, `single return type audit`

```text
N = 200
```

N = total self-loop steps budget that the agents will perform.

/goal Autonomously scan, discover, plan, refactor, and fix all function naming conventions, boolean predicate prefixes, multi-value returns, raw generic errors, and result envelopes across the codebase, enforcing semantic verb/predicate naming, universal `*AppError` wrapping, single `Result[T]` return envelopes with `.IsSuccess()`/`.IsFailed()` methods, and strict relative Git paths until 100% green without stopping.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan the target codebase using AST and grep tools to inventory all functions with generic error returns (`(T, error)`), unformatted boolean predicates missing `is`/`has`/`can` prefixes, raw `fmt.Errorf()` or standard `errors.New()`, anti-garbage names, and functions lacking typed `Result[T]` envelopes. Write the master audit spec in `.lovable/plans/pending/XX-function-signatures-audit.md` with an exhaustive Violation Ledger table, decompose into granular subtasks in `.lovable/plans/subtasks/XX-function-signatures/`, and verify/create the function signature linter.
- [ ] /goal Second N/2 steps (Phase 2): Directly open each offending source file. Refactor function signatures to use semantic verb/predicate names, convert multi-value returns to single `Result[T]` envelopes, replace generic errors with domain-specific `*AppError` wrappers, enforce <= 8–15 line function decomposition, run signature linters, and verify local CI quality gates exit with code 0 (`exit 0`).
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/00-canonical-size-tier.md`, `spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`, `spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`, `spec/03-error-manage/01-error-architecture.md`, `spec/03-error-manage/02-response-envelopes.md`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2: Scan Signatures, Build Violation Ledger in .lovable/plans/pending/, Subtasks, Linter Hook)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N: Actively Edit Code, Refactor Signatures, Implement Result[T] Envelopes, Verify Local CI)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization. Never modify them mid-execution.

---

## Dedicated Section: Function Naming, Single Return Types & Result Envelopes

A clean codebase relies on deterministic function contracts. Ambiguous function names, raw generic error returns, and unencapsulated multi-value returns obscure domain failures and cause high cognitive friction.

---

### 1. Constants vs Enums Architecture

Before structuring function signatures, understand when to use a Constant vs an Enum:

1. **Singular Standalone Values (Use Typed Constants):**
   - If a literal is an isolated constant (e.g. `IndentSpaces = "    "`, `DefaultTimeoutSeconds = 30`, `MaxCmdColumnWidth = 26`), define it as a typed constant in a centralized `constants` module.
2. **Selectable Variant Sets (Use Enums with `*Type` Suffix):**
   - If a concept represents a group or finite set of selectable options in a specific context (e.g. `AlignmentType` with `Left`, `Right`, `Center`; `IndentLevelType` with `Compact`, `Standard`, `Wide`; `OrderStatusType` with `Pending`, `Processing`, `Completed`), it **MUST be defined as a typed Enum** ending with `Type`.
   - Enums must live in a dedicated `enums/` package/directory in Go, TypeScript, Rust, PHP, Python, and C#.

---

### 2. Semantic Function Naming Principles

1. **Action Functions (Verb + Noun):**
   - Every function performing an action MUST start with a clear, active verb: `fetchUser()`, `calculateTax()`, `renderHelpRow()`, `validatePayload()`.
   - Ban vague garbage names: `handle()`, `process()`, `doStuff()`, `manage()`, `temp()`.
2. **Boolean Predicate Functions (`is`, `has`, `can`, `should`, `was`):**
   - Every function returning a boolean MUST begin with an affirmative prefix: `isValid()`, `hasPermissions()`, `canExecute()`, `shouldRetry()`.
   - Negative prefixes (`isNotReady()`, `hasNoData()`) are **strictly prohibited**. Frame positively (`isReady()`, `hasData()`) and invert at the call site (`if !isReady { ... }`).

---

### 3. The Single Return Type Principle & Universal `Result[T]` Envelope

In domain services, handlers, and internal business logic, functions MUST return a single encapsulated result envelope rather than raw multi-value tuples `(T, error)`.

#### 3a. The Universal `Result[T]` Structure (Go)

```go
// ❌ FORBIDDEN: Raw generic (T, error) multi-value return
func GetUser(id string) (*User, error) {
    if id == "" {
        return nil, errors.New("user ID required") // ❌ Raw stdlib error
    }
    // ...
}

// ✅ REQUIRED: Single Result[T] envelope with *AppError and helper methods
package models

import "gitmap/apperror"

type Result[T any] struct {
    Value T
    Err   *apperror.AppError
}

func (r Result[T]) IsSuccess() bool {
    return r.Err == nil
}

func (r Result[T]) IsFailed() bool {
    return r.Err != nil
}

func (r Result[T]) Unwrap() (T, *apperror.AppError) {
    return r.Value, r.Err
}

func SuccessResult[T any](val T) Result[T] {
    return Result[T]{Value: val}
}

func FailureResult[T any](err *apperror.AppError) Result[T] {
    return Result[T]{Err: err}
}
```

```go
// ✅ REQUIRED: Service function returning single Result[T]
func GetUser(id string) Result[*User] {
    if id == "" {
        appErr := apperror.New(
            apperror.ErrCodeValidationFailed,
            "user ID is required",
            "GetUser",
        )
        return FailureResult[*User](appErr)
    }

    user, isFound := userRepo.Find(id)

    if !isFound {
        appErr := apperror.New(
            apperror.ErrCodeNotFound,
            "user not found",
            "GetUser",
        )
        return FailureResult[*User](appErr)
    }

    return SuccessResult[*User](user)
}
```

---

#### 3b. TypeScript `Result<T>` Envelope

```typescript
// ❌ FORBIDDEN: Throwing raw errors or returning undefined on failure
async function fetchAccount(id: string): Promise<Account | undefined> { ... }

// ✅ REQUIRED: Strongly-typed Result<T, AppError> envelope
export type Result<T> =
    | { isSuccess: true; isFailed: false; value: T; error: null }
    | { isSuccess: false; isFailed: true; value: null; error: AppError };

export function successResult<T>(value: T): Result<T> {
    return { isSuccess: true, isFailed: false, value, error: null };
}

export function failureResult<T>(error: AppError): Result<T> {
    return { isSuccess: false, isFailed: true, value: null, error };
}

export async function fetchAccount(id: string): Promise<Result<Account>> {
    if (!id) {
        return failureResult(new AppError(ErrorCodeType.ValidationFailed, "Account ID is required"));
    }

    const account = await accountRepo.find(id);

    if (!account) {
        return failureResult(new AppError(ErrorCodeType.NotFound, "Account not found"));
    }

    return successResult(account);
}
```

---

#### 3c. Python `Result[T]` Dataclass

```python
# ✅ REQUIRED: Generic Result[T] envelope with helper predicates
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

@dataclass(frozen=True)
class Result(Generic[T]):
    value: Optional[T] = None
    error: Optional[AppError] = None

    @property
    def is_success(self) -> bool:
        return self.error is None

    @property
    def is_failed(self) -> bool:
        return self.error is not None

def get_user_profile(user_id: str) -> Result[UserProfile]:
    if not user_id:
        return Result(error=AppError(ErrorCodeType.VALIDATION_FAILED, "user_id required"))

    profile = db.find_profile(user_id)

    if profile is None:
        return Result(error=AppError(ErrorCodeType.NOT_FOUND, "profile not found"))

    return Result(value=profile)
```

---

### 4. Total Ban on Generic `error` (Universal `AppError` Mandate)

1. **No Stdlib `error` in Internal Logic:**
   - NEVER return bare `error`, `errors.New()`, or `fmt.Errorf()` in domain packages.
   - All errors MUST return `*AppError` (or language equivalent `AppException`) carrying:
     - `Code`: Strongly-typed error enum (`ErrCodeValidationFailed`, `ErrCodeNotFound`).
     - `Message`: Human-readable context.
     - `Op`: Function / operation name (e.g. `"GetUser"`, `"ConnectSsh"`).
     - `Cause`: Original underlying error.
2. **Boundary Exception:**
   - The outermost binary entry point (`main()` in Go, root CLI handler) is the only place where `*AppError` is unwrapped and formatted into a terminal exit code or JSON envelope.

---

## 5. Phase 1 Violation Ledger Format

In Phase 1, you MUST generate `.lovable/plans/pending/XX-function-signatures-audit.md` containing the following master inventory table:

```markdown
| Function / Method | File Path | Line | Current Return Type | Target Return Type | Violations (Naming / Error / Tuple) | Planned Fix | Status |
|---|---|:---:|---|---|---|---|:---:|
| `GetUser` | `src/services/user.go` | 42 | `(*User, error)` | `Result[*User]` | Multi-value return, stdlib error | Wrap in `Result[*User]` with `*AppError` | PENDING |
| `validUser` | `src/auth/validate.ts` | 18 | `boolean` | `boolean` | Missing predicate prefix `is`/`has` | Rename to `isValidUser` | PENDING |
| `Process` | `pkg/worker/job.go` | 89 | `error` | `*apperror.AppError` | Generic error, vague verb name | Rename to `ExecuteJob`, return `*AppError` | PENDING |
```

---

## Strict In-Repository Execution & `.lovable/` Bounding Mandate

> [!IMPORTANT]
> **STRICT IN-REPOSITORY EXECUTION & `.lovable/` STORAGE CONTRACT:**
>
> 1. **In-Codebase Execution Only:** Whenever a Python script (runner, autofixer, linter, test aggregator) is executed or created, it MUST be executed **strictly within the repository root** (current working directory), NEVER outside the codebase or against external arbitrary directories.
> 2. **Strict Folder Bounding (`.lovable/`):** All AI scripts, local runners, autofixers, helper utilities, memory issue logs, and planning files MUST be created inside the `.lovable/` folder:
>    - Python AI Scripts: `.lovable/ai-fix-scripts/` (e.g. `01-file-manipulator.py`, `02-guideline-autofixer.py`, `03-cicd-local-runner.py`, `04-relative-path-fixer.py`, `05-naming-autofixer.py`, `06-cli-help-auditor.py`).
>    - RCA & Issue Logs: `.lovable/memory/issues/` and `.lovable/cicd-issues/`.
>    - Execution Plans & Subtasks: `.lovable/plans/pending/`, `.lovable/plans/subtasks/`.
>    - Coding Guidelines Mirror: `.lovable/coding-guidelines/`.
> 3. **Worker Pool & Log Aggregation Architecture:** All local runners and test orchestrators must use a concurrent worker pool (2–3 workers via `ThreadPoolExecutor`), announce enqueued tasks upfront, show real-time progress, handle failures gracefully without cancelling sibling workers, and print a consolidated final summary with full stdout/stderr error logs for failed jobs.
> 4. **`force` Keyword Support:** If the user wrote `force`, `force rebuild`, or `force create` on top of the prompt or trigger: **ALWAYS recreate/regenerate the Python runner script from scratch**, regardless of whether the file already exists on disk.
> 5. **No External or Random File Creation:** NEVER write scripts, temporary test scripts, or scratch files to root, `/tmp`, global system paths, or outside the repository boundary.

---

## AI Fix Scripts Memory (Reusable Tooling)

- [ ] `/goal` **Reuse First:** I have rigorously scanned and `/learn`ed `.lovable/ai-fix-scripts/index.md` to check if a helper script already exists before writing any new temporary code.
- [ ] **Strict In-Repository Execution:** All Python scripts (`.lovable/ai-fix-scripts/*.py`) MUST be executed strictly within the codebase repository root, NEVER outside the codebase.
- [ ] **Strict .lovable/ Folder Storage:** All AI scripts, local runners, autofixers, and helper utilities MUST be created inside `.lovable/ai-fix-scripts/`. NEVER create scripts in root or external paths.
- [ ] **Automated Naming & Style Fixers:** Use `python .lovable/ai-fix-scripts/05-naming-autofixer.py` and `02-guideline-autofixer.py` to audit boolean prefixes and newlines.
- [ ] **Go Generate Sync:** If you modify Go constants, enums, or stringers, you MUST run `go generate ./...` in the relevant directory (e.g., `cd gitmap && go generate ./...`) and commit the resulting generated files to prevent CI drift.
- [ ] **Commit & Track:** All new helper scripts were written strictly to `.lovable/ai-fix-scripts/` and committed to Git for future reuse.
- [ ] **Index Documentation:** I have updated `.lovable/ai-fix-scripts/index.md` using sequential script naming. For every script, I have included a `<details>` collapsible tag explaining exactly why the script is there and what it does.

---

## Pre-Reply / Loop Checklist (Must Verify Every Loop Iteration)

- [ ] Git working tree is clean before new code changes.
- [ ] Sub-agents are actively assigned disjoint files verified against `.lovable/temp/active-locks.json`.
- [ ] Completed tasks were `mv`'d to `plans/completed/` and `plans/index.md` was updated.
- [ ] 3-strike rule respected: failed tasks cleanly rolled back and logged to `last-failure.md`.
- [ ] **Strict Relative Git Paths:** All file paths, markdown links, citations, and subtask references in plans, specs, and memory logs are strictly relative to the git repository root. Zero absolute paths (`D:\...`, `C:\...`) or `file:///` URIs.
- [ ] **Semantic Naming:** All functions start with active verbs; all boolean functions start with `is`, `has`, `can`, `should`.
- [ ] **Single Return Types:** Multi-value `(T, error)` returns refactored to single `Result[T]` envelopes in services.
- [ ] **Universal `AppError`:** Zero generic `error` or `fmt.Errorf()` returns in domain logic.
- [ ] **LF Line Endings (`\n`):** All files use Unix LF line endings. Zero CRLF (`\r\n`).
- [ ] **UTF-8 Encoding (No BOM):** All files encoded in UTF-8 without BOM.
- [ ] **Single Trailing Newline:** Every file ends with exactly one terminating newline (`\n`).
- [ ] **Blank Line Before `if`:** Exactly one blank line precedes every `if` statement (unless at the top of a block).
- [ ] **Blank Line After `}`:** Exactly one blank line follows every closing brace `}` (unless closing the enclosing block).
- [ ] **Blank Line Before `return`:** Exactly one blank line precedes `return` / `throw` in multi-line blocks.
- [ ] **Zero Nested `if`:** All conditionals flattened to depth 0 using guard clauses and early returns.
- [ ] **Function Sizing:** All functions <= 8 lines preferred (hard cap 15 lines).
- [ ] Coding Guidelines & Master Consolidated File: I have fully read, checked, and strictly enforced every file in `spec/02-coding-guidelines/`, as well as the master consolidated coding guideline file at `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] /learn and apply as a /goal `.lovable/coding-guidelines/coding-guidelines.md` and also make sure the agent rules are created in the repo to read in the future quickly.
- [ ] `python linter-scripts/check-newline-styling.py` and `python linter-scripts/check-function-lengths.py` exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## Non-Negotiable Coding Guidelines Checklist (Auto-Reject on Violation)

/goal You MUST verify every item on this checklist before committing any code. If a subagent violated one of these rules, you must reject their work.

- [ ] Strict Relative Git Paths: All file paths, markdown links, citations, and subtask references in plans, specs, and memory logs are strictly relative to the git repository root. Zero absolute paths or `file:///` URIs.
- [ ] Master Guidelines: I have fully read and strictly enforced `spec/02-coding-guidelines/` and `spec/03-error-manage/` and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Result Envelope: Enforced `Result[T]` and `*AppError` across domain services.
- [ ] LF Line Endings & UTF-8 (No BOM): Verified Unix LF and UTF-8 across all files.
- [ ] Blank Line Before `if`: Verified blank line before every `if` statement across all modified files.
- [ ] Blank Line After `}`: Verified blank line after every closing brace `}` followed by code.
- [ ] Blank Line Before `return`: Verified blank line before every `return`/`throw` in multi-line blocks.
- [ ] Zero Nested `if`: Zero nested `if` statements (depth > 1).
- [ ] /learn the section as a /goal [AI Fix Scripts Memory](#ai-fix-scripts-memory)
- [ ] Action Summary: I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to prove I did not hallucinate.

---

## Mandatory Linter & CI/CD Integration

1. **Linter Scripts:** `linter-scripts/check-function-lengths.py`, `linter-scripts/check-mws-error-codes.py`, `linter-scripts/check-newline-styling.py`
2. **Local Run Command:** `python linter-scripts/check-function-lengths.py`
3. **Autofixer Command:** `python .lovable/ai-fix-scripts/02-guideline-autofixer.py <file>`
4. **CI/CD Integration (`.github/workflows/ci.yml`):**
   ```yaml
   - name: Validate Function Signatures & Error Envelopes
     run: |
       python linter-scripts/check-function-lengths.py
       python linter-scripts/check-mws-error-codes.py
       python linter-scripts/check-newline-styling.py
   ```
5. **Runner Registration (`.lovable/ai-fix-scripts/03-cicd-local-runner.py`):**
   ```python
   JOBS = {
       "Function Signatures Check": [sys.executable, "linter-scripts/check-function-lengths.py"],
       "Error Codes Check": [sys.executable, "linter-scripts/check-mws-error-codes.py"],
       "Newline Styling Check": [sys.executable, "linter-scripts/check-newline-styling.py"],
   }
   ```
