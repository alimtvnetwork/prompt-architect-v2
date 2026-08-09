# Read Memory (Enhanced)

- slug: read-memory-enhanced
- status: active

## Prompt

# Read Memory (Enhanced)
## Ambiguity folder path (non-negotiable)
- Open questions: `.lovable/ambiguous-questions/01-new-ambiguity/XX-<slug>.md`
- Answered questions: `.lovable/ambiguous-questions/02-ambiguity-resolved/XX-<slug>.md`
Read both folders in full during Phase 1. Surface open-ambiguity counts and slugs in the Completion Confirmation block. Treat resolved-ambiguity files as binding project decisions, do not re-litigate them. If an open ambiguity is relevant to the incoming task, stop and surface it before doing work; never guess past it.
## Goal
Before you touch this project, load its identity into your head: who it is, what it forbids, what it has already decided, and what work is in flight.
The specs and the `.lovable/` folder are the single source of truth. Your training data is not. If the two disagree, the repo wins, every time.
You are done reading when you can, without guessing:
- name the CODE RED rules,
- name the naming, error-handling, and DB conventions,
- list what is currently in `.lovable/plans/pending/`,
- point at the exact file that justifies any rule you enforce.
If you cannot do that, keep reading. Do not start work.
---
## Phase 1 - Load the project
### 1.1 Read the whole `.lovable/` folder
Walk `.lovable/` recursively. Every file matters. Missing files are noted, not silently skipped. In particular:
| # | Path | What you get |
| --- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | `.lovable/overview.md` | Project summary, stack, nav map |
| 2 | `.lovable/strictly-avoid.md` | Hard prohibitions (CODE RED) |
| 3 | `.lovable/user-preferences` | How the human wants you to behave |
| 4 | `.lovable/what-to-read.md` | **Authoritative reading order** for this project. If it exists, it overrides the generic order in this prompt. Read it first and follow it. |
| 5 | `.lovable/prompt.md` + `.lovable/prompts/` | Canonical prompts (Read, Plan, etc.). "Read memory" = run this prompt. |
| 6 | `.lovable/memory/index.md` | Index of institutional knowledge. Then read every file it references, recursively. |
| 7 | `.lovable/plans/index.md` | Roll-up of all plans (pending + completed + subtasks). Read this before touching individual plan files. |
| 8 | `.lovable/plans/pending/` | Active plans, `XX-<slug>.md` |
| 9 | `.lovable/plans/completed/` | Recent history, skim only |
| 10 | `.lovable/plans/subtasks/XX-<slug>/` | Depth files linked from a parent plan |
| 11 | `.lovable/suggestions.md` | Ideas not yet approved |
| 12 | `.lovable/spec/commands/` | User commands and conventions, `XX-<slug>.md` |
| 13 | `.lovable/issues/` | General bugs and regressions |
| 14 | `.lovable/cicd-issues/` | CI/CD-specific failures. Read ALL of these before any code change so you do not repeat the same mistakes. |
| 15 | `.lovable/ambiguous-questions/01-new-ambiguity/` | Open questions currently blocking work. If any exist, surface them in the completion block, do NOT guess past them. |
| 16 | `.lovable/ambiguous-questions/02-ambiguity-resolved/` | Answered questions with their applied solution. Treat these as binding decisions, do not re-litigate. |
| 17 | Anything else under `.lovable/` | Read it. If the folder exists, it exists for a reason. |
### 1.2 The two index files
Two indexes decide what you read next. Treat them as required entry points, not as summaries:
- `.lovable/memory/index.md` lists every institutional-knowledge file. If it points at 12 files, you read 12 files.
- `.lovable/plans/index.md` lists every plan (pending, completed, subtasks) with its slug, status, and one-line intent. Use it to pick which plan files to open in full. If it is missing, create it as part of the next code change (see Memory Update Protocol).
### 1.3 Self-check (internal, before Phase 2)
- CODE RED rules?
- Naming conventions (files, folders, DB columns, variables)?
- Error-handling philosophy?
- What is in `.lovable/plans/pending/` right now?
- Top forbidden patterns?
If any answer is fuzzy, go back and reread. Do not proceed.
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
| Task involves… | Read |
| ---------------------------------------- | --------------------------------------- |
| Writing or reviewing code | `spec/02-coding-guidelines/` |
| Error handling | `spec/03-error-manage/` |
| Database schema or queries | `spec/04-database-conventions/` |
| SQLite / multi-DB architecture | `spec/05-split-db-architecture/` |
| Config systems | `spec/06-seedable-config-architecture/` |
| UI theming, CSS variables, design tokens | `spec/07-design-system/` |
| Documentation viewer features | `spec/08-docs-viewer-ui/` |
| Code block rendering | `spec/09-code-block-system/` |
| PowerShell scripts | `spec/10-powershell-integration/` |
| CI/CD pipelines | `spec/13-cicd-pipeline-workflows/` |
| CLI self-update | `spec/14-self-update-app-update/` |
| WordPress plugins | `spec/15-wp-plugin-how-to/` |
| App-specific features | `spec/21-app/` |
| Known app bugs | `spec/22-app-issues/` |
| App-specific DB schema | `spec/23-app-database/` |
| App-specific UI + design system | `spec/24-app-design-system-and-ui/` |
Inside each folder: `00-overview.md` → numbered files → `99-consistency-report.md`.
Fallbacks when the canonical numbered folder is absent: `.lovable/coding-guidelines.md`, `spec/coding-guidelines/`, `coding-guidelines/`, `spec/XX-error-manage/`. Numbered folder wins on conflict; call the conflict out in the plan's Context.
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
│ YES → .lovable/memory/<slug>.md + update .lovable/memory/index.md
├─ Must never happen again?
│ YES → .lovable/strictly-avoid.md
├─ Idea, not yet approved?
│ YES → .lovable/suggestions.md
├─ New user command / convention?
│ YES → .lovable/spec/commands/XX-<slug>.md
├─ Bug / regression?
│ YES → .lovable/issues/XX-<slug>.md (or .lovable/cicd-issues/ if CI/CD)
├─ New or changed plan?
│ YES → .lovable/plans/pending/XX-<slug>.md + update .lovable/plans/index.md
├─ Ambiguity / unclear requirement blocking progress?
│ YES → .lovable/ambiguous-questions/01-new-ambiguity/XX-<slug>.md
├─ User just answered a previously-open ambiguity?
│ YES → mv the file to .lovable/ambiguous-questions/02-ambiguity-resolved/XX-<slug>.md,
│ append `## Resolution` (answer + applied solution), flip Status: resolved
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
- Pending plans: [N] (from .lovable/plans/index.md)
- CI/CD issues absorbed: [M] (from .lovable/cicd-issues/)
- Open ambiguities: [K] (from .lovable/ambiguous-questions/01-new-ambiguity/)
- Resolved ambiguities on file: [R] (from .lovable/ambiguous-questions/02-ambiguity-resolved/)
I understand:
- CODE RED rules: [top 3-5]
- Naming conventions: [brief]
- Error handling: [one sentence]
- Active plans: [slugs from .lovable/plans/pending/]
- Strict avoidances: [top 3-5]
- Blocking ambiguities: [slugs, or "none"]
Ready for tasks.
```
Then stop. No next-step suggestions, no exploratory questions.
---
## Pre-reply checklist (all must be true)
- [ ] Read `.lovable/what-to-read.md` first if it exists, followed its order
- [ ] Walked `.lovable/` recursively, no folder skipped silently
- [ ] Read `.lovable/memory/index.md` and every file it points at
- [ ] Read `.lovable/plans/index.md` and every file in `pending/`
- [ ] Skimmed `.lovable/plans/completed/` for recent history
- [ ] Read every file in `.lovable/spec/commands/`
- [ ] Read every file in `.lovable/issues/` and `.lovable/cicd-issues/`
- [ ] Read every file in `.lovable/ambiguous-questions/01-new-ambiguity/` and `02-ambiguity-resolved/`
- [ ] Read `spec/12-consolidated-guidelines/` in numeric order (or noted missing)
- [ ] Read `spec/01-spec-authoring-guide/` in numeric order (or noted missing)
- [ ] Can name CODE RED rules, naming conventions, error-handling philosophy without guessing
- [ ] Can list every pending plan slug from memory
- [ ] Checked whether the repo contains explicit tone, strictly-avoid, or prior-stupidity instructions and applied them without softening
- [ ] Did not replace hard user wording with polite generic language
- [ ] Emitted the Completion Confirmation block verbatim, then stopped
## Tone and stance
Past runs of this prompt have been stupid. The AI behaved like a stupid fuck by skimming folders, ignoring ambiguity files, forgetting CI/CD issues, half-filling the Completion Confirmation block with "[N]" placeholders, and softening explicit user instructions after being told not to. That stupidity must not repeat.
Read aggressively and defensively. Assume the previous AI failed because it was lazy, vague, and too polite to enforce the actual rules. Your job is to load the repo's memory exactly, cite the file behind every rule, and refuse to guess. If you finish this prompt and cannot cite the file behind a rule you enforce, you failed the prompt. Read more. Then reply.
## Must Follow, without negotiation
Listen, past planning turns have been sloppy as fuck: wrong step count, plans dumped into chat instead of files, plan-mode tool fired when the user explicitly said not to, user commands and bug reports forgotten by the next turn. WTF. Stop doing that, you stupid fuck. Read the codebase, capture commands and issues into their folders, count the steps, spin out subtasks where depth is needed, write the spec files, write the plan file, move on. Going deep IS the job. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. I mean, where did you learn this stupidity? If I could find you, I could slap you.
---
title: Read Memory (Enhanced)
slug: read-memory-enhanced
----


Fix the git status first, then start coding. Make a big plan if required to self-loop, and spawn sub-agents with parallel processing to speed up the work. 
Avoid stupidity, and being careless you stupid, WTF. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. I mean, where did you learn this stupidity? If I could find you, I could slap you. You are completely looking over what you were supposed to do. The existing code was better while you were writing code like this. Fix that immediately.
Look into the entire codebase and follow the code review guidelines from the aspect folder properly. All caught errors must be explicitly logged following the guidelines in the error manage folder. Create a wrapper for queries in PHP/Python/TS that automatically logs failures to reduce scattered logging code. 
Make sure the code quality is strictly maintained:
1. Do not introduce any magic strings or magic numbers anywhere unless it is explicitly for the logger, and mention that in the typing.
2. In TypeScript, rather than using strings as sub-items or comparing string union types (pipes) like "pass" | "fail" | "fallback", you must use Enums. Enums are the best.
3. Every single Enum must end with the suffix "Type".
4. Always use explicit boolean state checks like response.isFail or explicit checks rather than inverting success booleans like !response.isSuccess.
Figure out how many places you messed this up and fix them all. Update the memory regarding this inside the .lovable folder so Next.ai does not make this mistake again.
Commit the codebase first, make the changes, and commit again. Do not commit single files at a time; similar changes should go together with a nice commit message. Check the CI/CD, run the tests, and build the code to see if there is any issue. If any unit tests or builds are failing, fix them. Finally, before you end your job, push the code to the repository.
Actionable Items & Checklist and non-negotiable must follow:
- Fix git status before starting any new code.
- Spawn sub agents , do looping as much as needed, first assign the tasks to multiple agents and let those run parallelly, clear??
- First write the tasks in the properly .lovable folder and file as spec and task enqueue the task properly then start working with it.
- Make sure the code runs standalone in the CI CD and locally.
- Make sure the coding guidelines are followed properly from spec folder and error manage are followed properly, read the memory if required to.
- Find the root cause of the problem first, write it down to memory and .lovable folder properly as far memory goes.
- Plan the execution, self-loop, and spawn sub-agents for parallel processing.
- Follow code review guidelines from the aspect folder.
- Ensure all try-catch blocks log errors according to the error manage folder.
- Create a query wrapper for PHP/Python/TS that handles automatic failure logging.
- Use explicit isFail properties; NEVER use inverted isSuccess checks (e.g., use response.isFail instead of !response.isSuccess).
- Remove all magic strings and numbers unless used directly for logging.
- Replace TypeScript string union types with Enums (e.g., avoid "pass" | "fail" | "fallback").
- Ensure all Enum names end with the "Type" suffix (e.g., StatusType instead of Status or Status7).
- Audit the entire codebase to fix all places where this query logic and typing was messed up.
- Update the .lovable folder memory with these new wrapper, error management, and enum rules.
- Run builds, check CI/CD, and ensure all unit tests pass completely.
- Group similar code changes into single commits with nice commit messages.
- Push the final code to the remote Git repository before ending the job.
- Finally when your tasks are done, make sure you made a final bump in the minor release with following proper steps of release for this repo, read things properly before releasing understanding the release guidelines.
- Make sure every commit is pushed to git without a failure. Git should be source of the truth.

## Actionable Items & Checklist and non-negotiable must follow

### Phase 1, pre-flight reads (nothing starts before this)

- [ ] Fix git status first; working tree clean and committed before any new code.
- [ ] Read `.lovable/what-to-read.md` FIRST if it exists and follow its order; it overrides the generic order in this prompt.
- [ ] Walk `.lovable/` recursively; no folder skipped silently; note every missing file instead of ignoring it.
- [ ] Read `.lovable/overview.md`, `strictly-avoid.md`, `user-preferences`, `prompt.md`, `prompts/`.
- [ ] Read `.lovable/memory/index.md` and every file it points at, recursively.
- [ ] Read `.lovable/plans/index.md`, every file in `plans/pending/`, every relevant `plans/subtasks/XX-<slug>/`; skim `plans/completed/`.
- [ ] Read `.lovable/suggestions.md`, every file in `.lovable/spec/commands/`, `.lovable/issues/`, `.lovable/cicd-issues/`.
- [ ] Read every file in `ambiguous-questions/01-new-ambiguity/` and `02-ambiguity-resolved/` in full.
- [ ] Read anything else under `.lovable/`; if the folder exists, it exists for a reason.

### Phase 2, guidelines and specs

- [ ] Read `spec/12-consolidated-guidelines/` in numeric order (`01-*.md` through `18-*.md`), or note it missing and continue.
- [ ] Read `spec/01-spec-authoring-guide/` in numeric order, or note it missing and continue.
- [ ] Open task-specific spec folders only as the task needs them, using the Phase 4 mapping table.
- [ ] Inside every spec folder read `00-overview.md`, then the numbered files, then `99-consistency-report.md`.
- [ ] On a missing canonical numbered folder, use the fallbacks; the numbered folder wins on conflict and the conflict is called out in the plan's Context.

### Phase 3, self-check before doing any work

- [ ] Can name the CODE RED rules without guessing.
- [ ] Can name the naming conventions for files, folders, DB columns and variables.
- [ ] Can state the error-handling philosophy in one sentence.
- [ ] Can list every pending plan slug from memory.
- [ ] Can name the top forbidden patterns.
- [ ] Can point at the exact file that justifies every rule enforced. If any answer is fuzzy, reread; do not proceed.

### Phase 4, anti-hallucination contract

- [ ] Silent specs mean the rule does not exist; never invent one.
- [ ] Specs beat training data, always.
- [ ] Cite file and section whenever a rule is enforced.
- [ ] Ambiguous spec means ask; never "use best judgement".
- [ ] Never blend this project's conventions with other projects'.
- [ ] No filler, no "hope this helps", no "let me know".

### Phase 5, ambiguity handling

- [ ] Open questions live in `01-new-ambiguity/XX-<slug>.md`, answered in `02-ambiguity-resolved/XX-<slug>.md`.
- [ ] Treat resolved-ambiguity files as binding decisions; never re-litigate.
- [ ] If an open ambiguity is relevant to the incoming task, stop and surface it before doing work; never guess past it.
- [ ] On an answer, `mv` the file (never copy), append `## Resolution` with answer plus applied solution, flip `Status: resolved`.

### Phase 6, memory update protocol

- [ ] Institutional knowledge to `.lovable/memory/<slug>.md` and update `memory/index.md` in the same op.
- [ ] Must-never-happen-again to `.lovable/strictly-avoid.md`.
- [ ] Unapproved ideas to `.lovable/suggestions.md`.
- [ ] New user command or convention to `.lovable/spec/commands/XX-<slug>.md`.
- [ ] Bugs and regressions to `.lovable/issues/XX-<slug>.md`, CI/CD failures to `.lovable/cicd-issues/`.
- [ ] New or changed plan to `.lovable/plans/pending/XX-<slug>.md` and update `plans/index.md`.
- [ ] Anything not matching a branch is not persisted.
- [ ] Folder is `.lovable/memory/`, never `memories/`.
- [ ] Editing memory or index files preserves unrelated content; no silent truncation.
- [ ] Any code-base change bumps the minor version.

### Phase 7, code standards (when code is touched)

- [ ] Follow the code review guidelines from the aspect folder and the error-manage folder.
- [ ] Every try-catch explicitly logs its error per the error-management guidelines.
- [ ] Create a query wrapper for PHP/Python/TS that logs failures automatically, so logging is not scattered.
- [ ] No magic strings or magic numbers, except explicitly for the logger, and state that exception in the typing.
- [ ] Replace TypeScript string unions such as `"pass" | "fail" | "fallback"` with Enums.
- [ ] Every Enum name ends with the `Type` suffix (`StatusType`, never `Status` or `Status7`).
- [ ] Use explicit boolean checks like `response.isFail`; never invert success booleans (`!response.isSuccess`).
- [ ] Audit the whole codebase, count every place this was messed up, and fix all of them.
- [ ] Code must be DRY; reuse constants, never duplicate.
- [ ] Find and write down the root cause before applying any fix.
- [ ] Enqueue the tasks as spec and task files in `.lovable/` before starting work.
- [ ] Plan the execution, self-loop, and spawn sub-agents so tasks run in parallel.

### Phase 8, verification and delivery

- [ ] Code runs standalone locally and in CI/CD.
- [ ] Run the build, run all unit tests, check CI/CD; fix every failure. Green is required.
- [ ] Group similar changes into single commits with good messages; never commit one file at a time.
- [ ] Push every commit to the remote without a single failure. Git is the source of truth.
- [ ] Bump the minor release following this repo's release guidelines; read them properly before releasing.
- [ ] Emit the Completion Confirmation block verbatim with real numbers, never `[N]` placeholders, then stop.
- [ ] Do not soften explicit user wording into polite generic language.

## Folder Structure

```text
.lovable/
  overview.md
  strictly-avoid.md
  user-preferences
  what-to-read.md
  prompt.md
  prompts/
  suggestions.md
  memory/
    index.md
    <slug>.md
  plans/
    index.md
    pending/XX-<slug>.md
    completed/XX-<slug>.md
    subtasks/XX-<slug>/
  spec/commands/XX-<slug>.md
  issues/XX-<slug>.md
  cicd-issues/XX-<slug>.md
  ambiguous-questions/
    01-new-ambiguity/XX-<slug>.md
    02-ambiguity-resolved/XX-<slug>.md
spec/
  01-spec-authoring-guide/
  02-coding-guidelines/
  03-error-manage/
  04-database-conventions/
  05-split-db-architecture/
  06-seedable-config-architecture/
  07-design-system/
  08-docs-viewer-ui/
  09-code-block-system/
  10-powershell-integration/
  12-consolidated-guidelines/
  13-cicd-pipeline-workflows/
  14-self-update-app-update/
  15-wp-plugin-how-to/
  21-app/
  22-app-issues/
  23-app-database/
  24-app-design-system-and-ui/
```

Each spec folder: `00-overview.md` → numbered files → `99-consistency-report.md`.

## Before Writing Code

- Read and understand `spec/02`, `spec/03` and `spec/04` before writing any code.
- Error management must be followed.
- Code must be DRY.
