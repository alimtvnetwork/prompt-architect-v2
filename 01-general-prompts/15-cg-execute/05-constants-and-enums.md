# Instruction (must follow): Execute Coding Guidelines — Constants, Enums & Magic Literal Elimination

Trigger Keywords & Aliases: `cg-enums`, `cg-constants`, `cg-execute enums`, `audit constants`, `fix enums`, `eliminate magic strings`, `enforce enum suffix`

```text
N = 200
```

N = total self-loop steps budget that the agents will perform.

/goal Autonomously scan, plan, refactor, and fix all constants, enums, magic string literals, and magic number violations across the codebase, modifying source files directly to enforce the `*Type` enum suffix, extract magic numbers/strings into dedicated constant files, and use typed enums in function signatures until 100% green without stopping.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan all repository source files using AST and grep tools to inventory all enums missing the `*Type` suffix, raw magic strings (e.g. `"pending"`, `"active"`, `"admin"`), magic numbers (e.g. exit code `1`, status `404`, timeouts `5000`), inline enum definitions, functions > 8 lines, and files > 100 coding lines. Write the master audit spec in `.lovable/plans/pending/XX-constants-and-enums-audit.md`, break it down into `.lovable/plans/subtasks/XX-constants-and-enums/`, and verify/create the enum linter.
- [ ] /goal Second N/2 steps (Phase 2): Directly open each offending source file, rename enums to include `*Type`, extract magic literals to centralized definition packages (`constants/`, `enums/`, `types/`), update call sites to use typed enum symbols, run the enum linter, and verify local CI gates exit with code 0.
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/00-canonical-size-tier.md`, `spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`, `spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`, `spec/02-coding-guidelines/01-cross-language/27-types-folder-convention.md`, `spec/02-coding-guidelines/`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2: Scan Codebase for Enum/Constant Violations, Write .lovable/plans/pending/ Spec, Create .lovable/plans/subtasks/, Verify/Create Linter Hook)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N: Actively Edit Code, Rename Enums with Type Suffix, Extract Constants, Update Call Sites, Verify Local CI)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization. Never modify them mid-execution.

---

## Dedicated Section: Constants, Enums & Zero Magic Literals Architecture

Hardcoded string literals and magic numbers degrade code maintainability and invite subtle runtime bugs. Enums and constants must be strictly centralized and typed.

### Mandatory Rules for Constants & Enums

1. **Mandatory `*Type` Suffix on All Enums:**
   - Every Enum type definition MUST end with `Type` (e.g. `UserRoleType`, `ExitCodeType`, `SeverityLevelType`, `FileModeType`).
   - Suffix is mandatory regardless of language (Go, TypeScript, PHP, Python, C#).

2. **Absolute Ban on Magic Numbers & Strings:**
   - NEVER pass raw integer literals (e.g. `exit(1)`, `timeout: 5000`, `retryCount: 3`) directly at call sites.
   - NEVER pass raw status/role string literals (e.g. `role == "admin"`, `status == "completed"`).
   - Extract all magic literals into named constants or enum entries in dedicated definition files.

3. **Dedicated Definition Files (No Inline Enum Sprawl):**
   - Enums and constants MUST live in dedicated packages/files (e.g. `enums/user_role.go`, `src/types/auth.types.ts`).
   - Never define enums inline inside business logic files.

4. **Go Generate & Stringer Sync:**
   - If Go enums use `stringer` or code generation, run `go generate ./...` in the package directory and commit the generated artifacts.

### Generic Code Patterns with Compliant Newline Gaps

```go
// ❌ FORBIDDEN: Magic numbers, magic strings, and enum missing Type suffix
type UserRole int

const (
    RoleAdmin UserRole = 1
)

func CheckPermission(role string) {
    if role == "admin" { // ❌ Magic string literal
        handleExit(1)    // ❌ Magic integer literal
    }
}

// ✅ REQUIRED: *Type suffix, typed enum constants, and dedicated definition
type UserRoleType string

const (
    UserRoleTypeAdmin UserRoleType = "ADMIN"
    UserRoleTypeUser  UserRoleType = "USER"
)

type ExitCodeType int

const (
    ExitCodeTypeSuccess ExitCodeType = 0
    ExitCodeTypeError   ExitCodeType = 1
)

func CheckPermission(role UserRoleType) {
    if role == UserRoleTypeAdmin {
        exitHandler.HandleWithCode(ExitCodeTypeError)
        return
    }

    exitHandler.HandleWithCode(ExitCodeTypeSuccess)
}
```

```typescript
// ❌ FORBIDDEN: Missing Type suffix and magic string comparisons
enum OrderStatus {
    Pending = 'PENDING',
    Success = 'SUCCESS',
}

function processOrder(status: string) {
    if (status === 'SUCCESS') {
        saveRecord(status);
    }
}

// ✅ REQUIRED: *Type suffix and typed parameter references
export enum OrderStatusType {
    Pending = 'PENDING',
    Success = 'SUCCESS',
}

function processOrder(status: OrderStatusType): void {
    if (status === OrderStatusType.Success) {
        saveRecord(status);
    }
}
```

---

## 1. Ruthless Orchestration & Insult Protocol

/goal You are the master orchestrator. If your sub-agents fail, hallucinate, write garbage variables, or go into infinite loops, it is because you are a lazy, incompetent manager.

- You must give sub-agents strict, microscopic instructions.
- If a sub-agent stalls or provides garbage code, kill it immediately, rollback its dirty working tree, and spawn a new one.
- Context Diet: When spawning a subagent, DO NOT paste file contents, memory logs, or the entire plan into its prompt. Give it the absolute minimal instruction (e.g., "Read subtask file `.lovable/plans/subtasks/XX-constants-and-enums/01-task.md` and execute it"). The subagent MUST read the necessary files itself.

---

## 2. Phase 1: Scan Codebase & Write Implementation Spec First (Steps 1 to PHASE_1_STEPS)

Before modifying application code, you MUST thoroughly scan the repository and write an actionable execution spec.

- **Actionable Scan:** Use search/grep and AST tools across all source files to identify:
  1. Enums missing the `Type` suffix (e.g. `enum Role`, `type Priority int`).
  2. Magic string literals used in equality comparisons (`== "active"`, `=== "failed"`).
  3. Magic integer literals passed into handlers or API calls (`HandleError(err, 1)`).
  4. Enums defined inline inside service/component files instead of dedicated definition files.
  5. Functions exceeding 8 lines (hard cap 15 lines) or files exceeding 100 coding lines (recommended <= 80).
- **Where to save it:** Save this master plan into `.lovable/plans/pending/XX-constants-and-enums-audit.md` listing every affected file, exact line numbers, and extraction plans.
- **Create a Task-Specific Rule Set:** Analyze the specific domain and write 3-5 custom rules inside the spec file.
- **Subtasks:** Break the plan down into granular subtask files inside `.lovable/plans/subtasks/XX-constants-and-enums/` (e.g. `01-enum-type-suffix-renaming.md`, `02-extract-magic-literals.md`, `03-update-call-sites.md`).

---

## 3. Authoritative Spec Files Checklist (Non-Negotiable Action Items)

You MUST read, follow, and mechanically verify every single specification file below before and during execution:

- [ ] **`spec/02-coding-guidelines/00-canonical-size-tier.md`**
  - **Why:** Universal sizing limits and enum type enforcement.
  - **How:** Structs/classes <= 120 lines. Functions <= 8 lines preferred. Files <= 100 lines coding max (recommended <= 80 lines).
- [ ] **`spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`**
  - **Why:** Comprehensive catalog of forbidden vs required generation patterns.
  - **How:** Strictly follow AH-N1 to AH-T2 rules. Zero ghost diffs, zero truncation stubs (`// ...`), zero unverified claims.
- [ ] **`spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`**
  - **Why:** Grounded rule enforcement and traceability.
  - **How:** Cite authoritative spec files for every code modification made.
- [ ] **`spec/02-coding-guidelines/01-cross-language/27-types-folder-convention.md`**
  - **Why:** Mandatory `*Type` enum suffix and definition folder organization.
  - **How:** All enums end with `Type`. All enums and constants placed in dedicated files.
- [ ] **`spec/02-coding-guidelines/01-cross-language/22-variable-naming-conventions.md`**
  - **Why:** Eliminates generic constants and magic strings.
  - **How:** Constants use descriptive PascalCase or SCREAMING_SNAKE_CASE with semantic meaning.

---

## 4. Mandatory Linter & CI/CD Connection Checklist

Code standards must be mechanically enforced by automated linters. You MUST verify or create the linter and connect it to CI:

- [ ] **Linter Script Identification:** Check if `linter-scripts/check-enum-and-boolean.mjs` or `linter-scripts/check-forbidden-strings.py` exists in the repository.
- [ ] **Auto-Create Linter if Missing:** If no dedicated enum linter exists, create `linter-scripts/check-enum-guidelines.py` that AST-scans for:
  1. Enums lacking `Type` suffix.
  2. Raw magic strings in comparisons.
  3. Magic integer exit codes in function calls.
- [ ] **Local Linter Command:** Execute and verify the linter locally:
  ```bash
  python linter-scripts/check-enum-guidelines.py
  # Run automated autofixer:
  python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
  ```
- [ ] **CI/CD Local Runner Connection:** Register the linter script inside `.lovable/ai-fix-scripts/03-cicd-local-runner.py` under the `JOBS` dictionary:
  ```python
  JOBS["lint:enums"] = ["python", "linter-scripts/check-enum-guidelines.py"]
  ```
- [ ] **GitHub Actions Workflow Connection:** Verify that `.github/workflows/ci.yml` contains a dedicated step running the enum linter.

---

## 5. Phase 2: Active Code Refactoring & Autonomous Fix Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Open the offending source code files and directly rewrite the code to eliminate violations. Maintain continuous self-looping until all checks pass 100% green.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Read the next subtask from .lovable/plans/subtasks/XX-constants-and-enums/
    2. Open and modify the actual source code files:
       - Rename all enums to end with Type suffix.
       - Extract magic strings and numbers to dedicated constant files.
       - Update call sites to reference typed enum constants.
       - If Go constants/enums changed, run go generate ./...
       - Keep function bodies <= 8 lines (max 15 lines) and files <= 100 lines.
    3. Run the enum linter:
          python linter-scripts/check-enum-guidelines.py
    4. Run project test suites to verify zero functional regression.
    5. Run the local CI runner:
          python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    6. IF any check fails:
          - Diagnose failure, fix code directly, and re-run immediately.
       IF all checks pass (exit code 0):
          - Mark subtask completed and proceed to next subtask.

    7. When all subtasks are finished and local CI is 100% green:
          - Move .lovable/plans/pending/XX-constants-and-enums-audit.md to .lovable/plans/completed/
          - Update .lovable/plans/index.md
          - Stage modified files with git add and create semantic commit:
            git commit -m "refactor(enums): enforce Type suffix, eliminate magic literals, and extract constants"
          - BREAK and finish turn.
```

---

## AI Fix Scripts Memory (Reusable Tooling)

- [ ] `/goal` **Reuse First:** I have rigorously scanned and `/learn`ed `.lovable/ai-fix-scripts/index.md` to check if a helper script already exists before writing any new temporary code.
- [ ] **Strict In-Repository Execution:** All Python scripts (`.lovable/ai-fix-scripts/*.py`) MUST be executed strictly within the codebase repository root, NEVER outside the codebase.
- [ ] **Strict .lovable/ Folder Storage:** All AI scripts, local runners, autofixers, and helper utilities MUST be created inside `.lovable/ai-fix-scripts/`. NEVER create scripts in root or external paths.
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
- [ ] All Enums end with `Type` suffix (`UserRoleType`, `ExitCodeType`).
- [ ] Zero Magic Strings: All string constants centralized and exported.
- [ ] Zero Magic Numbers: All integer codes and timeouts extracted to constants.
- [ ] Function Size: All functions <= 8 lines preferred, hard cap 15 lines.
- [ ] File Size: Files <= 100 lines coding max (recommended <= 80 lines).
- [ ] If Go enums modified, `go generate ./...` was executed and committed.
- [ ] `python linter-scripts/check-enum-guidelines.py` exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## Non-Negotiable Coding Guidelines Checklist (Auto-Reject on Violation)

/goal You MUST verify every item on this checklist before committing any code. If a subagent violated one of these rules, you must reject their work.

- [ ] Master Guidelines: I have fully read and strictly enforced `spec/02-coding-guidelines/01-cross-language/27-types-folder-convention.md` and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Enum Suffix: Every single enum ends with `Type`.
- [ ] Zero Magic Literals: All strings and numbers extracted to constants.
- [ ] Function Limits: <= 8 lines preferred, <= 15 lines max.
- [ ] File Limits: <= 100 lines coding max (recommended <= 80 lines).
- [ ] Anti-Compression: Zero single-line `if/else` or compressed whitespace tricks.
- [ ] /learn the section as a /goal [AI Fix Scripts Memory](#ai-fix-scripts-memory)
- [ ] Action Summary: I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to prove I did not hallucinate.

---

## Anti-Hallucination & Blast Radius Checklist (Mandatory for Every Turn)

Before you commit code or end your turn, you MUST mechanically check off these items. If you fail to do this, your work will be rejected.

- [ ] Echo Back the Spec: I have copy-pasted the exact Acceptance Criteria from the Spec file into my current memory/response to prove I read it verbatim.
- [ ] Exhaustive Violation Ledger: I have maintained an exact markdown table ledger in `.lovable/plans/pending/` tracking every single violation `| Id | File | Line | Snippet | Planned Fix | Status |` and reconciled every item.
- [ ] Pre-Commit Diff Proof (Disk Reality Check): I have executed `git status --porcelain` and `git diff --stat` and verified that every file I claim to have modified is actually listed as modified in the terminal output before committing.
- [ ] Zero Truncation / No Placeholder Search: I ran a regex search for `TODO`, `FIXME`, `\[.*\]`, `// ...`, and `/* ... */` in my modified files and confirmed I left zero placeholders or truncated stubs behind. I actually wrote the complete implementation.
- [ ] Verifiable Tool Execution: I did not fabricate test/linter passes. I executed the actual linter script and test runner via tool calls and captured `exit code 0`.
- [ ] Spec Citation Grounding: Every refactoring action cites the exact authoritative rule in `spec/` (e.g. `spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`).
- [ ] Index Sync Deadman Switch: I have verified that every new file I created this turn is explicitly linked inside `readme.md` and enqueued in `.lovable/what-to-read.md`. I did not leave any orphaned files.
- [ ] Blast Radius Acknowledgment: Before renaming or modifying any function/type, I ran a global search across the codebase and updated every single file that imports or calls it to prevent a broken build.

---

## No Automatic Releases (Strict Policy)

You MUST NOT bump versions, update changelogs, or cut a release at the end of this task. Commits must remain standard development commits. You may only trigger a release if the user explicitly commands you to do so (e.g., "cut a release" or "bump the version").

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.

---

## STRICT AVOIDANCE: Anti-Compression & Formatting Integrity (No Cheating)

> [!CAUTION]
> **TOTAL BAN ON LINE-COMPRESSION CHEATING:**
> When enforcing file size (<= 100 coding lines) and function size (8–15 lines), AI agents frequently attempt to "cheat" the line counter by destroying formatting. This is strictly forbidden and results in immediate rejection.

- **NO Single-Line If/Else:** NEVER collapse `if/else`, return statements, or blocks into a single line (e.g. `if (x) return y;` or `if (x) { y(); }` are strictly forbidden). Every statement requires its own line and curly braces.
- **NO Deleting Required Blank Lines (R13-R16):** NEVER delete blank lines before `return`/`throw` or after closing `}` to artificially reduce file size.
- **NO Stripping Types or Comments:** NEVER remove TypeScript types, docstrings, or clean indentation to cram code into fewer lines.
- **Mandatory Solution:** The ONLY acceptable way to satisfy line limits is **legitimate modular decomposition** — extracting helper functions into separate files and breaking large components into child components.

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

- slug: cg-constants-and-enums
- priority: medium
- status: active
