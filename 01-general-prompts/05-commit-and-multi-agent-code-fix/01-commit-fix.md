# Commit Fix

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

**4. Sub-Agent Lifecycle (Non-negotiable)**

Every sub-agent that is spawned MUST follow this lifecycle without exception:

- **Step 1 — Read:** The sub-agent reads its assigned task file from `.lovable/spec/tasks/XX-<slug>.md` before doing anything. It must fully understand the scope before touching any code.
- **Step 2 — Work:** The sub-agent executes its task. It may only run a MAXIMUM of 2-3 async operations at a time. No more. This limits resource usage and prevents cascading failures.
- **Step 3 — Update:** Once the sub-agent completes its task, it MUST update the task entry in `.lovable/spec/tasks/XX-<slug>.md`, marking the subtask as done with a `✅ Done` marker and a brief note of what was changed.
- **Step 4 — Signal:** The sub-agent MUST explicitly signal completion to the main orchestrator. It is not done until it has done this. Silence is not completion.
- Sub-agents do NOT commit. They only write to the file system.
- If a sub-agent stalls, gives garbage, or fails to signal completion, kill it immediately and spawn a new one.

Avoid stupidity, and being careless you stupid, WTF. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. I mean, where did you learn this stupidity? If I could find you, I could slap you. The existing code was better while you were writing code like this. Fix that immediately.

**5. Root Cause First**

Before applying any fix, you must identify the root cause.

- Do not blindly patch symptoms.
- Write the root cause into `.lovable` memory per the write protocols before touching code.
- If sub-agents are fixing things without understanding root cause, they are doing garbage work. Stop them.

**6. High-Stakes Code Standards**

Look into the entire codebase and follow the code review guidelines from the aspect folder properly. All caught errors must be explicitly logged following the guidelines in the error manage folder. Create a wrapper for queries in PHP/Python/TS that automatically logs failures to reduce scattered logging code.

- Do not introduce any magic strings or magic numbers anywhere unless it is explicitly for the logger, and mention that in the typing.
- In TypeScript, rather than using strings as sub-items or comparing string union types (pipes) like "pass" | "fail" | "fallback", you must use Enums. Enums are the best.
- Every single Enum must end with the suffix "Type".
- Enum values must use PascalCase (e.g., `ActiveState`, not `_activeState` or `activeState`) in most languages including TypeScript, GoLang, and C#, unless you are writing in a language like Rust where another casing is the standard convention.
- Always use explicit boolean state checks like `response.isFail` rather than inverting success booleans like `!response.isSuccess`.

**7. Main Agent Delivery (Commit & Push)**

Once ALL sub-agents have signaled completion and updated their task entries in `.lovable/spec/tasks/`:

- YOU (the main agent) must group everything together into a logical commit.
- **RED FLAG:** NEVER upload or commit test reports, test data, artifacts, or compiled binaries to Git. Check and update `.gitignore` to explicitly exclude them if needed.
- If there are issues during the commit process, fix those git issues and try again.
- You MUST push the commit to the repository immediately. Pushing after commits is non-negotiable.

**8. End-of-Loop Final Verification**

This verification happens ONCE at the very end, after all commits and pushes are done. Not per-subtask. Not per-commit. At the end of the full loop only.

- Check the build. If broken, fix it, commit, and push.
- Run all tests. If any fail, fix them, commit, and push.
- Check CI/CD status.
- Audit that coding guidelines have been followed (aspect folder, error manage folder).
- Finish your job ONLY when everything is green, pushed, and verified.

Update the memory so this mistake is not repeated.

## Actionable Items & Checklist and non-negotiable must follow

### 1. Pre-flight & Planning

- [ ] Ensure the git repository starts completely clean. If dirty, commit, stash, or fix git issues before writing any new code.

- [ ] Read the overarching main task plan from `.lovable/plans/pending/XX-<slug>.md` to understand what needs to be executed.

- [ ] Ensure the plan is highly extensive, explicitly detailing *where* and *how* to make changes so sub-agents can easily execute tasks (Non-negotiable).

- [ ] Write the tasks as a spec file in `.lovable/spec/tasks/XX-<slug>.md` and update plans in `.lovable/plans/pending/XX-<slug>.md`. Do not write randomly into `.lovable`.

- [ ] Read the memory files and the spec folder coding guidelines + error manage guidelines before touching code.

### 2. Ruthless Management & Subtask Looping

- [ ] Map out the subtasks from the big plan and spawn sub-agents for all independent tasks simultaneously (MAXIMUM 2 sub-agents concurrently to avoid RAM and caching issues).

- [ ] Each sub-agent may only run a MAXIMUM of 2-3 async operations at a time.

- [ ] Enforce lifecycle: sub-agent reads task file → works → updates `.lovable/spec/tasks/` → signals completion.

- [ ] If a sub-agent fails to signal completion or gives garbage, kill it immediately and restart it.

- [ ] Verify every sub-agent explicitly signals "done" before the main agent proceeds to commit.

### 3. Root Cause

- [ ] Find the root cause of the problem first, before applying any fix.

- [ ] Record the root cause strictly into the `.lovable` memory structure per the write protocols.

### 4. File System Writes & Main Agent Commit

- [ ] Sub-agents write to the file system and update their task entries. They do NOT commit.

- [ ] Wait until all sub-agents have signaled completion and updated `.lovable/spec/tasks/`.

- [ ] Ensure `.gitignore` explicitly excludes test reports, test data, artifacts, and compiled binaries (Non-negotiable).

- [ ] **RED FLAG:** Verify absolutely NO test results or binaries are staged before making the commit.

- [ ] Group all completed work into a single logical commit.

- [ ] If issues arise during the commit, fix them immediately and retry.

- [ ] Push the commit to the remote repository. Pushing is non-negotiable.

### 5. Code Standards (non-negotiable)

- [ ] Follow the code review guidelines from the aspect folder.

- [ ] Ensure every try-catch block explicitly logs the error according to the error manage folder.

- [ ] Create a query wrapper for PHP/Python/TS that handles automatic failure logging, so logging is not scattered.

- [ ] Use explicit `isFail` properties; NEVER use inverted success checks (use `response.isFail`, not `!response.isSuccess`).

- [ ] Remove all magic strings and magic numbers unless used directly for logging — and state that logger exception in the typing.

- [ ] Replace TypeScript string union types (e.g. `"pass" | "fail" | "fallback"`) with Enums.

- [ ] Ensure every Enum name ends with the `Type` suffix (e.g. `StatusType`, never `Status` or `Status7`).

- [ ] Ensure all Enum values are written in PascalCase (e.g., `enum StatusType { ActiveState = "ACTIVE" }`), avoiding `_camelCase` or `camelCase`, unless the specific language (like Rust) conventionally dictates otherwise.

- [ ] Reuse constants — never duplicate them. Code must always be DRY; never repeat code. This is high priority.

### 6. End-of-Loop Final Verification (Once only, at the very end)

- [ ] Check the full build. Fix every build failure, commit, and push.

- [ ] Run all unit tests. Fix every failing test, commit, and push.

- [ ] Check CI/CD status and ensure pipelines pass.

- [ ] Audit that coding guidelines from the aspect folder and error manage folder have been followed across all changed files.

- [ ] Finish the job only when everything is green, pushed, and fully verified.
