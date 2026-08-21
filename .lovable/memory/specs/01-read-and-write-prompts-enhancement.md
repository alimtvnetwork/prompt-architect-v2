# Read and Write Prompts Enhancement Spec

> Captured user directives for updating the canonical Read Memory and Write Memory prompts.

## Date
2026-08-22

## User Directives & Specifications

### 1. Read Memory (Enhanced) Directive
- **Autonomous Self-Looping Enforcement**: The AI agent must systematically and autonomously loop through the entire codebase and all spec folders in `spec/` (e.g. `spec/01`, `spec/02`, `spec/03`, `spec/04`, `spec/21`, etc.), either directly or via dedicated parallel subagents with explicit titles.
- Read the entire `.lovable/` folder recursively without omitting any file.
- Most importantly, read `.lovable/memory/what-to-read.md` (or `.lovable/what-to-read.md`) first and follow all referenced files in full.
- **Root `readme.md` Lowercase Enforcement & Auto-Fix**: Confirm that the root readme is strictly named lowercase `readme.md`. If an uppercase `README.md` or incorrectly cased file is detected during read or write time, immediately fix it to `readme.md`, delete any uppercase duplicate, commit the change, and push to git without second-guessing or waiting for confirmation.
- Read all domain specifications (`spec/21/` app spec), coding guidelines (`spec/02/`), error management (`spec/03/`), and database rules (`spec/04/`). If folders contain only `.gitkeep`, fallback to guidelines in `01-general-prompts/` or request the files from the user.

### 2. Write Memory Directive
- Capture recent conversations, instructions, directives, and decisions from the current session as a spec or memory summary inside `.lovable/memory/specs/` or `.lovable/memory/learned/`.
- Permit consolidation of simple, routine, or ephemeral tasks that do not warrant separate files, avoiding unnecessary repo clutter.
- **CRITICAL NON-NEGOTIABLE RULE**: Highly detailed and important specs (e.g. `spec/21`, domain architecture, detailed requirements, complex error handling, coding standards) MUST NEVER be consolidated, summarized, resumed, or reduced in size. They must remain 100% complete, granular, and verbatim.
- Verify and enforce lowercase root `readme.md` during write-memory time as well, auto-fixing and committing/pushing if needed.

### 3. Artifact Clean & Git History Purge Directive
- Detect and prevent committing artifact zips, test data, temporary scripts, or unwanted generated code.
- Itemize candidate files with full path, size, creation step, and origin/purpose.
- Present questions to the developer using strictly **positive framing** (no negative words, double negatives, or inverted questions).
- On removal choice, execute **dual removal**: delete from the local filesystem AND purge from Git history to prevent repository bloat.
- Finalize with combined unsoftened insults from Read Memory and Insult Code Fix prompts.
- Maintain dedicated consolidated insults collection under `01-general-prompts/09-insults/01-raw-insults.md`.

### 4. Execution & Workflow Rules
- Synchronize `.lovable/memory/index.md`, `.lovable/plans/index.md`, `.lovable/memory/what-to-read.md`, and root `readme.md`.
- Ensure all prompt copies across categories remain updated and consistent.
- Perform clean git commit and push.
