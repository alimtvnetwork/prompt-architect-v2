# Instruction (must follow): Fix CI CD and Run Scripts All

Trigger Keywords & Aliases: `fix with RCA`, `FRCA : Fix with RCA`, `fix`, `fix, fix`, `CI/CD fix`, `fix run scripts`

/goal Perform a Root Cause Analysis (RCA) on all failing run scripts and CI/CD workflows, persist the RCA into `.lovable/cicd-issues/` and `.lovable/strictly-avoid.md`, implement universal query wrappers with explicit success/failure boolean results and automated error logging, verify clean builds, commit logically, and push to git.

/learn Ingest recent Root Cause Analysis (RCA) records from `.lovable/cicd-issues/`, `.lovable/issues/`, and `spec/03-error-manage/` so previous mistakes and anti-patterns are never repeated.

Fix CI CD and run scripts all

Find the root cause analysis write the root cause of it in the avoid part in the .lovable memeory

Please have a look into all the code base, try to make the Git commits properly, try to check the CI/CD, and also try to run the tests, build the code, see if there is any issue, try to fix that. And also, I've given you the screenshot. So when you are making a query in PHP/Python/TS and other places, you should have a wrapper that actually gives you this logging behavior. You don't log it everywhere else, but when you make the query, if it fails, it would log it automatically, it would reduce the code. That is the idea. That needs to be figured out how many places you have messed this up. And also, the result should have its own, like, is success, is failure. So you should have a wrapper type of code that actually yells that. You should update the memory regarding this inside the .lovable folder, the memory aspect so that Next.ai does not make the mistake. So make sure that you do plan this out, whatever you have to make, and you loop it. And also make sure that similar type of code should go all together, not like single commits at a time, with a nice commit message. After you commit the code, finally, before you end your job, you should actually push the code to the repository. Remember this. So if you have any issues, remember to fix those out

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

## Actionable Items & Checklist

- [ ] /learn previous RCAs in `.lovable/cicd-issues/` and `.lovable/strictly-avoid.md`.
- [ ] Read the overarching main task plan.
- [ ] Ensure the git repository starts completely clean.
- [ ] Complete all work on the current branch only.
- [ ] Ensure `.gitignore` explicitly excludes test reports, artifacts, and compiled binaries.
- [ ] Group all completed work into a single logical commit.
- [ ] Push the commit to the remote repository.



## Core Rules & Non-Negotiable Checklist for AI (Must Verify Before Completing Task)

Before finalizing any code modification, you MUST manually verify the following:
- [ ] **Function Signatures (R4, R5, R9):** If a function has `> 3 parameters` or the signature is `> 100 chars`, you MUST split it so there is exactly **one parameter per line**.
- [ ] **Error Handling (R7):** No silent failures or swallowed errors. Use explicit boolean states (e.g., `isFail`). Never invert success booleans (e.g., avoid `!isSuccess`).
- [ ] **Magic Strings/Numbers (R8):** Extract all magic strings/numbers into named constants.
- [ ] **Enums:** TypeScript string unions are banned. All Enums must end with the `Type` suffix.
- [ ] **Naming & Casing (R1, R2):** PascalCase everywhere. Acronyms (Id, Json, Url) are Pascal case, never all-caps (e.g., `UserId`, not `UserID`).
- [ ] **Blank Lines (R13-R20):** One blank line before every `return`/`throw`. One blank line after closing `}`. Never two blank lines in a row.

## End of Tunnel Release & Version Bump (Mandatory)

When EVERYTHING is completely finished and fixed (at the very end of the tunnel), you MUST trigger a release.
- You must bump the MINOR version.
- You must focus on the `version.json` file as the source of truth for the release.
- If you do not know how to cut a release for this specific repository, or if `version.json` is missing/unclear, you must either search the repository for release instructions or explicitly ask the user for help. Do not guess.
- You MUST strictly exclude all test files (e.g., `*test*`, `*.spec.*`) from version scanning and modification, as they contain mock data.
- You must create and maintain `.lovable/memory/release-architecture-map.md` documenting exactly how releases work in the repository. Ensure it is enqueued in `what-to-read.md` and linked in the root `readme.md`.

