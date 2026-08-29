---
name: ci-cd-fix
description: >-
  Use this skill to autonomously diagnose, fix, and verify CI/CD pipelines using local runner scripts, 4-part RCA, and self-looping.
---

# Instruction (must follow): Autonomous CI/CD Fix Loop (with Local Runner & RCA)

Trigger Keywords & Aliases: `fix with RCA`, `fix`, `fix, fix`, `CI/CD fix`, `cicd fix`

/goal Autonomously diagnose, execute, and resolve all CI/CD build, lint, and test failures using a local Python runner script. You MUST generate the runner script first (translating Docker to native local execution), run it to identify all failures locally, self-loop continuously to fix the code, record 4-part RCAs, and repeat the verification loop until the local runner and CI checks are 100% green. DO NOT stop after one turn; DO NOT wait for remote pipelines or user feedback to continue fixing.

/learn Ingest recent Root Cause Analysis (RCA) records from `.lovable/cicd-issues/`, `.lovable/issues/`, and `spec/03-error-manage/` before touching code so past mistakes and build traps are never repeated.

---

## Phase 0: Antigravity Skill Bootstrap (Memory Optimization)

Before executing or diagnosing CI/CD:

1. Check if `.agents/skills/ci-cd-fix/skill.md` exists in the workspace.
2. If it does NOT exist, you MUST create it now. Extract the core instructions of this prompt and write it to `.agents/skills/ci-cd-fix/skill.md` with standard YAML frontmatter (`name: ci-cd-fix`, `description: "Use this skill to autonomously diagnose, fix, and verify CI/CD pipelines using local runner scripts and self-looping."`).
3. Once installed, rely on progressive disclosure for future runs.

---

## Phase 1: Local Runner Script Bootstrap (`03-cicd-local-runner.py`)

To fix CI/CD rapidly without waiting 10-15 minutes for remote GitHub Actions or external runners, you MUST operate using a dedicated local test runner.

1. **Check Script Existence:** Check if `.lovable/ai-fix-scripts/03-cicd-local-runner.py` exists.
2. **Mandatory Generation Rule:** If the script is missing, or if forced to rebuild:
   - Deeply inspect all CI/CD configuration files (e.g., `.github/workflows/*.yml`, `.gitlab-ci.yml`, `azure-pipelines.yml`, etc.).
   - Extract every test, build, lint, typecheck, and formatting command.
   - **Docker Translation Rule (CRITICAL):** Strip out all Docker wrappers (`docker run`, containerized mounts). Translate the commands so they execute directly and natively on the host machine using Python's `subprocess`.
   - Write the complete script to `.lovable/ai-fix-scripts/03-cicd-local-runner.py`. Make sure it supports running checks in parallel and returns exit code `0` only when all checks pass.
3. **Execute Local Runner Immediately:** Run `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` as your first diagnostic action. Capture all failing commands and stack traces in your context window.

---

## Phase 2: Autonomous Self-Looping Fix Cycle (DO NOT STOP)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE:**
> Do NOT stop after making one code change. Do NOT tell the user to test or push. Do NOT await remote CI/CD results.
> You must execute a tight, autonomous loop until the local runner reports ZERO errors:
> 
> ```text
> WHILE (exit_code != 0):
>     1. Parse error output from 03-cicd-local-runner.py
>     2. Document 4-part RCA in .lovable/memory/issues/XX-<slug>.md
>     3. Apply surgical code fixes to the codebase
>     4. Re-run: python .lovable/ai-fix-scripts/03-cicd-local-runner.py
>     5. Check exit code:
>        - If exit_code != 0: Loop immediately to step 1 (DO NOT STOP).
>        - If exit_code == 0: Proceed to commit and push.
> ```

---

## Phase 3: The 4-Part RCA Requirement (Mandatory Memory File)

For each distinct failure category diagnosed, you MUST document the issue in `.lovable/memory/issues/XX-<slug>.md` (where XX is the next available sequential number). The file MUST contain these exact four sections:

1. **Why it happened:** The high-level business, logical, or architectural breakdown of the failure.
2. **How it happened:** The technical execution flow that triggered the bug or build failure.
3. **Root Cause:** The exact file, line, and dependency responsible for the failure.
4. **Code Fix:** The exact code snippets showing what needed to be changed to fix the root cause.

---

## No Automatic Releases (Strict Policy)

> [!CAUTION]
> **This is a development fix workflow.**
> You MUST NOT bump versions, update changelogs, or cut a release at the end of this task. Commits must remain standard development commits (`fix(ci): ...`). You are strictly forbidden from triggering a release or running version bump scripts unless the user explicitly commands you in chat (e.g., "cut a release").

---

## STRICT AVOIDANCE: Never Disable CI/CD

> [!CAUTION]
> **NEVER disable any CI/CD checks, GitHub Actions, or validation workflows.** 
> Strictly avoid commenting out, bypassing, deleting CI/CD steps, or adding `|| true` to force a pipeline to pass. Your job is to fix the underlying source code so that the CI/CD pipeline passes legitimately. Disabling CI/CD is an auto-reject failure.

---

## Non-Negotiable Coding Standards

Before committing, verify all modified files adhere to the project's coding standards:

- [ ] **Return New Line Concept (R13-R16):** One blank line before every `return`, `throw`, or `raise` (unless only statement in block). One blank line after closing `}`. Never two blank lines in a row.
- [ ] **No Explicit True Checks:** NEVER use `== true` or `=== true` (e.g., write `if isReady`, never `if isReady == true`).
- [ ] **No Mixed Polarity:** NEVER combine positive and negative checks in a single condition (`if isA && !isB` is banned; extract to a named boolean).
- [ ] **Function Length:** Hard cap of 15 lines per function. Flatten all nested conditionals.
- [ ] **Error Management:** No swallowed errors. Wrap all propagated errors with operation context (`apperror.Wrap`).
- [ ] **Go Generate Sync:** If Go constants, enums, or stringers were modified, run `go generate ./...` in the relevant directory and commit the generated files.
- [ ] **Strict Lowercase Naming:** All files must be lowercase (`readme.md`, `agents.md`, `skill.md`).

---

## End of Tunnel Checklist

- [ ] **Local CI Runner Clean:** `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0 (100% green).
- [ ] **RCA Documented:** Memory files written to `.lovable/memory/issues/XX-<slug>.md` with all 4 parts.
- [ ] **Stage & Commit:** Group related fixes into a clean commit with descriptive message (e.g., `fix(ci): resolve build and lint failures`).
- [ ] **Push to Remote:** Push commit to the current branch.
- [ ] **File Change Summary:** Provide a detailed summary in chat listing exactly which files were changed, what was changed inside them, and why they were changed.

---

## Metadata

- slug: cicd-fix
- status: active
