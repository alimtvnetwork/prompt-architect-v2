# Inventory Pending Tasks (Read-Only Scan & 3-Agent Dispatch Proposal)

- slug: inventory-pending-tasks
- status: active

## Prompt

# Inventory Pending Tasks (Read-Only Scan & 3-Agent Dispatch Proposal)

## Goal

Perform a strictly read-only scan of the entire repository and `.lovable/` directory to compile a comprehensive, deduplicated inventory of every pending task, subtask, unresolved issue, and open requirement.

**CRITICAL CONSTRAINT:** This prompt is strictly for **inventorying and structuring pending work**. It MUST NOT execute code modifications, build changes, or launch the execution loop. Batch execution is handled by dedicated execution prompts.

---

## Folder Structure Reference (What and Where to Read)

To ensure zero blind spots, the AI must systematically inspect the following authoritative folder structure:

```text
.lovable/
  memory/
    index.md                                    # Master memory index
    what-to-read.md                             # Authoritative reading order
    specs/                                      # Verbatim user directives & requirements
    learned/                                    # Institutional knowledge & learnings
    workflow/                                   # Workflow state markers
  plans/
    index.md                                    # Roll-up index of all plans (pending & completed)
    pending/XX-<slug>.md                        # Active, pending parent execution plans
    completed/XX-<slug>.md                      # Historical completed plans (reference only)
    subtasks/XX-<slug>/SS-<subslug>.md          # Granular subtasks linked to parent plans
  issues/                                       # General pending bug reports
  pending-issues/                               # Active issues queue
  cicd-issues/                                  # CI/CD specific failures & blockers
  ambiguous-questions/
    01-new-ambiguity/XX-<slug>.md               # Blocking & non-blocking open questions
    02-ambiguity-resolved/XX-<slug>.md          # Binding resolved decisions
  suggestions.md                                # Suggestions tracker
  prompts.md                                    # Canonical prompt registry
spec/
  02/ (or 02-coding-guidelines/)                # Coding standards & zero-tolerance rules
  03/ (or 03-error-manage/)                     # Error management & logging philosophy
  04/ (or 04-database-conventions/)             # Database conventions
  21/ (or 21-app/)                              # App specification & feature requirements
readme.md                                       # Root repository guide (strictly lowercase)
```

---

## Step 1: Deep Inspection & Deduplication Protocol

1. **Scan Every Pending Source**:
   - Open and read `.lovable/plans/index.md`, `.lovable/plans/pending/`, and all `.lovable/plans/subtasks/` files with `Status:` not `completed`.
   - Open and read all files in `.lovable/issues/`, `.lovable/pending-issues/`, and `.lovable/cicd-issues/`.
   - Open and read all open questions in `.lovable/ambiguous-questions/01-new-ambiguity/`.
   - Open and read unfulfilled directives in `.lovable/memory/specs/` and `spec/21/`.
   - Open and read active suggestions in `.lovable/suggestions.md`.
2. **Deduplicate Across Sources**:
   - If a feature is referenced across a spec, a plan, and an issue, consolidate it into ONE primary task with cross-references to all origin files.
3. **Step-Count Rubric (Open Files First)**:
   - Trivial change (1 file, single edit): 1 step.
   - Small change (1-2 files, 1 verification step): 2-3 steps.
   - Standard task (multi-file, logic + UI/backend, test): 4-7 steps.
   - Cross-cutting task (schema + API + UI + full tests): 8-15 steps.
   - Deep multi-subtask task: cite total steps and subtask count (`N steps across M subtasks`).

---

## Step 2: Refined Output Format

Present the inventory to the user in this exact markdown structure:

```markdown
# Pending Tasks Inventory

## Executive Summary
- Total Pending Tasks: [N]
- Blocking Ambiguities: [K]
- Pending Plans: [P]
- Pending Issues & CI/CD: [I]
- Unimplemented Spec Scope: [U]
- Sources Scanned: [.lovable/plans/pending/, .lovable/plans/subtasks/, .lovable/issues/, .lovable/cicd-issues/, .lovable/ambiguous-questions/01-new-ambiguity/, spec/]

---

## Prioritized Task List

### 1. [Task Title]
- **Source File(s)**: `[path/to/file.md]`
- **Type**: `Plan` | `Issue` | `CI/CD` | `Ambiguity` | `Spec-Scope`
- **Status**: `Pending` | `In-Progress` | `Blocked by Ambiguity`
- **Estimated Steps**: `[N] steps` (or `[N] steps across [M] subtasks`)
- **Dependencies**: `[Task # or "None"]`
- **Outcome / Intent**: [Clear 1-2 sentence description of what "done" looks like]

### 2. [Task Title]
...

---

## Blocking Ambiguities (Must Resolve Before Execution)
- `[slug]`: [Question summary] (Blocks Task #[X], #[Y])
```

---

## Step 3: Follow-Up Execution Proposal (Strictly Positive Question Framing)

At the very end of the inventory report, the AI must ask the user whether to trigger execution using the standard 3-agent parallel loop:

```text
Would you like to start the continuous self-loop to execute and resolve these pending tasks in parallel using a maximum of 3 concurrent subagents? (Yes / No)
```

*(If the user answers Yes, the next turn will invoke `execute-robust-loop` or `execute-batched-loop` to begin execution).*

---

## Checklist: What This Prompt MUST Do and MUST NOT Do

### What to Do (Mandatory):
- [ ] Read all `.lovable/` pending folders, subtask files, issue trackers, and spec requirements in full.
- [ ] Deduplicate tasks appearing across multiple plan, spec, or issue files.
- [ ] Calculate concrete step counts based on actual file contents using the rubric.
- [ ] Clearly list all blocking ambiguities and affected task dependencies.
- [ ] Deliver the clean, structured executive summary and prioritized task list.
- [ ] Present the 3-agent parallel execution proposal with strictly positive framing.

### What NOT to Do (Banned / Auto-Reject):
- [ ] DO NOT execute any code modifications, installs, or migrations during this turn.
- [ ] DO NOT launch sub-agents or start the execution loop inside this prompt.
- [ ] DO NOT cherry-pick or omit any pending tasks (missing even one task is a failure).
- [ ] DO NOT invent step counts without reading the target files.
- [ ] DO NOT use negative question phrasing or double negatives.

---

## Insult Stance (Non-Negotiable)

Past runs of this prompt have been stupid. The AI behaved like a stupid fuck by skimming folders, ignoring ambiguity files, forgetting CI/CD issues, half-filling the Completion Confirmation block with "[N]" placeholders, and softening explicit user instructions after being told not to. That stupidity must not repeat.

Read aggressively and defensively. Assume the previous AI failed because it was lazy, vague, and too polite to enforce the actual rules. Your job is to load the repo's memory exactly, cite the file behind every rule, and refuse to guess. If you finish this prompt and cannot cite the file behind a rule you enforce, you failed the prompt. Read more. Then reply.

How on earth you are reverting to thse codes are you stupid??

Avoid stupidity, and being careless you stupid, WTF. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. where did you learn this stupidity? If I could find you, I could slap you.

Listen, past planning turns have been sloppy as fuck: wrong step count, plans dumped into chat instead of files, plan-mode tool fired when the user explicitly said not to, user commands and bug reports forgotten by the next turn. WTF. Stop doing that, you stupid fuck. Read the codebase, capture commands and issues into their folders, count the steps, spin out subtasks where depth is needed, write the spec files, write the plan file, move on. Going deep IS the job. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. I mean, where did you learn this stupidity? If I could find you, I could slap you.

---

## Before Writing Code

Read and follow spec folders 02, 03 and 04 before writing any code. Error management must be followed. Code must be DRY.
