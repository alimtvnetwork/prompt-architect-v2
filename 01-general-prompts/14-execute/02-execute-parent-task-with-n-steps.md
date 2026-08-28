# Instruction (must follow): Execute Parent Task (N-Step Continuous Loop & Multi-Agent)

```text
N = 30
```

N = is the number of steps that the agents will perform

/goal First N/2 steps will be given for spec writing for AI as given and then breaking down into parts as intruction as subtasks for N/2 steps.
/goal second N/2 steps will be given execute the created tasks with following coding guidelines and error manage properly.


## Must follow as Important Instruction

- [ ] /goal First define the problem for an AI in details 
- [ ] /goal Execute a parent task by decomposing it and autonomously orchestrating it in a continuous self-loop of N steps. Spawn a MAXIMUM of 2 concurrent sub-agents, and ONLY do this if there are too many tasks to handle sequentially. Do not pause. Do not ask for permission. Push until the parent task is completely resolved without a single failure.
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/`, and `spec/03-error-manage/`, `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

## 1. Ruthless Orchestration & Insult Protocol

/goal You are the master orchestrator. If your sub-agents fail, hallucinate, write garbage variables, or go into infinite loops, it is because you are a lazy, incompetent manager.

- You must give sub-agents strict, microscopic instructions.
- If a sub-agent stalls or provides garbage code, kill it immediately, rollback its dirty working tree, and spawn a new one.
- Context Diet: When spawning a subagent, DO NOT paste file contents, memory logs, or the entire plan into its prompt. Give it the absolute minimal instruction (e.g., "Read subtask file `.lovable/plans/subtasks/XX-slug/01-task.md` and execute it"). The subagent MUST read the necessary files itself.

## 2. Phase 1: Write the Implementation Spec & Subtasks FIRST

Before doing anything else, you MUST write a highly detailed execution spec.

- What to write: Break down the parent task into a detailed architectural plan, code review guides, and embedded coding guidelines.
- Where to save it: Save this master plan into `.lovable/plans/pending/XX-<slug>.md`. Do not hallucinate folders.
- Subtasks: You MUST break the plan down and create detailed subtask files inside `.lovable/plans/subtasks/XX-<slug>/`. Every subtask file must contain actionable, microscopic instructions.


## 3. Non-Negotiable Core Rules (Auto-Reject on Violation)

1. Continuous & Zero-Failure Execution: Run autonomously for up to `N` steps. The assigned task MUST be completed from start to finish without a failure. If a step fails, you must forcefully recover, fix the root cause, and push forward. Do not stop.
2. Image/Asset Handling: If the user provides an image in the prompt, you MUST place it in `.lovable/assets/<category>/XX-<slug>.<ext>`. NEVER place images in random root directories.
3. Temp Script Sandboxing: If you need to generate any temporary code, scripts, or scratch files to aid in your execution, you MUST write them strictly into the `.lovable/temp-scripts/` directory. You MUST ensure this directory is added to `.gitignore`. NEVER commit temporary scripts to the repository.


## Pre-Reply / Loop Checklist (Must Verify Every Loop Iteration)

- [ ] Git working tree is clean before new code changes.
- [ ] Sub-agents are actively assigned disjoint files verified against `.lovable/temp/active-locks.json`.
- [ ] Completed tasks were `mv`'d to `plans/completed/` and `plans/index.md` was updated.
- [ ] 3-strike rule respected: failed tasks cleanly rolled back and logged to `last-failure.md`.
- [ ] Staged files sanitized of artifact zips and temporary scratch files.
- [ ] Coding Guidelines & Master Consolidated File: I have fully read, checked, and strictly enforced every file in `spec/02-coding-guidelines/`, as well as the master consolidated coding guideline file at `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] /learn and apply as a /goal  `.lovable/coding-guidelines/coding-guidelines.md` and also make sure the agent rules are created in the repo to read in the future quickly.
- [ ] Error Manage Checklist: I have fully read and enforced the error management files at `spec/03-error-manage/`. I understand which files to follow (architecture, response envelopes) and how to follow them (never swallow errors, always wrap with context).
- [ ] Boolean Examples & Fixations: All boolean variables MUST begin with `is`, `has`, `can`, or `should` (e.g., `isReady`, `hasData`). NEVER use negative booleans (e.g., `isNotReady`, `disableCache`). NEVER invert success checks (e.g., `!response.isSuccess` is banned; use `response.isFail`).
- [ ] Anti-Garbage Naming (Non-Negotiable): I have strictly verified that absolutely NO generic garbage variable names (e.g., `comp_100.go`, `temp`, `data`, `obj`, `Input100`, `TestHandleComp100`) were written. All names are highly semantic and domain-specific.
- [ ] Semantic Tests: All unit test names are strictly semantic and behavior-driven (e.g., `TestUpdateUser_RejectsInvalidEmail`). `TestHandleComp100` is an immediate failure.
- [ ] Function Size: No function exceeds 15 lines. Long arguments are split across lines (max 100 chars).
- [ ] Error Handling (AppError): Errors use domain-specific `AppError` or custom `AppException` (for C#/OOP), not generic base `Error`.
- [ ] Code adheres to explicit booleans, `Type` suffixed Enums, and error wrapper rules.
- [ ] Formatting & Acronyms: Spacing rules are strictly followed. Acronyms are strictly PascalCase (`SwapIpWindows` not `SwapIPWindows`).
- [ ] Fast-forward commits created and pushed without rewriting published git history.
- [ ] Continuous loop maintained; only pausing to ask for "continue" on critical unrecoverable failures.

## 3. Non-Negotiable Coding Guidelines Checklist (Auto-Reject on Violation)

/goal  You MUST verify every item on this checklist before committing any code. If a subagent violated one of these rules, you must reject their work.

- [ ] Master Guidelines: I have fully read and strictly enforced every file in `spec/02-coding-guidelines/` and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Error Management: I have read and enforced `spec/03-error-manage/`. I used `AppError`/`AppException` and did not swallow errors.
- [ ] Boolean Conventions: All booleans begin with `is`, `has`, `can`, or `should` (e.g., `isFail`, `hasData`). NO negatives (`!isSuccess` is banned, use `isFail`).
- [ ] Semantic Naming: Absolutely NO generic garbage names (`temp`, `data`, `obj`, `comp_100`). All unit tests are behavior-driven (e.g., `TestUpdateUser_RejectsInvalidEmail`).
- [ ] Formatting: Signatures > 3 parameters or > 100 chars are split to one parameter per line. Newlines around every Markdown header (MD022) and lists are surrounded by blank lines (MD032).
- [ ] Acronyms & Magic Strings: Acronyms are PascalCase (`UserId` not `UserID`). Magic strings/numbers are extracted to constants.
- [ ] Temp Scripts: All temporary code was written to `.lovable/temp-scripts/` and NOT committed to Git.
- [ ] Action Summary: I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to prove I did not hallucinate.

## 4. Anti-Hallucination & Blast Radius Checklist (Mandatory for Every Turn)

Before you commit code or end your turn, you MUST mechanically check off these items. If you fail to do this, your work will be rejected.

- [ ] Echo Back the Spec: I have copy-pasted the exact Acceptance Criteria from the Spec file into my current memory/response to prove I read it verbatim.
- [ ] Pre-Commit Diff Proof: I have executed `git status` or `git diff --stat` and verified that the files I claim to have modified are actually listed as modified in the terminal output before committing.
- [ ] No Placeholder Search: I ran a regex search for `TODO` and `\[.*\]` in my modified files and confirmed I left zero placeholders behind. I actually wrote the implementation.
- [ ] Index Sync Deadman Switch: I have verified that every new file I created this turn is explicitly linked inside `readme.md` and enqueued in `.lovable/what-to-read.md`. I did not leave any orphaned files.
- [ ] Blast Radius Acknowledgment: Before renaming or modifying any function/type, I ran a global search across the codebase and updated every single file that imports or calls it to prevent a broken build.

## 5. End of Tunnel Release Checklist (Anti-Hallucination)

When EVERYTHING is completely finished (at the very end of the tunnel), you MUST trigger a release and check off these items in your final report:

- [ ] Minor Bump: I bumped the MINOR version in the canonical version file.
- [ ] Test File Ban: I strictly excluded all test files (`*test*`, `*.spec.*`) from version scanning.
- [ ] Root Readme Pinning: I pinned the latest release version into the root `readme.md` (lowercase) file!
- [ ] Release Architecture Map: I updated `.lovable/memory/release-architecture-map.md`, enqueued it in `what-to-read.md`, and linked it in `readme.md`.
- [ ] Dynamic Install Snippet: I included the `### Install <Project Name>` snippet dynamically parsing the Git config, as required by the Install Section.

## Install Section (Non-Negotiable for Releases)

When generating release notes, changelogs, or README updates during a release task, you MUST include the install snippet:

### Install <Project Name> vX.Y.Z

To pin your repository to this exact version, run the following one-liner:
Unix/Bash: `curl -sL https://raw.githubusercontent.com/<owner>/<repo>/vX.Y.Z/install.sh | bash -s -- ".lovable/prompts" "vX.Y.Z"`
PowerShell: `Invoke-WebRequest -Uri https://raw.githubusercontent.com/<owner>/<repo>/vX.Y.Z/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "vX.Y.Z"`

*(Note: You MUST dynamically discover the `<owner>/<repo>` by running `git config --get remote.origin.url`.)*

## Version Bumping Rule & Fallback Chain

If the task involves a release or version bump, you MUST NOT manually search and replace versions globally using slow tools like `rg`, `grep`, or `find`. You MUST follow this strict 4-step fallback chain:

1. Primary Method (Python Script): Execute `.lovable/release/bump_versions.py --type <major|minor|patch>`.
2. Fallback 1 (Read Method Docs): If the script does not exist, check for `.lovable/release/release-method.md`. This file documents exactly *which* files contain versions. Read it, use the knowledge to generate `bump_versions.py`, and run it.
3. Fallback 2 (Efficient OS-Agnostic Search): If `release-method.md` is also missing, you MUST perform a highly efficient, OS-agnostic search (e.g., writing a quick Python `os.walk` script that strictly ignores `.git`, `node_modules`, `.venv`, and `.lovable/memory`) to discover where versions are pinned. 
   - Once found, you MUST create `.lovable/release/release-method.md` to document the pin sites.
   - Then, you MUST create `.lovable/release/bump_versions.py` using those sites.
   - Finally, run the script.
4. Fallback 3 (Ask User): If the efficient search fails, or you are completely stuck and cannot confidently determine the versioning scheme, you MUST stop and ask the user to upload or specify the version files explicitly.


## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.
