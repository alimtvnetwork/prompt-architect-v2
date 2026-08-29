# Style Guidelines, Formatting & Line-Gaps — Coding Guideline (must follow)

Trigger Keywords & Aliases: `cg-style`, `cg-execute style`, `audit style`, `fix formatting`, `enforce newline styling`, `flatten nested if`, `newline before if`, `return newline style`, `style guidelines audit`, `line gaps audit`, `fix line endings`, `enforce utf8 lf`


> **Prompt Version:** 2.1.0
> **Synchronization:** Main Meta-Repo & Connected Workspaces

```text
N = 200
```

N = total self-loop steps budget that the agents will perform.

/goal Autonomously scan, plan, refactor, and fix all coding style, newline formatting, blank line before `if`, blank line after `}`, blank line before `return`, nested `if`, function length, file size, LF line ending (`\n`), UTF-8 (no BOM) encoding, and trailing newline violations across the codebase, flattening nested conditionals, decomposing functions to <= 8–15 lines, enforcing standard 100-line file caps, and applying Return New Line rules (R13-R16) until 100% green without stopping.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan all repository source and markdown files for missing blank lines before `if` statements, missing blank lines after closing `}`, missing blank lines before `return`/`throw`/`raise`, nested `if` blocks (depth > 1), functions starting with empty lines, double blank lines (`\n\n\n`), CRLF line endings (`\r\n`), missing EOF newlines, non-UTF-8 encodings, functions exceeding 8–15 lines, and files exceeding 100 coding lines (recommended <= 80). Write the master audit spec in `.lovable/plans/pending/XX-style-guidelines-audit.md`, break it down into `.lovable/plans/subtasks/XX-style-guidelines/`, and verify/create the style linters (`check-newline-styling.py`, `check-function-lengths.py`, `check-nested-ifs.py`, `check-markdown-header-spacing.py`).
- [ ] /goal Second N/2 steps (Phase 2): Directly open each offending file, insert mandatory blank lines before `if`, after `}`, and before `return`, eliminate double blank lines, remove leading empty lines inside functions, convert line endings to LF (`\n`), ensure UTF-8 without BOM, ensure exactly one trailing newline at EOF, separate consecutive guard clauses, flatten nested if statements with early returns, break long functions into <= 8-line single-responsibility helpers, decompose files to <= 100 lines, run style linters and autofixers, and verify local CI gates exit with code 0 (`exit 0`).
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/00-canonical-size-tier.md`, `spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`, `spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`, `spec/02-coding-guidelines/01-cross-language/04-code-style/`, `spec/02-coding-guidelines/01-cross-language/21-newline-styling-examples.md`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2: Scan Codebase for Style & Newline Violations, Write .lovable/plans/pending/ Spec, Create .lovable/plans/subtasks/, Verify/Create Linter Hook)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N: Actively Edit Code, Insert Newlines Before if / After } / Before return, Normalize LF & UTF-8, Flatten Nested Ifs, Verify Local CI)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization. Never modify them mid-execution.

---

## Dedicated Section: Comprehensive Coding Style, Line-Gaps & Anti-Pattern Gallery (Zero Tolerance)

Proper vertical spacing and code hygiene are essential for readability and automated analysis. Dense, squeezed code without blank lines around control flow statements leads to missed edge cases, obscured invariants, and severe cognitive fatigue.

---

### Rule 1: Mandatory Blank Line BEFORE Control Structures (`if`, `for`, `switch`, `while`, `try`)

Whenever a control structure (`if`, `for`, `switch`, `while`, `try`) is preceded by **any statement** (variable declaration, assignment, method call, channel receive, or loop), there **MUST be exactly one blank line before the control structure**.

*Exception:* If the control structure is the **very first line** of a function body or immediately follows an opening brace `{`, no blank line is required before it.

#### 1a. Go: Blank Line Before `if`

```go
// ❌ WRONG: Squeezed variable declaration / map lookup directly against if
func ProcessUser(id string) error {
    user, isFound := userCache.Get(id)
    if !isFound {
        return ErrUserNotFound
    }
    config, isLoaded := loadConfig()
    if !isLoaded {
        return ErrConfigMissing
    }
    return executeUser(user, config)
}

// ✅ CORRECT: Clean blank line before each if statement, after each closing brace, and before return
func ProcessUser(id string) error {
    user, isFound := userCache.Get(id)

    if !isFound {
        return ErrUserNotFound
    }

    config, isLoaded := loadConfig()

    if !isLoaded {
        return ErrConfigMissing
    }

    return executeUser(user, config)
}
```

#### 1b. TypeScript / React: Blank Line Before `if`

```typescript
// ❌ WRONG: Squeezed variable declarations and function calls against if
function getFormattedPrice(item: Item): string {
    const rawPrice = calculateBasePrice(item);
    const hasDiscount = item.discountPercent > 0;
    if (hasDiscount) {
        return applyDiscount(rawPrice, item.discountPercent);
    }
    const formatted = formatCurrency(rawPrice);
    return formatted;
}

// ✅ CORRECT: Clean blank line before if and before final return
function getFormattedPrice(item: Item): string {
    const rawPrice = calculateBasePrice(item);
    const hasDiscount = item.discountPercent > 0;

    if (hasDiscount) {
        return applyDiscount(rawPrice, item.discountPercent);
    }

    const formatted = formatCurrency(rawPrice);

    return formatted;
}
```

#### 1c. Python: Blank Line Before `if`

```python
# ❌ WRONG: Assignment directly followed by if without blank line
def fetch_user_profile(user_id: str) -> Profile:
    auth_token = get_session_token()
    is_valid_token = verify_token(auth_token)
    if not is_valid_token:
        raise UnauthorizedError()
    user_record = db.find_user(user_id)
    if user_record is None:
        raise NotFoundError()
    return Profile.from_record(user_record)

# ✅ CORRECT: Clean blank line before if and before returns
def fetch_user_profile(user_id: str) -> Profile:
    auth_token = get_session_token()
    is_valid_token = verify_token(auth_token)

    if not is_valid_token:
        raise UnauthorizedError()

    user_record = db.find_user(user_id)

    if user_record is None:
        raise NotFoundError()

    return Profile.from_record(user_record)
```

#### 1d. PHP: Blank Line Before `if` and `foreach`

```php
// ❌ WRONG: Squeezed statements before if and foreach
$result = $this->apiRequest($agentId, HttpMethodType::Post->value, $endpoint);
if (is_wp_error($result)) {
    return $result;
}
$items = $this->fetchItems();
foreach ($items as $item) {
    $this->process($item);
}

// ✅ CORRECT: Separated with blank lines before control structures
$result = $this->apiRequest($agentId, HttpMethodType::Post->value, $endpoint);

if (is_wp_error($result)) {
    return $result;
}

$items = $this->fetchItems();

foreach ($items as $item) {
    $this->process($item);
}
```

#### 1e. C#: Blank Line Before `if`

```csharp
// ❌ WRONG: Squeezed method invocation against if
var account = await _accountRepository.GetByIdAsync(accountId);
if (account is null)
{
    return Result.Fail("Account not found");
}

// ✅ CORRECT: Blank line before if
var account = await _accountRepository.GetByIdAsync(accountId);

if (account is null)
{
    return Result.Fail("Account not found");
}
```

---

### Rule 2: Mandatory Blank Line AFTER Closing Brace `}` When Followed by Code

Whenever a closing brace `}` (from an `if`, `for`, `switch`, `while`, or `try/catch` block) is followed by further executable code or another statement, there **MUST be exactly one blank line after `}`**.

*Exception:* No blank line is needed when `}` is followed by another closing `}`, `else`, `catch`, `finally`, or the end of a function body.

#### 2a. Go: Blank Line After `}` Following Control Flow

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

// ✅ CORRECT: Clean blank line after every closing brace
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

#### 2b. TypeScript: Blank Line After Loops & Try/Catch

```typescript
// ❌ WRONG: Loop and try/catch squeezed against subsequent logic
for (const item of items) {
    processed.push(transform(item));
}
const result = merge(processed);

try {
    saveToStorage(result);
} catch (error) {
    logger.error(error);
}
cleanup();

// ✅ CORRECT: Blank line after each closing brace
for (const item of items) {
    processed.push(transform(item));
}

const result = merge(processed);

try {
    saveToStorage(result);
} catch (error) {
    logger.error(error);
}

cleanup();
```

---

### Rule 3: Mandatory Blank Line BEFORE `return`, `throw`, `raise`, `yield`

In multi-line functions and blocks, there **MUST be a blank line before `return` / `throw` / `raise` / `yield`**.

*Exception:* Single-statement function body (`func GetId() string { return c.Id }`) or when `return` is the immediate first statement inside a block.

```go
// ❌ WRONG: Return squeezed directly under statements
func CalculateTotal(items []Item, taxRate float64) float64 {
    subtotal := computeSubtotal(items)
    tax := subtotal * taxRate
    total := subtotal + tax
    return total
}

// ✅ CORRECT: Blank line before final return
func CalculateTotal(items []Item, taxRate float64) float64 {
    subtotal := computeSubtotal(items)
    tax := subtotal * taxRate
    total := subtotal + tax

    return total
}
```

```typescript
// ❌ WRONG: Throw squeezed under validation
function validatePayload(payload: Payload): void {
    const trimmed = payload.name.trim();
    throw new Error(`Invalid payload name: ${trimmed}`);
}

// ✅ CORRECT: Blank line before throw
function validatePayload(payload: Payload): void {
    const trimmed = payload.name.trim();

    throw new Error(`Invalid payload name: ${trimmed}`);
}
```

---

### Rule 4: Zero Clumping of Consecutive Guard Clauses

When multiple guard clauses follow one another sequentially, **each guard clause MUST be separated by a blank line** after its closing brace `}`. Never clump or stack guard clauses together without vertical breathing room.

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
    if order.IsExpired() {
        return ErrOrderExpired
    }
    return nil
}

// ✅ CORRECT: Clean blank lines between every single guard clause
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

    if order.IsExpired() {
        return ErrOrderExpired
    }

    return nil
}
```

---

### Rule 5: Nested `if` Elimination & Guard Inversion (Zero Tolerance)

Nested `if` statements (an `if` inside another `if`, nesting depth > 1) are **strictly forbidden** across all languages. Invert conditions and return early:

```typescript
// ❌ FORBIDDEN: Deep nested conditionals (depth = 3)
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

// ✅ REQUIRED: Inverted guard clauses with zero nesting and proper line gaps
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

```go
// ❌ FORBIDDEN: Nested type assertion and error checks
func HandleResponse(resp *Response) error {
    if resp != nil {
        if appErr, ok := resp.Err.(*AppError); ok {
            if appErr.IsRetryable {
                return retry(resp)
            }
        }
    }
    return nil
}

// ✅ REQUIRED: Flat guard clauses with semantic boolean and clean newlines
func HandleResponse(resp *Response) error {
    if resp == nil {
        return nil
    }

    appErr, isAppErr := resp.Err.(*AppError)

    if !isAppErr {
        return nil
    }

    if appErr.IsRetryable {
        return retry(resp)
    }

    return nil
}
```

---

### Rule 6: Mandatory Braces for All Control Blocks (No Single-Line `if`)

Every `if`, `for`, `foreach`/`for...of`, `while` block **must** use curly braces `{}` on dedicated lines, even for single-statement bodies (TypeScript, PHP, C#):

```typescript
// ❌ FORBIDDEN: Single-line unbraced if
if (isLoading) return null;
if (hasError) throw new Error("Load failed");

// ✅ REQUIRED: Multi-line braced if with blank lines
if (isLoading) {
    return null;
}

if (hasError) {
    throw new Error("Load failed");
}
```

---

### Rule 7: Multi-Line Parameter & Argument Wrapping (>2 Parameters)

When a function signature or call has **more than two arguments** or exceeds 100 characters, break each parameter onto its own line with consistent indentation, a trailing comma (where permitted), and the closing parenthesis on its own line:

```go
// ❌ FORBIDDEN: Long single-line signature (>2 params)
func BuildRecord(label string, path string, isSuccess bool, errMsg string) (*Record, error) {

// ✅ REQUIRED: Multi-line parameter wrapping
func BuildRecord(
    label string,
    path string,
    isSuccess bool,
    errMsg string,
) (*Record, error) {
    if label == "" {
        return nil, ErrEmptyLabel
    }

    return newRecord(label, path, isSuccess, errMsg)
}
```

```typescript
// ❌ FORBIDDEN: Long single-line call
const record = createAuditEntry(user.id, ActionType.Update, resource.id, StatusType.Success, metadata);

// ✅ REQUIRED: Multi-line call formatting
const record = createAuditEntry(
    user.id,
    ActionType.Update,
    resource.id,
    StatusType.Success,
    metadata,
);
```

---

### Rule 8: No Double Blank Lines & No Blank Line at Function Body Start

1. **No Consecutive Blank Lines:** Never use 2 or more consecutive blank lines in any code or markdown file (`\n\n\n` is banned). Normalize all multiple blank lines to exactly 1 blank line (`\n\n`).
2. **No Leading Blank Line:** Never place an empty line as the very first line inside a function body (immediately after the opening brace `{` or `:`).

```go
// ❌ WRONG: Empty line right after opening brace, followed by double blank lines
func ComputeMetrics() int {

    count := fetchCount()


    return count * 2
}

// ✅ CORRECT: No leading blank line, single blank line before return
func ComputeMetrics() int {
    count := fetchCount()

    return count * 2
}
```

---

### Rule 9: Universal File Hygiene, Line Endings (LF `\n` Only) & Encoding (UTF-8 No BOM)

1. **Unix LF (`\n`) Line Endings Only:**
   - Every file MUST use Unix-style line feeds (`\n`, `0x0A`).
   - Total ban on Windows CRLF (`\r\n`).
2. **Strict UTF-8 Encoding (NO BOM):**
   - All source code and markdown files MUST be saved in UTF-8 without Byte Order Mark (BOM).
   - Zero `\xef\xbb\xbf` header bytes. UTF-16 and UTF-32 are strictly forbidden.
3. **Mandatory Single Trailing Newline at EOF:**
   - Every file MUST terminate with **exactly one newline (`\n`)** on the final line.
   - Zero files missing a newline at EOF (`\ No newline at end of file` in Git diffs is an auto-reject).
   - Zero multiple trailing blank lines at the end of a file.

---

### Rule 10: Markdown Spacing (MD022 / MD032) & Heading Rules

All markdown files (`.md`) MUST have:
- **Before Header:** Exactly **ONE blank line BEFORE** every markdown heading `#` through `######` (EXCEPT when the heading is on line 1 of the file — line 1 has NO blank line before it).
- **After Header:** Exactly **ONE blank line AFTER** every markdown heading.
- **Zero Double Blank Lines:** No `\n\n\n` anywhere in markdown.
- Exactly one blank line before and after lists (`-`, `1.`), fenced code blocks (` ``` `), and blockquotes (`>`).

---

### Rule 11: Universal Sizing Tier Limits & Anti-Cheating Rules

1. **Functions:** Target <= 8 lines body logic preferred; hard cap <= 15 lines maximum.
2. **Files:** Standard max <= 100 lines of code (recommended <= 80 lines).
3. **Cheating Cheats Are Banned:**
   - Cheating by deleting necessary blank lines around `if` or `return` to fit into 8 lines is strictly forbidden.
   - Semicolon packing or multi-statement lines (`a = 1; b = 2; return a + b`) are auto-rejected.
   - Decompose logic into focused, single-responsibility helper functions instead of compressing lines.

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
- [ ] **LF Line Endings (`\n`):** All files use Unix LF line endings. Zero CRLF (`\r\n`).
- [ ] **UTF-8 Encoding (No BOM):** All files encoded in UTF-8 without BOM.
- [ ] **Single Trailing Newline:** Every file ends with exactly one terminating newline (`\n`).
- [ ] **Blank Line Before `if`:** Exactly one blank line precedes every `if` statement (unless at the very top of a block).
- [ ] **Blank Line After `}`:** Exactly one blank line follows every closing brace `}` (unless closing the enclosing block).
- [ ] **Blank Line Before `return`:** Exactly one blank line precedes `return` / `throw` in multi-line blocks.
- [ ] **Guard Clause Separation:** All consecutive guard clauses are separated by clean blank lines.
- [ ] **No Function Starts with Blank Line:** Functions start immediately on line 1 with code.
- [ ] **Zero Double Blank Lines:** No `\n\n\n` in code or markdown.
- [ ] **Markdown Heading Spacing:** Exactly one blank line before and after headings (no leading blank line on line 1).
- [ ] **Zero Nested `if`:** All conditionals flattened to depth 0 using guard clauses and early returns.
- [ ] **Function Sizing:** All functions <= 8 lines preferred (hard cap 15 lines).
- [ ] Coding Guidelines & Master Consolidated File: I have fully read, checked, and strictly enforced every file in `spec/02-coding-guidelines/`, as well as the master consolidated coding guideline file at `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] /learn and apply as a /goal `.lovable/coding-guidelines/coding-guidelines.md` and also make sure the agent rules are created in the repo to read in the future quickly.
- [ ] `python linter-scripts/check-newline-styling.py`, `python linter-scripts/check-function-lengths.py`, and `python linter-scripts/check-markdown-header-spacing.py` exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## Non-Negotiable Coding Guidelines Checklist (Auto-Reject on Violation)

/goal You MUST verify every item on this checklist before committing any code. If a subagent violated one of these rules, you must reject their work.

- [ ] Strict Relative Git Paths: All file paths, markdown links, citations, and subtask references in plans, specs, and memory logs are strictly relative to the git repository root. Zero absolute paths or `file:///` URIs.
- [ ] Master Guidelines: I have fully read and strictly enforced `spec/02-coding-guidelines/01-cross-language/04-code-style/`, `spec/02-coding-guidelines/01-cross-language/21-newline-styling-examples.md`, and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] LF Line Endings & UTF-8 (No BOM): Verified Unix LF and UTF-8 across all files.
- [ ] Blank Line Before `if`: Verified blank line before every `if` statement across all modified files.
- [ ] Blank Line After `}`: Verified blank line after every closing brace `}` followed by code.
- [ ] Blank Line Before `return`: Verified blank line before every `return`/`throw` in multi-line blocks.
- [ ] Zero Nested `if`: Zero nested `if` statements (depth > 1).
- [ ] /learn the section as a /goal [AI Fix Scripts Memory](#ai-fix-scripts-memory)
- [ ] Action Summary: I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to prove I did not hallucinate.

---

## Mandatory Linter & CI/CD Integration

1. **Linter Scripts:** `linter-scripts/check-newline-styling.py`, `linter-scripts/check-function-lengths.py`, `linter-scripts/check-nested-ifs.py`, `linter-scripts/check-markdown-header-spacing.py`
2. **Local Run Command:** `python linter-scripts/check-newline-styling.py`
3. **Autofixer Command:** `python .lovable/ai-fix-scripts/02-guideline-autofixer.py <file>`
4. **CI/CD Integration (`.github/workflows/ci.yml`):**
   ```yaml
   - name: Validate Newline Styling & Function Lengths
     run: |
       python linter-scripts/check-newline-styling.py
       python linter-scripts/check-function-lengths.py
       python linter-scripts/check-nested-ifs.py
       python linter-scripts/check-markdown-header-spacing.py
   ```
5. **Runner Registration (`.lovable/ai-fix-scripts/03-cicd-local-runner.py`):**
   ```python
   JOBS = {
       "Newline Styling Check": [sys.executable, "linter-scripts/check-newline-styling.py"],
       "Function Lengths Check": [sys.executable, "linter-scripts/check-function-lengths.py"],
       "Nested If Check": [sys.executable, "linter-scripts/check-nested-ifs.py"],
       "Markdown Header Check": [sys.executable, "linter-scripts/check-markdown-header-spacing.py"],
   }
   ```
