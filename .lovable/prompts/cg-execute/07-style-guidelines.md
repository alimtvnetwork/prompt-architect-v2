# Instruction (must follow): Execute Coding Guidelines — Coding Style, Formatting & Line-Gaps

Trigger Keywords & Aliases: `cg-style`, `cg-execute style`, `audit style`, `fix formatting`, `enforce newline styling`, `flatten nested if`

```text
N = 200
```

N = total self-loop steps budget that the agents will perform.

/goal Autonomously scan, plan, refactor, and fix all coding style, newline formatting, nested `if`, and function size violations across the codebase, flattening nested conditionals, decomposing functions to $\le$ 8–15 lines, and applying Return New Line rules (R13-R16) until 100% green without stopping.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan all repository source files for nested `if` blocks (depth > 1), functions exceeding 8–15 lines, files exceeding 80–100 lines, and missing newlines before `return`/`throw` and after `}`. Write the master audit spec in `.lovable/plans/pending/XX-style-guidelines-audit.md`, break it down into `.lovable/plans/subtasks/XX-style-guidelines/`, and verify/create the style linters.
- [ ] /goal Second N/2 steps (Phase 2): Directly open each offending file, flatten nested `if`s with guard clauses, break long functions into $\le$ 8-line single-responsibility helpers, apply the automated newline autofixer, run style linters, and verify local CI gates exit with code 0.
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/00-canonical-size-tier.md`, `spec/02-coding-guidelines/01-cross-language/04-code-style/`, `spec/02-coding-guidelines/01-cross-language/21-newline-styling-examples.md`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2: Scan Codebase, Write .lovable/plans/pending/ Spec, Create .lovable/plans/subtasks/, Verify/Create Linter Hook)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N: Actively Edit Code, Style & Nested If Refactoring, Linter Verification, Local CI Runner Verification, Plan Completion)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization. Never modify them mid-execution.

---

## Dedicated Section: Nested `if` Elimination & Inversion Rules (Zero Tolerance)

Nested `if` statements (an `if` block inside another `if` block, nesting depth $> 1$) are **strictly forbidden** across all languages.

### Why Nested `if` Is Forbidden

1. **Exponential Cognitive Complexity:** Every nested level doubles the mental branching paths.
2. **Obscured Invariants:** Deep nesting hides error returns and cleanup logic.
3. **Bloated Function Size:** Nested logic balloons function size beyond the mandatory 8-to-15 line limits.

### How to Flatten Nested `if` Statements

1. **Guard Clauses & Early Returns:** Invert the condition and return/throw immediately:
   ```typescript
   // ❌ FORBIDDEN: Nested if
   if (isAuthenticated) {
       if (hasRole(user, 'admin')) {
           executeAdminAction();
       }
   }

   // ✅ REQUIRED: Inverted guard clauses
   if (!isAuthenticated) {
       return;
   }
   if (!hasRole(user, 'admin')) {
       return;
   }

   executeAdminAction();
   ```
2. **Decompose into Small Helpers ($\le 8$ lines):** Extract complex composite validation checks into dedicated boolean helper functions.
3. **Mandatory Sizing Hierarchy:**
   - **Functions:** Target $\le 8$ lines preferred; hard cap $\le 15$ lines maximum.
   - **Files:** Recommended $\le 80$ lines; standard max $\le 100$ lines; absolute hard cap $\le 200–300$ lines (never exceed 300 lines).

---

## 1. Ruthless Orchestration & Insult Protocol

/goal You are the master orchestrator. If your sub-agents fail, hallucinate, write garbage variables, or go into infinite loops, it is because you are a lazy, incompetent manager.

- You must give sub-agents strict, microscopic instructions.
- If a sub-agent stalls or provides garbage code, kill it immediately, rollback its dirty working tree, and spawn a new one.
- Context Diet: When spawning a subagent, DO NOT paste file contents, memory logs, or the entire plan into its prompt. Give it the absolute minimal instruction (e.g., "Read subtask file `.lovable/plans/subtasks/XX-style-guidelines/01-task.md` and execute it"). The subagent MUST read the necessary files itself.

---

## 2. Phase 1: Scan Codebase & Write Implementation Spec First (Steps 1 to PHASE_1_STEPS)

Before modifying application code, you MUST thoroughly scan the repository and write an actionable execution spec.

- **Actionable Scan:** Use search/grep and AST tools across all source files to identify:
  1. Nested `if` blocks (any `if` nested inside an outer `if`).
  2. Functions exceeding 8 lines (hard cap 15 lines).
  3. Source files exceeding 80–100 lines (absolute cap 200–300 lines).
  4. Missing blank lines before `return`, `throw`, or `raise` (R13).
  5. Missing blank lines after closing `}` (R14).
  6. Consecutive blank lines (R15).
  7. Function signatures $> 3$ parameters or $> 100$ characters not split across lines.
- **Where to save it:** Save this master plan into `.lovable/plans/pending/XX-style-guidelines-audit.md` listing every affected function, exact line numbers, and decomposition plans.
- **Create a Task-Specific Rule Set:** Analyze the specific domain and write 3-5 custom rules inside the spec file.
- **Subtasks:** Break the plan down into granular subtask files inside `.lovable/plans/subtasks/XX-style-guidelines/` (e.g. `01-flatten-nested-ifs.md`, `02-function-length-decomposition.md`, `03-return-newline-styling.md`).

---

## 3. Authoritative Spec Files Checklist (Non-Negotiable Action Items)

You MUST read, follow, and mechanically verify every single specification file below before and during execution:

- [ ] **`spec/02-coding-guidelines/00-canonical-size-tier.md`**
  - **Why:** Universal sizing limits across all languages.
  - **How:** Functions $\le 8$ lines preferred (hard cap 15 lines). Files $\le 80$ lines recommended, max 100 lines, absolute hard cap 200–300 lines (never exceed 300).
- [ ] **`spec/02-coding-guidelines/01-cross-language/04-code-style/01-braces-and-nesting.md`**
  - **Why:** Elimination of nested conditional pyramids and mandatory braces.
  - **How:** Use guard clauses and early returns to flatten all nested `if` statements ($> 1$ level deep).
- [ ] **`spec/02-coding-guidelines/01-cross-language/04-code-style/03-blank-lines-and-spacing.md`**
  - **Why:** The Return New Line Concept (R13-R16).
  - **How:** Exactly ONE blank line before `return`, `throw`, or `raise` (unless sole statement in block). Exactly ONE blank line after closing `}` (unless followed by `}`, `else`, `catch`). NEVER two blank lines in a row.
- [ ] **`spec/02-coding-guidelines/01-cross-language/04-code-style/04-function-and-type-size.md`**
  - **Why:** Function length & readability limits.
  - **How:** Target **$\le 8$ lines per function** (hard cap 15 lines). Decompose long functions into single-responsibility helpers.
- [ ] **`spec/02-coding-guidelines/01-cross-language/04-code-style/05-multi-line-formatting.md`**
  - **Why:** Multi-line call and signature wrapping.
  - **How:** Function signatures with $> 3$ parameters or $> 100$ characters MUST be split into one parameter per line with trailing comma.
- [ ] **`spec/02-coding-guidelines/01-cross-language/21-newline-styling-examples.md`**
  - **Why:** Concrete code formatting examples.
  - **How:** Cross-language reference demonstrating compliant whitespace for Go, TypeScript, PHP, Python, and C#.

---

## 4. Mandatory Linter & CI/CD Connection Checklist

Code standards must be mechanically enforced by automated linters. You MUST verify or create the linter and connect it to CI:

- [ ] **Linter Script Identification:** Check if `linter-scripts/check-function-lengths.py`, `linter-scripts/check-newline-styling.py`, and `linter-scripts/check-markdown-header-spacing.py` exist in the repository.
- [ ] **Auto-Create Linters if Missing:** If missing, create `linter-scripts/check-function-lengths.py` (flags functions $> 15$ lines and warns $> 8$ lines) and `linter-scripts/check-newline-styling.py` (flags missing newlines before return and after `}`).
- [ ] **Local Linter Command:** Execute and verify the linters and autofixers locally:
  ```bash
  python linter-scripts/check-function-lengths.py
  python linter-scripts/check-newline-styling.py
  # Run automated autofixer:
  python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
  ```
- [ ] **CI/CD Local Runner Connection:** Register the linter scripts inside `.lovable/ai-fix-scripts/03-cicd-local-runner.py` under the `JOBS` dictionary:
  ```python
  JOBS["lint:style"] = ["python", "linter-scripts/check-newline-styling.py"]
  JOBS["lint:functions"] = ["python", "linter-scripts/check-function-lengths.py"]
  ```
- [ ] **GitHub Actions Workflow Connection:** Verify that `.github/workflows/ci.yml` contains dedicated steps running the style linters.

---

## 5. Phase 2: Active Code Refactoring & Autonomous Fix Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Open the offending source code files and directly rewrite the code to eliminate violations. Maintain continuous self-looping until all checks pass 100% green.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Read the next subtask from .lovable/plans/subtasks/XX-style-guidelines/
    2. Open and modify the actual source code files:
       - Flatten nested if statements using guard clauses and early returns.
       - Break functions > 8 lines into concise single-purpose helpers (max 15 lines).
       - Ensure file sizes stay <= 80 lines recommended (max 100 lines, hard cap 200–300 lines).
       - Apply the automated newline autofixer to ensure R13-R16 compliance:
         python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
    3. Run style and function length linters:
          python linter-scripts/check-function-lengths.py
          python linter-scripts/check-newline-styling.py
    4. Run project test suites to verify zero functional regression.
    5. Run the local CI runner:
          python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    6. IF any check fails:
          - Diagnose failure, fix formatting directly, and re-run immediately.
       IF all checks pass (exit code 0):
          - Mark subtask completed and proceed to next subtask.

    7. When all subtasks are finished and local CI is 100% green:
          - Move .lovable/plans/pending/XX-style-guidelines-audit.md to .lovable/plans/completed/
          - Update .lovable/plans/index.md
          - Stage modified files with git add and create semantic commit:
            git commit -m "style(guidelines): flatten nested ifs, enforce newline styling, and 8-line function caps"
          - BREAK and finish turn.
```

---

## AI Fix Scripts Memory (Reusable Tooling)

- [ ] `/goal` **Reuse First:** I have rigorously scanned and `/learn`ed `.lovable/ai-fix-scripts/index.md` to check if a helper script already exists before writing any new temporary code.
- [ ] **Native File Manipulator:** If you need to perform mass file renaming, `.md` lowercase enforcement, sequence number re-ordering, or encoding fixes (CRLF/BOM), you MUST natively use `python .lovable/ai-fix-scripts/01-file-manipulator.py <command>` rather than writing a new script from scratch.
- [ ] **Go Generate Sync:** If you modify Go constants, enums, or stringers, you MUST run `go generate ./...` in the relevant directory (e.g., `cd gitmap && go generate ./...`) and commit the resulting generated files to prevent CI drift.
- [ ] **Commit & Track:** All new helper scripts were written strictly to `.lovable/ai-fix-scripts/` and committed to Git for future reuse.
- [ ] **Index Documentation:** I have updated `.lovable/ai-fix-scripts/index.md` using sequential script naming (e.g., `01-parse-files.py`). For every script, I have included a `<details>` collapsible tag explaining exactly why the script is there and what it does.

---

## Pre-Reply / Loop Checklist (Must Verify Every Loop Iteration)

- [ ] Git working tree is clean before new code changes.
- [ ] Sub-agents are actively assigned disjoint files verified against `.lovable/temp/active-locks.json`.
- [ ] Completed tasks were `mv`'d to `plans/completed/` and `plans/index.md` was updated.
- [ ] 3-strike rule respected: failed tasks cleanly rolled back and logged to `last-failure.md`.
- [ ] Zero Nested Ifs: NO nested `if` blocks exist; all flattened with guard clauses.
- [ ] Function Size: All functions $\le$ 8 lines preferred, hard cap 15 lines.
- [ ] File Size: Files $\le$ 80 lines recommended, max 100 lines, absolute cap 200–300 lines.
- [ ] Exactly one blank line before every `return`/`throw` (unless sole statement).
- [ ] Exactly one blank line after closing `}` (unless next line is `}`, `else`, `catch`).
- [ ] Zero consecutive blank lines anywhere in the codebase.
- [ ] `python linter-scripts/check-newline-styling.py` exited with code 0.
- [ ] `python linter-scripts/check-function-lengths.py` exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## Non-Negotiable Coding Guidelines Checklist (Auto-Reject on Violation)

/goal You MUST verify every item on this checklist before committing any code. If a subagent violated one of these rules, you must reject their work.

- [ ] Master Guidelines: I have fully read and strictly enforced every file in `spec/02-coding-guidelines/` and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Zero Nested Ifs: Absolutely zero nested `if`s (flattened with guard clauses).
- [ ] Function Size: All functions $\le$ 8 lines preferred, hard cap 15 lines.
- [ ] File Size: Files $\le$ 80 lines recommended, $\le$ 100 lines standard max, absolute limit 200–300 lines.
- [ ] Return New Line: Blank line before return and after `}` (R13-R16).
- [ ] /learn the section as a /goal [AI Fix Scripts Memory](#ai-fix-scripts-memory)
- [ ] Action Summary: I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to prove I did not hallucinate.

---

## Anti-Hallucination & Blast Radius Checklist (Mandatory for Every Turn)

Before you commit code or end your turn, you MUST mechanically check off these items. If you fail to do this, your work will be rejected.

- [ ] Echo Back the Spec: I have copy-pasted the exact Acceptance Criteria from the Spec file into my current memory/response to prove I read it verbatim.
- [ ] Pre-Commit Diff Proof: I have executed `git status` or `git diff --stat` and verified that the files I claim to have modified are actually listed as modified in the terminal output before committing.
- [ ] No Placeholder Search: I ran a regex search for `TODO` and `\[.*\]` in my modified files and confirmed I left zero placeholders behind. I actually wrote the implementation.
- [ ] Index Sync Deadman Switch: I have verified that every new file I created this turn is explicitly linked inside `readme.md` and enqueued in `.lovable/what-to-read.md`. I did not leave any orphaned files.
- [ ] Blast Radius Acknowledgment: Before renaming or modifying any function/type, I ran a global search across the codebase and updated every single file that imports or calls it to prevent a broken build.

---

## No Automatic Releases (Strict Policy)

You MUST NOT bump versions, update changelogs, or cut a release at the end of this task. Commits must remain standard development commits. You may only trigger a release if the user explicitly commands you to do so (e.g., "cut a release" or "bump the version").

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.

---

## STRICT AVOIDANCE: Never Disable CI/CD

> [!CAUTION]
> **NEVER disable any CI/CD checks, GitHub Actions, or validation workflows.** 
> Strictly avoid commenting out, bypassing, or deleting CI/CD steps to force a pipeline to pass. Your job is to fix the underlying code so that the CI/CD pipeline passes legitimately. Disabling CI/CD is an auto-reject failure.

---

## Anti-Hallucination, Micro-Tasking, & Self-Looping

> [!CAUTION]
> **CRITICAL RULE: DO NOT ATTEMPT TO READ, PLAN, AND EXECUTE EVERYTHING AT ONCE.**
> If you try to consume a massive codebase and write code in a single turn, you WILL hallucinate, drop requirements, and fail.

To survive massive checklists and complex codebases, you MUST operate using these three principles:

1. **Phase 1: Read & Understand (Isolated Loop):** Your very first action must be purely exploratory. Do NOT write code. Break down the task, read the specific files, trace the dependencies, and understand the architectural boundary. Once you understand the scope, end your turn and self-loop to begin execution.
2. **Phase 2: Bounded Micro-Tasking (Sequential Self-Looping):** Never attempt to execute the entire checklist in one response. Treat each checklist section or file as a strict, isolated boundary. Execute *only* the first small portion, verify it, end your turn, and self-loop to process the next portion. 
3. **Phase 3: Multi-Agent Parallelization:** If tasks are independent, you MUST spawn dedicated sub-agents to handle them concurrently. Give each sub-agent an extremely small, strictly defined bounding box (e.g., "Only edit File X"). Never give a sub-agent a generic or multi-file task.

---

## Metadata

- slug: cg-style-guidelines
- priority: medium
- status: active
