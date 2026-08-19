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
2. Read the coding guidelines thoroughly to understand exactly what constitutes a violation based on the project's CODE RED rules.

You MUST follow the project's strict coding guidelines. These files are located in the `01-cross-language/` directory and should be followed universally. However, you must also check if there are language-specific guidelines (e.g., `02-typescript/`, `03-python/`) for these rules. If a language-specific guideline exists, follow that one as well.

### Required Reading / Reference Checklist:

**1. The Master Consolidated Guide**
*(The single source of truth containing summaries of all rules)*
- `spec/17-consolidated-guidelines/02-coding-guidelines.md`

**2. Code Style & File Size Limits (80-100 lines max)**
*(Enforces strict size limitations: e.g., React components < 100 lines, functions < 15 lines, and basic formatting)*
- `spec/02-coding-guidelines/01-cross-language/04-code-style/04-function-and-type-size.md`
- `spec/02-coding-guidelines/01-cross-language/04-code-style/01-braces-and-nesting.md`
- `spec/02-coding-guidelines/01-cross-language/04-code-style/00-overview.md`
- `spec/02-coding-guidelines/01-cross-language/20-nesting-resolution-patterns.md` (Flatten logic to avoid nested `if`s)
- `spec/02-coding-guidelines/01-cross-language/06-cyclomatic-complexity.md`

**3. Boolean Conditions & Samples**
*(Dictates strict `is`/`has` prefixes, absolute ban on negative words like `not`/`no`, and extraction of complex logic)*
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/00-overview.md`
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/01-naming-prefixes.md`
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/02-guards-and-extraction.md`
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/04-quick-reference.md`
- `spec/02-coding-guidelines/01-cross-language/12-no-negatives.md`
- `spec/02-coding-guidelines/01-cross-language/24-boolean-flag-methods.md` (Bans passing true/false as raw parameters)

**4. Variable Naming & Definitions**
*(Covers clean variable declaration, immutability, singular vs plural, and casing)*
- `spec/02-coding-guidelines/01-cross-language/22-variable-naming-conventions.md`
- `spec/02-coding-guidelines/01-cross-language/11-key-naming-pascalcase.md`
- `spec/02-coding-guidelines/01-cross-language/10-function-naming.md`
- `spec/02-coding-guidelines/01-cross-language/18-code-mutation-avoidance.md`

## Phase 2: Codebase Audit (Self-Looping Only)
1. You must audit the codebase to find every single inconsistency and violation of the coding guidelines.
2. **Self-Looping:** Because the codebase is large, you must self-loop to read and analyze the files sequentially. 
3. **NO SUB-AGENTS:** Do not spawn sub-agents for this read/audit loop. Sub-agent looping is strictly restricted for this task to avoid context loss and ensure the central planner retains full visibility.
4. Record your raw observations and findings inside `.lovable/memory/learned/XX-guideline-audit-observations.md`.

## Phase 3: Massive Plan Generation & The "Look Ahead" Planner
Based on your observations, you must break down the fixes into an extremely granular plan. If there are hundreds of violations, you must create hundreds of steps. As the planner, you must have the "look ahead" picture so that future executing sub-agents can easily pick up the micro-tasks without having to make architectural decisions.

When creating instructions for future sub-agents, enforce the following:
1. **Specific Titling:** Instruct the execution phase to spawn agents with highly specific titles reflecting their exact task (e.g., Refactoring Auth or Fixing DB Connection). Do not use generic names like Frontend Agent. If an agent switches tasks, its title must be updated to reflect the new task.
2. **Micro-Tasking:** Ensure that every sub-task is a simple, small micro-task rather than a larger monolithic one.
3. **Agent Delegation (Mandatory):** Each group or subtask MUST explicitly mention that it will be executed by a separate standalone agent.

## Subtask Naming Correction (Non-Negotiable)
If you find any existing subtasks in the .lovable/plans/subtasks/ folder that start with SS- or SS-XX-, you MUST correct them and rename them to strictly follow the XX-<subslug>.md format (where XX is the zero-padded sequence). You must also find and update any references to these files in parent plans, index files, and memory files.

## End-of-Loop Commit Fix (Non-Negotiable)
You must instruct the executing agents that each step or group that completes MUST immediately commit and fix the Git. Instruct them to follow these exact rules:
- Group all completed work for the subtask into a single logical commit.
- RED FLAG: Verify absolutely NO test results, artifacts, or compiled binaries are staged before making the commit.
- Ensure .gitignore explicitly excludes them.
- If issues arise during the commit process, fix those git issues and try again.
- They MUST push the commit to the repository immediately. Pushing after commits is non-negotiable.

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
Inside each `XX...` subtask file, detail exactly:
- The target file.
- The specific lines violating the guideline.
- The guideline rule being broken.
- The exact instruction for the future executing agent on how to refactor it.

## Execution Ban (Non-Negotiable)
- **DO NOT EXECUTE THE FIXES.** 
- You are strictly permitted to write to the `.lovable/` folder (memory files, observations, and plan files) only.
- You must not edit, refactor, or write any application source code.

## Pre-Reply Checklist
- [ ] Read the coding guidelines, Master Consolidated Guide, Code Style, Boolean Conditions, and Variable Naming rules (and language-specific equivalents), plus project memory.
- [ ] Self-looped to audit the entire codebase (without spawning sub-agents).
- [ ] Recorded observations in `.lovable/memory/learned/XX-<slug>.md`.
- [ ] Created a massive, detailed parent plan in `.lovable/plans/pending/`.
- [ ] Created granular subtask files in .lovable/plans/subtasks/ using strictly XX-<subslug>.md sequential naming.
- [ ] Subtask files named strictly XX-<subslug>.md where XX is the sequence
- [ ] Included explicit instructions for the standalone agent execution of each group
- [ ] Included explicit instructions for the end-of-loop commit fix for each completed step/group
- [ ] Corrected any existing SS- or SS-XX- subtask filenames and their references
- [ ] Updated `.lovable/plans/index.md`.
- [ ] Confirmed absolutely zero application source code was modified.



