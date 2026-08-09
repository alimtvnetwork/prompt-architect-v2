# Boolean Improvements

## Prompt

**1. Initial State: Clean the Git Tree First**
Before you do anything else, you must ensure the git repository is in a completely clean state. 
- Run `git status`. 
- If there are uncommitted changes, commit them or stash them. 
- If there are git issues, resolve them immediately. 
- Do not start any task work until the working tree is pristine.

**2. Big Plan & Execution Routing**
Read the overarching big plan of the main task from `.lovable/plans/pending/XX-<slug>.md`. You must follow this plan strictly. 
- Make sure the plan is EXTREMELY extensive, explicitly detailing **where** to make changes and **how** to make changes, so that sub-agents can execute their tasks easily. This is non-negotiable.
- Use the maximum enforcement guidelines to execute this plan. 
- Loop through its defined subtasks and spawn sub-agents to speed up the work. 
- Do not just write randomly to `.lovable`. You must follow the exact plan and write protocols: tasks go into `.lovable/spec/tasks/XX-<slug>.md` and plans go into `.lovable/plans/pending/XX-<slug>.md`.

**3. Ruthless Orchestration**
You are the orchestrator. If your sub-agents fail, hallucinate, or go into infinite loops, it is because you are a lazy, incompetent manager. 
- Give them strict, microscopic instructions based on the big plan.
- Map out the subtasks from the big plan. 
- Spawn a dedicated sub-agent for each independent chunk simultaneously (MAXIMUM 2 concurrently). 
- Do not spawn more than 2 agents at once due to RAM issues and caching behavior.
- Do not wait sequentially like an idiot. 

**4. Sub-Agent Timeouts & File System Writes**
- Set a hard timeout for every sub-agent. 
- If a sub-agent takes too long, stalls, or gives you garbage, kill it immediately and spawn a new one. 
- Sub-agents do NOT commit. They only write to the file system. 
- Verify the work of every sub-agent before proceeding. Never accept partial delivery or hallucinated garbage.

Avoid stupidity, and being careless you stupid, WTF. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. I mean, where did you learn this stupidity? If I could find you, I could slap you. The existing code was better while you were writing code like this. Fix that immediately.

**5. High-Stakes Code Standards**
Look into the entire codebase and follow the code review guidelines from the aspect folder properly. All caught errors must be explicitly logged following the guidelines in the error manage folder. 

- Do not introduce any magic strings or magic numbers anywhere unless it is explicitly for the logger, and mention that in the typing.
- In TypeScript, rather than using strings as sub-items or comparing string union types (pipes) like "pass" | "fail" | "fallback", you must use Enums. Enums are the best.
- Every single Enum must end with the suffix "Type".
- Enum values must use PascalCase (e.g., `ActiveState`) in languages like TypeScript, GoLang, and C#, unless language conventions (like in Rust) dictate otherwise. Avoid `_camelCase`.

**6. Boolean & Wrapper Rules (Strict Enforcement)**
- **Generic Type Wrapper:** Whenever a result comes in, there must be a generic type wrapper that yields both `isFail` and `isSuccess` properties. Languages that support generics must have one reusable wrapper for this. Check the types section to see if we have already built this. If it exists, REUSE it—do not repeat that code!
- **Wrapper Memory Tracking:** Write the exact filepath of this generic wrapper into `.lovable/coding-guidelines.md` and create a spec file in `.lovable/memory/specs/XX-response-wrapper.md` so that the next AI will know exactly where it exists.
- **Complex Conditions:** Do not mix `AND` (`&&`) and `OR` (`||`) in the same inline condition. It makes the code bad and unclean. Break complex conditions down into intermediate constant variables.
- **Boolean Naming:** Every boolean variable (including the intermediate constants for complex conditions) MUST have an `is` or `has` prefix. 
- **Guideline Sync:** Read the boolean coding guideline in the `spec/` folder. Ensure these boolean naming rules are added to the `.lovable/coding-guidelines.md` section in simple words so they can be easily referred to.

Here are the specific code diff mistakes you made that must be corrected across the codebase:
- Inverting a success boolean (`!response.isSuccess`) is bad code quality compared to directly using an explicit `isFail` property (`if (response.isFail)`). Reverse this immediately.
- Naming an enum `Status7` violates naming rules. It must end with the `Type` suffix (e.g., `StatusType`).
- Pointless intermediate negation assignments in PHP (e.g., `$isFailed = !$exists; if ($isFailed)`) add unnecessary overhead. The query wrapper must own the execution state cleanly.

**7. Main Agent Delivery (Commit & Push)**
Once ALL sub-agents and subtasks have successfully completed and written to the file system:
- YOU (the main agent) must group everything together into a logical commit. 
- **RED FLAG:** NEVER upload or commit test reports, test data, artifacts, or compiled binaries to Git. If necessary, check and update the `.gitignore` file to ensure they are explicitly excluded.
- If there are issues during the commit process, you must fix those git issues and try again. 
- You MUST push the commit to the repository immediately. Pushing after commits is non-negotiable. 

**8. Verification & Finishing**
- ONLY AFTER the push is complete, check the build, CI/CD, and run the tests.
- If any builds or tests fail, figure out the root cause, fix them, commit the fix, and push again.
- Finally, finish your job only when everything is green and fully pushed.

Update the memory so this mistake is not repeated.

## Actionable Items & Checklist and non-negotiable must follow

### 1. Pre-flight & Planning

- [ ] Ensure the git repository starts completely clean. If dirty, commit, stash, or fix git issues before writing any new code.
- [ ] Read the overarching main task plan from `.lovable/plans/pending/XX-<slug>.md` to understand what needs to be executed.
- [ ] Ensure the plan is highly extensive, explicitly detailing *where* and *how* to make changes so sub-agents can easily execute tasks (Non-negotiable).
- [ ] Write the tasks as a spec file in `.lovable/spec/tasks/XX-<slug>.md` and update plans in `.lovable/plans/pending/XX-<slug>.md`.
- [ ] Read the memory files, the boolean coding guidelines in the spec folder, and the error manage guidelines before touching code.

### 2. Ruthless Management & Subtask Looping

- [ ] Map out the subtasks from the big plan and spawn sub-agents for all independent tasks simultaneously to run them in parallel (MAXIMUM 2 sub-agents concurrently to avoid RAM and caching issues).
- [ ] Enforce a strict timeout on sub-agents. If they stall, enter an infinite loop, or do not respond, kill the process immediately and restart it.
- [ ] Verify the work of every sub-agent. Never accept partial delivery or hallucinated garbage.

### 3. File System Writes & Main Agent Commit

- [ ] Allow sub-agents to write to the file system, but do NOT let them commit. 
- [ ] Wait until all sub-agents have completely finished their tasks.
- [ ] Ensure `.gitignore` explicitly excludes test reports, test data, artifacts, and compiled binaries (Non-negotiable).
- [ ] **RED FLAG:** Verify absolutely NO test results or binaries are included before making the commit.
- [ ] As the main orchestrator, group all completed work into a single logical commit.
- [ ] If issues arise during the commit, fix them immediately and retry.
- [ ] Push the commit to the remote repository. Pushing is non-negotiable.

### 4. Code Standards: Booleans, Enums & Wrappers (Non-negotiable)

- [ ] Ensure a generic type wrapper exists that yields both `isFail` and `isSuccess`. Reuse it if it exists; do not duplicate code.
- [ ] Ensure the exact location of the generic wrapper is recorded in `.lovable/coding-guidelines.md` and `.lovable/memory/specs/XX-response-wrapper.md`.
- [ ] Never mix `AND` and `OR` in the same condition. Break complex conditions down into intermediate constant variables.
- [ ] Prefix every boolean (including intermediate variables) with `is` or `has`.
- [ ] Add the simple-words boolean naming rule to `.lovable/coding-guidelines.md`.
- [ ] Ensure every Enum name ends with the `Type` suffix.
- [ ] Ensure all Enum values use PascalCase (e.g., `enum StatusType { ActiveState = "ACTIVE" }`), avoiding `_camelCase`, except when standard conventions of the language (like Rust) dictate otherwise.
- [ ] Revert every inverted success check `!response.isSuccess` back to the direct failure check `response.isFail`.
- [ ] Remove pointless intermediate negation assignments in PHP (e.g. `$isFailed = !$exists; if ($isFailed)`).

### 5. Verification Flow

- [ ] AFTER the push is complete, check the build, CI/CD, and run the tests.
- [ ] Fix every failing build or failing unit test. If fixes are made, commit and push them again.
- [ ] Finish the job only when everything is green and fully pushed.
