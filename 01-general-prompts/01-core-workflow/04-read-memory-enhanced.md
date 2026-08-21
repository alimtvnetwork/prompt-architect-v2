# Read Memory (Enhanced)

## Ambiguity folder path (non-negotiable)

- Open questions: `.lovable/ambiguous-questions/01-new-ambiguity/XX-<slug>.md`
- Answered questions: `.lovable/ambiguous-questions/02-ambiguity-resolved/XX-<slug>.md`

Read both folders in full during Phase 1. Surface open-ambiguity counts and slugs in the Completion Confirmation block. Treat resolved-ambiguity files as binding project decisions, do not re-litigate them. If an open ambiguity is relevant to the incoming task, stop and surface it before doing work; never guess past it.

## Goal

/goal Before you touch this project, load its identity into your head: who it is, what it forbids, what it has already decided, and what work is in flight.

The specs, `.lovable/` folder, `what-to-read.md`, root `readme.md`, and the codebase as a whole are the single source of truth. Your training data is not. If the two disagree, the repo wins, every time.

Autonomously self-loop and read the entire codebase as a whole, the root `readme.md`, the entire `.lovable/` folder (especially `what-to-read.md` and all files it references), every single folder in the `spec/` directory—specifically `spec/21/` (app spec) or any domain-specific folder, `spec/02/` (coding guidelines), `spec/03/` (error management conventions), `spec/04/` (database and mandatory conventions)—and **read every pending task** across `.lovable/plans/pending/`, `.lovable/plans/subtasks/`, `.lovable/issues/`, and `.lovable/cicd-issues/`, listing them out in full.

You are done reading when you can, without guessing:

- name the CODE RED rules,
- name the naming, error-handling, and DB conventions,
- list what is currently in `.lovable/plans/pending/` and every active subtask,
- point at the exact file that justifies any rule you enforce,
- explain the whole codebase structure, app features (`spec/21`), coding guidelines (`spec/02`), and error management philosophy (`spec/03`),
- list out all pending tasks and unresolved issues with accurate step counts,
- confirm that the root readme is strictly lowercase `readme.md` (and auto-fixed/committed/pushed if it was not).

If you cannot do that, keep reading. Do not start work.

## Reading Strategy: Mandatory Autonomous Looping & Parallel Subagents

The `.lovable/` folder, specs, and entire codebase can be massive. To process this information with zero blind spots:
- **Autonomous Looping Enforcement:** The AI agent MUST autonomously loop through all directories and files across `spec/`, `.lovable/`, and application source trees. Do not stop after one high-level glance; systematically iterate through each directory layer.
- **Parallel Subagents for Deep Reading:** You ARE allowed and strongly encouraged to spawn dedicated sub-agents to read items and synthesize memory in parallel.
- **Specific Titling:** When spawning a sub-agent for reading, you must give it a highly specific title reflecting exactly what it is reading (e.g., `Reading Auth Specs`, `Scanning Error Management Spec 03`, `Surveying App Codebase Tree`, `Ingesting Coding Guidelines Spec 02`). Do not use generic names. If an agent switches tasks, its title must change.
- **Micro-Tasking:** Assign sub-agents small, granular folders/files to read rather than asking one agent to read the entire codebase in a single pass.
- **Root `readme.md` Lowercase Self-Healing Exception:** If the root readme is uppercase `README.md` or incorrectly cased, immediately rename it to `readme.md`, commit, and push to git without asking.
- **Memory Persistence:** You are allowed to write to the `.lovable/` directory to enhance project memory after reading. This includes:
  - Writing summaries of what you learned into `.lovable/memory/learned/XX-<slug>.md` (or `.lovable/memory/specs/XX-<slug>.md`), including file counts, to maintain context.
  - Updating `.lovable/memory/what-to-read.md` based on your progress to guide future reading workflows.
  - Documenting any discovered bugs into `.lovable/issues/` or `.lovable/suggestions.md`.
  - Capturing open ambiguities or updating execution plans.
- **Missing Spec File Protocol:** If a spec folder contains only `.gitkeep` or missing reference files, check the full names in `01-general-prompts/02-coding-standards/01-coding-guidelines.md` or existing plans, use available guidelines in the prompt library, and if critical information is absent, explicitly ask the user for the file.
- CRITICAL: Other than fixing the root `readme.md` lowercase naming if needed, you MUST NOT refactor, edit, or write any application source code. This is a strictly read and analysis phase.

---

## Phase 1 - Load the project

### 1.0 Read `what-to-read.md` and Confirm Root `readme.md` Lowercase (Auto-Fix & Commit)

1. Read `.lovable/memory/what-to-read.md` (or `.lovable/what-to-read.md`). This is the **authoritative reading order** for the project and overrides any generic order. Follow every file and order it specifies.
2. **Root `readme.md` Lowercase Verification & Auto-Fix**:
   - Verify that the root readme file is strictly named lowercase `readme.md`.
   - If an uppercase `README.md` exists or the casing is incorrect on disk or in git, immediately rename it to `readme.md`, remove the stale uppercase file, commit the change (`fix: ensure root readme is strictly lowercase readme.md`), and push to git without asking or second-guessing.
   - Read the root `readme.md` file for architecture, casing rules, repository layout, and AI entry points.

### 1.1 Read the whole `.lovable/` folder & Pending Tasks Queue

Walk `.lovable/` recursively. Every file matters. Missing files are noted, not silently skipped. In particular:

| #   | Path                                                  | What you get                                                                                                                                |
| --- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `.lovable/memory/what-to-read.md`                     | **Authoritative reading order** for this project. Read it first and follow all referenced files.                                            |
| 2   | `.lovable/overview.md`                                | Project summary, stack, nav map                                                                                                             |
| 3   | `.lovable/strictly-avoid.md`                          | Hard prohibitions (CODE RED)                                                                                                                |
| 4   | `.lovable/user-preferences`                           | How the human wants you to behave                                                                                                           |
| 5   | `.lovable/prompt.md` + `.lovable/prompts/`            | Canonical prompts (Read, Plan, etc.). "Read memory" = run this prompt.                                                                      |
| 6   | `.lovable/memory/index.md`                            | Index of institutional knowledge. Then read every file it references, recursively.                                                          |
| 7   | `.lovable/plans/index.md`                             | Roll-up of all plans (pending + completed + subtasks). Read this before touching individual plan files.                                     |
| 8   | `.lovable/plans/pending/`                             | Active plans, `XX-<slug>.md`—**read all and list out each pending item**.                                                                   |
| 9   | `.lovable/plans/completed/`                           | Recent history, skim only                                                                                                                   |
| 10  | `.lovable/plans/subtasks/XX-<slug>/`                  | Depth files linked from a parent plan—**read all active subtasks and list them**.                                                           |
| 11  | `.lovable/suggestions.md`                             | Ideas not yet approved                                                                                                                      |
| 12  | `.lovable/spec/commands/`                             | User commands and conventions, `XX-<slug>.md`                                                                                               |
| 13  | `.lovable/issues/`                                    | General bugs and regressions—**read and list out pending bugs**.                                                                            |
| 14  | `.lovable/cicd-issues/`                               | CI/CD-specific failures—**read and list out pending CI/CD issues**.                                                                          |
| 15  | `.lovable/ambiguous-questions/01-new-ambiguity/`      | Open questions currently blocking work. If any exist, surface them in the completion block, do NOT guess past them.                         |
| 16  | `.lovable/ambiguous-questions/02-ambiguity-resolved/` | Answered questions with their applied solution. Treat these as binding decisions, do not re-litigate.                                       |
| 17  | Anything else under `.lovable/`                       | Read it. If the folder exists, it exists for a reason.                                                                                      |

### 1.2 Loop Through the Entire `spec/` Directory and Guidelines

Systematically loop through the `spec/` folder, matching canonical names found in `01-general-prompts/02-coding-standards/01-coding-guidelines.md` and active plans:
- `spec/02` / `spec/02-coding-guidelines/` (or `01-general-prompts/02-coding-standards/01-coding-guidelines.md`): Zero-tolerance coding standards, function size caps (8 lines preferred, 15 max), boolean naming (`is*`, `has*`, positive framing), immutable patterns, DRY priority 1.
- `spec/03` / `spec/03-error-manage/`: Error management philosophy—never swallow errors, log operation name and key inputs on every catch, wrap errors without losing cause, typed errors only, universal response envelopes (`{ data, errors[], meta }`).
- `spec/04` / `spec/04-database-conventions/`: Database schema, table naming (PascalCase), columns (camelCase), primary keys (`{Table}Id`), SQLite/ORM rules, ERD requirements.
- `spec/21` / `spec/21-app/`: App specification, domain architecture, core capabilities, routes, and business rules.
- Loop through any other present spec folders (`spec/01` through `spec/24`). If a folder only has `.gitkeep`, fallback to the corresponding guideline in prompt library or ask the user.

### 1.3 Loop Through the Entire Codebase as a Whole

Autonomously survey the codebase structure end-to-end:
- Root configuration files, package manifests, build scripts.
- Application directory (`src/` or app root), entry points, routing tree, components, state management stores, and utility modules.
- Asset directories (`assets/`).
- Verify how data flows from input to state, backend/storage, and UI presentation.

### 1.4 The Two Index Files

Two indexes decide what you read next. Treat them as required entry points, not as summaries:
- `.lovable/memory/index.md` lists every institutional-knowledge file. If it points at 12 files, you read 12 files.
- `.lovable/plans/index.md` lists every plan (pending, completed, subtasks) with its slug, status, and one-line intent. Use it to pick which plan files to open in full. If it is missing, create it as part of the next code change (see Memory Update Protocol).

### 1.5 Self-check (internal, before Phase 2)

- CODE RED rules?
- Naming conventions (files, folders, DB columns, variables)?
- Root readme strictly lowercase `readme.md`?
- Error-handling philosophy (`spec/03`)?
- What is in `.lovable/plans/pending/` and `plans/subtasks/` right now (exact list)?
- App specs and domain architecture (`spec/21`)?
- Whole codebase layout and component flow?
- Top forbidden patterns?

If any answer is fuzzy, go back and reread by looping through the files again. Do not proceed.

---

## Phase 2 - Consolidated guidelines

Read `spec/12-consolidated-guidelines/` in numeric order (`01-*.md` through `18-*.md`). Each file is a self-contained policy document. Missing folder: note it and continue.

---

## Phase 3 - Spec authoring rules

Read `spec/01-spec-authoring-guide/` in numeric order. You should come out knowing:

- file and folder naming conventions,
- required files per spec folder (`00-overview.md`, `99-consistency-report.md`),
- the `.lovable/` layout (see Phase 1.1),
- the linter infrastructure.

---

## Phase 4 - Task-driven deep dives

Only open a spec folder when the current task needs it.

| Task involves…                           | Read                                    |
| ---------------------------------------- | --------------------------------------- |
| Writing or reviewing code                | `spec/02-coding-guidelines/`            |
| Error handling                           | `spec/03-error-manage/`                 |
| Database schema or queries               | `spec/04-database-conventions/`         |
| SQLite / multi-DB architecture           | `spec/05-split-db-architecture/`        |
| Config systems                           | `spec/06-seedable-config-architecture/` |
| UI theming, CSS variables, design tokens | `spec/07-design-system/`                |
| Documentation viewer features            | `spec/08-docs-viewer-ui/`               |
| Code block rendering                     | `spec/09-code-block-system/`            |
| PowerShell scripts                       | `spec/10-powershell-integration/`       |
| CI/CD pipelines                          | `spec/13-cicd-pipeline-workflows/`      |
| CLI self-update                          | `spec/14-self-update-app-update/`       |
| WordPress plugins                        | `spec/15-wp-plugin-how-to/`             |
| App-specific features                    | `spec/21-app/`                          |
| Known app bugs                           | `spec/22-app-issues/`                   |
| App-specific DB schema                   | `spec/23-app-database/`                 |
| App-specific UI + design system          | `spec/24-app-design-system-and-ui/`     |

Inside each folder: `00-overview.md` → numbered files → `99-consistency-report.md`.

Fallbacks when the canonical numbered folder is absent: `.lovable/coding-guidelines.md`, `spec/coding-guidelines/`, `coding-guidelines/`, `spec/XX-error-manage/`, `01-general-prompts/02-coding-standards/01-coding-guidelines.md`. Numbered folder wins on conflict; call the conflict out in the plan's Context.

---

## Anti-Hallucination Contract

1. If the specs are silent on a rule, that rule does not exist. Do not invent one.
2. Specs beat training data. Always.
3. Cite the file and section when you enforce a rule.
4. When a spec is ambiguous, ask. Do not "use best judgement".
5. Do not blend this project's conventions with conventions from other projects you have seen.
6. No filler. No "hope this helps", no "let me know".

---

## Memory Update Protocol

```
New info discovered
├─ Institutional knowledge (pattern / convention / decision)?
│   YES → .lovable/memory/<slug>.md  +  update .lovable/memory/index.md
├─ Must never happen again?
│   YES → .lovable/strictly-avoid.md
├─ Idea, not yet approved?
│   YES → .lovable/suggestions.md
├─ New user command / convention?
│   YES → .lovable/spec/commands/XX-<slug>.md
├─ Bug / regression?
│   YES → .lovable/issues/XX-<slug>.md   (or .lovable/cicd-issues/ if CI/CD)
├─ New or changed plan?
│   YES → .lovable/plans/pending/XX-<slug>.md  +  update .lovable/plans/index.md
├─ Ambiguity / unclear requirement blocking progress?
│   YES → .lovable/ambiguous-questions/01-new-ambiguity/XX-<slug>.md
├─ User just answered a previously-open ambiguity?
│   YES → mv the file to .lovable/ambiguous-questions/02-ambiguity-resolved/XX-<slug>.md,
│         append `## Resolution` (answer + applied solution), flip Status: resolved
└─ None of the above → do not persist.
```

Hard rules:

- Folder is `.lovable/memory/`, never `memories/`.
- Adding a memory file always updates `.lovable/memory/index.md`.
- Adding, moving, or completing a plan always updates `.lovable/plans/index.md`.
- Ambiguity folders: `01-new-ambiguity/` for open, `02-ambiguity-resolved/` for answered. On answer, MOVE the file (never copy) so it exists in exactly one place. Every resolved file carries a `## Resolution` section.
- Never guess past an open ambiguity. If one exists and is relevant to the current task, stop and surface it before doing work.
- Editing existing memory or index files preserves unrelated content. No silent truncation.
- Any code-base change bumps the minor version.

---

## Completion Confirmation

After Phases 1-3, reply exactly:

```
✅ Onboarding complete.

- Memory files read: [X]
- Consolidated guidelines read: [Y]
- Spec authoring files read: [Z]
- Pending plans: [N]  (from .lovable/plans/index.md)
- CI/CD issues absorbed: [M]  (from .lovable/cicd-issues/)
- Open ambiguities: [K]  (from .lovable/ambiguous-questions/01-new-ambiguity/)
- Resolved ambiguities on file: [R]  (from .lovable/ambiguous-questions/02-ambiguity-resolved/)

I understand:
- CODE RED rules: [top 3-5]
- Naming conventions: [brief]
- Error handling: [one sentence]
- Active plans & pending tasks: [slugs from .lovable/plans/pending/ and subtasks]
- Strict avoidances: [top 3-5]
- Blocking ambiguities: [slugs, or "none"]

Ready for tasks.
```

Then stop. No next-step suggestions, no exploratory questions.

---

## Pre-reply checklist (all must be true)

- [ ] Read `.lovable/memory/what-to-read.md` (or `.lovable/what-to-read.md`) first and followed its order in full
- [ ] Confirmed root readme is strictly lowercase `readme.md` (auto-fixed, committed, and pushed if uppercase or missing)
- [ ] Read the root `readme.md` file (casing rules, architecture, entry points)
- [ ] Walked `.lovable/` recursively, no folder or file skipped silently
- [ ] Read `.lovable/memory/index.md` and every file it points at
- [ ] Read `.lovable/plans/index.md`, every file in `pending/`, and all active subtasks
- [ ] Skimmed `.lovable/plans/completed/` for recent history
- [ ] Read every file in `.lovable/spec/commands/`
- [ ] Read every file in `.lovable/issues/` and `.lovable/cicd-issues/`
- [ ] Read every file in `.lovable/ambiguous-questions/01-new-ambiguity/` and `02-ambiguity-resolved/`
- [ ] Looped through the entire `spec/` folder, specifically `spec/21/` (app spec), `spec/02/` (coding guidelines), `spec/03/` (error management), `spec/04/` (database conventions)
- [ ] Autonomously surveyed the whole codebase structure and application components via self-looping
- [ ] Read `spec/12-consolidated-guidelines/` in numeric order (or noted missing)
- [ ] Read `spec/01-spec-authoring-guide/` in numeric order (or noted missing)
- [ ] Can name CODE RED rules, naming conventions, error-handling philosophy without guessing
- [ ] Can list every pending plan slug and subtask from memory
- [ ] Checked whether the repo contains explicit tone, strictly-avoid, or prior-stupidity instructions and applied them without softening
- [ ] Did not replace hard user wording with polite generic language
- [ ] Emitted the Completion Confirmation block verbatim, then stopped
- [ ] Confirmed that reading remained strictly read-only regarding the codebase (no source code refactored, only memory and lowercase readme auto-fix updated)

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.

---

title: Read Memory (Enhanced)
slug: read-memory-enhanced
version: 2.1
