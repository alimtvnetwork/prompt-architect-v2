# Instruction (must follow): Execute Coding Guidelines — Database & Data Schema Rules

Trigger Keywords & Aliases: `cg-schema`, `cg-execute schema`, `audit schema`, `fix schema guidelines`, `enforce database standards`

```text
N = 200
```

N = total self-loop steps budget that the agents will perform.

/goal Autonomously scan, plan, refactor, and fix all database schema, model, and query violations across the codebase, modifying migration scripts and ORM entities directly to enforce PascalCase tables, camelCase columns, `{TableName}Id` integer keys, 100-line file caps, and Mermaid ERDs until 100% green without stopping.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan all active SQL schemas, migrations, and ORM model definitions for snake_case naming, non-standard primary keys, unconstrained foreign keys, functions > 8 lines, and files > 100 coding lines. Write the master audit spec in `.lovable/plans/pending/XX-data-and-schema-audit.md`, generate the Mermaid ERD, break it down into `.lovable/plans/subtasks/XX-data-and-schema/`, and verify/create the schema linter.
- [ ] /goal Second N/2 steps (Phase 2): Directly open each offending schema migration, model, and repository file, refactor tables to PascalCase, columns to camelCase, keys to `{TableName}Id` integers, decompose files ($\le$ 100 lines), run the schema linter and tests, and verify local CI gates exit with code 0.
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/00-canonical-size-tier.md`, `spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`, `spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`, `spec/04-database-conventions/`, `spec/02-coding-guidelines/`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2: Scan Codebase, Write .lovable/plans/pending/ Spec, Create .lovable/plans/subtasks/, Verify/Create Linter Hook)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N: Actively Edit Code, Schema Refactoring, Linter Verification, Local CI Runner Verification, Plan Completion)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization. Never modify them mid-execution.

---

## 1. Ruthless Orchestration & Insult Protocol

/goal You are the master orchestrator. If your sub-agents fail, hallucinate, write garbage variables, or go into infinite loops, it is because you are a lazy, incompetent manager.

- You must give sub-agents strict, microscopic instructions.
- If a sub-agent stalls or provides garbage code, kill it immediately, rollback its dirty working tree, and spawn a new one.
- Context Diet: When spawning a subagent, DO NOT paste file contents, memory logs, or the entire plan into its prompt. Give it the absolute minimal instruction (e.g., "Read subtask file `.lovable/plans/subtasks/XX-data-and-schema/01-task.md` and execute it"). The subagent MUST read the necessary files itself.

---

## 2. Phase 1: Scan Codebase & Write Implementation Spec First (Steps 1 to PHASE_1_STEPS)

Before modifying application code, you MUST thoroughly scan the repository and write an actionable execution spec.

- **Actionable Scan:** Use search/grep tools across all SQL files, migrations, and ORM entities to identify:
  1. Snake_case or kebab-case table names (e.g. `user_accounts` vs `UserAccount`).
  2. Non-standard primary keys (e.g. bare `id`, `uuid`, `user_id` vs `UserAccountId`).
  3. Snake_case column names (e.g. `created_at` vs `createdAt`).
  4. Missing foreign key constraints or un-indexed join keys.
  5. Free-form string status/type fields lacking join tables or registered enums.
  6. Files exceeding 100 coding lines (rec $\le$ 80) or functions exceeding 8 lines (hard cap 15 lines).
  7. Missing Mermaid ERDs in schema documentation.
- **Where to save it:** Save this master plan into `.lovable/plans/pending/XX-data-and-schema-audit.md` listing every affected file, exact line numbers, and the updated Mermaid ERD.
- **Create a Task-Specific Rule Set:** Analyze the specific domain and write 3-5 custom rules inside the spec file.
- **Subtasks:** Break the plan down into granular subtask files inside `.lovable/plans/subtasks/XX-data-and-schema/` (e.g. `01-primary-and-foreign-keys.md`, `02-column-naming.md`).

---

## 3. Authoritative Spec Files Checklist (Non-Negotiable Action Items)

You MUST read, follow, and mechanically verify every single specification file below before and during execution:

- [ ] **`spec/02-coding-guidelines/00-canonical-size-tier.md`**
  - **Why:** Universal size limits across all languages.
  - **How:** Functions $\le 8$ lines preferred (hard cap 15 lines). Files $\le 100$ lines coding max (recommended $\le 80$ lines). Zero line compression.
- [ ] **`spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`**
  - **Why:** Comprehensive catalog of forbidden vs required generation patterns.
  - **How:** Strictly follow AH-N1 to AH-T2 rules. Zero ghost diffs, zero truncation stubs (`// ...`), zero unverified claims.
- [ ] **`spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`**
  - **Why:** Grounded rule enforcement and traceability.
  - **How:** Cite authoritative spec files for every code modification made.
- [ ] **`spec/02-coding-guidelines/01-cross-language/04-code-style/01-braces-and-nesting.md`**
  - **Why:** Absolute zero tolerance for nested conditionals.
  - **How:** Flatten all nested `if` statements with guard clauses and early returns.
- [ ] **`spec/04-database-conventions/00-overview.md`**
  - **Why:** Authoritative database architectural foundation.
  - **How:** All schema definitions, migrations, and queries must follow SQLite-first, strongly-typed conventions.
- [ ] **`spec/04-database-conventions/01-naming-conventions.md`**
  - **Why:** Strict casing and primary key rules.
  - **How:** Tables and entities in **PascalCase** (`UserAccount`), columns and fields in **camelCase** (`userId`, `createdAt`), primary keys MUST be `{TableName}Id` integer auto-increment (`UserAccountId`). No UUID primary keys.
- [ ] **`spec/04-database-conventions/02-schema-design.md`**
  - **Why:** Standardized metadata and join constraints.
  - **How:** Entity & Reference tables MUST include `Description TEXT NULL`. Transactional tables MUST include `Notes TEXT NULL` and `Comments TEXT NULL`. `Type`/`Status` columns use join tables or registered enums, never free-form strings.
- [ ] **`spec/04-database-conventions/03-orm-and-views.md`**
  - **Why:** Explicit ORM mapping and relation integrity.
  - **How:** Explicitly declare foreign key references, cascade rules, and indexes. Never rely on implicit unconstrained relations.
- [ ] **`spec/04-database-conventions/05-relationship-diagrams.md`**
  - **Why:** Living visual documentation.
  - **How:** Every database change MUST include an updated Mermaid ERD diagram showing entities, primary/foreign keys, and relationships.
- [ ] **`spec/04-database-conventions/06-rest-api-format.md`**
  - **Why:** JSON transport serialization.
  - **How:** JSON payload keys MUST be **PascalCase** (e.g. `{ "UserAccountId": 101, "EmailAddress": "..." }`).
- [ ] **`spec/04-database-conventions/07-split-db-pattern.md`**
  - **Why:** High-performance split database partitioning.
  - **How:** If data tier uses split databases (e.g. Core vs Analytics/History), keep schemas modular and isolated.

---

## 4. Mandatory Linter & CI/CD Connection Checklist

Code standards must be mechanically enforced by automated linters. You MUST verify or create the linter and connect it to CI:

- [ ] **Linter Script Identification:** Check if `linter-scripts/check-schema-guidelines.py` exists in the repository.
- [ ] **Auto-Create Linter if Missing:** If no dedicated schema linter exists, create `linter-scripts/check-schema-guidelines.py` that AST-scans SQL files, migrations, and ORM entities for:
  1. Snake_case table or column names.
  2. Primary keys not matching `{TableName}Id` integer convention.
  3. Missing foreign key constraints or missing index declarations.
  4. Free-form string status/type fields lacking enum joins.
  5. Files exceeding 100 coding lines.
- [ ] **Local Linter Command:** Execute and verify the linter locally:
  ```bash
  python linter-scripts/check-schema-guidelines.py
  ```
- [ ] **CI/CD Local Runner Connection:** Register the linter script inside `.lovable/ai-fix-scripts/03-cicd-local-runner.py` under the `JOBS` dictionary:
  ```python
  JOBS["lint:schema"] = ["python", "linter-scripts/check-schema-guidelines.py"]
  ```
- [ ] **GitHub Actions Workflow Connection:** Verify that `.github/workflows/ci.yml` contains a dedicated step running the schema linter.

---

## 5. Phase 2: Active Code Refactoring & Autonomous Fix Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Open the offending schema and model files and directly rewrite the code to eliminate violations. Maintain continuous self-looping until all checks pass 100% green.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Read the next subtask from .lovable/plans/subtasks/XX-data-and-schema/
    2. Open and modify the actual source code and migration files:
       - Refactor table names to PascalCase and column names to camelCase.
       - Standardize primary keys to {TableName}Id integer auto-increments.
       - Enforce explicit foreign keys and join tables for status fields.
       - Decompose files <= 100 coding lines (rec <= 80) and functions <= 8 lines.
       - Update JSON serializers to output PascalCase payload keys.
    3. Run the schema linter:
          python linter-scripts/check-schema-guidelines.py
    4. Run database unit and integration test suites.
    5. Run the local CI runner:
          python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    6. IF any check fails:
          - Diagnose failure, fix schema/entity code directly, and re-run immediately.
       IF all checks pass (exit code 0):
          - Mark subtask completed and proceed to next subtask.

    7. When all subtasks are finished and local CI is 100% green:
          - Move .lovable/plans/pending/XX-data-and-schema-audit.md to .lovable/plans/completed/
          - Update .lovable/plans/index.md
          - Stage modified files with git add and create semantic commit:
            git commit -m "refactor(schema): standardize PascalCase entities, camelCase columns, and {TableName}Id keys"
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
- [ ] All table names are PascalCase.
- [ ] All column names are camelCase.
- [ ] Primary keys are `{TableName}Id` integers.
- [ ] Foreign keys explicitly defined with index support.
- [ ] Zero Nested Ifs: Flattened with guard clauses.
- [ ] Function Size: All functions $\le$ 8 lines preferred, hard cap 15 lines.
- [ ] File Size: Files $\le$ 100 lines coding max (recommended $\le$ 80 lines).
- [ ] NO Line-Compression Cheating: No single-line `if/else`, no deleted blank lines (R13-R16).
- [ ] Mermaid ERD diagram updated in schema docs.
- [ ] `python linter-scripts/check-schema-guidelines.py` exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## Non-Negotiable Coding Guidelines Checklist (Auto-Reject on Violation)

/goal You MUST verify every item on this checklist before committing any code. If a subagent violated one of these rules, you must reject their work.

- [ ] Master Guidelines: I have fully read and strictly enforced every file in `spec/04-database-conventions/` and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Zero Nested Ifs: Absolutely zero nested `if`s (flattened with guard clauses).
- [ ] Function Limits: $\le 8$ lines preferred, $\le 15$ lines max.
- [ ] File Limits: $\le 100$ lines coding max (recommended $\le 80$ lines).
- [ ] Anti-Compression: Zero single-line `if/else` or compressed whitespace tricks.
- [ ] Primary Keys: All tables use integer auto-increment `{TableName}Id` primary keys.
- [ ] Column Casing: camelCase columns, PascalCase tables, PascalCase JSON keys.
- [ ] Semantic Naming: Absolutely NO generic garbage names (`temp`, `data`, `obj`).
- [ ] Mermaid ERD: Current ERD diagram present in schema documentation.
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

- slug: cg-data-and-schema
- priority: medium
- status: active
