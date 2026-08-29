# Coding Guideline Execution Suite (`cg-execute`) — Index & Catalog

Welcome to the **Coding Guideline Execution Prompts (`cg-execute`)** suite. This catalog registers all specialized, sequenced prompts designed to enforce, audit, and autonomously refactor codebases against the master coding standards.

Every prompt in this suite is engineered with the standardized **N-Step Autonomous Self-Loop Architecture** (`N = 200` by default), splitting work equally between deep scanning/spec writing/skill creation (Phase 1) and autonomous subtask execution with automated linter enforcement (Phase 2).

---

## Prompts Catalog & Execution Order

Prompts are sequenced according to priority. Error management and reliability must always precede syntax and whitespace styling:

| Sequence | File | Title | Trigger Keywords | Focus Area | Linter Hook (`linter-scripts/`) |
|:---:|---|---|---|---|---|
| **01** | [`01-index.md`](file:///d:/work/02-prompts/prompt-architect/01-general-prompts/15-cg-execute/01-index.md) | Prompts Catalog & Registry | `cg-index`, `cg-execute index` | Master overview, lifecycle architecture, prompt routing | — |
| **02** | [`02-error-management.md`](file:///d:/work/02-prompts/prompt-architect/01-general-prompts/15-cg-execute/02-error-management.md) | Error Management & Architecture | `cg-error`, `cg-execute error`, `audit error` | `AppError` context wrappers, zero swallowed errors, universal `{ data, errors, meta }` response envelopes, anti-panic/exit rules | `check-mws-error-codes.py`, `validate-guidelines.py` |
| **03** | [`03-boolean-and-naming.md`](file:///d:/work/02-prompts/prompt-architect/01-general-prompts/15-cg-execute/03-boolean-and-naming.md) | Booleans, Naming & Enums | `cg-boolean`, `cg-execute boolean`, `audit boolean` | Positive boolean prefixes (`is`, `has`, `can`, `should`), no `== true`, no mixed polarity (`if a && !b`), semantic naming, `*Type` enum suffix | `check-enum-and-boolean.mjs`, `02-guideline-autofixer.py` |
| **04** | [`04-data-and-schema.md`](file:///d:/work/02-prompts/prompt-architect/01-general-prompts/15-cg-execute/04-data-and-schema.md) | Database & Data Schema Rules | `cg-schema`, `cg-execute schema`, `audit schema` | PascalCase tables, camelCase columns, `{TableName}Id` primary/foreign keys, Mermaid ERDs, SQLite/ORM explicit relations | `check-schema-guidelines.py` |
| **05** | [`05-react-frontend-guidelines.md`](file:///d:/work/02-prompts/prompt-architect/01-general-prompts/15-cg-execute/05-react-frontend-guidelines.md) | React & Frontend Architecture | `cg-react`, `cg-execute react`, `audit react` | Component size caps ($\le$ 100 lines), `useEffect` minimization, immutable state updates, named object hook returns (tuple ban) | `check-frontend-guidelines.mjs` |
| **06** | [`06-code-hygiene.md`](file:///d:/work/02-prompts/prompt-architect/01-general-prompts/15-cg-execute/06-code-hygiene.md) | Code Hygiene & Project Architecture | `cg-hygiene`, `cg-execute hygiene`, `audit hygiene` | File caps ($\le$ 300 lines), struct/class caps ($\le$ 120 lines), dedicated definition files, zero committed build artifacts/binaries, lowercase files | `check-file-sizes.py`, `check-placeholder-comments.py` |
| **07** | [`07-style-guidelines.md`](file:///d:/work/02-prompts/prompt-architect/01-general-prompts/15-cg-execute/07-style-guidelines.md) | Coding Style, Formatting & Line-Gaps | `cg-style`, `cg-execute style`, `audit style` | Return New Line concept (R13-R16: blank line before `return`/`throw`, blank line after `}`), 15-line function caps, flattening nested `if`, MD022/MD032 markdown spacing | `check-function-lengths.py`, `check-newline-styling.py` |

---

## Standardized N-Step Self-Loop Architecture

Every prompt in this suite operates using a strict two-phase loop budget:

```text
N = 200
PHASE_1_STEPS = N / 2   (Steps 1 .. 100: Ingest specs, scan codebase, create .agents/skills/ skill, write .lovable/plans/pending/ spec, break down into .lovable/plans/subtasks/, verify/create linter script)
PHASE_2_STEPS = N / 2   (Steps 101 .. 200: Autonomous subtask execution, surgical fixes, linter run, CI local runner verification, move completed plans to .lovable/plans/completed/)
```

### Phase 1: Scan, Spec & Subtasks (Steps 1 to N/2)

1. **Memory Ingestion:** Ingest `.lovable/coding-guidelines/coding-guidelines.md`, `.lovable/strictly-avoid.md`, and recent issues in `.lovable/memory/issues/`.
2. **Violation Scan:** Perform a comprehensive, AST-aware or targeted pattern scan across all active codebase files for violations specific to that guideline section.
3. **Master Spec Creation:** Write `.lovable/plans/pending/XX-<slug>-audit.md` capturing the full violation inventory, affected files, line numbers, and acceptance criteria.
4. **Subtask Decomposition:** Break down the master plan into granular subtasks in `.lovable/plans/subtasks/XX-<slug>/01-task.md`, `02-task.md`, etc.
5. **Linter Hook Verification:** Check if the automated linter script exists in `linter-scripts/`. If missing, generate the linter script and connect it to `.lovable/ai-fix-scripts/03-cicd-local-runner.py` and CI/CD pipelines.

### Phase 2: Autonomous Execution & Verification (Steps N/2+1 to N)

1. **Subtask Execution:** Sequentially execute each subtask, applying minimal, surgical code refactors without breaking existing tests.
2. **Linter & Autofixer Verification:** Run `python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>` and the section's dedicated linter script in `linter-scripts/`.
3. **Local CI Quality Gate:** Execute `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` to ensure all build, typecheck, lint, and test suites pass 100% green (`exit 0`).
4. **Plan Lifecycle Completion:** Move `.lovable/plans/pending/XX-<slug>-audit.md` to `.lovable/plans/completed/XX-<slug>-audit.md` and update `.lovable/plans/index.md`.
5. **Stage & Commit:** Group changes into clean commits (e.g. `refactor(guidelines): enforce <section> rules`).

---

## Mandatory Linter & CI/CD Integration Contract

Every prompt in this suite enforces that code standards must be mechanically verified by automated tooling:

1. **Specific Linter Script:** Each prompt names the exact file in `linter-scripts/` responsible for validating its rules.
2. **Auto-Creation Mandate:** If the linter script does not exist, the executing agent is strictly commanded to create it using Python/Node.js/Go.
3. **Local Execution:** The prompt provides the exact local command to execute the linter with zero external overhead.
4. **CI/CD Integration:** The prompt provides the exact configuration snippet to wire the linter script into `.github/workflows/ci.yml` and register it inside `03-cicd-local-runner.py` under the `JOBS` dictionary.

---

## Metadata

- slug: cg-execute-index
- version: 1.0.0
- status: active
