# Instruction (must follow): Coding Guideline Execution — Booleans, Naming & Enums

Trigger Keywords & Aliases: `cg-boolean`, `cg-execute boolean`, `audit boolean`, `fix boolean naming`, `enforce enum standards`

```text
N = 100
```

N = total self-loop steps budget for scanning, spec planning, and autonomously resolving all boolean, naming, and enum guideline violations.

- [ ] /goal First `N/2` steps (Phase 1) are dedicated to scanning the codebase for boolean, naming, and enum violations, writing the master audit spec into `.lovable/plans/pending/XX-boolean-and-naming-audit.md`, decomposing into subtasks in `.lovable/plans/subtasks/XX-boolean-and-naming/`, and verifying/creating the dedicated boolean & naming linter in `linter-scripts/`.
- [ ] /goal Second `N/2` steps (Phase 2) are dedicated to executing each subtask sequentially, refactoring variables, conditions, and enums to adhere strictly to positive prefixes, implicit checks, and `*Type` suffixes, running the linters, and verifying all local CI gates exit with code 0.
- [ ] /learn Ingest `.lovable/coding-guidelines/coding-guidelines.md`, `spec/02-coding-guidelines/`, `.lovable/strictly-avoid.md`, and `.lovable/memory/issues/` before modifying code.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization.

---

## Phase 0: Antigravity Skill Bootstrap (Memory Optimization)

Before execution, check if `.agents/skills/coding-guidelines/skill.md` exists. If missing, create it with YAML frontmatter (`name: coding-guidelines`, `description: "Audits and enforces cross-language coding standards, booleans, and naming."`).

---

## Phase 1: Scan, Spec, Subtasks & Linter Verification (Steps 1 to PHASE_1_STEPS)

> [!IMPORTANT]
> **Phase 1 is dedicated to discovery, planning, and tooling setup. Do NOT refactor business code in Phase 1.**

### Step 1: Ingest Authoritative Boolean & Naming Rules

1. **Positive Boolean Prefixes:** Every boolean variable MUST start with one of: `is`, `has`, `can`, `should`, `was`, `will`, `did`, `must` (e.g. `isReady`, `hasPermission`, `canSubmit`). Negative names (`isNotReady`, `disableCache`, `hasNoAccess`) are strictly banned.
2. **TOTAL BAN on Explicit True Checks:** NEVER evaluate a boolean explicitly against `true` (e.g. `if isReady == true` or `if (isValid === true)`). Positive booleans MUST ALWAYS be evaluated implicitly: `if isReady { ... }` or `if (isValid) { ... }`.
3. **No Mixed Polarity:** NEVER combine a positive check and a negative check in the same condition (e.g. `if isA && !isB`). Extract to a named boolean variable: `isConditionMet = isA && isBDisabled; if isConditionMet { ... }`.
4. **Anti-Garbage Semantic Naming:** Generic, non-descriptive names (`temp`, `data`, `obj`, `item`, `input100`, `foo`, `bar`, `comp_100`) are FORBIDDEN. All identifiers must reflect their exact domain purpose (e.g. `userProfilePayload`, `activeConnectionRecord`).
5. **Enum Naming Convention:** All enum types MUST end with the suffix `Type` (e.g. `UserRoleType`, `TransactionStatusType`, `PaymentMethodType`). Enum member comparisons must be against named symbols, never raw magic strings.

### Step 2: Codebase-Wide Violation Scan

Search all active source files for:

- Explicit boolean comparisons: `== true`, `=== true`, `== false`, `=== false`.
- Mixed polarity conditional joins: `&& !`, `|| !`, `and not`, `or not`.
- Missing boolean prefixes: bare adjectives like `enabled`, `valid`, `active`, `ready` (must be `isEnabled`, `isValid`, `isActive`, `isReady`).
- Generic variable names: `temp`, `data`, `obj`, `item`, `res`, `val`, `input100`.
- Enums missing the `Type` suffix (e.g. `enum UserRole` vs `enum UserRoleType`).

### Step 3: Write Master Audit Spec

Save the violation inventory to `.lovable/plans/pending/XX-boolean-and-naming-audit.md`:

- Document exact files, line numbers, variable names, and required refactoring replacements.
- Register the spec in `.lovable/plans/index.md`.

### Step 4: Decompose into Subtasks

Break down into subtasks under `.lovable/plans/subtasks/XX-boolean-and-naming/`:

- `01-boolean-comparisons.md` (Removing explicit `== true` and fixing mixed polarity)
- `02-variable-renaming.md` (Refactoring non-standard boolean prefixes and garbage names)
- `03-enum-standardization.md` (Standardizing `*Type` suffixes and eliminating magic strings)

### Step 5: Linter Verification & CI/CD Connection (Mandatory Checklist)

- [ ] **Check Linter Script Existence:** Check if `linter-scripts/check-enum-and-boolean.mjs` or `linter-scripts/validate-guidelines.py` exists.
- [ ] **Create Linter Script if Missing:** If no boolean linter exists, create `linter-scripts/check-enum-and-boolean.mjs` or `linter-scripts/check-boolean-naming.py` that AST-scans for explicit `== true` comparisons, non-prefixed booleans, and enums missing `Type` suffix.
- [ ] **Local Linter Command:** Verify the linter runs locally with:
  ```bash
  node linter-scripts/check-enum-and-boolean.mjs
  # Or Python equivalent:
  python .lovable/ai-fix-scripts/02-guideline-autofixer.py --check
  ```
- [ ] **CI/CD Integration:** Connect the linter into `.lovable/ai-fix-scripts/03-cicd-local-runner.py` under `JOBS`:
  ```python
  JOBS["lint:booleans"] = ["node", "linter-scripts/check-enum-and-boolean.mjs"]
  ```
  And verify it is connected into `.github/workflows/ci.yml`.

---

## Phase 2: Autonomous Subtask Execution Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Sequentially execute each subtask, applying surgical refactoring until all boolean and naming checks pass 100% green.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Read the next subtask from .lovable/plans/subtasks/XX-boolean-and-naming/
    2. Apply surgical refactoring (implicit booleans, positive prefixes, *Type enums, semantic names).
    3. Run the guideline autofixer to automatically clean boolean patterns:
          python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
    4. Run the dedicated boolean linter:
          node linter-scripts/check-enum-and-boolean.mjs
    5. Run the local CI runner:
          python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    6. IF any check fails:
          - Diagnose failure, fix code, and re-run immediately.
       IF all checks pass (exit code 0):
          - Mark subtask completed and proceed to next subtask.

    7. When all subtasks are finished and local CI is 100% green:
          - BREAK and proceed to End of Tunnel.
```

---

## Authoritative Boolean & Naming Code Reference

```typescript
// BAD: Explicit true, negative boolean, mixed polarity, garbage naming
const disabled = false;
const valid = true;
if (valid === true && !disabled) {
    const temp = fetch();
}

// GOOD: Positive prefixes, implicit evaluation, no mixed polarity, semantic naming
const isEnabled = true;
const isValid = true;
const canProcessTransaction = isValid && isEnabled;

if (canProcessTransaction) {
    const userAccountRecord = fetchUserAccount();
}

// BAD: Enum missing Type suffix, raw string comparison
enum UserRole { Admin, Member }
if (role === "Admin") { ... }

// GOOD: *Type suffix, symbol comparison
enum UserRoleType { Admin = "ADMIN", Member = "MEMBER" }
if (role === UserRoleType.Admin) { ... }
```

---

## Pre-Reply / Loop Checklist

- [ ] Zero explicit `== true` / `=== true` / `== false` checks in modified files.
- [ ] Zero mixed polarity conditions (`if a && !b` extracted to named boolean).
- [ ] All booleans start with `is`, `has`, `can`, `should`, `was`, `will`, `did`, or `must`.
- [ ] All enums end with `Type` suffix.
- [ ] No generic garbage names (`temp`, `data`, `obj`, `item`).
- [ ] `node linter-scripts/check-enum-and-boolean.mjs` exited with code 0.
- [ ] `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## No Automatic Releases (Strict Policy)

> [!CAUTION]
> This is a development refactoring workflow. You MUST NOT bump versions, update changelogs, or cut a release at the end of this task. Commits must remain standard development commits (e.g. `refactor(naming): normalize booleans and enums`).

---

## End of Tunnel Checklist

- [ ] All boolean and naming linters pass cleanly (`exit 0`).
- [ ] Local CI runner `03-cicd-local-runner.py` exits with code 0.
- [ ] Master plan moved to `.lovable/plans/completed/XX-boolean-and-naming-audit.md`.
- [ ] Clean git commit pushed to current branch.
- [ ] File Change Summary posted in chat.

---

## Metadata

- slug: cg-boolean-and-naming
- priority: high
- status: active
