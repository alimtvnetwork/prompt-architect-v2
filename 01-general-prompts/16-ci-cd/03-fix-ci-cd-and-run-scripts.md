# Instruction (must follow): Fix CI CD and Run Scripts All

Trigger Keywords & Aliases: `fix with RCA`, `FRCA : Fix with RCA`, `fix`, `fix, fix`, `CI/CD fix`, `fix run scripts`

/goal Perform a Root Cause Analysis (RCA) on all failing run scripts and CI/CD workflows, persist the RCA into `.lovable/cicd-issues/` and `.lovable/strictly-avoid.md`, implement universal query wrappers with explicit success/failure boolean results and automated error logging, verify clean builds, commit logically, and push to git.

/learn Ingest recent Root Cause Analysis (RCA) records from `.lovable/cicd-issues/`, `.lovable/issues/`, and `spec/03-error-manage/` so previous mistakes and anti-patterns are never repeated.

Fix CI CD and run scripts all

Find the root cause analysis write the root cause of it in the avoid part in the .lovable memeory

Please have a look into all the code base, try to make the Git commits properly, try to check the CI/CD, and also try to run the tests, build the code, see if there is any issue, try to fix that. And also, I've given you the screenshot. So when you are making a query in PHP/Python/TS and other places, you should have a wrapper that actually gives you this logging behavior. You don't log it everywhere else, but when you make the query, if it fails, it would log it automatically, it would reduce the code. That is the idea. That needs to be figured out how many places you have messed this up. And also, the result should have its own, like, is success, is failure. So you should have a wrapper type of code that actually yells that. You should update the memory regarding this inside the .lovable folder, the memory aspect so that Next.ai does not make the mistake. So make sure that you do plan this out, whatever you have to make, and you loop it. And also make sure that similar type of code should go all together, not like single commits at a time, with a nice commit message. After you commit the code, finally, before you end your job, you should actually push the code to the repository. Remember this. So if you have any issues, remember to fix those out


## No Automatic Releases (Strict Policy)

You MUST NOT bump versions, update changelogs, or cut a release at the end of this task. Commits must remain standard development commits. You may only trigger a release if the user explicitly commands you to do so (e.g., "cut a release" or "bump the version").

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.

## Action Items — Must Follow (Non-Negotiable)

- [ ] Ingest past RCAs from `.lovable/cicd-issues/` and `.lovable/issues/` before coding.
- [ ] Fix CI/CD and run all scripts.
- [ ] Find the root cause of the issue and write it into the 'avoid' part of the `.lovable` memory (`.lovable/strictly-avoid.md` and `.lovable/cicd-issues/01-<slug>.md`).
- [ ] Make Git commits properly.
- [ ] Check the CI/CD, run the tests, and build the code; fix any issues found.
- [ ] Create a query wrapper for PHP/Python/TS that automatically logs failures to reduce code duplication.
- [ ] Ensure the wrapper explicitly returns success or failure states (e.g., `isSuccess`, `isFail`).
- [ ] Identify everywhere this logging wrapper pattern was missed or messed up and fix those places.
- [ ] Update the memory inside the `.lovable` folder regarding this wrapper pattern so future AI agents do not make the same mistake.
- [ ] Make a plan for the required fixes and self-loop to execute it.
- [ ] Group similar code changes together into single commits (do not commit one file at a time) and include a nice commit message.
- [ ] Push the code to the repository before ending the job.
- [ ] Fix any remaining issues that arise before completion.

## Before Writing Code

Read and follow spec folders `02`, `03` and `04` before writing any code. Error management must be followed. Code must be DRY.


## Anti-Hallucination & Checklist Execution (Strict Sequential Self-Looping)

> [!CAUTION]
> **CRITICAL RULE: DO NOT ATTEMPT TO DO EVERYTHING AT ONCE.**
> You have massive checklists and strict architectural guidelines. If you try to execute all tasks in a single response, you WILL hallucinate, drop requirements, and fail the task. 

To solve this, you MUST operate using these two principles:

1. **Sequential Self-Looping:** Break the instructions down. Treat each checklist section or task as a completely separate execution step. Complete *only* the first section, verify it, end your turn, and self-loop (continue execution) to process the next checklist item one by one.
2. **Multi-Agent Parallelization:** To solve tasks faster, you are highly encouraged to spawn 2 or more sub-agents concurrently to handle independent tasks. If tasks are dependent on one another (e.g., sequential coding guideline audits), you must process them strictly one by one in your self-loop.

## Actionable Items & Checklist (must follow)

- [ ] /learn previous RCAs in `.lovable/cicd-issues/` and `.lovable/strictly-avoid.md`.
- [ ] Read the overarching main task plan.
- [ ] Ensure the git repository starts completely clean.
- [ ] Complete all work on the current branch only.
- [ ] Ensure `.gitignore` explicitly excludes test reports, artifacts, and compiled binaries.
- [ ] Group all completed work into a single logical commit.
- [ ] Push the commit to the remote repository.


## Core Rules & Non-Negotiable Checklist for AI (Must Verify Before Completing Task)

Before finalizing any code modification, you MUST manually verify the following:

- [ ] Coding Guidelines & Master Consolidated File: I have fully read, checked, and strictly enforced every file in `spec/02-coding-guidelines/`, as well as the master consolidated coding guideline file at `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Error Manage Checklist: I have fully read and enforced the error management files at `spec/03-error-manage/`. I understand which files to follow (architecture, response envelopes) and how to follow them (never swallow errors, always wrap with context).
- [ ] Boolean Examples & Fixations: All boolean variables MUST begin with `is`, `has`, `can`, or `should` (e. NEVER use explicit true/false comparisons (e.g., `if isReady == true` is FORBIDDEN, use `if isReady`).g., `isReady`, `hasData`). NEVER use negative booleans (e.g., `isNotReady`, `disableCache`). NEVER invert success checks (e.g., `!response.isSuccess` is banned; use `response.isFail`).
- [ ] Anti-Garbage Naming (Non-Negotiable): I have strictly verified that absolutely NO generic garbage variable names (e.g., `comp_100.go`, `temp`, `data`, `obj`, `Input100`, `TestHandleComp100`) were written. All names are highly semantic and domain-specific.
- [ ] Function Signatures (R4, R5, R9): If a function has `> 3 parameters` or the signature is `> 100 chars`, you MUST split it so there is exactly one parameter per line.
- [ ] Error Handling (R7): No silent failures or swallowed errors. Use explicit boolean states (e.g., `isFail`). Never invert success booleans (e.g., avoid `!isSuccess`).
- [ ] Magic Strings/Numbers (R8): Extract all magic strings/numbers into named constants.
- [ ] Enums: TypeScript string unions are banned. All Enums must end with the `Type` suffix.
- [ ] Naming & Casing (R1, R2): PascalCase everywhere. Acronyms (Id, Json, Url) are Pascal case, never all-caps (e.g., `UserId`, not `UserID`).
- [ ] Blank Lines (R13-R20): One blank line before every `return`/`throw`. One blank line after closing `}`. Never two blank lines in a row.

## Language-Specific Requirements

- [ ] **Go Generate Sync:** If you modify Go constants, enums, or stringers, you MUST run `go generate ./...` in the relevant directory (e.g., `cd gitmap && go generate ./...`) and commit the resulting generated files to prevent CI drift.

## End of Tunnel Release & Version Bump (Mandatory)

When EVERYTHING is completely finished and fixed (at the very end of the tunnel), you MUST trigger a release.

- [ ] **Local CI Pass Required:** You MUST absolutely ensure that `02-cicd-local-runner.py` runs with zero errors locally BEFORE you are permitted to trigger this release.
- [ ] You must bump the MINOR version.
- [ ] You must focus on the `version.json` file as the source of truth for the release.
- [ ] Root README Pinning (FATAL): You MUST pin the latest release version into the root `readme.md` file! Do not skip this! Also, update the changelog according to `version.json` format.
- [ ] If you do not know how to cut a release for this specific repository, or if `version.json` is missing/unclear, you must either search the repository for release instructions or explicitly ask the user for help. Do not guess.
- [ ] You MUST strictly exclude all test files (e.g., `*test*`, `*.spec.*`) from version scanning and modification, as they contain mock data.
- [ ] You must create and maintain `.lovable/memory/release-architecture-map.md` documenting exactly how releases work in the repository. Ensure it is enqueued in `what-to-read.md` and linked in the root `readme.md`.




