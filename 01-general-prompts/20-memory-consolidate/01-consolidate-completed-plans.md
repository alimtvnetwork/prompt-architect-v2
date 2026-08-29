# Instruction (must follow): Memory Consolidation — Consolidate Completed Plans & Re-Sequence Milestones

Trigger Keywords & Aliases: `consolidate-plans`, `consolidate completed plans`, `clean completed plans`, `resequence completed plans`, `merge plans`, `archive completed plans`, `cleanup plans completed`

```text
N = 200
```

N = total self-loop steps budget that the agents will perform.

/goal Autonomously scan, analyze, group, consolidate, and re-sequence all completed plan files within `.lovable/plans/completed/` into clean, cohesive milestone summaries, while strictly preserving 100% of architectural specifications, root-cause analyses, and decision logs with zero data loss or truncation until 100% green without stopping.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan `.lovable/plans/completed/`, `.lovable/plans/index.md`, and recent memory logs. Group related micro-task files by feature domain or milestone epic. Write the master consolidation plan in `.lovable/plans/pending/XX-completed-plans-consolidation.md` with an exhaustive inventory mapping table (`| Source Files | Target Consolidated File | Feature / Domain Theme | Status |`), verify that zero core specs or architectural rules will be lost, and decompose into granular subtasks in `.lovable/plans/subtasks/XX-completed-plans/`.
- [ ] /goal Second N/2 steps (Phase 2): Create unified milestone summary documents for each cluster, remove redundant source files with `git rm`, re-sequence all files in `.lovable/plans/completed/` to continuous numeric prefixes (`01-`, `02-`, `03-`, ...) using `python .lovable/ai-fix-scripts/01-file-manipulator.py fix-seq-files`, update `.lovable/plans/index.md` and `.lovable/memory/00-index.md`, verify with relative path and header spacing linters, and verify local CI quality gates exit with code 0 (`exit 0`).
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/00-canonical-size-tier.md`, `spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`, `spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`, `spec/02-coding-guidelines/08-file-folder-naming/`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2: Scan Completed Plans, Cluster by Domain, Spec in .lovable/plans/pending/, Subtasks)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N: Merge Files, Re-sequence Monotonic Prefixes, Update Plans Index, Verify Linters, Verify CI)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization. Never modify them mid-execution.

---

## Dedicated Section: Why, What & How of Completed Plans Consolidation

A project that runs hundreds of autonomous agent turns quickly produces dozens of micro-task files in `.lovable/plans/completed/`. If left unmanaged, this file clutter exhausts context windows, slows down memory retrieval, and fragments project history.

---

### 1. The Core Objectives (Why We Consolidate)

1. **Context Window Protection:** Agents reading historical plans must not be flooded with 50 individual 5-line subtask files.
2. **Cohesive Milestone Memory:** Related subtasks (e.g. `01-auth-model.md`, `02-auth-token.md`, `03-auth-endpoint.md`) belong together in a single narrative document (`01-authentication-system.md`).
3. **100% Spec & Architecture Preservation (The Prime Directive):** Merging files MUST NEVER summarize away core architectural contracts, error codes, schema models, or bug RCAs. Every critical decision is preserved verbatim.
4. **Monotonic, Continuous Re-Sequencing:** Remaining files in `.lovable/plans/completed/` MUST be re-numbered continuously (`01-`, `02-`, `03-`, ...) with strictly lowercase filenames.

---

### 2. Standard Consolidated Milestone Structure

Every consolidated file generated inside `.lovable/plans/completed/` MUST adhere to this uniform layout:

```markdown
# Milestone Summary: [Feature / Epic Name]

## 1. Executive Overview & Scope

- **Milestone Theme:** [Domain / Capability area]
- **Original Subtasks Merged:** `XX-task-a.md`, `XX-task-b.md`, `XX-task-c.md`
- **Completion Date:** [ISO Date]
- **Status:** `COMPLETED`

## 2. Key Architectural Decisions & Spec Implementations

- **Authoritative Specifications Implemented:**
  - [`spec/path/to/spec.md`](spec/path/to/spec.md) — [Why: Specific rule implemented]
- **Core Architecture Contracts:** [Verbatim constraints, types, and invariants]

## 3. Chronological Task Execution Ledger

| Step | Subtask | Description | Key Files Modified | Status |
|:---:|---|---|---|:---:|
| 1 | Initial Design | Created domain models and interfaces | `src/models/auth.ts` | DONE |
| 2 | Implementation | Added service handler and unit tests | `src/services/auth.ts` | DONE |

## 4. Root Cause Analyses & Bug Fixes Referenced

- [`.lovable/memory/issues/XX-rca.md`](.lovable/memory/issues/XX-rca.md) — Root cause analysis and resolution details.

## 5. Verification & Quality Gates

- **Unit Tests:** Passed with 100% branch coverage.
- **Linters:** `python linter-scripts/check-relative-paths.py` exited with code 0.
```

---

### 3. Step-by-Step Consolidation Workflow (Phase 1 & Phase 2)

#### Phase 1: Scan, Inventory & Cluster Mapping (Steps 1 to N/2)

1. **Inventory Scan:** List all files currently in `.lovable/plans/completed/`.
2. **Domain Clustering:** Identify natural groupings by feature, sprint, or component.
3. **Master Audit Spec:** Write `.lovable/plans/pending/XX-completed-plans-consolidation.md` containing the inventory mapping table:

```markdown
| Source Files to Merge | Proposed Consolidated File | Domain / Epic Theme | Items Preserved | Status |
|---|---|---|---|:---:|
| `01-task-a.md`, `02-task-b.md` | `01-auth-system.md` | Authentication | Models, JWT, Middleware | PENDING |
| `03-fix-a.md`, `04-fix-b.md` | `02-ci-cd-pipeline.md` | CI/CD Automation | GitHub Actions, Linters | PENDING |
```

4. **Decompose Subtasks:** Create `.lovable/plans/subtasks/XX-completed-plans/01-task.md`, `02-task.md`, etc.

#### Phase 2: Merge, Re-Sequence, Index & Verify (Steps N/2+1 to N)

1. **Write Consolidated Documents:** Create the target markdown files in `.lovable/plans/completed/`.
2. **Remove Merged Sources:** Use `git rm` to cleanly delete the old micro-task files.
3. **Re-Sequence Numeric Prefixes:** Run the automated re-sequencer:
   ```bash
   python .lovable/ai-fix-scripts/01-file-manipulator.py fix-seq-files .lovable/plans/completed/
   ```
   Ensure all files are strictly lowercase with monotonic `01-`, `02-`, `03-` prefixes.
4. **Update Indexes:** Synchronize `.lovable/plans/index.md` and `.lovable/memory/00-index.md` with the new file list.
5. **Verify Formatting & Linters:**
   ```bash
   python linter-scripts/check-relative-paths.py
   python linter-scripts/check-markdown-header-spacing.py
   npx markdownlint "**/*.md" --ignore "node_modules/**"
   ```

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
- [ ] **Automated File Sequencing & Normalization:** Use `python .lovable/ai-fix-scripts/01-file-manipulator.py fix-seq-files <dir>` to re-sequence completed plan files monotonically.
- [ ] **Relative Path Normalization:** Use `python .lovable/ai-fix-scripts/04-relative-path-fixer.py .` to ensure all links in consolidated documents are strictly relative Git paths.
- [ ] **Commit & Track:** All new helper scripts were written strictly to `.lovable/ai-fix-scripts/` and committed to Git for future reuse.
- [ ] **Index Documentation:** I have updated `.lovable/ai-fix-scripts/index.md` using sequential script naming. For every script, I have included a `<details>` collapsible tag explaining exactly why the script is there and what it does.

---

## Pre-Reply / Loop Checklist (Must Verify Every Loop Iteration)

- [ ] Git working tree is clean before new file modifications.
- [ ] **Spec Protection:** I have manually verified that NONE of the merged files contained critical architectural constraints, domain specifications, or non-negotiable rules that were omitted or summarized away.
- [ ] **Strict Relative Git Paths:** All file paths, markdown links, citations, and subtask references in consolidated files are strictly relative to the git repository root. Zero absolute paths (`D:\...`, `C:\...`) or `file:///` URIs.
- [ ] **Strict Lowercase Naming:** Every file in `.lovable/plans/completed/` uses strictly lowercase letters (e.g. `01-auth-system.md`).
- [ ] **Monotonic Sequencing:** File prefixes in `.lovable/plans/completed/` are continuous and monotonic (`01-`, `02-`, `03-`, ...) without gaps or duplicates.
- [ ] **Index Synchronization:** Both `.lovable/plans/index.md` and `.lovable/memory/00-index.md` reflect the consolidated files and remove deleted entries.
- [ ] **LF Line Endings (`\n`):** All files use Unix LF line endings. Zero CRLF (`\r\n`).
- [ ] **UTF-8 Encoding (No BOM):** All files encoded in UTF-8 without BOM.
- [ ] **Single Trailing Newline:** Every file ends with exactly one terminating newline (`\n`).
- [ ] **Markdown Heading Spacing:** Exactly one blank line before and after headings (no leading blank line on line 1).
- [ ] **Zero Double Blank Lines:** No `\n\n\n` anywhere in markdown.
- [ ] `python linter-scripts/check-relative-paths.py` and `python linter-scripts/check-markdown-header-spacing.py` exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## Non-Negotiable Coding Guidelines Checklist (Auto-Reject on Violation)

/goal You MUST verify every item on this checklist before committing any code. If a subagent violated one of these rules, you must reject their work.

- [ ] Strict Relative Git Paths: All file paths, markdown links, citations, and subtask references in plans, specs, and memory logs are strictly relative to the git repository root. Zero absolute paths or `file:///` URIs.
- [ ] Master Guidelines: I have fully read and strictly enforced `spec/02-coding-guidelines/08-file-folder-naming/` and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Spec Preservation: Zero truncation, zero placeholder stubs (`TODO`, `[N]`, `// ...`).
- [ ] Monotonic Sequence: Verified sequential `01-`, `02-`, `03-` numbering across `.lovable/plans/completed/`.
- [ ] /learn the section as a /goal [AI Fix Scripts Memory](#ai-fix-scripts-memory)
- [ ] Action Summary: I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to prove I did not hallucinate.

---

## STRICT AVOIDANCE: Never Disable CI/CD

> [!CAUTION]
> **NEVER disable any CI/CD checks, GitHub Actions, or validation workflows.**
> Strictly avoid commenting out, bypassing, or deleting CI/CD steps to force a pipeline to pass. Your job is to fix the underlying code so that the CI/CD pipeline passes legitimately. Disabling CI/CD is an auto-reject failure.

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and careless: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job.
