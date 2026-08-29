# Instruction (must follow): Coding Guideline Execution — Code Hygiene & Project Architecture

Trigger Keywords & Aliases: `cg-hygiene`, `cg-execute hygiene`, `audit hygiene`, `fix file sizes`, `enforce code hygiene`

```text
N = 100
```

N = total self-loop steps budget for scanning, spec planning, and autonomously resolving all code hygiene, file size, and artifact violations.

- [ ] /goal First `N/2` steps (Phase 1) are dedicated to scanning the entire codebase for oversized files (> 300 lines), oversized structs/classes (> 120 lines), inline definitions, committed build artifacts, and placeholder comments, writing the master audit spec into `.lovable/plans/pending/XX-code-hygiene-audit.md`, decomposing into subtasks in `.lovable/plans/subtasks/XX-code-hygiene/`, and verifying/creating the dedicated hygiene linters in `linter-scripts/`.
- [ ] /goal Second `N/2` steps (Phase 2) are dedicated to executing each subtask sequentially, extracting oversized files and inline definitions into dedicated modules, updating `.gitignore`, running file size and placeholder linters, and verifying all local CI gates exit with code 0.
- [ ] /learn Ingest `.lovable/coding-guidelines/coding-guidelines.md`, `.lovable/strictly-avoid.md`, and `.lovable/memory/issues/` before modifying code.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization.

---

## Phase 0: Antigravity Skill Bootstrap (Memory Optimization)

Before execution, check if `.agents/skills/coding-guidelines/skill.md` exists. If missing, create it with YAML frontmatter (`name: coding-guidelines`, `description: "Audits and enforces cross-language coding standards and code hygiene."`).

---

## Phase 1: Scan, Spec, Subtasks & Linter Verification (Steps 1 to PHASE_1_STEPS)

> [!IMPORTANT]
> **Phase 1 is dedicated to discovery, planning, and tooling setup. Do NOT delete or split files in Phase 1.**

### Step 1: Ingest Authoritative Code Hygiene Rules

1. **File Size Caps:**
   - Any source code file: **300 lines maximum** (excluding blank lines/comments).
   - Any class or struct definition: **120 lines maximum**.
   - Any React component (`.tsx`): **100 lines maximum**.
2. **Dedicated Definition Files:** Types, enums, interfaces, and constants MUST live in their own dedicated files (e.g. `src/types/UserRecord.ts`, `enums/OrderStatusType.go`), never defined inline next to their first use.
3. **Zero Committed Build Artifacts / Binaries:** NEVER commit generated code (`*.generated.*`), cache files (`__pycache__`, `*.pyc`), test results, temporary test data, compiled binaries (`.exe`, `.dll`, `.so`), or output directories (`build/`, `bin/`). Update `.gitignore` proactively.
4. **No Placeholder Comments:** All code must be fully implemented. Banned placeholders include `// TODO: implement later`, `/* WIP */`, and unfilled `[N]` tokens.
5. **Strict Lowercase Filenames:** All files and system paths in the repository must use strictly lowercase naming (`readme.md`, `agents.md`, `skill.md`).

### Step 2: Codebase-Wide Hygiene Scan

Search all files across the repository for:

- Files exceeding 300 lines of code.
- Classes/structs exceeding 120 lines.
- Inline type/enum/struct definitions mixed with business functions.
- Untracked or committed build artifacts (`.pyc`, compiled binaries, temp logs).
- Leftover `TODO`, `WIP`, or placeholder comments.
- Any uppercase markdown or source filenames.

### Step 3: Write Master Audit Spec

Save the complete hygiene audit to `.lovable/plans/pending/XX-code-hygiene-audit.md`:

- List all files $> 300$ lines with exact line counts and extraction plans.
- Inventory inline definitions requiring extraction to dedicated files.
- Register the spec in `.lovable/plans/index.md`.

### Step 4: Decompose into Subtasks

Break down into subtasks under `.lovable/plans/subtasks/XX-code-hygiene/`:

- `01-oversized-file-splits.md` (Decomposing files $> 300$ lines into modular packages)
- `02-definition-extractions.md` (Moving inline enums, interfaces, and structs to dedicated files)
- `03-gitignore-and-artifact-purge.md` (Updating `.gitignore` and removing committed build artifacts)

### Step 5: Linter Verification & CI/CD Connection (Mandatory Checklist)

- [ ] **Check Linter Script Existence:** Check if `linter-scripts/check-file-sizes.py`, `linter-scripts/check-placeholder-comments.py`, and `linter-scripts/check-forbidden-strings.py` exist.
- [ ] **Create Linter Script if Missing:** If missing, create `linter-scripts/check-file-sizes.py` to enforce the 300-line file cap and 120-line struct cap, and `linter-scripts/check-placeholder-comments.py` to detect `TODO`/`WIP` comments.
- [ ] **Local Linter Command:** Verify the linters run locally with:
  ```bash
  python linter-scripts/check-file-sizes.py
  python linter-scripts/check-placeholder-comments.py
  ```
- [ ] **CI/CD Integration:** Connect the linters into `.lovable/ai-fix-scripts/03-cicd-local-runner.py` under `JOBS`:
  ```python
  JOBS["lint:file-sizes"] = ["python", "linter-scripts/check-file-sizes.py"]
  JOBS["lint:placeholders"] = ["python", "linter-scripts/check-placeholder-comments.py"]
  ```
  And verify both are present in `.github/workflows/ci.yml`.

---

## Phase 2: Autonomous Subtask Execution Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Sequentially execute each subtask, decomposing oversized files and extracting definitions until all hygiene linters pass 100% green.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Read the next subtask from .lovable/plans/subtasks/XX-code-hygiene/
    2. Decompose oversized file into cohesive sub-modules (ensuring each is <= 300 lines).
    3. Extract inline enums/structs to dedicated files.
    4. Run file size and placeholder linters:
          python linter-scripts/check-file-sizes.py
          python linter-scripts/check-placeholder-comments.py
    5. Run the local CI runner:
          python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    6. IF any check fails:
          - Diagnose failure, fix import paths/file sizes, and re-test immediately.
       IF all checks pass (exit code 0):
          - Mark subtask completed and proceed to next subtask.

    7. When all subtasks are finished and local CI is 100% green:
          - BREAK and proceed to End of Tunnel.
```

---

## Pre-Reply / Loop Checklist

- [ ] All source files are $\le$ 300 lines (classes $\le$ 120 lines).
- [ ] Definitions live in dedicated files.
- [ ] `.gitignore` contains `__pycache__/`, `*.pyc`, and build artifact patterns.
- [ ] Zero committed binaries or generated artifacts.
- [ ] Zero `TODO` or placeholder comments remaining.
- [ ] `python linter-scripts/check-file-sizes.py` exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## No Automatic Releases (Strict Policy)

> [!CAUTION]
> This is a development refactoring workflow. You MUST NOT bump versions, update changelogs, or cut a release at the end of this task. Commits must remain standard development commits (e.g. `refactor(hygiene): split oversized modules and extract definitions`).

---

## End of Tunnel Checklist

- [ ] File size and placeholder linters pass with code 0.
- [ ] `03-cicd-local-runner.py` passes 100% green.
- [ ] Master plan moved to `.lovable/plans/completed/XX-code-hygiene-audit.md`.
- [ ] Clean commit pushed to current branch.
- [ ] File Change Summary posted in chat.

---

## Metadata

- slug: cg-code-hygiene
- priority: high
- status: active
