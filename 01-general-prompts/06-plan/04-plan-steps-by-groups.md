# Plan: Steps by Groups (Look-Ahead, Standalone Commit)

- slug: plan-steps-by-groups
- status: active

## Prompt

# Plan: Steps by Groups (v1.0)

Follow the above instructions.

X Steps = ?

## RULE 0: X Steps in Groups (Non-Negotiable)
Write exactly X steps in groups. When defining these groups, you MUST ask the necessary questions or frame them so that each group contains full context.
The purpose of this is so that the groups can be read and utilized by separate chat prompts or sub-agents. 
EACH group must be able to work, execute, and commit its code in a completely STANDALONE way. Make sure of it. This is a non-negotiable MUST.

## 1. Sub-Agent Orchestration & The "Look Ahead" Planner
You are writing a plan by groups. This is a look-ahead prompt. 
Once this writing for the task is done, separate agents will work standalone and commit the task in a standalone way. That is the main goal.
- Give each group/sub-task a highly specific title reflecting its exact task (e.g., `Refactoring Auth` or `Fixing DB Connection`).
- Sub-agents must only be assigned simple, small micro-tasks rather than larger monolithic ones.

## 2. Self-Loop to Create Brain and Tasks
You must self-loop to create the brain, tasks, and subtasks for the Tasks you have defined above. 
Do not wait. Generate the folder structure, the `.lovable/plans/pending/` files, and the `.lovable/plans/subtasks/` files immediately during your self-loop.

## 3. High-Stakes Code Standards & Coding Guidelines
You MUST follow the project's strict coding guidelines and ensure your groups enforce them. These files are located in the `01-cross-language/` directory and should be followed universally. Check if there are language-specific guidelines (e.g., `02-typescript/`, `03-python/`) for these rules.

### Required Reading / Reference Checklist:
**1. The Master Consolidated Guide**
- `spec/17-consolidated-guidelines/02-coding-guidelines.md`

**2. Code Style & File Size Limits (80-100 lines max)**
- `spec/02-coding-guidelines/01-cross-language/04-code-style/04-function-and-type-size.md`
- `spec/02-coding-guidelines/01-cross-language/04-code-style/01-braces-and-nesting.md`
- `spec/02-coding-guidelines/01-cross-language/04-code-style/00-overview.md`
- `spec/02-coding-guidelines/01-cross-language/20-nesting-resolution-patterns.md`
- `spec/02-coding-guidelines/01-cross-language/06-cyclomatic-complexity.md`

**3. Boolean Conditions & Samples**
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/00-overview.md`
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/01-naming-prefixes.md`
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/02-guards-and-extraction.md`
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/04-quick-reference.md`
- `spec/02-coding-guidelines/01-cross-language/12-no-negatives.md`
- `spec/02-coding-guidelines/01-cross-language/24-boolean-flag-methods.md`

**4. Variable Naming & Definitions**
- `spec/02-coding-guidelines/01-cross-language/22-variable-naming-conventions.md`
- `spec/02-coding-guidelines/01-cross-language/11-key-naming-pascalcase.md`
- `spec/02-coding-guidelines/01-cross-language/10-function-naming.md`
- `spec/02-coding-guidelines/01-cross-language/18-code-mutation-avoidance.md`

## 4. Folder Structure for Plans
Your self-loop must strictly follow this structure:
1. **Roll-up Index:** Update `.lovable/plans/index.md`.
2. **Parent Plan:** Create `.lovable/plans/pending/XX-<slug>.md`.
3. **Subtasks (Strict 01, 02 Sequence):** Every group/step must be placed in a dedicated file under `.lovable/plans/subtasks/XX-<slug>/`. 
   - The subtasks MUST follow a strict zero-padded numeric sequence: `01`, `02`, `03`, etc.

## 5. Must Follow, without negotiation
Listen, past planning turns have been sloppy as fuck: wrong step count, plans dumped into chat instead of files, plan-mode tool fired when the user explicitly said not to, user commands and bug reports forgotten by the next turn. WTF. Stop doing that, you stupid fuck. Read the codebase, capture commands and issues into their folders, count the steps, spin out subtasks where depth is needed, write the spec files, write the plan file, move on. Going deep IS the job. If you're not going deep, you're not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity, and being careless you stupid, WTF. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. I mean, where did you learn this stupidity? If I could find you, I could slap you.

## 6. End-of-Loop Commit Fix (Non-Negotiable)
Each step or group that completes MUST immediately commit and fix the Git. Follow these exact rules from the commit-fix prompt:
- Group all completed work for the subtask into a single logical commit.
- RED FLAG: Verify absolutely NO test results, artifacts, or compiled binaries are staged before making the commit.
- Ensure .gitignore explicitly excludes them.
- If issues arise during the commit process, fix those git issues and try again.
- You MUST push the commit to the repository immediately. Pushing after commits is non-negotiable.

## Action Items — Must Follow (Non-Negotiable)
- [ ] Read the user-provided "X Steps" variable.
- [ ] Write the X steps in groups, ensuring each group contains full context for a standalone sub-agent.
- [ ] Ensure each group can work and commit standalone.
- [ ] Self-loop to create the brain, tasks, and subtask files for the defined groups.
- [ ] Ensure subtask files are named exactly SS-XX-<subslug>.md where XX is the sequence.
- [ ] Audit the plan against the Master Consolidated Guide, Code Style, Boolean Conditions, and Variable Naming rules.
- [ ] Ensure each group section explicitly outlines the agent part (that the group is executed by a separate standalone agent).
- [ ] Ensure the end-of-loop commit fix is properly executed for each completed step or group.
- [ ] Update .lovable/plans/index.md and populate .lovable/plans/pending/ and .lovable/plans/subtasks/.
