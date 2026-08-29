---
name: ci-cd-fix
description: >-
  Use this skill to autonomously diagnose, fix, and verify CI/CD pipelines using local runner scripts, 4-part RCA, and self-looping.
---

# Instruction (must follow): Autonomous CI/CD Fix Loop (with Local Runner & RCA)

Trigger Keywords & Aliases: `fix with RCA`, `fix`, `fix, fix`, `CI/CD fix`, `cicd fix`

/goal Autonomously diagnose, update or create the local Python CI/CD runner script (`.lovable/ai-fix-scripts/03-cicd-local-runner.py`) from repository workflows or screenshot pipeline names, and fix all failures by executing a singly-done self-looping sequence (zeroing in on one failure at a time) until the runner exits with code 0 without stopping.

/learn Ingest recent RCAs from `.lovable/cicd-issues/`, `.lovable/issues/`, `spec/02-coding-guidelines/00-canonical-size-tier.md`, `spec/02-coding-guidelines/06-ai-optimization/01-anti-hallucination-rules.md`, `spec/02-coding-guidelines/06-ai-optimization/05-citation-requirement.md`, and `spec/03-error-manage/` before touching any code so past mistakes are never repeated.

---

## Variables — Configurable at Runtime

```text
N = 200  (Total self-loop steps budget. The user may override this when triggering the prompt.)

PHASE_1_STEPS = N / 2  (Steps 1 .. N/2: Screenshot Pipeline Discovery, Update 03-cicd-local-runner.py, Register New JOBS)
PHASE_2_STEPS = N / 2  (Steps N/2+1 .. N: Singly-Done Self-Loop Fixing, Zero in on Errors, 4-Part RCA, Green Gate Verification)
```

Both N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after the user sets them.

---

## Screenshot & Pipeline Discovery Protocol (Execute First When Any Image Is Provided)

> [!IMPORTANT]
> **If the user provides any image or screenshot showing a CI/CD pipeline name, failing workflow, or error log:**
>
> 1. **FIRST ACTION — Update Python Runner:** Locate the pipeline/job in `.github/workflows/*.yml` (or repo CI configs) to find whatever new jobs, steps, or linters were added, and **immediately update `.lovable/ai-fix-scripts/03-cicd-local-runner.py`** to include them in the `JOBS` dictionary.
> 2. **SECOND ACTION — Singly-Done Self-Loop Execution:** Run the Python script iteratively, zeroing in on one failing error at a time using strictly bounded self-loop turns until all checks exit with code 0 (`exit 0`).

### Bounded Single-Step Self-Loop Sequence (Singly Done — No Overloaded Steps)

Every step must be **singly done** using bounded self-looping turns:

- **Self-Loop Step 1 (Extract Pipeline Name from Screenshot):**
  1. Read image to extract the pipeline name, failing job name, and error snippet.
  2. Scan `.github/workflows/*.yml` to identify the corresponding shell commands and dependencies.

- **Self-Loop Step 2 (FIRST ACTION: Update Python Runner Script):**
  1. Open `.lovable/ai-fix-scripts/03-cicd-local-runner.py`.
  2. If new jobs/steps are found in workflows, strip Docker wrappers and register the new commands in the `JOBS` dictionary.
  3. Save the runner script and verify syntax.

- **Self-Loop Step 3 (Execute Runner & Baseline Failures):**
  1. Run `python .lovable/ai-fix-scripts/03-cicd-local-runner.py`.
  2. If exit code = 0, proceed to End of Tunnel. If exit code != 0, zero in on the first specific failure.

- **Self-Loop Step 4 (RCA & Zero In on Error):**
  1. Write 4-part RCA in `.lovable/memory/issues/XX-<slug>.md`.
  2. Register in `.lovable/memory/issues/index.md` and `.lovable/strictly-avoid.md`.

- **Self-Loop Step 5 (Surgical Code Fix):**
  1. Open the specific file and line, apply minimal surgical fix.
  2. Run `python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>`.

- **Self-Loop Step 6 (Re-Verify & Loop):**
  1. Re-run `python .lovable/ai-fix-scripts/03-cicd-local-runner.py`.
  2. If resolved and more errors remain, self-loop to Step 4 to zero in on the next error until exit code = 0.

---

## Phase 1: Local Runner Script Generation (Steps 1 to PHASE_1_STEPS)

> [!IMPORTANT]
> **This phase is dedicated ONLY to creating `.lovable/ai-fix-scripts/03-cicd-local-runner.py`.**
> Do NOT fix code in this phase. Read, understand, and generate the script.

### Step 1: Check for Existing Script

- If `.lovable/ai-fix-scripts/03-cicd-local-runner.py` EXISTS and user did NOT say "force rebuild": skip to Phase 2.
- If MISSING or "force rebuild" was requested: execute Steps 2–4 for up to PHASE_1_STEPS iterations.

### Step 2: Deep CI/CD Configuration Scan

Spend up to PHASE_1_STEPS self-loop iterations reading in this order:

1. **CI/CD configuration files:**
   - GitHub Actions: `.github/workflows/*.yml` (ALL files)
   - GitLab CI: `.gitlab-ci.yml`
   - Azure Pipelines: `azure-pipelines.yml`
   - Bitbucket: `bitbucket-pipelines.yml`
   - CircleCI: `.circleci/config.yml`
   - Custom runners: `Makefile`, `scripts/ci.sh`, `run.sh`, `run.ps1`
2. **Language configuration:** `.nvmrc`, `.python-version`, `go.mod`, `pyproject.toml`, `tsconfig.json`, lockfiles
3. **For every CI/CD job, record:**
   - `runs-on` image (e.g., `ubuntu-latest`, `node:20-alpine`)
   - All `run:` shell commands and `uses:` action steps
   - Environment variables from `env:` blocks
   - Dependency install commands (`npm ci`, `go mod download`, `pip install -r requirements.txt`)
   - Lint, typecheck, build, and test commands
4. **Check local toolchain:** Run `node --version`, `go version`, `python3 --version`, etc. to know what is available natively.

### Step 3: Docker Translation Rule (CRITICAL)

The host machine IS the Docker container. Strip all Docker wrappers:

- `docker run --rm node:20 npm ci` → `npm ci`
- `docker run --rm python:3.12 pytest` → `python3 -m pytest`
- `docker run --rm golang:1.22 go test ./...` → `go test ./...`
- Replace Docker `env` injection with Python `os.environ` assignments.
- **Skip entirely:** `docker login`, image tagging, container registry pushes — these are deployment steps, not CI checks.

### Step 4: Write `03-cicd-local-runner.py`

Generate `.lovable/ai-fix-scripts/03-cicd-local-runner.py` that:

1. Runs ALL extracted CI/CD steps natively with `subprocess` and `check=False`.
2. Runs independent jobs in parallel using `concurrent.futures.ThreadPoolExecutor`.
3. Captures per-job stdout/stderr in separate buffers.
4. Exits `0` only when ALL jobs pass; exits non-zero if ANY job fails.
5. Prints a clear summary: `✅ PASS [job-name]` or `❌ FAIL [job-name]` with exact error output.

**Template (adapt JOBS dict from actual CI/CD config):**

```python
#!/usr/bin/env python3
"""Auto-generated CI/CD local runner. Do not edit manually."""
import subprocess
import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Environment (extracted from CI/CD env: blocks)
os.environ.setdefault("CI", "true")

# Jobs (extracted from CI/CD steps — adapt to actual project)
JOBS = {
    "install":   ["npm", "ci"],
    "lint":      ["npm", "run", "lint"],
    "typecheck": ["npx", "tsc", "--noEmit"],
    "build":     ["npm", "run", "build"],
    "test":      ["npm", "test", "--", "--watchAll=false"],
}

def run_job(name, cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)

    return name, result.returncode, result.stdout, result.stderr

def main():
    results = {}
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(run_job, name, cmd): name for name, cmd in JOBS.items()}
        for future in as_completed(futures):
            name, code, out, err = future.result()
            results[name] = (code, out, err)

    all_passed = True
    for name, (code, out, err) in results.items():
        status = "✅ PASS" if code == 0 else "❌ FAIL"
        print(f"\n{status} [{name}]")
        if code != 0:
            all_passed = False
            print(err or out)

    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()
```

---

## Phase 2: Autonomous Fix Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Never stop to tell the user "here are the errors". Fix them. Never await remote CI/CD results.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Run: python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    2. Capture exit_code and full output.

    IF exit_code == 0:
        BREAK  ← All checks pass. Proceed to End of Tunnel.

    ELSE:
        3. Parse failure: identify exact failing job, error message, file, and line.
        4. Document 4-part RCA in .lovable/memory/issues/XX-<slug>.md
        5. Apply the minimal surgical code fix.
        6. Run: python .lovable/ai-fix-scripts/02-guideline-autofixer.py <modified-files>
        7. Loop immediately to step 1. DO NOT stop.

IF STEP >= PHASE_2_STEPS AND exit_code != 0:
    Report remaining failures clearly in chat and ask the user for guidance.
```

**Sub-Agent Parallelization:** If multiple unrelated jobs fail (e.g., lint + test + typecheck), spawn one dedicated sub-agent per failure with a single-file bounding box. Parent agent collects results and re-runs the runner.

---

## Phase 3: 4-Part RCA Requirement

For each distinct failure write `.lovable/memory/issues/XX-<slug>.md` with:

1. **Why it happened:** High-level architectural reason.
2. **How it happened:** Exact execution flow that triggered the error.
3. **Root Cause:** Exact file, line number, and dependency responsible.
4. **Code Fix:** Before/after code snippet.

Also append any new forbidden patterns to `.lovable/strictly-avoid.md`.

---

## STRICT AVOIDANCE: Never Disable CLI Linting, Static Analysis, or CI/CD Checks (No Shortcut Cheating)

> [!CAUTION]
> **TOTAL BAN ON DISABLING, SKIPPING, OR BYPASSING CLI LINTERS AND CI/CD GATES:**
>
> - **NEVER** disable, comment out, delete, or skip any CLI linting command (`golangci-lint`, `eslint`, `markdownlint`, `tsc`, `pytest`, `phpstan`, `mypy`, `check-*.py`), build step, or test suite.
> - **NEVER** add `|| true`, `continue-on-error: true`, `# nolint`, `// eslint-disable`, or ignore flags to "quickly win the race" or fake a pipeline pass.
> - **Your job is to legitimately fix the underlying source code.** If resolving complex lint errors or test failures requires multiple sub-steps, sub-agents, or nested self-looping turns, you MUST execute all necessary turns until the code is 100% clean and compliant.
> - Disabling or bypassing any CI/CD or CLI lint check is an automatic and immediate rejection.

---

## No Automatic Releases

> [!CAUTION]
> Do NOT bump versions or cut a release unless the user explicitly says so. Use `fix(ci): <description>` commits only.

---

## Non-Negotiable Coding Standards

- [ ] **No Disabling CLI Linting (Zero Bypassing):** All CLI linters and CI/CD quality gates executed fully without `|| true`, `continue-on-error`, or suppression comments. Code was legitimately fixed.
- [ ] **Legitimate Multi-Step Self-Looping:** If complex errors occurred, I performed dedicated, single-step self-loop iterations to resolve each underlying failure instead of taking shortcuts.
- [ ] **Return New Line (R13-R16):** Blank line before `return`/`throw` (unless sole statement). Blank line after `}`. Never two blank lines in a row.
- [ ] **No Explicit True Checks:** Never `== true`. Write `if isReady`.
- [ ] **No Mixed Polarity:** Never `if isA && !isB`. Extract to a named boolean.
- [ ] **Strict Lowercase Files:** All generated/modified files use lowercase naming.

---

## End of Tunnel Checklist

- [ ] **Zero Linting/CI/CD Bypass:** Confirmed that NO CLI linters, static analysis tools, or test scripts were disabled, commented out, skipped, or bypassed with `|| true`.
- [ ] `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.
- [ ] All failures documented in `.lovable/memory/issues/XX-<slug>.md`.
- [ ] Changes committed: `fix(ci): resolve <summary>`.
- [ ] Pushed to the current branch.
- [ ] File change summary posted in chat (file, what changed, why).

---

## Metadata

- slug: cicd-fix
- status: active
