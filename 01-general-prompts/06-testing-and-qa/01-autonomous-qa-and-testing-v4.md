# Instruction (must follow): Autonomous QA & Unit Testing Loop (v4)

/goal Create a comprehensive execution plan to achieve 100% test coverage across the repository, split the work into logical subtasks, and autonomously spawn subagents in a continuous self-loop to execute the testing plan until complete. 

/learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, and `spec/02-coding-guidelines/` before touching any code.

## Variables - Auto-Discovered at Runtime

```text
N = 200 (Default loop limit. User can override.)
```

## Phase 1: Planning & Segmentation

1. Identify packages with incomplete test coverage.
2. Segment large packages (>1000 lines) into discrete tasks (e.g., 200 lines per task).
3. Create a master plan file in `.lovable/plans/pending/XX-qa-coverage.md`.
4. Create explicit subtasks for each package segment in `.lovable/plans/subtasks/XX-qa-coverage/SS-<subslug>.md`.

## Phase 2: Autonomous Execution Loop

1. Spawn dedicated sub-agents to handle the subtasks (MAXIMUM 3 concurrent agents).
2. Context Diet: When spawning a subagent, DO NOT paste file contents, memory logs, or the entire plan into its prompt. Give it the absolute minimal instruction (e.g., "Read subtask file `.lovable/plans/subtasks/XX-qa-coverage/01-task.md` and execute it"). The subagent MUST read the necessary files itself.
3. Subagents must follow the AAA pattern (Arrange, Act, Assert).
4. Subagents must verify tests locally before marking the task `[Done]`.
5. Loop continuously until every subtask in the master plan is marked `[Done]`.


## Pre-Completion Checklist (Must Follow Non-Negotiable)

- [ ] Anti-Garbage Naming (Non-Negotiable): I have strictly verified that absolutely NO generic garbage variable names (e.g., `comp_100.go`, `temp`, `data`, `obj`, `Input100`, `TestHandleComp100`) were written. All names are highly semantic and domain-specific.
- [ ] All tests follow the AAA pattern.
- [ ] All tests run and pass locally.

## Anti-Garbage Naming & Quality (Zero Tolerance)

- NEVER generate arbitrary, generic, or sequential names like `TestComp100`. Test functions must explicitly define exactly what behavior is being tested (e.g., `TestUpdateUserProfile_RejectsInvalidEmail`).
- Do not hallucinate mock interfaces or use arbitrary IDs. Use semantic domain concepts.

## Ambiguity State Management

- If an ambiguity prevents a test from being written, log it to `.lovable/ambiguous-questions/`.
- Immediately update the plan file to mark that specific subtask as `[Blocked]`.
- The execution loop must safely skip `[Blocked]` tasks and continue executing other disjoint tasks. Do not retry blocked tasks.

## Temp Script Sandboxing (Global Law)

If you need to generate any temporary code, scripts, or scratch files to aid in your execution or test generation, you MUST write them strictly into the `.lovable/temp-scripts/` directory. You MUST ensure this directory is added to `.gitignore`. NEVER commit temporary scripts to the repository.

### Temp-Agent State Management Protocol (Non-Negotiable)

To ensure agents do not lose context, you MUST use the `.lovable/temp-agents/` directory for tracking sub-agent tasks.

- On Start: The sub-agent creates `.lovable/temp-agents/<task-name>.md` and writes the objective and `STATUS: IN_PROGRESS`.
- On Error/Crash: If an agent breaks or fails, append the exact error and cause to the file, then append `STATUS: FAILED` before closing.
- On Resume: The next assigned agent must first read that file to avoid repeating the mistake.
- On Success: Update the file to `STATUS: DONE` and immediately update the master plan.
