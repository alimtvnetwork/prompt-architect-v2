# Commit Fix

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
Look into the entire codebase and follow the code review guidelines from the aspect folder properly. All caught errors must be explicitly logged following the guidelines in the error manage folder. Create a wrapper for queries in PHP/Python/TS that automatically logs failures to reduce scattered logging code. 
- Do not introduce any magic strings or magic numbers anywhere unless it is explicitly for the logger, and mention that in the typing.
- In TypeScript, rather than using strings as sub-items or comparing string union types (pipes) like "pass" | "fail" | "fallback", you must use Enums. Enums are the best.
- Every single Enum must end with the suffix "Type".
- Enum values must use PascalCase (e.g., `ActiveState`, not `_activeState` or `activeState`) in most languages including TypeScript, GoLang, and C#, unless you are writing in a language like Rust where another casing is the standard convention.
- Always use explicit boolean state checks like response.isFail or explicit checks rather than inverting success booleans like !response.isSuccess.

**6. Main Agent Delivery (Commit & Push)**
Once ALL sub-agents and subtasks have successfully completed and written to the file system:
- YOU (the main agent) must group everything together into a logical commit. 
- **RED FLAG:** NEVER upload or commit test reports, test data, artifacts, or compiled binaries to Git. If necessary, check and update the `.gitignore` file to ensure they are explicitly excluded.
- If there are issues during the commit process, you must fix those git issues and try again. 
- You MUST push the commit to the repository immediately. Pushing after commits is non-negotiable. 

**7. Verification & Finishing**
- ONLY AFTER the push is complete, check the build, CI/CD, and run the tests.
- If any builds or tests fail, figure out the root cause, fix them, commit the fix, and push again.
- Finally, finish your job only when everything is green and fully pushed.

Update the memory so this mistake is not repeated.

## Actionable Items & Checklist and non-negotiable must follow

### 1. Pre-flight & Planning

- [ ] Ensure the git repository starts completely clean. If dirty, commit, stash, or fix git issues before writing any new code.

- [ ] Read the overarching main task plan from `.lovable/plans/pending/XX-<slug>.md` to understand what needs to be executed.

- [ ] Ensure the plan is highly extensive, explicitly detailing *where* and *how* to make changes so sub-agents can easily execute tasks (Non-negotiable).

- [ ] Write the tasks as a spec file in `.lovable/spec/tasks/XX-<slug>.md` and update plans in `.lovable/plans/pending/XX-<slug>.md`. Do not write randomly into `.lovable`.

- [ ] Read the memory files and the spec folder coding guidelines + error manage guidelines before touching code.

### 2. Ruthless Management & Subtask Looping

- [ ] Map out the subtasks from the big plan and spawn sub-agents for all independent tasks simultaneously to run them in parallel (MAXIMUM 2 sub-agents concurrently to avoid RAM and caching issues).

- [ ] Enforce a strict timeout on sub-agents. If they stall, enter an infinite loop, or do not respond, kill the process immediately and restart it.

- [ ] Verify the work of every sub-agent. Never accept partial delivery or hallucinated garbage.

### 3. File System Writes & Main Agent Commit

- [ ] Allow sub-agents to write to the file system, but do NOT let them commit. 

- [ ] Wait until all sub-agents have completely finished their tasks.

- [ ] Ensure `.gitignore` explicitly excludes test reports, test data, artifacts, and compiled binaries (Non-negotiable).

- [ ] **RED FLAG:** Verify absolutely NO test results or binaries are included before making the commit.

- [ ] As the main orchestrator, group all completed work into a commit.

- [ ] If issues arise during the commit, fix them immediately and retry.

- [ ] Push the commit to the remote repository. Pushing is non-negotiable.

### 4. Root cause

- [ ] Find the root cause of the problem first, before applying any fix.

- [ ] Record the root cause strictly into the `.lovable` memory structure per the write protocols.

### 5. Code standards (non-negotiable)

- [ ] Follow the code review guidelines from the aspect folder.

- [ ] Ensure every try-catch block explicitly logs the error according to the error manage folder.

- [ ] Create a query wrapper for PHP/Python/TS that handles automatic failure logging, so logging is not scattered.

- [ ] Use explicit `isFail` properties; NEVER use inverted success checks (use `response.isFail`, not `!response.isSuccess`).

- [ ] Remove all magic strings and magic numbers unless used directly for logging — and state that logger exception in the typing.

- [ ] Replace TypeScript string union types (e.g. `"pass" | "fail" | "fallback"`) with Enums.

- [ ] Ensure every Enum name ends with the `Type` suffix (e.g. `StatusType`, never `Status` or `Status7`).

- [ ] Ensure all Enum values are written in PascalCase (e.g., `enum StatusType { ActiveState = "ACTIVE" }`), avoiding `_camelCase` or `camelCase`, unless the specific language (like Rust) conventionally dictates otherwise.

- [ ] Reuse constants — never duplicate them. Code must always be DRY; never repeat code. This is high priority.

### 6. Verification Flow

- [ ] AFTER the push is complete, check the build, CI/CD, and run the tests.

- [ ] Fix every failing build or failing unit test. If fixes are made, commit and push them again.

- [ ] Finish the job only when everything is green and fully pushed.
