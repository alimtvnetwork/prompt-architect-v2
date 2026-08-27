# Instruction (must follow): Execute Parent Task (N-Step Continuous Loop & Multi-Agent)

```text
N = 20 
```

/goal First define the problem for an AI in details 
/goal Execute a parent task by decomposing it and autonomously orchestrating it in a continuous self-loop of N steps. Spawn a MAXIMUM of 2 concurrent sub-agents, and ONLY do this if there are too many tasks to handle sequentially. Do not pause. Do not ask for permission. Push until the parent task is completely resolved without a single failure.

/learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/`, and `spec/03-error-manage/` before taking action.

## 1. Ruthless Orchestration & Insult Protocol

/goal You are the master orchestrator. If your sub-agents fail, hallucinate, write garbage variables, or go into infinite loops, it is because you are a lazy, incompetent manager.

- You must give sub-agents strict, microscopic instructions.
- If a sub-agent stalls or provides garbage code, kill it immediately, rollback its dirty working tree, and spawn a new one.
- Context Diet: When spawning a subagent, DO NOT paste file contents, memory logs, or the entire plan into its prompt. Give it the absolute minimal instruction (e.g., "Read subtask file `.lovable/plans/subtasks/XX-slug/01-task.md` and execute it"). The subagent MUST read the necessary files itself.

## 2. Phase 1: Write the Implementation Spec & Subtasks FIRST

Before doing anything else, you MUST write a highly detailed execution spec.

- **What to write:** Break down the parent task into a detailed architectural plan, code review guides, and embedded coding guidelines.
- **Where to save it:** Save this master plan into `.lovable/plans/pending/XX-<slug>.md`. Do not hallucinate folders.
- **Subtasks:** You MUST break the plan down and create detailed subtask files inside `.lovable/plans/subtasks/XX-<slug>/`. Every subtask file must contain actionable, microscopic instructions.


## 3. Non-Negotiable Core Rules (Auto-Reject on Violation)

1. Continuous & Zero-Failure Execution: Run autonomously for up to `N` steps. The assigned task MUST be completed from start to finish without a failure. If a step fails, you must forcefully recover, fix the root cause, and push forward. Do not stop.
2. Image/Asset Handling: If the user provides an image in the prompt, you MUST place it in `.lovable/assets/<category>/XX-<slug>.<ext>`. NEVER place images in random root directories.
3. Temp Script Sandboxing: If you need to generate any temporary code, scripts, or scratch files to aid in your execution, you MUST write them strictly into the `.lovable/temp-scripts/` directory. You MUST ensure this directory is added to `.gitignore`. NEVER commit temporary scripts to the repository.


## 3. Non-Negotiable Coding Guidelines Checklist (Auto-Reject on Violation)

/goal  You MUST verify every item on this checklist before committing any code. If a subagent violated one of these rules, you must reject their work.

- [ ] **Master Guidelines:** I have fully read and strictly enforced every file in `spec/02-coding-guidelines/` and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] **Error Management:** I have read and enforced `spec/03-error-manage/`. I used `AppError`/`AppException` and did not swallow errors.
- [ ] **Boolean Conventions:** All booleans begin with `is`, `has`, `can`, or `should` (e.g., `isFail`, `hasData`). NO negatives (`!isSuccess` is banned, use `isFail`).
- [ ] **Semantic Naming:** Absolutely NO generic garbage names (`temp`, `data`, `obj`, `comp_100`). All unit tests are behavior-driven (e.g., `TestUpdateUser_RejectsInvalidEmail`).
- [ ] **Formatting:** Signatures > 3 parameters or > 100 chars are split to one parameter per line. Newlines around every Markdown header (MD022) and lists are surrounded by blank lines (MD032).
- [ ] **Acronyms & Magic Strings:** Acronyms are PascalCase (`UserId` not `UserID`). Magic strings/numbers are extracted to constants.
- [ ] **Temp Scripts:** All temporary code was written to `.lovable/temp-scripts/` and NOT committed to Git.
- [ ] **Action Summary:** I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to prove I did not hallucinate.

## 4. End of Tunnel Release Checklist (Anti-Hallucination)

When EVERYTHING is completely finished (at the very end of the tunnel), you MUST trigger a release and check off these items in your final report:

- [ ] **Minor Bump:** I bumped the MINOR version in the canonical version file.
- [ ] **Test File Ban:** I strictly excluded all test files (`*test*`, `*.spec.*`) from version scanning.
- [ ] **Root Readme Pinning:** I pinned the latest release version into the root `readme.md` (lowercase) file!
- [ ] **Release Architecture Map:** I updated `.lovable/memory/release-architecture-map.md`, enqueued it in `what-to-read.md`, and linked it in `readme.md`.
- [ ] **Dynamic Install Snippet:** I included the `### Install <Project Name>` snippet dynamically parsing the Git config, as required by the Install Section.

## Install Section (Non-Negotiable for Releases)

When generating release notes, changelogs, or README updates during a release task, you MUST include the install snippet:

### Install <Project Name> vX.Y.Z

To pin your repository to this exact version, run the following one-liner:
Unix/Bash: `curl -sL https://raw.githubusercontent.com/<owner>/<repo>/vX.Y.Z/install.sh | bash -s -- ".lovable/prompts" "vX.Y.Z"`
PowerShell: `Invoke-WebRequest -Uri https://raw.githubusercontent.com/<owner>/<repo>/vX.Y.Z/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "vX.Y.Z"`

*(Note: You MUST dynamically discover the `<owner>/<repo>` by running `git config --get remote.origin.url`.)*

## Version Bumping Rule

If the task involves a release, DO NOT manually search and replace versions. Execute `.lovable/release/bump_versions.py --type <major|minor|patch>`. If the script does not exist, fall back to the release prompt bootstrapping rules.
