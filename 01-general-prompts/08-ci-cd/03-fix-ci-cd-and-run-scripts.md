# Instruction (must follow): Fix CI CD and Run Scripts All

> This instruction provides guidelines and directives for fix ci cd and run scripts all.

Fix CI CD and run scripts all

Find the root cause analysis write the root cause of it in the avoid part in the .lovable memeory

Please have a look into all the code base, try to make the Git commits properly, try to check the CI/CD, and also try to run the tests, build the code, see if there is any issue, try to fix that. And also, I've given you the screenshot. So when you are making a query in PHP/Python/TS and other places, you should have a wrapper that actually gives you this logging behavior. You don't log it everywhere else, but when you make the query, if it fails, it would log it automatically, it would reduce the code. That is the idea. That needs to be figured out how many places you have messed this up. And also, the result should have its own, like, is success, is failure. So you should have a wrapper type of code that actually yells that. You should update the memory regarding this inside the .lovable folder, the memory aspect so that Next.ai does not make the mistake. So make sure that you do plan this out, whatever you have to make, and you loop it. And also make sure that similar type of code should go all together, not like single commits at a time, with a nice commit message. After you commit the code, finally, before you end your job, you should actually push the code to the repository. Remember this. So if you have any issues, remember to fix those out

## Action Items — Must Follow (Non-Negotiable)

- [ ] Fix CI/CD and run all scripts.
- [ ] Find the root cause of the issue and write it into the "avoid" part of the `.lovable` memory.
- [ ] Make Git commits properly.
- [ ] Check the CI/CD, run the tests, and build the code; fix any issues found.
- [ ] Create a query wrapper for PHP/Python/TS that automatically logs failures to reduce code duplication.
- [ ] Ensure the wrapper explicitly returns success or failure states (e.g., `is success`, `is failure`).
- [ ] Identify everywhere this logging wrapper pattern was missed or messed up and fix those places.
- [ ] Update the memory inside the `.lovable` folder regarding this wrapper pattern so future AI agents do not make the same mistake.
- [ ] Make a plan for the required fixes and self-loop to execute it.
- [ ] Group similar code changes together into single commits (do not commit one file at a time) and include a nice commit message.
- [ ] Push the code to the repository before ending the job.
- [ ] Fix any remaining issues that arise before completion.

## Before Writing Code

Read and follow spec folders `02`, `03` and `04` before writing any code. Error management must be followed. Code must be DRY.

## Actionable Items & Checklist

- [ ] Read the overarching main task plan.
- [ ] Ensure the git repository starts completely clean.
- [ ] Complete all work on the current branch only.
- [ ] Ensure `.gitignore` explicitly excludes test reports, artifacts, and compiled binaries.
- [ ] Group all completed work into a single logical commit.
- [ ] Push the commit to the remote repository.
