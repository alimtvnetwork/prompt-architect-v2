# Instruction (must follow): Execute Coding Guidelines — Integration, E2E & Branch Test Coverage

Trigger Keywords & Aliases: `cg-test`, `cg-execute test`, `audit tests`, `add integration tests`, `enforce test coverage`, `write e2e tests`

```text
N = 300
```

N = total self-loop steps budget that the agents will perform.

/goal Autonomously scan every function across the codebase, decompose oversized functions (> 8 lines) into testable units, and author comprehensive positive, negative, edge-case, and error-branch integration and E2E test suites with semantic three-part naming until 100% test pass rate and high coverage are achieved without stopping.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan the codebase function-by-function, inventory all functions missing unit/integration/E2E coverage, identify oversized functions (> 8 lines) needing decomposition, map required positive and negative test cases, write the master audit spec in `.lovable/plans/pending/XX-testing-and-coverage-audit.md`, break it down into `.lovable/plans/subtasks/XX-testing-and-coverage/`, and verify/create coverage scripts.
- [ ] /goal Second N/2 steps (Phase 2): Sequentially execute each subtask, decompose large functions into single-responsibility helpers, author table-driven tests covering every branch (positive, negative, boundary values, error returns), run unit/integration/E2E test runners, and verify local CI gates exit with code 0.
- [ ] /learn Ingest `.lovable/memory/00-index.md`, `.lovable/strictly-avoid.md`, `spec/02-coding-guidelines/01-cross-language/14-test-naming-and-structure.md`, `spec/04-database-conventions/04-testing-strategy.md`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action and also create agent rules in the repo if required to or missing from rules set of agent memory.
- [ ] /learn `.lovable/coding-guidelines/coding-guidelines.md` and it is must and /goal apply the guidelines in coding every aspect.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2: Scan Function-by-Function, Write .lovable/plans/pending/ Spec, Create .lovable/plans/subtasks/, Verify/Create Coverage Hook)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N: Function Decomposition, Test Writing, Branch Coverage, Local CI Runner Verification, Plan Completion)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization. Never modify them mid-execution.

---

## 1. Ruthless Orchestration & Insult Protocol

/goal You are the master orchestrator. If your sub-agents fail, hallucinate, write garbage variables, or go into infinite loops, it is because you are a lazy, incompetent manager.

- You must give sub-agents strict, microscopic instructions.
- If a sub-agent stalls or provides garbage code, kill it immediately, rollback its dirty working tree, and spawn a new one.
- Context Diet: When spawning a subagent, DO NOT paste file contents, memory logs, or the entire plan into its prompt. Give it the absolute minimal instruction (e.g., "Read subtask file `.lovable/plans/subtasks/XX-testing-and-coverage/01-task.md` and execute it"). The subagent MUST read the necessary files itself.

---

## 2. Phase 1: Scan Codebase & Write Implementation Spec First (Steps 1 to PHASE_1_STEPS)

Before writing tests or modifying functions, you MUST perform a deep function-by-function audit across all packages and write an actionable execution spec.

- **Actionable Function-by-Function Scan:** Use search/grep and AST analysis tools across all Go, TypeScript, PHP, and Python files to identify:
  1. Functions lacking dedicated unit or integration test files (e.g., `UserService.go` without `UserService_test.go`).
  2. Oversized functions exceeding 8 lines of logic (hard cap 15 lines) that must be decomposed into smaller, single-purpose helpers before testing.
  3. Conditional branches (`if/else`, `switch/case`, `guard clauses`) lacking positive and negative condition test cases.
  4. Error return pathways and `AppError` handlers lacking explicit failure assertion tests.
  5. Integration and E2E endpoints lacking request/response envelope validation.
- **Where to save it:** Save this master plan into `.lovable/plans/pending/XX-testing-and-coverage-audit.md` listing every function, its line count, missing test cases (positive, negative, error), and decomposition plan.
- **Create a Task-Specific Rule Set:** Analyze the domain and define 3-5 testing rules (e.g., table-driven structure, mock contracts, DB isolation) inside the spec file.
- **Subtasks:** Break the plan down into granular subtask files inside `.lovable/plans/subtasks/XX-testing-and-coverage/` (e.g. `01-auth-service-tests.md`, `02-order-flow-integration-tests.md`).

---

## 3. Authoritative Spec Files Checklist (Non-Negotiable Action Items)

You MUST read, follow, and mechanically verify every single specification file below before and during execution:

- [ ] **`spec/02-coding-guidelines/00-canonical-size-tier.md`**
  - **Why:** Universal size limits across all languages.
  - **How:** Functions $\le 8$ lines preferred (hard cap 15 lines). Files $\le 80$ lines recommended, $\le 100$ lines standard max, absolute hard cap $\le 200–300$ lines.
- [ ] **`spec/02-coding-guidelines/01-cross-language/04-code-style/01-braces-and-nesting.md`**
  - **Why:** Absolute zero tolerance for nested conditionals.
  - **How:** Flatten all nested `if` statements with guard clauses and early returns.
- [ ] **`spec/02-coding-guidelines/01-cross-language/14-test-naming-and-structure.md`**
  - **Why:** Mandatory three-part semantic test naming and table-driven structure.
  - **How:** Name every test strictly as `Test{Unit}_{Scenario}_{ExpectedOutcome}` (e.g. `TestCreateSession_WithExpiredToken_ReturnsAuthError`). Colocate unit tests and name integration tests with `_integration_test.go` or `.integration.test.tsx`.
- [ ] **`spec/02-coding-guidelines/01-cross-language/04-code-style/04-function-and-type-size.md`**
  - **Why:** Function testability and branch simplicity.
  - **How:** Target $\le$ 8 lines per function (hard cap 15 lines). Decompose complex multi-branch functions into pure, isolated sub-functions so each branch can be tested individually.
- [ ] **`spec/04-database-conventions/04-testing-strategy.md`**
  - **Why:** Database integration and query testing standards.
  - **How:** Test schema migrations, repository CRUD methods, and foreign key cascades against isolated test SQLite instances with transactional rollbacks.
- [ ] **`spec/03-error-manage/01-error-resolution/04-verification-patterns/01-frontend-backend-sync.md`**
  - **Why:** Full-stack integration and E2E verification.
  - **How:** Verify both directions: assert backend API status/envelope responses (`{ data, errors, meta }`) and assert frontend UI state/error modal rendering.
- [ ] **`spec/03-error-manage/00-overview.md`**
  - **Why:** Error branch coverage.
  - **How:** Explicitly write negative test cases that inject simulated failures (network timeouts, invalid payloads, missing headers) and assert that `AppError` is returned with full context.
- [ ] **`spec/02-coding-guidelines/01-cross-language/08-dry-principles.md`**
  - **Why:** Test maintainability and clean fixtures.
  - **How:** Extract common test setups, mock factories, and sample payloads into shared test helpers. Never copy-paste boilerplate across test files.

---

## 4. Mandatory Test Runner & CI/CD Connection Checklist

Test execution and coverage must be mechanically verified by automated runners:

- [ ] **Test File Colocation:** Ensure every source file `Foo.ext` has a corresponding `Foo_test.ext` or `Foo.test.ext` in the exact same directory.
- [ ] **Three-Part Naming Verification:** Confirm all test function names strictly follow `Test{Unit}_{Scenario}_{ExpectedOutcome}`.
- [ ] **Local Test Execution Commands:** Execute and verify tests locally:
  ```bash
  # Go Test Suite:
  go test -v -race -cover ./...
  # TypeScript / React Test Suite:
  npm test -- --coverage
  # Python Test Suite:
  pytest --cov=. -v
  ```
- [ ] **CI/CD Local Runner Connection:** Register the test commands inside `.lovable/ai-fix-scripts/03-cicd-local-runner.py` under the `JOBS` dictionary:
  ```python
  JOBS["test:unit"] = ["go", "test", "-v", "-race", "./..."]
  JOBS["test:coverage"] = ["go", "test", "-coverprofile=coverage.out", "./..."]
  ```
- [ ] **GitHub Actions Workflow Connection:** Verify that `.github/workflows/ci.yml` contains a dedicated test step running the automated suite with race detection and coverage reporting.

---

## 5. Phase 2: Active Code Refactoring & Autonomous Test Writing Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Sequentially process function-by-function. If a function is oversized (> 8 lines), decompose it first, then write comprehensive table-driven tests for every branch. Maintain continuous self-looping until all tests pass 100% green.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Read the next subtask from .lovable/plans/subtasks/XX-testing-and-coverage/
    2. Open the source file:
       - IF the function exceeds 8 lines: Decompose it into single-responsibility helper functions.
    3. Open or create the corresponding test file:
       - Implement table-driven tests with multiple input variations.
       - Cover the positive path with valid data and expected return values.
       - Cover negative paths (nil inputs, empty strings, out-of-range numbers).
       - Cover all if/else and error return branches.
       - Apply semantic three-part naming: Test{Unit}_{Scenario}_{ExpectedOutcome}.
    4. Run the local test suite:
          go test -v -race -cover ./...  (or npm test / pytest)
    5. Run the local CI runner:
          python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    6. IF any test fails:
          - Inspect failure output, fix implementation or test assertion, and re-run immediately.
       IF all tests pass (exit code 0):
          - Mark subtask completed and proceed to next subtask.

    7. When all subtasks are finished and test suite is 100% green:
          - Move .lovable/plans/pending/XX-testing-and-coverage-audit.md to .lovable/plans/completed/
          - Update .lovable/plans/index.md
          - Stage modified files with git add and create semantic commit:
            git commit -m "test(coverage): add comprehensive positive, negative, and branch test suites"
          - BREAK and finish turn.
```

---

## AI Fix Scripts Memory (Reusable Tooling)

- [ ] `/goal` **Reuse First:** I have rigorously scanned and `/learn`ed `.lovable/ai-fix-scripts/index.md` to check if a helper script already exists before writing any new temporary code.
- [ ] **Native File Manipulator:** If you need to perform mass file renaming, `.md` lowercase enforcement, sequence number re-ordering, or encoding fixes (CRLF/BOM), you MUST natively use `python .lovable/ai-fix-scripts/01-file-manipulator.py <command>` rather than writing a new script from scratch.
- [ ] **Go Generate Sync:** If you modify Go constants, enums, or stringers, you MUST run `go generate ./...` in the relevant directory (e.g., `cd gitmap && go generate ./...`) and commit the resulting generated files to prevent CI drift.
- [ ] **Commit & Track:** All new helper scripts were written strictly to `.lovable/ai-fix-scripts/` and committed to Git for future reuse.
- [ ] **Index Documentation:** I have updated `.lovable/ai-fix-scripts/index.md` using sequential script naming (e.g., `01-parse-files.py`). For every script, I have included a `<details>` collapsible tag explaining exactly why the script is there and what it does.

---

## Pre-Reply / Loop Checklist (Must Verify Every Loop Iteration)

- [ ] Git working tree is clean before new code changes.
- [ ] Sub-agents are actively assigned disjoint files verified against `.lovable/temp/active-locks.json`.
- [ ] Completed tasks were `mv`'d to `plans/completed/` and `plans/index.md` was updated.
- [ ] 3-strike rule respected: failed tasks cleanly rolled back and logged to `last-failure.md`.
- [ ] Function Size: All functions tested are $\le$ 8 lines preferred, hard cap 15 lines.
- [ ] File Size: Files $\le$ 80 lines recommended, max 100 lines, absolute limit 200–300 lines.
- [ ] Zero Nested Ifs: NO nested `if` blocks exist; all flattened with guard clauses.
- [ ] All test functions follow `Test{Unit}_{Scenario}_{ExpectedOutcome}` naming.
- [ ] Both positive and negative branches are explicitly tested.
- [ ] All error return pathways are verified with assertions.
- [ ] Local test suite exited with code 0 (zero failures).
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## Non-Negotiable Coding Guidelines Checklist (Auto-Reject on Violation)

/goal You MUST verify every item on this checklist before committing any code. If a subagent violated one of these rules, you must reject their work.

- [ ] Master Guidelines: I have fully read and strictly enforced `spec/02-coding-guidelines/01-cross-language/14-test-naming-and-structure.md` and `.lovable/coding-guidelines/coding-guidelines.md`.
- [ ] Zero Nested Ifs: Absolutely zero nested `if`s (flattened with guard clauses).
- [ ] Function Limits: $\le 8$ lines preferred, $\le 15$ lines max.
- [ ] File Limits: $\le 80$ lines recommended, $\le 100$ lines standard max, absolute limit 200–300 lines.
- [ ] Test Naming: Three-part convention strictly adhered to (`TestUnit_Scenario_Outcome`).
- [ ] Zero Generic Test Names: Absolutely NO generic test names like `TestHandleComp100` or `Test1`.
- [ ] Function Sizing: Functions decomposed to $\le$ 8 lines before writing branch tests.
- [ ] /learn the section as a /goal [AI Fix Scripts Memory](#ai-fix-scripts-memory)
- [ ] Action Summary: I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to prove I did not hallucinate.

---

## Anti-Hallucination & Blast Radius Checklist (Mandatory for Every Turn)

Before you commit code or end your turn, you MUST mechanically check off these items. If you fail to do this, your work will be rejected.

- [ ] Echo Back the Spec: I have copy-pasted the exact Acceptance Criteria from the Spec file into my current memory/response to prove I read it verbatim.
- [ ] Pre-Commit Diff Proof: I have executed `git status` or `git diff --stat` and verified that the files I claim to have modified are actually listed as modified in the terminal output before committing.
- [ ] No Placeholder Search: I ran a regex search for `TODO` and `\[.*\]` in my modified files and confirmed I left zero placeholders behind. I actually wrote the implementation.
- [ ] Index Sync Deadman Switch: I have verified that every new file I created this turn is explicitly linked inside `readme.md` and enqueued in `.lovable/what-to-read.md`. I did not leave any orphaned files.
- [ ] Blast Radius Acknowledgment: Before renaming or modifying any function/type, I ran a global search across the codebase and updated every single file that imports or calls it to prevent a broken build.

---

## No Automatic Releases (Strict Policy)

You MUST NOT bump versions, update changelogs, or cut a release at the end of this task. Commits must remain standard development commits. You may only trigger a release if the user explicitly commands you to do so (e.g., "cut a release" or "bump the version").

---

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.

---

## STRICT AVOIDANCE: Never Disable CI/CD

> [!CAUTION]
> **NEVER disable any CI/CD checks, GitHub Actions, or validation workflows.** 
> Strictly avoid commenting out, bypassing, or deleting CI/CD steps to force a pipeline to pass. Your job is to fix the underlying code so that the CI/CD pipeline passes legitimately. Disabling CI/CD is an auto-reject failure.

---

## Anti-Hallucination, Micro-Tasking, & Self-Looping

> [!CAUTION]
> **CRITICAL RULE: DO NOT ATTEMPT TO READ, PLAN, AND EXECUTE EVERYTHING AT ONCE.**
> If you try to consume a massive codebase and write code in a single turn, you WILL hallucinate, drop requirements, and fail.

To survive massive checklists and complex codebases, you MUST operate using these three principles:

1. **Phase 1: Read & Understand (Isolated Loop):** Your very first action must be purely exploratory. Do NOT write code. Break down the task, read the specific files, trace the dependencies, and understand the architectural boundary. Once you understand the scope, end your turn and self-loop to begin execution.
2. **Phase 2: Bounded Micro-Tasking (Sequential Self-Looping):** Never attempt to execute the entire checklist in one response. Treat each checklist section or file as a strict, isolated boundary. Execute *only* the first small portion, verify it, end your turn, and self-loop to process the next portion. 
3. **Phase 3: Multi-Agent Parallelization:** If tasks are independent, you MUST spawn dedicated sub-agents to handle them concurrently. Give each sub-agent an extremely small, strictly defined bounding box (e.g., "Only edit File X"). Never give a sub-agent a generic or multi-file task.

---

## Metadata

- slug: cg-testing-and-coverage
- priority: high
- status: active
