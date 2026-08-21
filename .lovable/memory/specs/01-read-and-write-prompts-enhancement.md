# Read, Execution, and Pending Prompts Enhancement Spec

> Captured user directives for updating the canonical Read Memory, Execution Loop, and Pending Inventory prompts.

## Date
2026-08-22

## User Directives & Specifications

### 1. Read Memory (Enhanced) Improvements
- **Broken Link & Missing Spec Detection**: Scan internal markdown references across `.lovable/` and `spec/`. If a referenced spec, overview, or issue file is missing on disk, automatically register it as an open question in `.lovable/ambiguous-questions/01-new-ambiguity/XX-<slug>.md` or surface it directly to the user rather than guessing past missing docs.
- **Active Schema & API Contract Mapping**: Ingest and maintain an in-memory map of active DB tables/schemas (`spec/04-database-conventions/`, `spec/23-app-db/`), API endpoints, and global state stores so downstream planning and coding tasks make zero assumptions on field names or parameter shapes.
- **Tooling & Runtime Compatibility Check**: Inspect package manifests (`package.json`, build configs, tsconfig) to catalog runtime targets, linter rules, and banned packages before completing onboarding.
- **Autonomous Self-Looping & Full Codebase Survey**: Systematically loop through the entire codebase as a whole and recursively traverse every subfolder and nested `.md` file in `spec/` (`spec/01-spec-authoring-guide/`, `spec/02-coding-guidelines/`, `spec/03-error-manage/`, `spec/04-database-conventions/`, `spec/21-app/`).
- **Root `readme.md` Lowercase Auto-Fix**: Automatically verify lowercase root `readme.md`, rename/delete stale uppercase files, commit and push without waiting for confirmation.

### 2. Execution Loop Improvements (`execute-pending-tasks`, `execute-robust-loop`, `execute-batched-loop`)
- **File Collision Locking Matrix (`active-locks.json`)**: Parallel sub-agents register their active target files in `.lovable/temp/active-locks.json` to physically prevent two agents from modifying the same files or shared exports concurrently.
- **Automated Clean Rollback on 3-Strike Failure**: If a sub-agent fails unit tests or build checks 3 consecutive times, automatically rollback dirty working tree (`git checkout -- <modified_files>`), log root cause and stack trace to `.lovable/memory/last-failure.md` and `.lovable/issues/`, and proceed to the next disjoint task.
- **Embedded Artifact Sanitizer in Commit Fix**: Phase 5 Commit Fix automatically audits staged files and working tree for zip archives, temporary scratch files, or test outputs before committing and purging them if unapproved.
- **Lovable Branch Preservation Guard**: Strictly avoid force pushes, rebasing, or squashing published Git history (per `AGENTS.md`) so the Lovable editor synchronization remains pristine.
- **Consolidated Insults Section**: Standardized closing section titled `## MUST FOLLOW NON-NEGOTIABLE` in a single consolidated unsoftened paragraph.

### 3. Pending List / Inventory Improvements (`inventory-pending-tasks`, `pending-tasks`)
- **Execution Wave Sequencing (Wave 1, Wave 2, Wave 3)**: Group pending tasks into sequenced Execution Waves based on dependencies (*Wave 1: Schemas/DB/wrappers*, *Wave 2: Business services & logic*, *Wave 3: UI & docs*).
- **Automatic Subtask Decomposition Alert (>7 steps)**: Flag any pending task exceeding 7 steps in the rubric with `[DECOMPOSITION REQUIRED]` to split it into `.lovable/plans/subtasks/XX-<slug>/` before entering the execution queue.
- **Ambiguity Impact Severity Scoring**: Rank open questions in `01-new-ambiguity/` by blast radius (*High*: blocks multiple core plans; *Medium*: blocks 1 plan; *Low*: non-blocking cosmetic detail).
- **Strictly Positive Framing**: Concluding question asking whether to trigger continuous 3-agent parallel execution uses strictly positive phrasing.

### 4. Consolidated Prompts Routing & Registry
- `01-general-prompts/03-read-write/` is the single home for Read & Write prompts (`01-write-antigravity.md`, `02-read-memory-enhanced.md`, `03-write-memory.md`).
- `01-general-prompts/07-execute/` contains the execution and inventory prompts (`01-execute-pending-tasks.md`, `02-execute-robust-loop.md`, `03-execute-batched-loop.md`, `04-inventory-pending-tasks.md`).
- `.lovable/prompts.md`, `.lovable/memory/what-to-read.md`, and root `readme.md` are synchronized and kept in strict alignment.
