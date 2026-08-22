# Read, Execution, Planning, and Pending Prompts Architecture Spec

> Captured user directives for updating the canonical Read Memory, Execution Loop, Planning, and Pending Inventory prompts.

## Date

2026-08-22

## User Directives & Specifications

### 1. Read Memory (Enhanced) Improvements

- **Broken Link & Missing Spec Detection**: Scan internal markdown references across `.lovable/` and `spec/`. If a referenced spec, overview, or issue file is missing on disk, automatically register it as an open question in `.lovable/ambiguous-questions/01-new-ambiguity/01-<slug>.md` or surface it directly to the user rather than guessing past missing docs.
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
- **Automatic Subtask Decomposition Alert (>7 steps)**: Flag any pending task exceeding 7 steps in the rubric with `[DECOMPOSITION REQUIRED]` to split it into `.lovable/plans/subtasks/01-<slug>/` before entering the execution queue.
- **Ambiguity Impact Severity Scoring**: Rank open questions in `01-new-ambiguity/` by blast radius (*High*: blocks multiple core plans; *Medium*: blocks 1 plan; *Low*: non-blocking cosmetic detail).
- **Strictly Positive Framing**: Concluding question asking whether to trigger continuous 3-agent parallel execution uses strictly positive phrasing.

### 4. Canonical Pending Queue Architecture & 2-Digit Sequence Prefix

- **Single Source of Truth**: All actionable execution plans and pending tasks live exclusively in `.lovable/plans/pending/01-<slug>.md` and `.lovable/plans/subtasks/01-<slug>/01-<subslug>.md`. The legacy `.lovable/spec/tasks/` location is completely eliminated.
- **Verbatim Requirements**: Specs, user requirements, and directives are saved under `.lovable/memory/specs/01-<slug>.md` or domain folders in `spec/<NN>-<slug>/`.
- **Strict 2-Digit Sequence Prefixes**: All pending task files MUST use two-digit sequence prefixes (`01-`, `02-`, `03-`, etc.).
- **Anti-Hallucination & Clarifying Questions**: If files, specs, or requirements are missing or ambiguous, the AI MUST NOT guess or invent rules. It must stop and ask clarifying questions or check with the user to verify alignment.

### 5. Consolidated Prompts Routing & Registry

- `01-general-prompts/03-read-write/` is the single home for Read & Write prompts (`01-write-antigravity.md`, `02-read-memory-enhanced.md`, `03-write-memory.md`).
- `01-general-prompts/07-execute/` contains the execution and inventory prompts (`01-execute-pending-tasks.md`, `02-execute-robust-loop.md`, `03-execute-batched-loop.md`, `04-inventory-pending-tasks.md`).
- `.lovable/prompts.md`, `.lovable/memory/what-to-read.md`, and root `readme.md` are synchronized and kept in strict alignment.

## Markdown Header Spacing Rule

Every markdown heading (any line starting with `#`) MUST have:

- Exactly one blank line BEFORE the heading (unless it is the very first line of the file)
- Exactly one blank line AFTER the heading

This rule is enforced by `linter-scripts/check-markdown-header-spacing.py` which runs as part of the CI linter pipeline.

### Prompt File Structure Convention

Prompt files in `01-general-prompts/` MUST follow this structure:

1. `# Title` at the very top
2. One blank line after the title
3. Body content
4. `---` separator at the bottom
5. `## Metadata` section at the bottom with `- slug:` and `- status:` lines

The slug and status lines belong at the BOTTOM of the file, not at the top. This keeps the prompt clean and machine-readable without cluttering the opening.

### Example

```markdown

# My Prompt Title

## Section One

Content here.

## Section Two

More content.

---

## Metadata

- slug: my-prompt-slug
- status: active
```
