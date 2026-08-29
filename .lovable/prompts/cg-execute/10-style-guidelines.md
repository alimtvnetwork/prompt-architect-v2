# Instruction (must follow): Execute Coding Guidelines — Coding Style, Formatting & Line-Gaps

Trigger Keywords & Aliases: `cg-style`, `cg-execute style`, `audit style`, `fix formatting`, `enforce newline styling`, `flatten nested if`, `newline before if`, `return newline style`, `style guidelines audit`

```text
N = 200
```

N = total self-loop steps budget that the agents will perform.

/goal Autonomously scan, plan, refactor, and fix all coding style, newline formatting, blank line before `if`, blank line after `}`, blank line before `return`, nested `if`, and function size violations across the codebase, flattening nested conditionals, decomposing functions to <= 8–15 lines, enforcing standard 100-line file caps, and applying Return New Line rules (R13-R16) until 100% green without stopping.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan all repository source files for missing blank lines before `if` statements, missing blank lines after closing `}`, missing blank lines before `return`/`throw`/`raise`, nested `if` blocks (depth > 1), functions exceeding 8–15 lines, and files exceeding 100 coding lines (recommended <= 80). Write the master audit spec in `.lovable/plans/pending/XX-style-guidelines-audit.md`, break it down into `.lovable/plans/subtasks/XX-style-guidelines/`, and verify/create the style linters (`check-newline-styling.py`, `check-function-lengths.py`).
- [ ] /goal Second N/2 steps (Phase 2): Directly open each offending file, insert mandatory blank lines before `if`, after `}`, and before `return`, flatten nested if statements with guard clauses, break long functions into <= 8-line single-responsibility helpers, decompose files to <= 100 lines, run style linters and autofixers, and verify local CI gates exit with code 0 (`exit 0`).
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/00-canonical-size-tier.md`, `spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`, `spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`, `spec/02-coding-guidelines/01-cross-language/04-code-style/`, `spec/02-coding-guidelines/01-cross-language/21-newline-styling-examples.md`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2: Scan Codebase for Style & Newline Violations, Write .lovable/plans/pending/ Spec, Create .lovable/plans/subtasks/, Verify/Create Linter Hook)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N: Actively Edit Code, Insert Newlines Before if / After } / Before return, Flatten Nested Ifs, Verify Local CI)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization. Never modify them mid-execution.

---

## Dedicated Section: Comprehensive Style, Line-Gaps & Newline Gallery (Zero Tolerance)

Proper vertical spacing is essential for readability and mental parsing. Dense, squeezed code without blank lines around control flow statements leads to missed edge cases and severe cognitive fatigue.

---

### Rule 1: Mandatory Blank Line BEFORE `if` Statements (The Critical Missing Case)

Whenever an `if` statement is preceded by any executable statement (variable declaration, assignment, method call, loop, or channel operation), there **MUST be exactly one blank line before the `if`**.

*Exception:* If the `if` statement is the very first line of a function body or immediately follows an opening brace `{`, no blank line is required before it.

#### Go: Blank Line Before `if`

```go
// ❌ WRONG: No blank line before if statement (squeezed code)
func ProcessUser(id string) error {
    user, isFound := userCache.Get(id)
    if !isFound {
        return ErrUserNotFound
    }
    return nil
}

// ✅ CORRECT: Clean blank line before if statement and before return
func ProcessUser(id string) error {
    user, isFound := userCache.Get(id)

    if !isFound {
        return ErrUserNotFound
    }

    return nil
}
```

#### TypeScript / React: Blank Line Before `if`

```typescript
// ❌ WRONG: Squeezed variable declaration directly against if
function getFormattedPrice(item: Item): string {
    const rawPrice = calculateBasePrice(item);
    const hasDiscount = item.discountPercent > 0;
    if (hasDiscount) {
        return applyDiscount(rawPrice, item.discountPercent);
    }
    return formatCurrency(rawPrice);
}

// ✅ CORRECT: Separated with blank lines before if and before final return
function getFormattedPrice(item: Item): string {
    const rawPrice = calculateBasePrice(item);
    const hasDiscount = item.discountPercent > 0;

    if (hasDiscount) {
        return applyDiscount(rawPrice, item.discountPercent);
    }

    return formatCurrency(rawPrice);
}
```

#### Python: Blank Line Before `if`

```python
# ❌ WRONG: Assignment directly followed by if without blank line
def fetch_user_profile(user_id: str) -> Profile:
    auth_token = get_session_token()
    is_valid_token = verify_token(auth_token)
    if not is_valid_token:
        raise UnauthorizedError()
    return load_profile_from_db(user_id)

# ✅ CORRECT: Blank line before if and before return
def fetch_user_profile(user_id: str) -> Profile:
    auth_token = get_session_token()
    is_valid_token = verify_token(auth_token)

    if not is_valid_token:
        raise UnauthorizedError()

    return load_profile_from_db(user_id)
```

---

### Rule 2: Mandatory Blank Line AFTER Closing Brace `}` When Followed by Code

Whenever a closing brace `}` (from an `if`, `for`, `switch`, `while`, or `try/catch` block) is followed by further executable code or another statement, there **MUST be exactly one blank line after `}`**.

#### Go: Blank Line After `}`

```go
// ❌ WRONG: Closing brace squeezed against next statement
func ExecuteStep(step Step) error {
    if err := step.Validate(); err != nil {
        return err
    }
    result, err := step.Run()
    if err != nil {
        return err
    }
    return saveResult(result)
}

// ✅ CORRECT: Clean blank line after every closing brace and before every if / return
func ExecuteStep(step Step) error {
    if err := step.Validate(); err != nil {
        return err
    }

    result, err := step.Run()
    if err != nil {
        return err
    }

    return saveResult(result)
}
```

---

### Rule 3: Mandatory Blank Line BEFORE `return`, `throw`, `raise`, `yield`

In multi-line functions and blocks, there **MUST be a blank line before `return` / `throw` / `raise`**.

*Exception:* Single-statement function body (`func GetId() string { return c.Id }`) or when `return` is the immediate first statement after an opening brace `{`.

```go
// ❌ WRONG: Multi-line function with return squeezed directly under statement
func CalculateTax(amount float64, rate float64) float64 {
    base := amount * rate
    total := base + surcharge
    return total
}

// ✅ CORRECT: Blank line before return
func CalculateTax(amount float64, rate float64) float64 {
    base := amount * rate
    total := base + surcharge

    return total
}
```

---

### Rule 4: Zero Clumping of Consecutive Guard Clauses

When multiple guard clauses follow one another, each guard clause **MUST be separated by a blank line** after its closing brace `}`. Never stack guard clauses together without vertical space.

```go
// ❌ WRONG: Clumped guard clauses with zero spacing
func ValidateOrder(order *Order) error {
    if order == nil {
        return ErrNilOrder
    }
    if !order.HasItems() {
        return ErrEmptyOrder
    }
    if order.TotalAmount <= 0 {
        return ErrInvalidAmount
    }
    return nil
}

// ✅ CORRECT: Clean blank lines between every guard clause
func ValidateOrder(order *Order) error {
    if order == nil {
        return ErrNilOrder
    }

    if !order.HasItems() {
        return ErrEmptyOrder
    }

    if order.TotalAmount <= 0 {
        return ErrInvalidAmount
    }

    return nil
}
```

---

### Rule 5: Nested `if` Elimination & Guard Inversion (Zero Tolerance)

Nested `if` statements (nesting depth > 1) are **strictly forbidden**. Invert conditions and return early:

```typescript
// ❌ FORBIDDEN: Nested if with depth > 1
function processPayment(user: User, order: Order): PaymentResult {
    if (user.isActive) {
        if (order.hasValidItems) {
            if (user.hasSufficientBalance(order.total)) {
                return executeCharge(user, order);
            } else {
                return PaymentResult.InsufficientFunds;
            }
        }
    }
    return PaymentResult.Failed;
}

// ✅ REQUIRED: Inverted guard clauses with zero nesting and proper newlines
function processPayment(user: User, order: Order): PaymentResult {
    if (!user.isActive) {
        return PaymentResult.Failed;
    }

    if (!order.hasValidItems) {
        return PaymentResult.Failed;
    }

    if (!user.hasSufficientBalance(order.total)) {
        return PaymentResult.InsufficientFunds;
    }

    return executeCharge(user, order);
}
```

---

### Rule 6: Sizing Tier & Function Parameter Wrapping

1. **Functions:** Target <= 8 lines body logic preferred; hard cap of <= 15 lines maximum.
2. **Files:** Max 100 coding lines per file (recommended <= 80 lines).
3. **Parameter Wrapping:** When a function signature exceeds 3 parameters or 100 characters, break each parameter onto its own line:

```go
// ✅ CORRECT: Multi-line parameter wrapping
func CreateInvoice(
    ctx context.Context,
    customerId string,
    billingAddress *Address,
    lineItems []LineItem,
) (*Invoice, error) {
    if ctx == nil {
        return nil, ErrNilContext
    }

    return invoiceService.Generate(ctx, customerId, billingAddress, lineItems)
}
```

---

### Rule 7: No Double Blank Lines & No Leading Function Blank Line

1. **Never use 2 or more consecutive blank lines** (always normalize to exactly 1 blank line).
2. **Never place an empty blank line as the very first line of a function body** (immediately after `{`).

---

## Strict In-Repository Execution & `.lovable/` Bounding Mandate

> [!IMPORTANT]
> **STRICT IN-REPOSITORY EXECUTION & `.lovable/` STORAGE CONTRACT:**
>
> 1. **In-Codebase Execution Only:** Whenever a Python script (runner, autofixer, linter, test aggregator) is executed or created, it MUST be executed **strictly within the repository root** (current working directory), NEVER outside the codebase or against external arbitrary directories.
> 2. **Strict Folder Bounding (`.lovable/`):** All AI scripts, local runners, autofixers, helper utilities, memory issue logs, and planning files MUST be created inside the `.lovable/` folder:
>    - Python AI Scripts: `.lovable/ai-fix-scripts/` (e.g. `01-file-manipulator.py`, `02-guideline-autofixer.py`, `03-cicd-local-runner.py`, `04-relative-path-fixer.py`, `05-naming-autofixer.py`).
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
- [ ] **Automated Style & Newline Fixer:** Use `python .lovable/ai-fix-scripts/02-guideline-autofixer.py <file>` to automatically fix newlines before `return`, after `}`, and before `if`.
- [ ] **Go Generate Sync:** If you modify Go constants, enums, or stringers, you MUST run `go generate ./...` in the relevant directory (e.g., `cd gitmap && go generate ./...`) and commit the resulting generated files to prevent CI drift.
- [ ] **Commit & Track:** All new helper scripts were written strictly to `.lovable/ai-fix-scripts/` and committed to Git for future reuse.
- [ ] **Index Documentation:** I have updated `.lovable/ai-fix-scripts/index.md` using sequential script naming (e.g., `02-guideline-autofixer.py`). For every script, I have included a `<details>` collapsible tag explaining exactly why the script is there and what it does.

---

## Pre-Reply / Loop Checklist (Must Verify Every Loop Iteration)

- [ ] Git working tree is clean before new code changes.
- [ ] Sub-agents are actively assigned disjoint files verified against `.lovable/temp/active-locks.json`.
- [ ] Completed tasks were `mv`'d to `plans/completed/` and `plans/index.md` was updated.
- [ ] 3-strike rule respected: failed tasks cleanly rolled back and logged to `last-failure.md`.
- [ ] **Strict Relative Git Paths:** All file paths, markdown links, citations, and subtask references in plans, specs, and memory logs are strictly relative to the git repository root. Zero absolute paths (`D:\...`, `C:\...`) or `file:///` URIs.
- [ ] **Blank Line Before `if`:** Exactly one blank line precedes every `if` statement (unless at the very top of a block).
- [ ] **Blank Line After `}`:** Exactly one blank line follows every closing brace `}` (unless closing the enclosing block).
- [ ] **Blank Line Before `return`:** Exactly one blank line precedes `return` / `throw` in multi-line blocks.
- [ ] **Guard Clause Separation:** All consecutive guard clauses are separated by clean blank lines.
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
- [ ] Master Guidelines: I have fully read and strictly enforced `spec/02-coding-guidelines/01-cross-language/04-code-style/`, `spec/02-coding-guidelines/01-cross-language/21-newline-styling-examples.md`, and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Blank Line Before `if`: Verified blank line before every `if` statement across all modified files.
- [ ] Blank Line After `}`: Verified blank line after every closing brace `}` followed by code.
- [ ] Blank Line Before `return`: Verified blank line before every `return`/`throw` in multi-line blocks.
- [ ] Zero Nested `if`: Zero nested `if` statements (depth > 1).
- [ ] /learn the section as a /goal [AI Fix Scripts Memory](#ai-fix-scripts-memory)
- [ ] Action Summary: I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to prove I did not hallucinate.

---

## Mandatory Linter & CI/CD Integration

1. **Linter Scripts:** `linter-scripts/check-newline-styling.py`, `linter-scripts/check-function-lengths.py`, `linter-scripts/check-nested-ifs.py`
2. **Local Run Command:** `python linter-scripts/check-newline-styling.py`
3. **Autofixer Command:** `python .lovable/ai-fix-scripts/02-guideline-autofixer.py <file>`
4. **CI/CD Integration (`.github/workflows/ci.yml`):**
   ```yaml
   - name: Validate Newline Styling & Function Lengths
     run: |
       python linter-scripts/check-newline-styling.py
       python linter-scripts/check-function-lengths.py
       python linter-scripts/check-nested-ifs.py
   ```
5. **Runner Registration (`.lovable/ai-fix-scripts/03-cicd-local-runner.py`):**
   ```python
   JOBS = {
       "Newline Styling Check": [sys.executable, "linter-scripts/check-newline-styling.py"],
       "Function Lengths Check": [sys.executable, "linter-scripts/check-function-lengths.py"],
       "Nested If Check": [sys.executable, "linter-scripts/check-nested-ifs.py"],
   }
   ```
