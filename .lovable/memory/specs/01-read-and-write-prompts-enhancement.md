# Read and Write Prompts Enhancement Spec

> Captured user directives for updating the canonical Read Memory, Write Memory, and Execution/Inventory prompts.

## Date
2026-08-22

## User Directives & Specifications

### 1. Read Memory (Enhanced) Directive
- **Autonomous Self-Looping Enforcement**: The AI agent must systematically and autonomously loop through the entire codebase and all spec folders in `spec/` (e.g. `spec/01-spec-authoring-guide/`, `spec/02-coding-guidelines/`, `spec/03-error-manage/`, `spec/04-database-conventions/`, `spec/21-app/`, etc.), either directly or via dedicated parallel subagents with explicit titles.
- **Spec Folder Naming & Dynamic Numbering**: Spec folders strictly follow the hyphenated `spec/<NN>-<slug>/` pattern. Sequence numbers and folder placements can switch or be reorganized across projects; the AI must dynamically discover and inspect all nested subdirectories, markdown files (`*.md`), `00-overview.md`, `99-consistency-report.md`, and `spec-index.md`.
- Read the entire `.lovable/` folder recursively without omitting any file.
- Most importantly, read `.lovable/memory/what-to-read.md` (or `.lovable/what-to-read.md`) first and follow all referenced files in full.
- **Root `readme.md` Lowercase Enforcement & Auto-Fix**: Confirm that the root readme is strictly named lowercase `readme.md`. If an uppercase `README.md` or incorrectly cased file is detected during read or write time, immediately fix it to `readme.md`, delete any uppercase duplicate, commit the change, and push to git without second-guessing or waiting for confirmation.
- Read all domain specifications (`spec/21-app/`), coding guidelines (`spec/02-coding-guidelines/`), error management (`spec/03-error-manage/`), and database rules (`spec/04-database-conventions/`). If folders contain only `.gitkeep`, fallback to guidelines in `01-general-prompts/` or request the files from the user.
- **Pending Tasks Reading**: Systematically read and list all pending tasks and subtasks from `.lovable/plans/pending/`, `.lovable/plans/subtasks/`, `.lovable/issues/`, and `.lovable/cicd-issues/`.

### 2. Write Memory Directive
- Capture recent conversations, instructions, directives, and decisions from the current session as a spec or memory summary inside `.lovable/memory/specs/` or `.lovable/memory/learned/`.
- Permit consolidation of simple, routine, or ephemeral tasks that do not warrant separate files, avoiding unnecessary repo clutter.
- **CRITICAL NON-NEGOTIABLE RULE**: Highly detailed and important specs (e.g. `spec/21-app/`, domain architecture, detailed requirements, complex error handling, coding standards) MUST NEVER be consolidated, summarized, resumed, or reduced in size. They must remain 100% complete, granular, and verbatim.
- Verify and enforce lowercase root `readme.md` during write-memory time as well, auto-fixing and committing/pushing if needed.

### 3. Artifact Clean & Git History Purge Directive
- Detect and prevent committing artifact zips, test data, temporary scripts, or unwanted generated code.
- Itemize candidate files with full path, size, creation step, and origin/purpose.
- Present questions to the developer using strictly **positive framing** (no negative words, double negatives, or inverted questions).
- On removal choice, execute **dual removal**: delete from the local filesystem AND purge from Git history to prevent repository bloat.
- Finalize with unified single-block unsoftened insults under `## MUST FOLLOW NON-NEGOTIABLE`.

### 4. Pending Tasks Inventory Directive (Read-Only Scan)
- Dedicated read-only scan prompt (`01-general-prompts/07-execute/04-inventory-pending-tasks.md`) that lists all pending tasks without executing them.
- References the full `.lovable/` and `spec/` structure clearly.
- Concludes with a positively framed question asking if the user wishes to trigger a continuous self-loop via 3 parallel agents.
- Includes mandatory and banned checklist items along with `## MUST FOLLOW NON-NEGOTIABLE`.

### 5. Execution & Workflow Rules
- Synchronize `.lovable/memory/index.md`, `.lovable/plans/index.md`, `.lovable/memory/what-to-read.md`, and root `readme.md`.
- Ensure all prompt copies across categories remain updated and consistent.
- Perform clean git commit and push.
