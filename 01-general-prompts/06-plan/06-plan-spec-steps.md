# Instruction (must follow): Plan: Spec Steps (Look-Ahead, Standard)

Follow the above instructions.

N = [Number of steps the planning AI should self-loop to write the detailed task spec]

## RULE 0: Do NOT Execute (Non-Negotiable)

DO NOT EXECUTE the task initially. Your first responsibility is to write the spec based on what is given. No code edits, migrations, installs, or shell side effects should occur in this turn. Spec first, then plan.

## 1. Asset & Image Handling

If any images or files are provided, you MUST save them into the `assets/` folder.
- Rename them properly based on the task context (lowercase-hyphenated).
- You MUST refer back to these images in the markdown spec files you write.

## 2. High-Detail Task Breakdown (The "High-Powered Brain")

You must use your high-powered brain to write tasks that explicitly detail:
- **Where** the code is.
- **What** the issue is.
- **How** to change it.

The tasks must be so detailed and explicit that the next executing AI (who requires less brain) can simply follow the instructions without guessing. 

## 3. Self-Loop to Create Brain and Tasks

You must self-loop `N` times to create the brain, tasks, and detailed specs.
Generate the folder structure and the `.lovable/plans/pending/` files immediately during your self-loop.
Your self-loop must strictly follow this structure:
1. Roll-up Index: Update `.lovable/plans/index.md`.
2. Parent Plan: Create `.lovable/plans/pending/XX-<slug>.md`.
3. Detailed Steps (Strict 01, 02 Sequence): Every step must be detailed inside the parent plan or placed in a dedicated file under `.lovable/plans/subtasks/XX-<slug>/` if it requires more depth.
   - Any subtasks MUST follow a strict zero-padded numeric sequence: `01`, `02`, `03`, etc.

## 4. High-Stakes Code Standards, Error Management & Guidelines

You MUST follow the project's strict coding guidelines and ensure your plans enforce them.
For every task, you MUST check if the following files or folders exist. **If they exist, they MUST be followed and included in the task's checklist for the executing AI to follow. If they do not exist, they can be skipped.**

### Dynamic Required Reading / Reference Checklist (Non-Negotiable):

1. **Root Memory Guidelines**
- `.lovable/coding-guidelines/coding-guidelines.md` (and/or `.lovable/memory/coding-guidelines.md`)

2. **Master Consolidated Guide & Coding Guidelines**
- `spec/17-consolidated-guidelines/02-coding-guidelines.md`
- `spec/02-coding-guidelines/01-cross-language/15-master-coding-guidelines/00-overview.md`

3. **Error Management (Must Follow for all Coding Tasks)**
- `spec/03-error-manage/01-error-resolution/00-overview.md`
- `spec/03-error-manage/02-error-architecture/00-overview.md`
- `spec/03-error-manage/02-error-architecture/01-error-handling-reference.md`
- *Include most of the files from the error manage directory to ensure robust error handling is implemented per task.*

4. **Boolean Conditions, Wrappers & Samples**
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/00-overview.md`
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/01-naming-prefixes.md`
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/02-guards-and-extraction.md`
- `spec/02-coding-guidelines/01-cross-language/02-boolean-principles/04-quick-reference.md`
- `spec/02-coding-guidelines/01-cross-language/12-no-negatives.md`
- `spec/02-coding-guidelines/01-cross-language/24-boolean-flag-methods.md`

5. **Code Style & File Size Limits (80-100 lines max)**
- `spec/02-coding-guidelines/01-cross-language/04-code-style/04-function-and-type-size.md`
- `spec/02-coding-guidelines/01-cross-language/04-code-style/01-braces-and-nesting.md`
- `spec/02-coding-guidelines/01-cross-language/04-code-style/00-overview.md`
- `spec/02-coding-guidelines/01-cross-language/20-nesting-resolution-patterns.md`
- `spec/02-coding-guidelines/01-cross-language/06-cyclomatic-complexity.md`

6. **Variable Naming & Definitions**
- `spec/02-coding-guidelines/01-cross-language/22-variable-naming-conventions.md`
- `spec/02-coding-guidelines/01-cross-language/11-key-naming-pascalcase.md`
- `spec/02-coding-guidelines/01-cross-language/10-function-naming.md`
- `spec/02-coding-guidelines/01-cross-language/18-code-mutation-avoidance.md`

## 5. End-of-Loop Commit Fix (Non-Negotiable)

Each step that completes MUST immediately commit and fix the Git. Follow these exact rules from the commit-fix prompt:
- Group all completed work for the subtask into a single logical commit.
- RED FLAG: Verify absolutely NO test results, artifacts, or compiled binaries are staged before making the commit.
- Ensure .gitignore explicitly excludes them.
- If issues arise during the commit process, fix those git issues and try again.
- You MUST push the commit to the repository immediately. Pushing after commits is non-negotiable.

## Action Items — Must Follow (Non-Negotiable)

- [ ] Read the user-provided "N" variable.
- [ ] Do not execute anything; write the detailed spec and pending tasks first.
- [ ] Save all provided images to `assets/`, rename them contextually, and link them in the markdown.
- [ ] Write tasks using your high-powered brain, detailing explicitly where the code is, what the issue is, and how to change it.
- [ ] Self-loop `N` times to write detailed specs and task files.
- [ ] Ensure subtask files are named exactly XX-<subslug>.md where XX is the sequence.
- [ ] Check if the dynamic reading files exist. If so, enforce them in the task checklist.
- [ ] Ensure the end-of-loop commit fix is properly executed for each completed step.
- [ ] Update `.lovable/plans/index.md` and populate `.lovable/plans/pending/`.

## Actionable Items & Checklist

- [ ] Read and /learn the overarching main task plan.
- [ ] Read `.lovable/memory/index.md` and `.lovable/plans/index.md` before planning.
- [ ] Ensure the git repository starts completely clean.
- [ ] Complete all work on the current branch only.
- [ ] Ensure `.gitignore` explicitly excludes test reports, artifacts, and compiled binaries.
- [ ] Group all completed work into a single logical commit.
- [ ] Push the commit to the remote repository.

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.

---

## Metadata

- slug: plan-spec-steps
- status: active
