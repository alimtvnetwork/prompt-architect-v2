# Boolean Improvements

## Prompt

Fix the git status first, then start coding. Make a big plan if required to self-loop, and spawn sub-agents with parallel processing to speed up the work. 

Avoid stupidity, and being careless you stupid, WTF. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. I mean, where did you learn this stupidity? If I could find you, I could slap you. You are completely looking over what you were supposed to do. The existing code was better while you were writing code like this. Fix that immediately.

Look into the entire codebase and follow the code review guidelines from the aspect folder properly. All caught errors must be explicitly logged following the guidelines in the error manage folder. Create a wrapper for queries in PHP/Python/TS that automatically logs failures to reduce scattered logging code. 

Make sure the code quality is strictly maintained. Do not introduce any magic strings or magic numbers anywhere unless it is explicitly for the logger, and mention that in the typing. In TypeScript, rather than using strings as sub-items or comparing string union types (pipes) like "pass" | "fail" | "fallback", you must use Enums. Enums are the best. Furthermore, every single enum must end with the suffix "Type". Enum values must use PascalCase (e.g., `ActiveState`, not `_activeState` or `activeState`) in languages like TypeScript, GoLang, and C#, unless language conventions (like in Rust) dictate otherwise. 

Here are the specific code diff mistakes you made that must be corrected across the codebase:

1. In example you changed `if (response.isFail)` to `if (!response.isSuccess)`. Inverting a success boolean (`!response.isSuccess`) is bad code quality compared to directly using an explicit `isFail` property (`if (response.isFail)`). Reverse this immediately.

2. In example string union `status: "pass" | "fail" | "fallback"` with an Enum called `Status7`. While replacing string unions with enums is required, naming an enum `Status7` violates naming rules. It must end with the `Type` suffix (e.g., `StatusType`).

3. In your PHP reseller query check, replacing `if (!$exists)` with an intermediate assignment `$isFailed = !$exists; if ($isFailed)` is unnecessary overhead when a direct wrapper logic should handle execution state cleaner.

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

### 4. Specific defects to correct across the codebase

- [ ] Revert every inverted success check `!response.isSuccess` back to the direct failure check `response.isFail`.
- [ ] Rename every badly named Enum to end with the `Type` suffix (e.g. `Status7` -> `StatusType`).
- [ ] Eliminate TypeScript string unions such as `"pass" | "fail" | "fallback"` and convert them to properly named Enums.
- [ ] Ensure all Enum values use PascalCase (e.g., `enum StatusType { ActiveState = "ACTIVE" }`), avoiding `_camelCase`, except when standard conventions of the language (like Rust) dictate otherwise.
- [ ] Remove pointless intermediate negation assignments in PHP (e.g. `$isFailed = !$exists; if ($isFailed)`) — the query wrapper must own the execution-state logic cleanly.
- [ ] Audit the entire codebase, count every place this query logic and typing was messed up, and fix all of them.

### 5. Code standards (non-negotiable)

- [ ] Follow the code review guidelines from the aspect folder.
- [ ] Ensure every try-catch block explicitly logs the error according to the error manage folder.
- [ ] Create a query wrapper for PHP/Python/TS that handles automatic failure logging, so logging is not scattered.
- [ ] Remove all magic strings and magic numbers unless used directly for logging — and state that logger exception in the typing.
- [ ] Reuse constants — never duplicate them. Code must always be DRY; never repeat code. This is high priority.

### 6. Memory update

- [ ] Update the `.lovable` folder memory with the wrapper, error management, enum naming and boolean-check rules so the mistake is never repeated.

### 7. Verification

- [ ] Make sure the code runs standalone both locally and in CI/CD.
- [ ] Run the build, run all unit tests, and check CI/CD.
- [ ] Fix every failing build or failing unit test — a green run is required, not optional.

### 8. Delivery

- [ ] Group similar code changes into single commits with nice commit messages; never commit one file at a time.
- [ ] Push every commit to the remote repository without failure — git is the source of truth.
- [ ] Before ending the job, bump the minor release, following this repo's release guidelines — read and understand them properly before releasing.
