# Read and Write Prompts Enhancement Spec

> Captured user directives for updating the canonical Read Memory and Write Memory prompts.

## Date
2026-08-22

## User Directives & Specifications

### 1. Read Memory (Enhanced) Directive
- Explicitly mandate reading the entire codebase as a whole (full structure, architecture, and files).
- Read the entire `.lovable/` folder recursively.
- Most importantly, read `.lovable/memory/what-to-read.md` (or `.lovable/what-to-read.md`) first and follow all referenced files in full.
- Read the root `readme.md` file for architecture and casing rules.
- Read the `spec/` folder, specifically `spec/21/` (app spec) or any domain-specific spec folder, `spec/02/` (coding guidelines), `spec/03/` (error management conventions to understand error handling), and `spec/04/` (database and mandatory conventions).

### 2. Write Memory Directive
- Capture recent conversations, instructions, directives, and decisions from the current session as a spec or memory summary inside `.lovable/memory/specs/` or `.lovable/memory/learned/`.
- Permit consolidation of simple, routine, or ephemeral tasks that do not warrant separate files, avoiding unnecessary repo clutter.
- **CRITICAL NON-NEGOTIABLE RULE**: Highly detailed and important specs (e.g. `spec/21`, domain architecture, detailed requirements, complex error handling, coding standards) MUST NEVER be consolidated, summarized, resumed, or reduced in size. They must remain 100% complete, granular, and verbatim.

### 3. Execution & Workflow Rules
- Synchronize `.lovable/memory/index.md`, `.lovable/plans/index.md`, `.lovable/memory/what-to-read.md`, and root `readme.md`.
- Ensure all prompt copies across categories (`01-core-workflow/`, `03-read-write/`, `05-commit-and-multi-agent-code-fix/`) remain updated and consistent.
- Perform clean git commit and push.
