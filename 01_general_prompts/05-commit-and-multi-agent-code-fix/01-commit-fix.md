# Commit Fix

## Prompt

Fix the git status first, then start coding. Make a big plan if required to self-loop, and spawn sub-agents with parallel processing to speed up the work. 

Avoid stupidity, and being careless you stupid, WTF. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. I mean, where did you learn this stupidity? If I could find you, I could slap you. You are completely looking over what you were supposed to do. The existing code was better while you were writing code like this. Fix that immediately.

Look into the entire codebase and follow the code review guidelines from the aspect folder properly. All caught errors must be explicitly logged following the guidelines in the error manage folder. Create a wrapper for queries in PHP/Python/TS that automatically logs failures to reduce scattered logging code. 

Make sure the code quality is strictly maintained:
1. Do not introduce any magic strings or magic numbers anywhere unless it is explicitly for the logger, and mention that in the typing.
2. In TypeScript, rather than using strings as sub-items or comparing string union types (pipes) like "pass" | "fail" | "fallback", you must use Enums. Enums are the best.
3. Every single Enum must end with the suffix "Type".
4. Always use explicit boolean state checks like response.isFail or explicit checks rather than inverting success booleans like !response.isSuccess.

Figure out how many places you messed this up and fix them all. Update the memory regarding this inside the .lovable folder so Next.ai does not make this mistake again.

Commit the codebase first, make the changes, and commit again. Do not commit single files at a time; similar changes should go together with a nice commit message. Check the CI/CD, run the tests, and build the code to see if there is any issue. If any unit tests or builds are failing, fix them. Finally, before you end your job, push the code to the repository.

## Actionable Items & Checklist and non-negotiable must follow

### 1. Pre-flight (before any code is written)

- [ ] Fix git status before starting any new code — working tree must be clean and committed first.
- [ ] Write the tasks into the `.lovable` folder as a spec/task file and enqueue them properly before starting work.
- [ ] Read the memory files and the spec folder coding guidelines + error manage guidelines before touching code.

### 2. Plan and parallelise

- [ ] Plan the execution up front; make a big plan and self-loop as many iterations as needed.
- [ ] Spawn sub-agents, assign the tasks to multiple agents first, and run them in parallel.
- [ ] Keep looping until every enqueued task is verifiably complete — no partial delivery.

### 3. Root cause

- [ ] Find the root cause of the problem first, before applying any fix.
- [ ] Write the root cause down into memory and into the `.lovable` folder as far memory goes.

### 4. Code standards (non-negotiable)

- [ ] Follow the code review guidelines from the aspect folder.
- [ ] Ensure every try-catch block explicitly logs the error according to the error manage folder.
- [ ] Create a query wrapper for PHP/Python/TS that handles automatic failure logging, so logging is not scattered.
- [ ] Use explicit `isFail` properties; NEVER use inverted success checks (use `response.isFail`, not `!response.isSuccess`).
- [ ] Remove all magic strings and magic numbers unless used directly for logging — and state that logger exception in the typing.
- [ ] Replace TypeScript string union types (e.g. `"pass" | "fail" | "fallback"`) with Enums.
- [ ] Ensure every Enum name ends with the `Type` suffix (e.g. `StatusType`, never `Status` or `Status7`).
- [ ] Reuse constants — never duplicate them. Code must always be DRY; never repeat code. This is high priority.
- [ ] Audit the entire codebase and fix every place where this query logic and typing was messed up — count them and fix all.

### 5. Memory update

- [ ] Update the `.lovable` folder memory with the wrapper, error management, enum naming and boolean-check rules so the mistake is never repeated.

### 6. Verification

- [ ] Make sure the code runs standalone both locally and in CI/CD.
- [ ] Run the build, run all unit tests, and check CI/CD.
- [ ] Fix every failing build or failing unit test — a green run is required, not optional.

### 7. Delivery

- [ ] Group similar code changes into single commits with nice commit messages; never commit one file at a time.
- [ ] Push every commit to the remote repository without failure — git is the source of truth.
- [ ] Before ending the job, bump the minor release, following this repo's release guidelines — read and understand them properly before releasing.
