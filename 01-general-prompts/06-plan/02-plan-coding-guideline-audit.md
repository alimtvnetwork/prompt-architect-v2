# Plan: Coding Guideline Audit & Massive Execution Plan

- slug: plan-guideline-audit
- status: active

## Prompt

# Plan: Coding Guideline Audit & Massive Execution Plan

## Goal
Your objective is to read the project's coding guidelines, deeply audit the entire codebase for violations, and generate an exhaustive, granular execution plan (100 to 400 steps). 
**You are planning the fixes, not executing them.** You must only write your observations and the resulting plan files into the `.lovable/` folder. Do not refactor or modify any application source code during this run.

## Phase 1: Read Memory and Guidelines
1. Read `.lovable/what-to-read.md` and `.lovable/memory/index.md` to load the project's institutional knowledge.
2. Read the coding guidelines thoroughly (e.g., `spec/02-coding-guidelines/`, `spec/03-error-manage/`, and `.lovable/coding-guidelines.md`).
3. Understand exactly what constitutes a violation based on the project's CODE RED rules and memory files.

## Phase 2: Codebase Audit (Self-Looping Only)
1. You must audit the codebase to find every single inconsistency and violation of the coding guidelines.
2. **Self-Looping:** Because the codebase is large, you must self-loop to read and analyze the files sequentially. 
3. **NO SUB-AGENTS:** Do not spawn sub-agents for this read/audit loop. Sub-agent looping is strictly restricted for this task to avoid context loss and ensure the central planner retains full visibility.
4. Record your raw observations and findings inside `.lovable/memory/learned/XX-guideline-audit-observations.md`.

## Phase 3: Massive Plan Generation
Based on your observations, you must break down the fixes into an extremely granular plan. If there are hundreds of violations, you must create hundreds of steps. The goal is to create a detailed roadmap that future sub-agents can pick up and execute flawlessly.

### Folder Structure & Naming Conventions
All plans must strictly follow this structure:
1. **Roll-up Index:** Update `.lovable/plans/index.md` with the new plan.
2. **Parent Plan:** Create `.lovable/plans/pending/XX-<slug>.md` (e.g., `04-global-guideline-fixes.md`). This file will list the high-level roadmap and refer to the subtasks.
3. **Subtasks (Strict 01, 02 Sequence):** Every single fix must be placed in a dedicated subtask file under `.lovable/plans/subtasks/XX-<slug>/`. 
   - The subtasks MUST follow a strict zero-padded numeric sequence: `01`, `02`, `03`, etc.
   - Example: `.lovable/plans/subtasks/04-global-guideline-fixes/01-fix-auth-boolean.md`
   - Example: `.lovable/plans/subtasks/04-global-guideline-fixes/02-fix-db-magic-strings.md`
   - Do not use any other naming convention for the subtasks. Maintain this `01, 02, 03...` sequence everywhere.

### Subtask Content
Inside each `01...` subtask file, detail exactly:
- The target file.
- The specific lines violating the guideline.
- The guideline rule being broken.
- The exact instruction for the future executing agent on how to refactor it.

## Execution Ban (Non-Negotiable)
- **DO NOT EXECUTE THE FIXES.** 
- You are strictly permitted to write to the `.lovable/` folder (memory files, observations, and plan files) only.
- You must not edit, refactor, or write any application source code.

## Pre-Reply Checklist
- [ ] Read the coding guidelines and project memory.
- [ ] Self-looped to audit the entire codebase (without spawning sub-agents).
- [ ] Recorded observations in `.lovable/memory/learned/XX-<slug>.md`.
- [ ] Created a massive, detailed parent plan in `.lovable/plans/pending/`.
- [ ] Created granular subtask files in `.lovable/plans/subtasks/` using strictly `01`, `02`, `03` sequential naming.
- [ ] Updated `.lovable/plans/index.md`.
- [ ] Confirmed absolutely zero application source code was modified.
