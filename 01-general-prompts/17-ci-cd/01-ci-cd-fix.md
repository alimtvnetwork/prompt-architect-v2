# Instruction (must follow): Autonomous CI/CD Fix Loop (with Local Runner & RCA)

Trigger Keywords & Aliases: `fix with RCA`, `fix`, `fix, fix`, `CI/CD fix`, `cicd fix`

```text
N = 200
```

N = total self-loop steps budget. The user may override this number when triggering the prompt.

- [ ] /goal First `N/2` steps (Phase 1) are dedicated to reading all CI/CD configuration files and generating `.lovable/ai-fix-scripts/03-cicd-local-runner.py` with native host commands (Docker stripped out).
- [ ] /goal Second `N/2` steps (Phase 2) are dedicated to running that script in an autonomous loop, applying surgical fixes to the codebase after each failure, until exit code = 0.
- [ ] /learn Ingest `.lovable/cicd-issues/`, `.lovable/strictly-avoid.md`, and `spec/03-error-manage/` before touching any code so past mistakes are never repeated.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after the user sets them. Never change them mid-execution.

---

## Phase 0: Antigravity Skill Bootstrap (Memory Optimization)

Before any execution, check if this prompt is installed as a native Antigravity Skill.

1. Check if `.agents/skills/ci-cd-fix/skill.md` exists.
2. If it does NOT exist, create it now. Write the core instructions of this prompt to `.agents/skills/ci-cd-fix/skill.md` with frontmatter:
   ```yaml
   ---
   name: ci-cd-fix
   description: >-
     Use this skill to autonomously diagnose, fix, and verify CI/CD pipelines using local runner scripts, 4-part RCA, and self-looping.
   ---
   ```
3. Once installed, load it on-demand via progressive disclosure for all future runs.

---

## Image Input Handling (Execute First When Any Screenshot or Image Is Provided)

> [!IMPORTANT]
> **If the user provides any image — a CI/CD dashboard, a pipeline run view, a failure screenshot, or a log screenshot — you MUST process it BEFORE entering Phase 1 or Phase 2.**
> Images are first-class diagnostic input. Treat every pixel of text in the image as ground truth.

### Step I-1: Extract the Pipeline Name from the Image

1. Carefully read the image. Locate and extract:
   - The **pipeline or workflow name** visible in the UI header or breadcrumb (e.g., `"build-and-test"`, `"CI / lint"`, `"Deploy to staging"`, `"node (18.x)"`)
   - The **job name(s)** shown in the sidebar, status board, or step list
   - The **step name(s)** that are marked as failed (❌, red, or labeled "Failure")
   - Any **error text, log snippets, or stack traces** visible directly in the screenshot
2. Record all extracted names and errors. They become your primary targeting inputs for the rest of the workflow.

### Step I-2: Verify Runner Coverage

After identifying the pipeline and job names from the image:

1. Open `.lovable/ai-fix-scripts/03-cicd-local-runner.py` if it exists.
2. Check whether the `JOBS` dict already contains an entry whose key matches or maps to the extracted pipeline/job name.
3. **If the pipeline is NOT covered:**
   - Open the corresponding CI/CD configuration file (`.github/workflows/*.yml` or equivalent).
   - Locate the exact job definition by name.
   - Extract its full step list.
   - Apply the Docker Translation Rule (see Phase 1 Step 3).
   - Add the new job entry to the `JOBS` dict and save the updated runner script.
   - Log the addition: `"Added job '<name>' from image input to 03-cicd-local-runner.py"`.
4. **If the pipeline IS already covered:** proceed without modification.

### Step I-3: Fix Errors Visible in the Image

1. For every error, failure message, or stack trace extracted from the image in Step I-1:
   - Identify the exact source file, line number, and symbol named in the error.
   - Open that file in the codebase and apply the surgical fix.
   - Do NOT wait for the runner to surface the same error — fix it now based on the image evidence.
2. After applying all image-derived fixes, run the guideline autofixer on all modified files:
   ```text
   python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
   ```

### Step I-4: Run the Runner and Verify

1. Run `python .lovable/ai-fix-scripts/03-cicd-local-runner.py`.
2. Capture the full output and exit code.
3. If exit code is non-zero, continue into Phase 2 with the combined evidence (image errors + runner output).
4. If exit code is 0, skip Phase 2 and proceed directly to Phase 3 (RCA) and End of Tunnel.

### Step I-5: RCA for Image-Derived Failures (Mandatory)

For every error extracted from the image that required a fix, write a 4-part RCA file:

- Path: `.lovable/memory/issues/XX-<slug>.md` (next sequential number)
- Sections: **Why it happened / How it happened / Root Cause / Code Fix**
- Update `.lovable/memory/issues/index.md` to register the new entry.
- Append any new forbidden pattern to `.lovable/strictly-avoid.md`.

---

## Phase 1: Local Runner Script Generation (Steps 1 to PHASE_1_STEPS)

> [!IMPORTANT]
> **This entire phase is dedicated to one goal ONLY: creating `.lovable/ai-fix-scripts/03-cicd-local-runner.py`.**
> Do NOT attempt to fix code in this phase. Read, understand, and generate the script.
> If Image Input Handling (above) already updated the runner, verify the update is complete and move on.

### Step 1: Check for Existing Script

- Check if `.lovable/ai-fix-scripts/03-cicd-local-runner.py` already exists.
- If it EXISTS and the user did **not** say "force rebuild": skip to Phase 2 immediately.
- If it is MISSING or the user said "force rebuild": execute Steps 2 through PHASE_1_STEPS.

### Step 2: Deep CI/CD Configuration Scan

Spend up to PHASE_1_STEPS self-loop iterations reading the codebase in this order:

1. **Locate all CI/CD runner configuration files:**
   - GitHub Actions: `.github/workflows/*.yml` (scan ALL workflow files)
   - GitLab CI: `.gitlab-ci.yml`
   - Azure Pipelines: `azure-pipelines.yml`
   - Bitbucket Pipelines: `bitbucket-pipelines.yml`
   - CircleCI: `.circleci/config.yml`
   - Any custom runner scripts: `Makefile`, `scripts/ci.sh`, `run.sh`, `run.ps1`
   - Project lockfiles: `package-lock.json`, `go.sum`, `poetry.lock`, `bun.lockb` (to detect toolchain versions)
   - Language config: `.nvmrc`, `.python-version`, `go.mod`, `pyproject.toml`, `tsconfig.json`

2. **Extract all jobs and steps:** For every CI/CD job, record:
   - The `runs-on` image (e.g., `ubuntu-latest`, `node:20-alpine`)
   - All `run:` shell commands or `uses:` action steps
   - Environment variables set with `env:`
   - Cache keys used (e.g., `actions/cache`, `cache: npm`)
   - The dependency install command (e.g., `npm ci`, `go mod download`, `pip install -r requirements.txt`)
   - The lint command (e.g., `npm run lint`, `golangci-lint run`)
   - The typecheck/static analysis command (e.g., `tsc --noEmit`, `mypy .`)
   - The build command (e.g., `npm run build`, `go build ./...`)
   - The test command (e.g., `npm test`, `go test ./...`, `pytest`)

3. **Understand the local environment:** Check which tools are already installed on the host machine:
   - `node --version`, `npm --version`, `go version`, `python3 --version`, `cargo --version`, `php --version`
   - This determines which commands need translation vs. which can run as-is.

### Step 3: Docker Translation Rule (CRITICAL)

CI/CD pipelines run inside Docker containers. Your local runner MUST treat the **host machine as if it were that Docker image**. This means:

- **Strip all Docker invocations:** Never include `docker run`, `docker build`, `docker-compose`, or `docker pull` commands in the runner script.
- **Translate container steps to native host commands:**
  - A step like `docker run --rm node:20 npm ci` becomes `npm ci` (run directly on host).
  - A step like `docker run --rm python:3.12 pytest` becomes `python3 -m pytest` (run directly on host).
  - A step like `docker run --rm golang:1.22 go test ./...` becomes `go test ./...` (run directly on host).
- **Replace Docker-specific env injection** with Python `os.environ` assignments before running subprocess commands.
- **Skip container-only operations** like `docker login`, image tagging, or container registry pushes — these are deployment steps, not CI checks.

### Step 4: Write `03-cicd-local-runner.py`

Using all information gathered, generate `.lovable/ai-fix-scripts/03-cicd-local-runner.py` that:

1. **Runs ALL extracted CI/CD steps natively** using Python's `subprocess` module with `check=False` (so failures are captured, not thrown).
2. **Runs independent jobs in parallel** using `concurrent.futures.ThreadPoolExecutor` to simulate CI speed.
3. **Captures output per job** in separate buffers and prints them sequentially at the end.
4. **Exits with code 0** only if ALL jobs pass; exits with non-zero if ANY job fails.
5. **Prints a clear structured summary** at the end listing which steps passed ✅ and which failed ❌ with their exact error output.
6. **Runs jobs in parallel batches** of `BATCH_SIZE` (default 3) with a configurable per-job timeout `JOB_TIMEOUT_SEC` (default 300). If a job times out, it is marked ⏱ TIMEOUT and the runner continues.

**Example template structure for the generated script:**

```python
#!/usr/bin/env python3
"""Auto-generated CI/CD local runner. Do not edit manually.
Re-generate by running: python .lovable/ai-fix-scripts/03-cicd-local-runner.py --rebuild
"""
import subprocess
import sys
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError as FuturesTimeout

# ── Configurable Variables ──────────────────────────────────────────────────
BATCH_SIZE      = 3    # Number of jobs to run in parallel per batch
JOB_TIMEOUT_SEC = 300  # Seconds before a single job is considered timed out

# ── Environment (extracted from CI/CD env: blocks) ─────────────────────────
os.environ.setdefault("CI", "true")
os.environ.setdefault("NODE_ENV", "test")  # adapt from actual CI/CD env: block

# ── Job Definitions (extracted from CI/CD steps — adapt JOBS to real config) ─
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
> After generating the runner script, you enter an autonomous fix loop.
> Never stop to tell the user "here are the errors". Fix them immediately.
> Never await remote CI/CD results. The local runner IS your CI/CD.

Execute this exact loop for up to PHASE_2_STEPS iterations:

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Run:  python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    2. Capture exit_code and full output

    IF exit_code == 0:
        BREAK  ← All checks pass. Proceed to End of Tunnel.

    ELSE:
        3. Parse the failure output: identify the exact failing job, error message, file, and line.
        4. Document 4-part RCA in .lovable/memory/issues/XX-<slug>.md
        5. Apply the minimal surgical code fix to the codebase.
        6. Run the guideline autofixer on modified files:
              python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
        7. Loop back to step 1 immediately. DO NOT stop.

IF STEP >= PHASE_2_STEPS AND exit_code != 0:
    Report the remaining failures clearly in chat and ask the user for guidance.
```

### Self-Looping Agent Rules

- **Each loop iteration = one AI tool call cycle.** After each iteration, self-loop by ending your turn and immediately starting the next iteration.
- **No output clutter:** Only print progress when a job status changes (new failure or new fix). Do not reprint passing jobs every iteration.
- **Spawn sub-agents for independent failures:** If multiple unrelated jobs are failing (e.g., lint + test + typecheck all failing independently), spawn one dedicated sub-agent per failure. Give each sub-agent a single-file bounding box. The parent agent collects results and re-runs the runner.

---

## Parallel Batch Execution Rules (Mandatory)

Every time `03-cicd-local-runner.py` is executed, it MUST run jobs in parallel batches, not one at a time:

- `BATCH_SIZE = 3` means at most 3 jobs run simultaneously within a batch.
- After each batch completes, wait for all futures to resolve before starting the next batch.
- Jobs within a batch that are NOT order-dependent (e.g., lint, typecheck, and unit tests) run concurrently.
- Jobs that ARE order-dependent (e.g., install → build → test) must be placed in **sequential batches**, not the same batch.
- After every batch, inspect the results immediately. Do not wait for the entire run to finish before reading output.

---

## Timeout Detection and Auto-Increase (Mandatory)

If any job is marked ⏱ TIMEOUT in the runner output:

1. **Do NOT treat it as a code failure.** Timeout ≠ broken code; it means the job took longer than `JOB_TIMEOUT_SEC` allows.
2. **Diagnose the cause:**
   - Is the job doing work proportional to a large input set (e.g., full test suite, large build)?
   - Is a network dependency involved (e.g., `npm ci` downloading packages)?
   - Did a previous step leave a hung process or lock file?
3. **Increase the timeout intelligently:**
   - If the job's measured elapsed time (before it was killed) was close to the limit: increase `JOB_TIMEOUT_SEC` by `50%`.
   - If the job appears to hang indefinitely (no output for >30s): look for a subprocess deadlock or missing stdin; fix the subprocess call, do not just increase the timer.
   - Open `03-cicd-local-runner.py`, update `JOB_TIMEOUT_SEC` to the new value, and save the file.
4. Re-run the runner immediately after the timeout fix. The timeout adjustment counts as one Phase 2 loop step.
5. Document the timeout increase in `.lovable/cicd-issues/` as a standard CI/CD issue entry.

---

## Error Enqueuing — Plan Task & CI/CD Issue (Mandatory on Every Failure)

Every time the runner reports a ❌ FAIL or ⏱ TIMEOUT, you MUST do **both** of the following before applying the code fix:

### A. Enqueue into Plan Tasks

Create (or append to) a pending plan task file at:

```text
.lovable/plans/pending/XX-cicd-<slug>.md
```

Where `XX` is the next available sequential number and `<slug>` is a short kebab-case description of the failure (e.g., `03-cicd-lint-unused-import`).

The plan task file MUST contain:

```markdown
# CI/CD Task: <short failure description>

## Source
- Runner job: <job-name>
- Error type: FAIL | TIMEOUT
- Detected at: <timestamp>

## Error Summary
<paste the exact error message or timeout log here>

## Required Fix
<one-sentence description of the fix needed>

## Acceptance Criteria
- [ ] `03-cicd-local-runner.py` reports ✅ PASS for job `<job-name>`
- [ ] No regression in any other job

## Status
- [ ] pending
```

Update `.lovable/plans/pending/index.md` to register the new task entry immediately.

### B. Record in CI/CD Issues

Create a CI/CD issue record at:

```text
.lovable/cicd-issues/XX-<slug>.md
```

The CI/CD issue file MUST contain:

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
<what was changed to fix it>

## Plan Task
Enqueued at `.lovable/plans/pending/XX-cicd-<slug>.md`
```

Update `.lovable/cicd-issues/index.md` in the same operation. Never delete existing entries.

---

## Phase 3: 4-Part RCA Requirement (Mandatory Memory File)

For each distinct failure type encountered in Phase 2, write a memory file at `.lovable/memory/issues/XX-<slug>.md` with exactly four sections:

1. **Why it happened:** High-level architectural reason for the failure.
2. **How it happened:** Exact execution flow that triggered the error.
3. **Root Cause:** Exact file, line number, and dependency responsible.
4. **Code Fix:** Code snippet showing the before and after of the fix.

Also append any new forbidden patterns to `.lovable/strictly-avoid.md`.

---

## Pre-Flight: Past RCA Ingestion

Before entering Phase 1 or Phase 2:

- Read `.lovable/cicd-issues/` and `.lovable/strictly-avoid.md`.
- Read the provided CI/CD error log if the user supplied one.
- These provide the known failure history and ensure you never repeat a past mistake.

---

## STRICT AVOIDANCE: Never Disable CI/CD

> [!CAUTION]
> **NEVER disable any CI/CD checks, GitHub Actions, or validation workflows.**
> Never comment out, bypass, delete CI/CD steps, or add `|| true` to force a pass.
> Your job is to fix the source code so the CI/CD passes legitimately.
> Disabling CI/CD is an auto-reject failure.

---

## No Automatic Releases (Strict Policy)

> [!CAUTION]
> This is a development fix workflow. You MUST NOT bump versions, update changelogs, or cut a release unless the user explicitly commands it in chat (e.g., "cut a release" or "bump the version"). All commits use `fix(ci): <description>`.

---

## Non-Negotiable Coding Standards

Run `.lovable/ai-fix-scripts/02-guideline-autofixer.py` on all modified files, then verify:

- [ ] **Return New Line (R13-R16):** One blank line before every `return`/`throw` (unless sole statement). One blank line after closing `}`. Never two blank lines in a row.
- [ ] **No Explicit True Checks:** NEVER write `== true` or `=== true`. Write `if isReady`, not `if isReady == true`.
- [ ] **No Mixed Polarity:** NEVER write `if isA && !isB`. Extract to a named boolean.
- [ ] **Boolean Prefixes:** All boolean variables start with `is`, `has`, `can`, `should`, `was`, `will`, `did`, or `must`.
- [ ] **Error Handling:** No swallowed errors. Every propagated error is wrapped with `apperror.Wrap(err, "opName", ctx)`.
- [ ] **Strict Lowercase Files:** All generated/modified files use strictly lowercase naming.
- [ ] **Go Generate Sync:** If Go constants, enums, or stringers were modified, run `go generate ./...` and commit generated files.

---

## End of Tunnel Checklist

When `03-cicd-local-runner.py` exits with code 0:

- [ ] **Local CI Runner 100% Green:** All jobs in `03-cicd-local-runner.py` passed (exit code = 0).
- [ ] **RCA Documented:** All encountered failures have memory files in `.lovable/memory/issues/`.
- [ ] **Stage & Commit:** Group all related fixes into a single descriptive commit: `fix(ci): resolve <summary>`.
- [ ] **Push to Remote:** Push the commit to the current branch.
- [ ] **File Change Summary (MANDATORY):** In chat, list every file changed, what specifically changed inside it, and why. This summary is critical.

---

## Metadata

- slug: cicd-fix
- status: active
