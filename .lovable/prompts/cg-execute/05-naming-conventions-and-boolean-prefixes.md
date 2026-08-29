# Naming Conventions, Boolean Prefixes & Anti-Ok Variables — Coding Guideline (must follow)

Trigger Keywords & Aliases: `cg-naming`, `cg-execute naming`, `audit naming`, `fix boolean naming`, `fix naming conventions`, `fix ok boolean`, `affirmative naming`, `positive boolean naming`, `naming conventions audit`


> **Prompt Version:** 2.1.0
> **Synchronization:** Main Meta-Repo & Connected Workspaces

```text
N = 200
```

N = total self-loop steps budget that the agents will perform.

/goal Autonomously scan, plan, refactor, and fix all variable and boolean naming violations across the codebase, directly modifying source files to replace bare `ok` identifiers, eliminate negative boolean variables (`hasNo*`, `isNot*`), enforce affirmative prefixes (`is`, `has`, `can`, `should`), apply positive framing with inverted `if` guard clauses, and normalize acronym casing until 100% green without stopping.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan all repository source files using AST and regex tools to inventory all bare `ok` variable declarations, negative boolean names (`hasNoColors`, `hasNoPayload`, `isNotReady`, `isNotDisabled`), missing boolean prefixes, generic placeholder identifiers (`temp`, `data`, `comp_100`), and non-PascalCase acronyms. Write the master audit spec in `.lovable/plans/pending/XX-naming-conventions-audit.md`, break it down into `.lovable/plans/subtasks/XX-naming-conventions/`, verify or create `.lovable/ai-fix-scripts/05-naming-autofixer.py`, index it in `.lovable/ai-fix-scripts/index.md`, and verify `linter-scripts/check-naming-guidelines.py`.
- [ ] /goal Second N/2 steps (Phase 2): Directly open each offending source file, rename bare `ok` to semantic affirmative identifiers (`isAppErr`, `isFound`, `hasValue`), convert negative booleans to positive framing (`hasColors`, `hasPayload`), invert checks inside `if` guard clauses, run the naming linter and autofixer, and verify local CI gates exit with code 0 (`exit 0`).
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/00-canonical-size-tier.md`, `spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`, `spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`, `spec/02-coding-guidelines/01-cross-language/02-boolean-principles.md`, `spec/02-coding-guidelines/01-cross-language/10-function-naming.md`, `spec/02-coding-guidelines/01-cross-language/11-key-naming-pascalcase.md`, `spec/02-coding-guidelines/01-cross-language/12-no-negatives.md`, `spec/02-coding-guidelines/`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2: Scan Codebase for Naming Violations, Write .lovable/plans/pending/ Spec, Create .lovable/plans/subtasks/, Verify/Create Linter Hook)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N: Actively Edit Code, Rename Bare `ok`, Invert Negative Booleans, Enforce Positive Guards, Verify Local CI)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization. Never modify them mid-execution.

---

## Dedicated Section: Variable & Boolean Naming Architecture (Zero Tolerance)

Naming clarity is the backbone of robust code. Vague identifiers, bare `ok` variables, and negative boolean flags cause cognitive fatigue and obscure critical edge-case bugs.

### 1. Mandatory Boolean Prefix Rule

Every boolean variable, parameter, struct field, or property MUST begin with one of the approved affirmative prefixes:
`is`, `has`, `can`, `should`, `was`, `will`, `did`, `must` (PascalCase `Is`, `Has`, `Can`, `Should` for exported symbols).

- Go: `isValid`, `hasPermission`, `canExecute`, `shouldRetry` (or `IsValid`, `HasPermission`).
- TypeScript/JavaScript: `isLoaded`, `hasColors`, `hasPayload`, `canSubmit`.
- Python: `is_valid`, `has_permission`, `can_proceed`.
- C#: `IsValid`, `HasAccess`, `CanExecute`.

---

### 2. TOTAL BAN on Bare `ok` (The `ok` Anti-Pattern)

In Go type assertions, map lookups, channel receives, and comma-ok idioms, the bare identifier `ok` is **strictly forbidden**. It carries zero domain semantics and violates the mandatory boolean prefix rule.

You MUST replace bare `ok` with a domain-specific boolean starting with `is` or `has`:

| Context | ❌ FORBIDDEN (Bare `ok`) | ✅ REQUIRED (Affirmative Semantic Boolean) |
|---|---|---|
| **Type Assertion** | `appErr, ok := err.(*apperror.AppError)` | `appErr, isAppErr := err.(*apperror.AppError)` |
| **Map Lookup** | `val, ok := userMap[id]` | `val, isFound := userMap[id]` or `val, isUserExist := userMap[id]` |
| **Map Key Check** | `_, ok := headers["Authorization"]` | `_, hasAuthHeader := headers["Authorization"]` |
| **Channel Receive** | `msg, ok := <-msgChan` | `msg, hasMessage := <-msgChan` or `msg, isChannelOpen := <-msgChan` |
| **Type Switch / Cast** | `str, ok := val.(string)` | `str, isString := val.(string)` |
| **Status Tuples** | `data, ok := fetch()` | `data, isSuccess := fetch()` |

---

### 3. TOTAL BAN on Negative Boolean Identifiers (Anti-`hasNo*`, Anti-`isNot*`)

Never name a boolean variable or property with negative prefixes or inverted words:
- ❌ **FORBIDDEN:** `hasNoColors`, `hasNoPayload`, `isNotReady`, `isNotDisabled`, `hasNoAccess`, `isNoOp`, `disallowGuest`, `unauthorized`.
- ✅ **REQUIRED:** `hasColors`, `hasPayload`, `isReady`, `isEnabled`, `hasAccess`, `isOp`, `allowGuest`, `isAuthorized`.

---

### 4. The Clean Solution: Positive Framing with Inverted `if` Guard Clauses

When you need to handle the absence, empty state, or failure condition of a resource, **ALWAYS declare the variable positively** and perform the negative check inside the `if` guard clause:

#### Go Example: Type Assertion & Guard Inversion

```go
// ❌ FORBIDDEN: Nested if with bare ok and else branch
if appErr, ok := err.(*apperror.AppError); ok {
    if appErr.Code != "E_INTERNAL_ERROR" {
        t.Errorf("expected E_INTERNAL_ERROR, got %s", appErr.Code)
    }
} else {
    t.Errorf("expected AppError, got %T", err)
}

// ✅ REQUIRED: Semantic isAppErr boolean + inverted guard clause
appErr, isAppErr := err.(*apperror.AppError)
if !isAppErr {
    t.Fatalf("expected AppError, got %T", err)
}

if appErr.Code != "E_INTERNAL_ERROR" {
    t.Errorf("expected E_INTERNAL_ERROR, got %s", appErr.Code)
}
```

#### TypeScript / React Example: Positive Framing with Inverted Guard

```tsx
// ❌ FORBIDDEN: Negative boolean variables (hasNoColors, hasNoPayload)
const hasNoColors = !colorConfig.length;
if (hasNoColors) {
    return null;
}

const hasNoPayload = !payload?.length;
if (hideLabel || hasNoPayload) {
    return null;
}

// ✅ REQUIRED: Positive boolean variables + inverted guard conditions
const hasColors = colorConfig.length > 0;
if (!hasColors) {
    return null;
}

const hasPayload = Boolean(payload?.length);
if (hideLabel || !hasPayload) {
    return null;
}
```

#### Python Example: Dictionary Lookup & Guard Inversion

```python
# ❌ FORBIDDEN: Negative boolean flag
is_not_authorized = user.role != "admin"
if is_not_authorized:
    raise PermissionDenied()

# ✅ REQUIRED: Positive boolean + inverted condition
is_authorized = user.role == "admin"
if not is_authorized:
    raise PermissionDenied()
```

---

### 5. Pros vs Cons: Why Positive Naming + Inverted Guards Is Superior

| Dimension | ❌ Negative Naming (`hasNoColors = !len`) | ✅ Positive Framing (`hasColors = len > 0; if (!hasColors)`) |
|---|---|---|
| **Cognitive Load** | **High:** Requires mental inversion on every read. | **Low:** Matches natural human language and domain models. |
| **Double Negative Risk** | **Severe:** Leads to monstrosities like `if (!hasNoColors)`. | **Zero:** Negation is always single and explicit: `if (!hasColors)`. |
| **Boolean Algebra** | **Confusing:** Combining `hasNoColors && hasNoPayload` obscures truth tables. | **Intuitive:** De Morgan's laws and logical OR/AND remain obvious. |
| **Single Source of Truth** | **Fragmented:** Some files use `hasColors`, others use `hasNoColors`. | **Standardized:** All components evaluate the presence of state uniformly. |
| **Guard Clause Flow** | **Awkward:** Hides happy-path invariants inside inverted branches. | **Clean:** Early returns eliminate nesting depth to level 0. |

---

### 6. General Variable & File Naming Conventions

1. **Strict Lowercase Filenames:** All files, scripts, documentation, and system files MUST use strictly lowercase naming (e.g., `readme.md`, `01-file-manipulator.py`, `agents.md`, `skill.md`).
2. **Anti-Garbage Variable Naming:** Absolutely NO generic garbage variable names (`comp_100.go`, `temp`, `data`, `obj`, `val1`, `item_01`, `TestHandleComp100`). All names must be semantic and domain-specific.
3. **PascalCase Acronyms:** Acronyms are formatted as regular words: first letter capitalized, remaining letters lowercase (`UserId`, `ApiUrl`, `HttpServer`, `IpAddress`, `JsonData` — NOT `UserID`, `APIURL`, `HTTPServer`).

---

## Strict In-Repository Execution & `.lovable/` Bounding Mandate

> [!IMPORTANT]
> **STRICT IN-REPOSITORY EXECUTION & `.lovable/` STORAGE CONTRACT:**
>
> 1. **In-Codebase Execution Only:** Whenever a Python script (runner, autofixer, linter, test aggregator) is executed or created, it MUST be executed **strictly within the repository root** (current working directory), NEVER outside the codebase or against external arbitrary directories.
> 2. **Strict Folder Bounding (`.lovable/`):** All AI scripts, local runners, autofixers, helper utilities, memory issue logs, and planning files MUST be created inside the `.lovable/` folder:
>    - Python AI Scripts: `.lovable/ai-fix-scripts/` (e.g. `01-file-manipulator.py`, `02-guideline-autofixer.py`, `03-cicd-local-runner.py`, `04-relative-path-fixer.py`).
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
- [ ] **Native Naming Autofixer:** If you need to scan and fix boolean naming or bare `ok` identifiers, use `python .lovable/ai-fix-scripts/02-guideline-autofixer.py <file>` or create and index `.lovable/ai-fix-scripts/05-naming-autofixer.py`.
- [ ] **Go Generate Sync:** If you modify Go constants, enums, or stringers, you MUST run `go generate ./...` in the relevant directory (e.g., `cd gitmap && go generate ./...`) and commit the resulting generated files to prevent CI drift.
- [ ] **Commit & Track:** All new helper scripts were written strictly to `.lovable/ai-fix-scripts/` and committed to Git for future reuse.
- [ ] **Index Documentation:** I have updated `.lovable/ai-fix-scripts/index.md` using sequential script naming (e.g., `05-naming-autofixer.py`). For every script, I have included a `<details>` collapsible tag explaining exactly why the script is there and what it does.

---

## Pre-Reply / Loop Checklist (Must Verify Every Loop Iteration)

- [ ] Git working tree is clean before new code changes.
- [ ] Sub-agents are actively assigned disjoint files verified against `.lovable/temp/active-locks.json`.
- [ ] Completed tasks were `mv`'d to `plans/completed/` and `plans/index.md` was updated.
- [ ] 3-strike rule respected: failed tasks cleanly rolled back and logged to `last-failure.md`.
- [ ] **Strict Relative Git Paths:** All file paths, markdown links, citations, and subtask references in plans, specs, and memory logs are strictly relative to the git repository root. Zero absolute paths (`D:\...`, `C:\...`) or `file:///` URIs.
- [ ] **Zero Bare `ok` Identifiers:** Absolutely zero bare `ok` variables in type assertions, map lookups, or status returns. All renamed to `isAppErr`, `isFound`, `hasValue`, etc.
- [ ] **Positive Boolean Framing:** All booleans named positively (`hasColors`, `hasPayload`, `isReady`). Zero `hasNo*` or `isNot*` variables.
- [ ] **Inverted Guard Clauses:** Negative checks handled via inverted guard returns (`if (!hasColors) return null;`).
- [ ] **Boolean Prefixes:** All booleans begin with `is`, `has`, `can`, `should`.
- [ ] **PascalCase Acronyms:** All acronyms formatted as `UserId`, `ApiUrl`, `JsonData`.
- [ ] Coding Guidelines & Master Consolidated File: I have fully read, checked, and strictly enforced every file in `spec/02-coding-guidelines/`, as well as the master consolidated coding guideline file at `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] /learn and apply as a /goal `.lovable/coding-guidelines/coding-guidelines.md` and also make sure the agent rules are created in the repo to read in the future quickly.
- [ ] `python linter-scripts/check-enum-and-boolean.mjs` or `python linter-scripts/check-boolean-guidelines.py` exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## Non-Negotiable Coding Guidelines Checklist (Auto-Reject on Violation)

/goal You MUST verify every item on this checklist before committing any code. If a subagent violated one of these rules, you must reject their work.

- [ ] Strict Relative Git Paths: All file paths, markdown links, citations, and subtask references in plans, specs, and memory logs are strictly relative to the git repository root. Zero absolute paths or `file:///` URIs.
- [ ] Master Guidelines: I have fully read and strictly enforced `spec/02-coding-guidelines/01-cross-language/02-boolean-principles.md`, `spec/02-coding-guidelines/01-cross-language/10-function-naming.md`, `spec/02-coding-guidelines/01-cross-language/11-key-naming-pascalcase.md`, `spec/02-coding-guidelines/01-cross-language/12-no-negatives.md`, and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Zero Bare `ok`: All type assertions and map lookups use affirmative boolean names (`isAppErr`, `isFound`).
- [ ] Positive Booleans & Inverted Guards: All booleans use affirmative names (`hasColors`, `hasPayload`); guard clauses invert condition (`if (!hasColors)`).
- [ ] /learn the section as a /goal [AI Fix Scripts Memory](#ai-fix-scripts-memory)
- [ ] Action Summary: I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to prove I did not hallucinate.

---

## Mandatory Linter & CI/CD Integration

1. **Linter Script:** `linter-scripts/check-enum-and-boolean.mjs` (or `linter-scripts/validate-guidelines.py`)
2. **Local Run Command:** `python linter-scripts/validate-guidelines.py`
3. **Autofixer Command:** `python .lovable/ai-fix-scripts/02-guideline-autofixer.py <file>`
4. **CI/CD Integration (`.github/workflows/ci.yml`):**
   ```yaml
   - name: Validate Naming & Boolean Conventions
     run: python linter-scripts/validate-guidelines.py
   ```
5. **Runner Registration (`.lovable/ai-fix-scripts/03-cicd-local-runner.py`):**
   ```python
   JOBS = {
       "Naming & Boolean Check": [sys.executable, "linter-scripts/validate-guidelines.py"],
   }
   ```
