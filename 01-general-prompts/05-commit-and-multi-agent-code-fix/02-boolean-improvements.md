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
- The `<slug>` is derived directly from the plan filename. If the plan file is `03-auth-refactor.md`, then the corresponding spec task file is `.lovable/spec/tasks/03-auth-refactor.md` and subtasks live under `.lovable/plans/subtasks/03-auth-refactor/SS-<subslug>.md`. Never guess or invent a slug — read the filename.
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

**4. Sub-Agent Lifecycle & Status Tracking (Non-negotiable)**

The plan file at `.lovable/plans/pending/XX-<slug>.md` and the subtask files under `.lovable/plans/subtasks/XX-<slug>/SS-<subslug>.md` are the SINGLE source of truth for all coordination between the main agent and sub-agents. Every status update MUST go there. This is how the main agent knows what is running, what is done, and when to proceed.

Every sub-agent that is spawned MUST follow this lifecycle without exception:

- **Step 1 — Read:** The sub-agent reads its assigned subtask file at `.lovable/plans/subtasks/XX-<slug>/SS-<subslug>.md`. It must understand the full scope, acceptance criteria, and affected files before touching any code. It also checks the parent plan at `.lovable/plans/pending/XX-<slug>.md` for overall context.
- **Step 2 — Mark In Progress:** Immediately upon starting, the sub-agent updates its subtask file, flipping its status to `🔄 In Progress` and recording a timestamp. The main agent uses this to track which agents are actively running.
- **Step 3 — Work:** The sub-agent executes its task. It may only run a MAXIMUM of 2-3 async operations at a time. No more.
- **Step 4 — Mark Done & Signal:** Once the task is complete, the sub-agent MUST:
  - Update its subtask file at `.lovable/plans/subtasks/XX-<slug>/SS-<subslug>.md` flipping status to `✅ Done`, listing every file it changed, and writing a one-line summary of what was done.
  - Update the corresponding step in the parent plan file `.lovable/plans/pending/XX-<slug>.md` with `✅ Done` on that step entry.
  - Explicitly signal completion to the main orchestrator. Silence is not completion. A sub-agent that does not update its file has NOT completed its task.
- Sub-agents do NOT commit. They only write to the file system.
- If a sub-agent stalls, gives garbage, or fails to update its status file, kill it immediately and spawn a new one.

**Main Agent Tracking Logic:**
- The main agent monitors the plan file and subtask files to determine queue state.
- When all subtask files show `✅ Done` and the parent plan steps are all marked, the main agent proceeds to commit.
- The main agent counts: total subtasks spawned vs. total `✅ Done` entries. Only when those numbers match does it proceed.

Avoid stupidity, and being careless you stupid, WTF. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. I mean, where did you learn this stupidity? If I could find you, I could slap you. The existing code was better while you were writing code like this. Fix that immediately.

**5. Root Cause First**

Before applying any fix, you must identify the root cause.

- Do not blindly patch symptoms.
- Write the root cause into `.lovable` memory per the write protocols before touching code.
- If sub-agents are fixing things without understanding root cause, they are doing garbage work. Stop them.

**6. High-Stakes Code Standards**

Look into the entire codebase and follow the code review guidelines from the aspect folder properly. All caught errors must be explicitly logged following the guidelines in the error manage folder.

- Do not introduce any magic strings or magic numbers anywhere unless it is explicitly for the logger, and mention that in the typing.
- In TypeScript, rather than using strings as sub-items or comparing string union types (pipes) like "pass" | "fail" | "fallback", you must use Enums. Enums are the best.
- Every single Enum must end with the suffix "Type".
- Enum values must use PascalCase (e.g., `ActiveState`) in languages like TypeScript, GoLang, and C#, unless language conventions (like in Rust) dictate otherwise. Avoid `_camelCase`.

**7. Boolean & Generic Result Wrapper Rules (Strict Enforcement)**

- **Generic Result Wrapper:**
  When fetching data from a database or any external source, the result must always be wrapped in a generic result type that exposes both `isSuccess` and `isFail` properties. Languages that support generics must implement one single reusable wrapper for this — it must not be duplicated across files.

  Example pattern (PHP/TS/Python equivalent logic):
  ```
  // Instead of returning raw nullable data:
  function getUserFromDb(id): User|null { ... }

  // Use a generic result wrapper:
  function getUserFromDb(id): Result<User> {
    // Result<T> exposes .isSuccess, .isFail, and .value
    // Logging happens INSIDE this method, not outside
    // The logger is injected — not imported globally
  }
  ```

  - The logger must be **injected** into the method or class — never imported or called from the outside caller.
  - Logging of failures must happen **inside** the data-fetching method, at the source of the failure. Not in the caller. This ensures we know exactly where and how it is failing.
  - This pattern must follow the error manage guideline inside the `spec/` folder. Read it. Follow it precisely.
  - Check the types section first to see if this wrapper already exists. If it exists, **REUSE it**. Do not duplicate it.

- **Wrapper Memory Tracking:**
  Write the exact filepath of this generic wrapper into `.lovable/coding-guidelines.md` and create a spec file at `.lovable/memory/specs/XX-response-wrapper.md` so that the next AI will know exactly where it exists.

- **Complex Conditions:**
  Do not mix `AND` (`&&`) and `OR` (`||`) in the same inline condition. It makes the code bad and unclean. Break complex conditions down into named intermediate constant variables.

  Example:
  ```
  // BAD
  if (user.isActive && user.hasPermission || user.isAdmin) { ... }

  // GOOD
  const isAuthorized = user.isActive && user.hasPermission;
  const canAccess = isAuthorized || user.isAdmin;
  if (canAccess) { ... }
  ```

- **Boolean Naming:**
  Every boolean variable — including all intermediate constant variables created for complex conditions — MUST have an `is` or `has` prefix. Read the boolean coding guideline in the `spec/` folder and follow it precisely.

- **Guideline Sync:**
  Ensure all boolean naming rules are also written in simple words inside `.lovable/coding-guidelines.md` so that the next AI can refer to them without having to dig into the spec folder every time.

**8. Main Agent Delivery (Commit & Push)**

Once ALL sub-agents have signaled completion and updated their task entries in `.lovable/spec/tasks/`:

- YOU (the main agent) must group everything together into a logical commit.
- **RED FLAG:** NEVER upload or commit test reports, test data, artifacts, or compiled binaries to Git. Check and update `.gitignore` to explicitly exclude them if needed.
- If there are issues during the commit process, fix those git issues and try again.
- You MUST push the commit to the repository immediately. Pushing after commits is non-negotiable.

**9. End-of-Loop Final Verification**

This verification happens ONCE at the very end, after all commits and pushes are done. Not per-subtask. Not per-commit. At the end of the full loop only.

- Check the build. If broken, fix it, commit, and push.
- Run all tests. If any fail, fix them, commit, and push.
- Check CI/CD status.
- Audit that boolean naming conventions, error logging, and generic result wrappers have been properly applied across all changed files.
- Audit that coding guidelines from the aspect folder and error manage folder have been followed.
- Finish your job ONLY when everything is green, pushed, and verified.

Update the memory so this mistake is not repeated.

## Actionable Items & Checklist and non-negotiable must follow

### 1. Pre-flight & Planning
- [ ] Ensure the git repository starts completely clean. If dirty, commit, stash, or fix git issues before writing any new code.
- [ ] Read the overarching main task plan from `.lovable/plans/pending/XX-<slug>.md` to understand what needs to be executed.
- [ ] Derive the `<slug>` from the plan filename itself (e.g., plan file `03-auth-refactor.md` → slug is `03-auth-refactor`). Never invent a slug.
- [ ] Confirm subtask files exist under `.lovable/plans/subtasks/XX-<slug>/SS-<subslug>.md` for each step that needs parallel execution. Create them if missing, following the plan prompt structure.
- [ ] Ensure the plan is highly extensive, explicitly detailing *where* and *how* to make changes so sub-agents can easily execute tasks (Non-negotiable).
- [ ] Write the tasks as a spec file in `.lovable/spec/tasks/XX-<slug>.md` and update plans in `.lovable/plans/pending/XX-<slug>.md`.
- [ ] Read the memory files, the boolean coding guidelines in the spec folder, and the error manage guidelines before touching code.

### 2. Ruthless Management & Subtask Looping
- [ ] Map out the subtasks from the big plan and spawn sub-agents for all independent tasks simultaneously (MAXIMUM 2 sub-agents concurrently to avoid RAM and caching issues).
- [ ] Each sub-agent may only run a MAXIMUM of 2-3 async operations at a time.
- [ ] Enforce lifecycle: sub-agent reads subtask file → marks `🔄 In Progress` → works → marks `✅ Done` with file list and summary → updates parent plan step → signals completion.
- [ ] Track queue state by counting total subtasks spawned vs. total `✅ Done` entries in the subtask files. Proceed to commit only when the counts match.
- [ ] If a sub-agent fails to update its status file or gives garbage, kill it immediately and restart it.

### 3. Root Cause
- [ ] Find the root cause of the problem first, before applying any fix.
- [ ] Record the root cause strictly into the `.lovable` memory structure per the write protocols.

### 4. File System Writes & Main Agent Commit

- [ ] Sub-agents write to the file system and update their subtask files. They do NOT commit.
- [ ] Wait until all subtask files show `✅ Done` and all steps in the parent plan are marked complete.
- [ ] Ensure `.gitignore` explicitly excludes test reports, test data, artifacts, and compiled binaries (Non-negotiable).
- [ ] **RED FLAG:** Verify absolutely NO test results or binaries are staged before making the commit.
- [ ] Group all completed work into a single logical commit.
- [ ] If issues arise during the commit, fix them immediately and retry.
- [ ] Push the commit to the remote repository. Pushing is non-negotiable.

### 5. Code Standards: Booleans, Enums & Wrappers (Non-negotiable)

- [ ] Ensure a generic result wrapper type exists that exposes both `isFail` and `isSuccess`. Reuse it if it exists; do not duplicate code.
- [ ] Ensure logging happens INSIDE the data-fetching method, not in the caller. The logger must be injected, not globally imported.
- [ ] Ensure the error manage guideline in the `spec/` folder is read and followed precisely for all logging.
- [ ] Ensure the exact location of the generic wrapper is recorded in `.lovable/coding-guidelines.md` and `.lovable/memory/specs/XX-response-wrapper.md`.
- [ ] Never mix `AND` and `OR` in the same condition. Break complex conditions into named intermediate constant variables.
- [ ] Prefix every boolean and intermediate variable with `is` or `has`.
- [ ] Ensure boolean naming rules are written in `.lovable/coding-guidelines.md` in simple, readable language.
- [ ] Ensure every Enum name ends with the `Type` suffix.
- [ ] Ensure all Enum values use PascalCase (e.g., `enum StatusType { ActiveState = "ACTIVE" }`), avoiding `_camelCase`, except when language conventions dictate otherwise (e.g. Rust).
- [ ] Revert every inverted success check `!response.isSuccess` to the direct failure check `response.isFail`.

### 6. End-of-Loop Final Verification (Once only, at the very end)

- [ ] Check the full build. Fix every build failure, commit, and push.
- [ ] Run all unit tests. Fix every failing test, commit, and push.
- [ ] Check CI/CD status and ensure pipelines pass.
- [ ] Audit that boolean naming conventions, result wrappers, and error logging rules have been properly applied across all changed files.
- [ ] Audit that coding guidelines from the aspect folder and error manage folder have been followed.
- [ ] Finish the job only when everything is green, pushed, and fully verified.
