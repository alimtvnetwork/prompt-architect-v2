# Instruction (must follow): Autonomous CI/CD Fix Loop + Release

Trigger Keywords & Aliases: `fix and release`, `ci release`, `fix CI/CD and release`, `cicd fix release`

```text
N = 200
```

N = total self-loop steps budget. The user may override this number when triggering the prompt.

- [ ] /goal First `N/2` steps (Phase 1) are dedicated to reading all CI/CD configuration files and generating `.lovable/ai-fix-scripts/03-cicd-local-runner.py` with native host commands (Docker stripped out).
- [ ] /goal Second `N/2` steps (Phase 2) are dedicated to running that script in an autonomous loop, applying surgical fixes to the codebase after each failure, until exit code = 0.
- [ ] /goal Once Phase 2 exits green, proceed immediately to Phase 3: Final Verification, then Phase 4: Release.
- [ ] /learn Ingest `.lovable/cicd-issues/`, `.lovable/strictly-avoid.md`, and `spec/03-error-manage/` before touching any code so past mistakes are never repeated.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after the user sets them. Never change them mid-execution.

> [!CAUTION]
> **This prompt includes a release.** The version bump and GitHub/GitLab release creation WILL run automatically at the end. Only use this prompt when you are ready to publish a new version.

---

## Phase 0: Antigravity Skill Bootstrap (Memory Optimization)

Before any execution, check if `.agents/skills/ci-cd-fix/skill.md` exists. If it does NOT exist, create it now with YAML frontmatter:

```yaml
---
name: ci-cd-fix
description: >-
  Use this skill to autonomously diagnose, fix, and verify CI/CD pipelines using local runner scripts, 4-part RCA, and self-looping.
---
```

---

## Image Input Handling (Execute First When Any Screenshot or Image Is Provided)

> [!IMPORTANT]
> If the user provides any image — a CI/CD dashboard, a pipeline run view, a failure screenshot, or a log screenshot — you MUST process it BEFORE entering Phase 1 or Phase 2.
> Images are first-class diagnostic input. Treat every pixel of text in the image as ground truth.

### Step I-1: Extract the Pipeline Name from the Image

1. Carefully read the image. Locate and extract:
   - The **pipeline or workflow name** visible in the UI header or breadcrumb (e.g., `"build-and-test"`, `"CI / lint"`, `"node (18.x)"`)
   - The **job name(s)** shown in the sidebar or status board
   - The **step name(s)** that are marked as failed (red, ❌, or "Failure")
   - Any **error text, log snippets, or stack traces** visible in the screenshot
2. Record all extracted names and errors as primary targeting inputs.

### Step I-2: Verify Runner Coverage

1. Open `.lovable/ai-fix-scripts/03-cicd-local-runner.py` if it exists.
2. Check whether the `JOBS` dict already contains the extracted pipeline/job name.
3. **If NOT covered:** open the matching CI/CD workflow YAML, extract the full step list, apply the Docker Translation Rule, add the new `JOBS` entry, and save the updated runner.
4. **If already covered:** proceed without modification.

### Step I-3: Fix Errors Visible in the Image

1. For every error or stack trace extracted in Step I-1, open the exact source file and line and apply a surgical fix immediately.
2. Run the guideline autofixer on all modified files:

   ```text
   python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
   ```

### Step I-4: Run the Runner and Branch

1. Run `python .lovable/ai-fix-scripts/03-cicd-local-runner.py`.
2. If exit code = 0: skip Phase 2 and proceed to Phase 3.
3. If exit code != 0: continue into Phase 2 with combined evidence (image + runner output).

### Step I-5: RCA for Image-Derived Failures (Mandatory)

For each image-sourced error that required a fix, write a 4-part RCA at `.lovable/memory/issues/XX-<slug>.md`. Update `.lovable/memory/issues/index.md` and `.lovable/cicd-issues/index.md` in the same operation.

---

## Phase 1: Local Runner Script Generation (Steps 1 to PHASE_1_STEPS)

> [!IMPORTANT]
> This phase is dedicated ONLY to creating `.lovable/ai-fix-scripts/03-cicd-local-runner.py`.
> Do NOT fix source code in this phase. If Image Input Handling already updated the runner, verify and move on.

### Step 1: Check for Existing Script

- If `.lovable/ai-fix-scripts/03-cicd-local-runner.py` EXISTS and user did NOT say "force rebuild": skip to Phase 2.
- If MISSING: execute Steps 2 through 4 for up to PHASE_1_STEPS iterations.

### Step 2: Deep CI/CD Configuration Scan

Read in this order:

1. **CI/CD configuration files:**
   - GitHub Actions: `.github/workflows/*.yml` (ALL files)
   - GitLab CI: `.gitlab-ci.yml`
   - Azure Pipelines: `azure-pipelines.yml`
   - Bitbucket: `bitbucket-pipelines.yml`
   - CircleCI: `.circleci/config.yml`
   - Custom: `Makefile`, `scripts/ci.sh`, `run.sh`, `run.ps1`
2. **Language config:** `.nvmrc`, `.python-version`, `go.mod`, `pyproject.toml`, `tsconfig.json`, lockfiles
3. **For every CI/CD job, record:**
   - `runs-on` image, all `run:` commands, `env:` variables, dependency install, lint, typecheck, build, and test commands
4. **Check local toolchain:** `node --version`, `go version`, `python3 --version`, etc.

### Step 3: Docker Translation Rule (CRITICAL)

The host machine IS the Docker container. Strip all Docker wrappers:

- `docker run --rm node:20 npm ci` → `npm ci`
- `docker run --rm python:3.12 pytest` → `python3 -m pytest`
- `docker run --rm golang:1.22 go test ./...` → `go test ./...`
- Replace Docker `env` injection with `os.environ` assignments.
- **Skip entirely:** `docker login`, image tagging, registry pushes.

### Step 4: Write `03-cicd-local-runner.py`

Generate `.lovable/ai-fix-scripts/03-cicd-local-runner.py`:

```python
#!/usr/bin/env python3
"""Auto-generated CI/CD local runner. Do not edit manually."""
import subprocess
import sys
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError as FuturesTimeout

# ── Configurable Variables ──────────────────────────────────────────────────
BATCH_SIZE      = 3    # Jobs run simultaneously per batch
JOB_TIMEOUT_SEC = 300  # Seconds before a single job is considered timed out

# ── Environment (extracted from CI/CD env: blocks) ─────────────────────────
os.environ.setdefault("CI", "true")
os.environ.setdefault("NODE_ENV", "test")  # adapt from actual CI/CD env: block

# ── Job Definitions (adapt JOBS dict to actual CI/CD config) ────────────────
JOBS = {
    "install":   ["npm", "ci"],
    "lint":      ["npm", "run", "lint"],
    "typecheck": ["npx", "tsc", "--noEmit"],
    "build":     ["npm", "run", "build"],
    "test":      ["npm", "test", "--", "--watchAll=false"],
}

def run_job(name, cmd):
    start = time.monotonic()
    result = subprocess.run(cmd, capture_output=True, text=True)
    elapsed = round(time.monotonic() - start, 1)

    return name, result.returncode, result.stdout, result.stderr, elapsed

def run_batch(batch):
    results = {}
    with ThreadPoolExecutor(max_workers=BATCH_SIZE) as executor:
        futures = {executor.submit(run_job, name, cmd): name for name, cmd in batch}
        for future in as_completed(futures, timeout=JOB_TIMEOUT_SEC + 10):
            try:
                name, code, out, err, elapsed = future.result(timeout=JOB_TIMEOUT_SEC)
                results[name] = ("timeout" if code is None else code, out, err, elapsed)
            except FuturesTimeout:
                job_name = futures[future]
                results[job_name] = ("timeout", "", f"Timed out after {JOB_TIMEOUT_SEC}s", 0)

    return results

def main():
    job_items = list(JOBS.items())
    batches = [job_items[i:i + BATCH_SIZE] for i in range(0, len(job_items), BATCH_SIZE)]
    all_results = {}

    for batch in batches:
        batch_results = run_batch(batch)
        all_results.update(batch_results)

    all_passed = True
    for name, (code, out, err, elapsed) in all_results.items():
        if code == "timeout":
            print(f"\n⏱ TIMEOUT [{name}] after {JOB_TIMEOUT_SEC}s — {err}")
            all_passed = False
        elif code == 0:
            print(f"\n✅ PASS [{name}] ({elapsed}s)")
        else:
            print(f"\n❌ FAIL [{name}] ({elapsed}s)\n{err or out}")
            all_passed = False

    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()
```

---

## Phase 2: Autonomous Fix Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Never stop to tell the user "here are the errors". Fix them. The local runner IS your CI/CD.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Run: python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    2. Capture exit_code and full output.

    IF exit_code == 0:
        BREAK  ← Proceed to Phase 3: Final Verification.

    ELSE:
        3. Parse failure: identify exact failing job, error message, file, and line.
        4. Enqueue into .lovable/plans/pending/XX-cicd-<slug>.md (see Error Enqueuing section).
        5. Record in .lovable/cicd-issues/XX-<slug>.md and update index.
        6. Document 4-part RCA in .lovable/memory/issues/XX-<slug>.md.
        7. Apply the minimal surgical code fix.
        8. Run: python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
        9. Loop immediately to step 1. DO NOT stop.

IF STEP >= PHASE_2_STEPS AND exit_code != 0:
    Report remaining failures clearly in chat and ask the user for guidance.
    DO NOT proceed to Phase 3 or Phase 4 until all failures are resolved.
```

### Self-Looping Agent Rules

- Each loop iteration = one AI tool call cycle. End your turn and immediately start the next.
- Only print progress when a job status changes. Do not reprint passing jobs every iteration.
- Spawn one sub-agent per independent failure (lint / test / typecheck failing separately). Give each sub-agent a single-file bounding box.

---

## Parallel Batch Execution Rules (Mandatory)

- `BATCH_SIZE = 3`: at most 3 jobs run simultaneously per batch.
- After each batch completes, wait for all futures before starting the next batch.
- Non-order-dependent jobs (lint, typecheck, unit tests) run within the same batch.
- Order-dependent jobs (install → build → test) must be placed in sequential batches.
- After every batch, inspect results immediately. Do not wait for the full run.

---

## Timeout Detection and Auto-Increase (Mandatory)

If any job shows ⏱ TIMEOUT:

1. Do NOT treat it as a code failure. Timeout means the job is slow, not broken.
2. Diagnose: large input set? network dependency (`npm ci`)? hung subprocess or lock file?
3. Increase `JOB_TIMEOUT_SEC` intelligently:
   - Elapsed close to the limit → increase by 50%.
   - Job hangs with no output for >30s → fix the subprocess call, not the timer.
   - Open `03-cicd-local-runner.py`, update `JOB_TIMEOUT_SEC`, save, re-run.
4. Re-run the runner. The timeout adjustment counts as one Phase 2 loop step.
5. Document the timeout change in `.lovable/cicd-issues/`.

---

## Error Enqueuing — Plan Task & CI/CD Issue (Mandatory on Every Failure)

On every ❌ FAIL or ⏱ TIMEOUT, BEFORE applying any code fix, do both:

### A. Enqueue into Plan Tasks (`.lovable/plans/pending/XX-cicd-<slug>.md`)

```markdown
# CI/CD Task: <short failure description>

## Source
- Runner job: <job-name>
- Error type: FAIL | TIMEOUT
- Detected at: <timestamp>

## Error Summary
<exact error message>

## Required Fix
<one-sentence description>

## Acceptance Criteria
- [ ] `03-cicd-local-runner.py` reports ✅ PASS for job `<job-name>`
- [ ] No regression in any other job

## Status
- [ ] pending
```

Update `.lovable/plans/pending/index.md` immediately.

### B. Record in CI/CD Issues (`.lovable/cicd-issues/XX-<slug>.md`)

```markdown
# CI/CD Issue: <short failure description>

- Job: <job-name>
- Type: FAIL | TIMEOUT
- Detected: <timestamp>
- Status: open | resolved

## Error
<exact error output>

## Root Cause
<one-sentence root cause>

## Fix Applied
<what was changed>

## Plan Task
Enqueued at `.lovable/plans/pending/XX-cicd-<slug>.md`
```

Update `.lovable/cicd-issues/index.md` in the same operation. Never delete existing entries.

---

## Phase 3: Final Verification (Gate Before Release)

> [!IMPORTANT]
> Phase 3 is a hard gate. The release MUST NOT start until every item below is green.
> If any item fails, loop back to Phase 2 immediately.

- [ ] **Full runner pass:** Run `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` one final time. Exit code MUST be 0.
- [ ] **No open plan tasks from this run:** All `.lovable/plans/pending/XX-cicd-*.md` files created in this run are marked `resolved` or closed.
- [ ] **All RCA files written:** Every failure encountered has a `.lovable/memory/issues/XX-<slug>.md` with all 4 sections.
- [ ] **Coding standards pass:** Run `python .lovable/ai-fix-scripts/02-guideline-autofixer.py` on all modified files. Zero violations remain.
- [ ] **Git working tree is clean:** Run `git status`. No untracked or unstaged files. Commit any remaining changes with `fix(ci): final pre-release fixes`.

---

## Phase 4: Release

> [!IMPORTANT]
> Only enter Phase 4 after Phase 3 passes 100%. No exceptions.

### Step R-1: Pre-Flight Checks

1. Run `git status`. If uncommitted changes remain: commit them now with `fix(ci): pre-release cleanup`.
2. Run `git pull` to merge any upstream changes.
3. Read the current version from `version.json` (canonical source). Print it.
4. Idempotency guard: if the canonical version already equals the computed new version, STOP. Someone half-ran a release. Detect what is done, resume from the first incomplete step. Do NOT double-bump.
5. Placeholder guard: if the previous version's changelog entry is empty or contains `TBD`/`WIP`, refuse to release until it is filled (or the user overrides).

### Step R-2: Bump the Version

**Primary path — use the exact script at this path:**

```text
python .lovable/release/bump_versions.py --type minor --create-release
```

The `--create-release` flag handles: creating the `release/vX.Y.Z` git branch, committing, tagging `vX.Y.Z`, pushing, and creating the GitHub/GitLab release via `gh release create` or `glab release create`.

**Fallback chain (if `.lovable/release/bump_versions.py` is missing):**

1. **Fallback 1:** Read `.lovable/release/release-method.md` to identify all version pin sites. Regenerate `bump_versions.py` from that documentation. Review and update its internal `FILES_TO_BUMP` array to match this repository's actual architecture. Run it.
2. **Fallback 2:** If `release-method.md` is also missing, walk the repository with Python `os.walk` (ignoring `.git`, `node_modules`, `.venv`) to discover all version pin sites. Write `release-method.md` documenting them. Generate `bump_versions.py` with the correct `FILES_TO_BUMP`, `git checkout -b`, `git commit`, `git tag`, `git push`, and `gh`/`glab` release logic. Run it.
3. **Fallback 3:** If discovery fails, stop and ask the user to specify the version pin sites explicitly.

> [!CAUTION]
> **NEVER use `rg`, `grep`, or `find` to globally search for version strings.** Follow the fallback chain above. Global searches on large repos are slow and error-prone.

### Step R-3: Pin the New Version in `readme.md`

Rewrite every occurrence of the previous version (`vX.Y.Z` and bare `X.Y.Z`) in badges, install snippets, and inline references. After this step, `grep "<previous-version>" readme.md` MUST return nothing.

### Step R-4: Write the Changelog Entry

Add the following block at the top of `changelog.md`, directly under `# Changelog`:

```markdown
## [vX.Y.Z] YYYY-MM-DD <short headline>

### Install <Project Name> vX.Y.Z

Unix/Bash:
`curl -sL https://raw.githubusercontent.com/<owner>/<repo>/vX.Y.Z/install.sh | bash -s -- ".lovable/prompts" "vX.Y.Z"`

PowerShell:
`Invoke-WebRequest -Uri https://raw.githubusercontent.com/<owner>/<repo>/vX.Y.Z/install.ps1 -OutFile install.ps1; .\install.ps1 -TargetDir ".lovable/prompts" -Version "vX.Y.Z"`

### Added / Changed / Fixed / Removed

- <one bullet per real change, naming the exact file or behaviour>

### Issues (only if any step failed)

- [XX-<slug>](.lovable/release/issues/XX-vX.Y.Z-<slug>.md) short description
```

Dynamically discover `<owner>/<repo>` by running `git config --get remote.origin.url`. Do NOT hardcode URLs.

### Step R-5: Final Verification After Bump

1. Run the version-sync check if one exists (`scripts/check-version-sync.*`, `scripts/verify-versions.*`). It MUST exit 0.
2. Verify ALL pin sites reference the new version. No previous-version strings outside the historic allow-list (`changelog.md`, `release_notes.md`, `.lovable/release/`, dated archives).
3. All markdown filenames in the repository MUST be strictly lowercase. Rename any uppercase files with `git mv` in the same turn.

### Step R-6: Issue Logging (If Anything Goes Wrong)

If any release step fails, write an issue file at:

```text
.lovable/release/issues/XX-vX.Y.Z-<slug>.md
```

Include: previous version, new version, step number and name, command run, full error output, files involved, resolution or `unresolved`. Link it from the `### Issues` bullet in the changelog entry.

---

## Phase 4 Release Checklist

- [ ] Phase 3 (Final Verification) passed with exit code 0.
- [ ] Git working tree was clean before release steps.
- [ ] `git pull` completed with no conflicts.
- [ ] Previous and new versions both stated explicitly.
- [ ] `python .lovable/release/bump_versions.py --type minor --create-release` ran successfully (or fallback used and documented).
- [ ] All version pin sites updated to the new version.
- [ ] `readme.md` pinned to new version. No previous version strings remain.
- [ ] Changelog entry added with real bullets. No `TBD` or empty entries.
- [ ] All markdown filenames in repo are strictly lowercase.
- [ ] `### Issues` block present in changelog if any step failed, with links.
- [ ] Release commit tagged `vX.Y.Z` and pushed to remote.
- [ ] GitHub/GitLab release created via `gh release create` or `glab release create`.
- [ ] Report posted in chat: previous version, new version, bump tier, exact files changed.

---

## STRICT AVOIDANCE: Never Disable CI/CD

> [!CAUTION]
> **NEVER** comment out, bypass, delete CI/CD steps, or add `|| true` to force a pass.
> Fix the source code. Disabling CI/CD is an auto-reject failure.

---

## Non-Negotiable Coding Standards

- [ ] **Return New Line (R13-R16):** Blank line before `return`/`throw` (unless sole statement). Blank line after `}`. Never two blank lines in a row.
- [ ] **No Explicit True Checks:** Never `== true`. Write `if isReady`.
- [ ] **No Mixed Polarity:** Never `if isA && !isB`. Extract to a named boolean.
- [ ] **Boolean Prefixes:** All booleans start with `is`, `has`, `can`, `should`, `was`, `will`, `did`, or `must`.
- [ ] **Error Handling:** No swallowed errors. Wrap with `apperror.Wrap(err, "opName", ctx)`.
- [ ] **Strict Lowercase Files:** All generated/modified files use strictly lowercase naming.
- [ ] **Go Generate Sync:** If Go constants, enums, or stringers were modified, run `go generate ./...` and commit generated files.

---

## Metadata

- slug: cicd-fix-with-release
- status: active
