# Instruction (must follow): Coding Guideline Execution Suite (`cg-execute`) — Index & Catalog

```text
N = 200
```

N = total self-loop steps budget that the agents will perform.

/goal Autonomously orchestrate and execute coding standard compliance across the repository by directly scanning files, generating verifiable audit specs, actively refactoring source code, and verifying with automated linters until 100% green without stopping.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan the target codebase using search and read tools, catalog every violation into an exhaustive ledger table, write the master audit spec in `.lovable/plans/pending/`, decompose into granular subtasks in `.lovable/plans/subtasks/`, and verify/create the dedicated linter script.
- [ ] /goal Second N/2 steps (Phase 2): Directly edit and refactor the actual source code files, eliminate all guideline violations, execute the linter and test suites, verify changes with `git status`/`git diff`, and verify all local CI quality gates exit with code 0.
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/00-canonical-size-tier.md`, `spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`, `spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`, `spec/02-coding-guidelines/`, `spec/03-error-manage/`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2: Scan, Spec with Violation Ledger in .lovable/plans/pending/, Subtasks, Linter Hook)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N: Active Code Refactoring, Disk Verification, Linter Verification, Local CI Runner Verification, Plan Completion)
```

---

## Prompts Catalog & Execution Order

Prompts are sequenced according to priority. Error management, control-flow flattening, and core semantics precede presentation styling:

| Sequence | File | Title | Trigger Keywords | Focus Area | Linter Hook (`linter-scripts/`) |
|:---:|---|---|---|---|---|
| **01** | [`01-index.md`](./01-index.md) | Prompts Catalog & Registry | `cg-index`, `cg-execute index` | Master overview, lifecycle architecture, prompt routing | — |
| **02** | [`02-error-management.md`](./02-error-management.md) | Error Management & Architecture | `cg-error`, `cg-execute error`, `audit error` | `AppError` context wrappers, zero dual-handling (leafs return `error`, callers handle exits), typed exit enums, specialized exit helpers, universal envelopes | `check-mws-error-codes.py`, `validate-guidelines.py` |
| **03** | [`03-nested-if-and-guard-clauses.md`](./03-nested-if-and-guard-clauses.md) | Nested `if` Elimination & Guard Clauses | `cg-nested-if`, `cg-execute nested-if`, `audit nested if` | Zero tolerance for nested if statements (depth > 1), condition inversion, early guard returns, validation helper extraction | `check-nested-ifs.py`, `02-guideline-autofixer.py` |
| **04** | [`04-booleans-and-complex-conditions.md`](./04-booleans-and-complex-conditions.md) | Booleans, Negatives & Complex Conditions | `cg-boolean`, `cg-execute boolean`, `audit boolean` | Affirmative prefixes (`is`, `has`), zero `== true`, positive framing (ban `!isSuccess` / `isNot*`), elimination of mixed polarity (`if a && !b`) | `check-boolean-guidelines.py`, `check-enum-and-boolean.mjs` |
| **05** | [`05-constants-and-enums.md`](./05-constants-and-enums.md) | Constants, Enums & Magic Literal Elimination | `cg-enums`, `cg-constants`, `cg-execute enums` | Mandatory `*Type` enum suffix, zero magic string/integer literals, centralized constants packages, typed enum function arguments | `check-enum-guidelines.py` |
| **06** | [`06-data-and-schema.md`](./06-data-and-schema.md) | Database & Data Schema Rules | `cg-schema`, `cg-execute schema`, `audit schema` | PascalCase tables, camelCase columns, `{TableName}Id` primary/foreign keys, Mermaid ERDs, SQLite/ORM explicit relations, zero nested if statements | `check-schema-guidelines.py` |
| **07** | [`07-react-frontend-guidelines.md`](./07-react-frontend-guidelines.md) | React & Frontend Architecture | `cg-react`, `cg-execute react`, `audit react` | Component size caps (<= 100 lines, recommended <= 80), functions (<= 8–15 lines), zero nested if statements, `useEffect` minimization, immutable state, named hook objects | `check-frontend-guidelines.mjs` |
| **08** | [`08-code-hygiene.md`](./08-code-hygiene.md) | Code Hygiene, File Caps & Parameter Reduction | `cg-hygiene`, `cg-execute hygiene`, `audit hygiene` | File caps (<= 100 lines coding max, recommended <= 80), functions (<= 8–15 lines), parameter reduction via specialized helpers, struct caps (<= 120 lines) | `check-file-sizes.py`, `check-placeholder-comments.py` |
| **09** | [`09-style-guidelines.md`](./09-style-guidelines.md) | Coding Style, Formatting & Line-Gaps | `cg-style`, `cg-execute style`, `audit style` | Return New Line concept (R13-R16: blank line before `return`/`throw`, blank line after `}`), zero nested if statements, <= 8–15 line function caps, MD022/MD032 spacing | `check-function-lengths.py`, `check-newline-styling.py` |
| **10** | [`10-testing-and-coverage.md`](./10-testing-and-coverage.md) | Integration, E2E & Branch Test Coverage | `cg-test`, `cg-execute test`, `audit tests`, `write e2e tests` | Three-part semantic naming (`TestUnit_Scenario_Outcome`), <= 8-line function decomposition, zero nested if statements, positive/negative/error branch coverage | `check-test-coverage.py`, `03-cicd-local-runner.py` |
| **11** | [`11-relative-paths.md`](./11-relative-paths.md) | Strict Relative Git Paths & Absolute Path Elimination | `cg-relative-paths`, `cg-execute relative-paths`, `fix absolute paths`, `fix file paths` | Total ban on absolute paths (`D:\...`, `/home/...`) and `file:///` URIs, automatic conversion to relative Git paths | `check-relative-paths.py`, `04-relative-path-fixer.py` |

---

## Canonical Sizing Tier & Formatting Rules

- **Standard File Size:** Max 100 coding lines per file (recommended <= 80 lines).
- **Functions:** Target <= 8 lines of body logic; hard cap of <= 15 lines.
- **React Components:** Recommended <= 80 lines; standard max <= 100 lines.
- **Nested `if` Statements:** Zero tolerance (must be flattened with guard clauses).
- **NO Line-Compression Cheating:** Never collapse `if/else` onto a single line or delete blank lines to fit under line caps. Reduce size by decomposing into separate files.

---

## Anti-Hallucination & Verifiable Execution Protocol (Zero-Drift Mandate)

> [!CAUTION]
> **TOTAL BAN ON GHOST DIFFS, CODE TRUNCATION, AND FABRICATED PASSES:**
> AI agents frequently hallucinate progress by outputting chat diffs without modifying disk, omitting violations from memory, or inserting lazy stubs (`// ... rest of code ...`). Every step must be mechanically grounded in disk reality.

### 1. The Exhaustive Violation Ledger (Phase 1 Mandate)

- Phase 1 audit plans (`.lovable/plans/pending/XX-*-audit.md`) MUST include a markdown table tracking every single violation:
  `| Violation Id | File Path | Line Number | Exact Snippet | Planned Fix | Status (PENDING/DONE) |`
- Never group files into vague summaries like "various files in pkg/". Every file and line must be explicitly numbered.

### 2. The Disk Reality Verification Gate (Phase 2 Mandate)

- Before claiming a file was refactored, the agent MUST run `git status --porcelain` or `git diff --stat`.
- If a file claimed as modified does NOT show as modified on disk in git, the turn is an immediate hallucination failure.

### 3. Absolute Ban on Code Truncation & Stubs

- NEVER write placeholder comments like `// ... existing code ...`, `/* unchanged */`, `TODO`, `FIXME`, or `[N]`.
- All file edits MUST be 100% complete and functionally working.

### 4. Grounded Command Veracity

- NEVER claim a linter or test suite passed without executing the actual command via tool calls and capturing `exit code 0`. Fabricating test outputs results in an immediate strike.

### 5. Spec Citation & Relative Git Path Requirement (TOTAL BAN on Absolute Paths / `file:///` URIs)

- Every refactoring action, plan file (`.lovable/plans/pending/`), subtask (`.lovable/plans/subtasks/`), and memory log must cite the authoritative specification path from `spec/` or `.lovable/` using **strictly relative paths from the git root**.
- **TOTAL BAN:** NEVER write absolute filesystem paths (`D:\...`, `C:\...`, `/home/...`) or absolute file URIs (`file:///d:/...`, `file:///C:/...`) into any committed or created files.
  - ❌ **BAD:** `[SSH Commands](file:///d:/work/gitmap/.lovable/spec/commands/01-ssh-commands.md)`
  - ❌ **BAD:** `Target: file:///d:/work/gitmap/gitmap/cmd/login.go`
  - ✅ **GOOD:** `[SSH Commands](.lovable/spec/commands/01-ssh-commands.md)`
  - ✅ **GOOD:** `Target: gitmap/cmd/login.go`

---

## Standardized N-Step Self-Loop Architecture

Every prompt in this suite operates using a strict two-phase loop budget:

### Phase 1: Scan, Spec & Subtasks (Steps 1 to N/2)

1. **Memory Ingestion:** Ingest `.lovable/coding-guidelines/coding-guidelines.md`, `.lovable/strictly-avoid.md`, and recent issues in `.lovable/memory/issues/`.
2. **Violation Scan:** Perform a comprehensive scan across all active codebase files using grep and AST inspection to detect violations specific to the guideline section.
3. **Master Spec Creation:** Write `.lovable/plans/pending/XX-<slug>-audit.md` capturing the full violation ledger, affected files, line numbers, and acceptance criteria.
4. **Subtask Decomposition:** Break down the master plan into granular subtasks in `.lovable/plans/subtasks/XX-<slug>/01-task.md`, `02-task.md`, etc.
5. **Linter Hook Verification:** Check if the automated linter script exists in `linter-scripts/`. If missing, generate the linter script and connect it to `.lovable/ai-fix-scripts/03-cicd-local-runner.py` and CI/CD pipelines.

### Phase 2: Autonomous Code Refactoring & Verification (Steps N/2+1 to N)

1. **Subtask Execution:** Sequentially execute each subtask by actively opening files and rewriting code to resolve violations cleanly.
2. **Linter & Autofixer Verification:** Run `python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>` and the section's dedicated linter script in `linter-scripts/`.
3. **Local CI Quality Gate:** Execute `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` to ensure all build, typecheck, lint, and test suites pass 100% green (`exit 0`).
4. **Plan Lifecycle Completion:** Move `.lovable/plans/pending/XX-<slug>-audit.md` to `.lovable/plans/completed/XX-<slug>-audit.md` and update `.lovable/plans/index.md`.
5. **Stage & Commit:** Group changes into clean commits (e.g. `refactor(guidelines): enforce <section> rules`).

---

## Mandatory Linter & CI/CD Integration Contract

Every prompt in this suite enforces that code standards must be mechanically verified by automated tooling:

1. **Specific Linter Script:** Each prompt names the exact relative path in `linter-scripts/` responsible for validating its rules.
2. **Auto-Creation Mandate:** If the linter script does not exist, the executing agent is strictly commanded to create it using Python/Node.js/Go.
3. **Local Execution:** The prompt provides the exact local command to execute the linter with zero external overhead.
4. **CI/CD Integration:** The prompt provides the exact configuration snippet to wire the linter script into `.github/workflows/ci.yml` and register it inside `03-cicd-local-runner.py` under the `JOBS` dictionary.

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

## Metadata

- slug: cg-execute-index
- version: 2.0.0
- status: active
