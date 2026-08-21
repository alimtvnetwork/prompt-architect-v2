# Execute Pending Tasks (Autonomous Execution)

- slug: execute-pending-tasks
- status: active

## Prompt

# Execute Pending Tasks (Autonomous Execution)

## 1. Initial State: Audit, Casing Check & Re-Sequence Pending Tasks

Before starting execution, you must ensure the queue of pending tasks is properly ordered, named, and structured into Execution Waves.

- Verify root readme is strictly lowercase `readme.md`.
- Read the `.lovable/plans/pending/` directory and `.lovable/plans/index.md`.
- Count exactly how many pending tasks exist.
- **Naming Correction**: Check if the pending task files are correctly sequenced with a 2-digit numerical prefix (e.g., `01-<slug>.md`, `02-<slug>.md`).
- If naming is incorrect or missing prefixes, **fix it immediately**. Rename the files to follow sequential `01-`, `02-` format and update `.lovable/plans/index.md` to match in the same operation.
- **Execution Waves**: Group tasks into Execution Waves (Wave 1: Schemas/DB/wrappers; Wave 2: Business services; Wave 3: UI & docs).

## 2. Uninterrupted Autonomous Execution (Self-Looping & Locking Matrix)

You are the sole orchestrator. Your job is to complete ALL pending tasks without stopping.

- **Make a Great Plan**: Analyze all pending tasks and devise a comprehensive execution plan. Tasks exceeding 7 steps must be decomposed into `plans/subtasks/XX-<slug>/`.
- **Do NOT Ask Questions**: Do not stop to ask the user for permission. Do not stop to ask clarifying questions.
- **File Collision Locking Matrix (`active-locks.json`):** Register active target files in `.lovable/temp/active-locks.json` so parallel tasks touch completely disjoint files.
- **Self-Loop**: Self-loop continuously until every single pending task in the queue is verifiably completed.
- **3-Strike Rollback:** If an agent fails unit tests or builds 3 consecutive times, automatically rollback dirty working tree (`git checkout -- <files>`), log failure context to `.lovable/memory/last-failure.md`, and advance to the next disjoint task.

## 3. High-Stakes Code Standards & Root Cause Analysis

While executing the pending tasks, you must adhere strictly to the project's code standards and root cause protocols:

- **Root Cause First**: Find the root cause of every problem before applying any fix. Record the root cause into `.lovable/` memory before touching code.
- **Error Management**: All caught errors must be explicitly logged following guidelines in `spec/03-error-manage/`. Use the established query wrapper that automatically logs failures.
- **No Magic Values**: Do not introduce any magic strings or magic numbers anywhere unless explicitly for the logger.
- **Enums Over Unions**: Replace TypeScript string union types (e.g., `"pass" | "fail"`) with Enums.
- **Enum Naming**: Every Enum name must end with the `Type` suffix (e.g., `StatusType`). Enum values must use `PascalCase` (e.g., `ActiveState`).
- **Boolean State Checks**: Always use explicit boolean state checks like `response.isFail`. NEVER use inverted success booleans like `!response.isSuccess`.
- **DRY Code**: Reuse constants; never duplicate them.

## 4. Sub-Agent Orchestration

To speed up the work, you may spawn sub-agents to handle independent chunks of the pending tasks.

- Spawn a maximum of 2 to 3 sub-agents concurrently to avoid RAM and caching issues.
- Give sub-agents highly specific titles (e.g., `Refactoring Auth Service`, `Fixing DB Connection`).
- Enforce the sub-agent lifecycle: they must read their subtask file, mark it `🔄 In Progress`, do the work, and mark it `✅ Done` with a summary of changed files.
- Sub-agents only write to the file system; they NEVER commit to Git.

## 5. End-of-Loop Final Verification, Artifact Sanitizer & Push

Once ALL pending tasks have been completed and marked `✅ Done`:

- **Final Verification**: Check full build, run all local unit tests, and check CI/CD status. Fix any build failures or failing tests immediately.
- **Artifact Sanitizer & Git History Guard**: Ensure no zip archives, temporary scratch files, test data, or binaries are committed. Never rewrite published Git history (no force push, no rebase, no squash) to protect Lovable editor synchronization.
- **Commit**: Group all completed work into a single logical Git commit with a clear, descriptive message summarizing executed tasks.
- **Push**: Push the commit to the remote GitHub repository. Pushing after the commit is non-negotiable.

---

## Actionable Items & Checklist (All Must Be True)

- [ ] Audited `.lovable/plans/pending/` and re-sequenced task filenames to `01-`, `02-`, etc., if incorrectly named.
- [ ] Grouped tasks into Execution Waves and checked `.lovable/temp/active-locks.json` for file collisions.
- [ ] Executed autonomously via continuous self-looping without stopping to ask user questions.
- [ ] 3-strike rule respected: failed tasks cleanly rolled back with `git checkout` and logged to `last-failure.md`.
- [ ] Followed all high-stakes code standards (Enums with `Type` suffix, `PascalCase` values, explicit `isFail` checks, no magic strings, DRY code).
- [ ] Root causes identified and logged in `.lovable/` before code was patched.
- [ ] Sub-agents followed strict lifecycle with specific titles and never exceeded 3 concurrent instances.
- [ ] End-of-loop verification passed: build is green, unit tests pass.
- [ ] Staged files sanitized of artifact zip bundles, temporary scripts, and test data.
- [ ] Fast-forward commit created and pushed without rewriting Git history.

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.
