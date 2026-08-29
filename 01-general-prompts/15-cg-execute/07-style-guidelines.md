# Instruction (must follow): Coding Guideline Execution — Coding Style, Formatting & Line-Gaps

Trigger Keywords & Aliases: `cg-style`, `cg-execute style`, `audit style`, `fix formatting`, `enforce newline styling`

```text
N = 100
```

N = total self-loop steps budget for scanning, spec planning, and autonomously resolving all formatting, newline, and function length violations.

- [ ] /goal First `N/2` steps (Phase 1) are dedicated to scanning the codebase for newline styling (R13-R16), function length (> 15 lines), nested `if`, and markdown spacing violations, writing the master audit spec into `.lovable/plans/pending/XX-style-guidelines-audit.md`, decomposing into subtasks in `.lovable/plans/subtasks/XX-style-guidelines/`, and verifying/creating the dedicated style linters in `linter-scripts/`.
- [ ] /goal Second `N/2` steps (Phase 2) are dedicated to executing each subtask sequentially, refactoring functions to $\le$ 15 lines, flattening nested conditionals, applying the Return New Line rules, running style linters and autofixers, and verifying all local CI gates exit with code 0.
- [ ] /learn Ingest `.lovable/coding-guidelines/coding-guidelines.md`, `spec/02-coding-guidelines/01-cross-language/21-newline-styling-examples.md`, `.lovable/strictly-avoid.md`, and `.lovable/memory/issues/` before modifying code.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization.

---

## Phase 0: Antigravity Skill Bootstrap (Memory Optimization)

Before execution, check if `.agents/skills/coding-guidelines/skill.md` exists. If missing, create it with YAML frontmatter (`name: coding-guidelines`, `description: "Audits and enforces cross-language coding style, function length, and newline formatting."`).

---

## Phase 1: Scan, Spec, Subtasks & Linter Verification (Steps 1 to PHASE_1_STEPS)

> [!IMPORTANT]
> **Phase 1 is dedicated to discovery, planning, and tooling setup. Do NOT reformat code in Phase 1.**

### Step 1: Ingest Authoritative Style & Line-Gap Rules

1. **The Return New Line Concept (R13-R16):**
   - **R13 (Blank Line Before Return):** Exactly ONE blank line before every `return`, `throw`, or `raise` statement (unless it is the only statement in the code block).
   - **R14 (Blank Line After Closing `}`):** Exactly ONE blank line after a closing `}` bracket, unless followed immediately by another `}`, `else`, `catch`, `finally`, or `case`.
   - **R15 (Never Consecutive Blank Lines):** NEVER place two or more consecutive blank lines anywhere in any file.
   - **R16 (No Blank Lines at Scope Boundaries):** No blank line immediately after `{` or immediately before `}`.
2. **Function Length Cap:** Hard cap of **15 lines per function** (excluding blank lines/comments). Target is $\le$ 8 lines. Functions exceeding 15 lines must be broken into single-responsibility helper functions.
3. **No Nested `if` Statements:** Guard clauses and early returns must be used to flatten all nested conditional branches.
4. **Grouped Imports:** Group import statements with exactly one blank line between categories (standard library, third-party, first-party absolute, first-party relative).
5. **Markdown Header & List Spacing:** Surround all markdown headers (MD022) and lists (MD032) with clean blank lines.

### Step 2: Codebase-Wide Style Scan

Search all active source and markdown files for:

- Missing blank lines before `return`, `throw`, or `raise`.
- Missing blank lines after closing `}`.
- Consecutive blank lines (`\n\n\n`).
- Functions exceeding 15 lines of logic.
- Deeply nested `if` statements ($> 1$ level deep).
- Markdown header and list spacing violations.

### Step 3: Write Master Audit Spec

Save the complete style audit to `.lovable/plans/pending/XX-style-guidelines-audit.md`:

- Document all functions $> 15$ lines with line counts and decomposition plans.
- Catalog newline and markdown spacing violations.
- Register the spec in `.lovable/plans/index.md`.

### Step 4: Decompose into Subtasks

Break down into subtasks under `.lovable/plans/subtasks/XX-style-guidelines/`:

- `01-function-length-refactoring.md` (Decomposing functions $> 15$ lines and flattening nested `if`s)
- `02-return-newline-styling.md` (Formatting blank lines around returns and closing brackets)
- `03-markdown-spacing.md` (Cleaning MD022/MD032 header and list spacing)

### Step 5: Linter Verification & CI/CD Connection (Mandatory Checklist)

- [ ] **Check Linter Script Existence:** Check if `linter-scripts/check-function-lengths.py`, `linter-scripts/check-newline-styling.py`, and `linter-scripts/check-markdown-header-spacing.py` exist.
- [ ] **Create Linter Scripts if Missing:** If missing, create `linter-scripts/check-function-lengths.py` (flags functions $> 15$ lines) and `linter-scripts/check-newline-styling.py` (flags missing newlines before return and after `}`).
- [ ] **Local Linter Command:** Verify the linters run locally with:
  ```bash
  python linter-scripts/check-function-lengths.py
  python linter-scripts/check-newline-styling.py
  # Run automated autofixer:
  python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
  ```
- [ ] **CI/CD Integration:** Connect the linters into `.lovable/ai-fix-scripts/03-cicd-local-runner.py` under `JOBS`:
  ```python
  JOBS["lint:style"] = ["python", "linter-scripts/check-newline-styling.py"]
  JOBS["lint:functions"] = ["python", "linter-scripts/check-function-lengths.py"]
  ```
  And verify both are present in `.github/workflows/ci.yml`.

---

## Phase 2: Autonomous Subtask Execution Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Sequentially execute each subtask, applying surgical refactoring and running autofixers until all style linters pass 100% green.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Read the next subtask from .lovable/plans/subtasks/XX-style-guidelines/
    2. Decompose functions > 15 lines into concise helpers and flatten nested `if`s.
    3. Run the guideline autofixer to automatically enforce newline rules (R13-R16):
          python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
    4. Run style linters:
          python linter-scripts/check-function-lengths.py
          python linter-scripts/check-newline-styling.py
    5. Run the local CI runner:
          python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    6. IF any check fails:
          - Diagnose failure, fix formatting, and re-test immediately.
       IF all checks pass (exit code 0):
          - Mark subtask completed and proceed to next subtask.

    7. When all subtasks are finished and local CI is 100% green:
          - BREAK and proceed to End of Tunnel.
```

---

## Authoritative Return New Line & Function Length Reference

```go
// BAD: No blank line before return, no blank line after }, nested if, function > 15 lines
func CalculateDiscount(user *User, order *Order) float64 {
    discount := 0.0
    if user != nil {
        if user.IsVip {
            discount = order.Total * 0.2
        } else if order.Total > 100 {
            discount = order.Total * 0.1
        }
    }
    return discount // BAD: Missing blank line before return
}

// GOOD: Guard clauses, flattened logic, blank line before return, <= 15 lines
func CalculateDiscount(user *User, order *Order) float64 {
    if user == nil || order == nil {
        return 0.0
    }

    if user.IsVip {
        return order.Total * 0.2
    }

    if order.Total > 100 {
        return order.Total * 0.1
    }

    return 0.0
}
```

---

## Pre-Reply / Loop Checklist

- [ ] All functions are $\le$ 15 lines of code.
- [ ] Exactly one blank line before every `return`/`throw` (unless sole statement).
- [ ] Exactly one blank line after closing `}` (unless next line is `}`, `else`, `catch`).
- [ ] Zero consecutive blank lines anywhere in the codebase.
- [ ] `python linter-scripts/check-newline-styling.py` exited with code 0.
- [ ] `python linter-scripts/check-function-lengths.py` exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## No Automatic Releases (Strict Policy)

> [!CAUTION]
> This is a development refactoring workflow. You MUST NOT bump versions, update changelogs, or cut a release at the end of this task. Commits must remain standard development commits (e.g. `style(guidelines): enforce newline styling and 15-line function caps`).

---

## End of Tunnel Checklist

- [ ] Function length and newline linters pass with code 0.
- [ ] `03-cicd-local-runner.py` passes 100% green.
- [ ] Master plan moved to `.lovable/plans/completed/XX-style-guidelines-audit.md`.
- [ ] Clean commit pushed to current branch.
- [ ] File Change Summary posted in chat.

---

## Metadata

- slug: cg-style-guidelines
- priority: medium
- status: active
