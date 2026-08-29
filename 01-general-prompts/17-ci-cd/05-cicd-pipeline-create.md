# Instruction (must follow): CI/CD Pipeline & Cross-Platform Python Automation Creation

Trigger Keywords & Aliases: `create-ci-cd`, `cicd-create`, `create cicd`, `setup cicd pipeline`, `build ci-cd pipeline`, `cicd create python`, `05-cicd-pipeline-create`

```text
N = 300
```

N = total self-loop steps budget for end-to-end CI/CD creation and cross-platform automation.

- [ ] /goal First N/2 steps (Phase 1): Deeply scan the repository, ingest all CI/CD and pipeline specifications (`index.md` or `00-overview.md` and all subfiles), design cross-platform Python automation scripts (build, test, lint, validate), and configure `.lovable/ai-fix-scripts/03-cicd-local-runner.py`.
- [ ] /goal Second N/2 steps (Phase 2): Generate complete GitHub Actions workflows (`.github/workflows/*.yml`) and GitLab CI configurations (`.gitlab-ci.yml`), implement Python linters and test harnesses, and execute autonomous self-loops until all local and remote CI checks pass with exit code 0.
- [ ] /learn Ingest `spec/12-cicd-pipeline-workflows/`, `spec/02-coding-guidelines/06-cicd-integration/`, `spec/11-powershell-integration/`, `spec/14-update/`, `spec/15-distribution-and-runner/`, `spec/16-generic-release/`, `spec/17-consolidated-guidelines/15-cicd-pipeline-workflows.md`, and `.lovable/coding-guidelines/coding-guidelines.md` before taking action.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. 150: Spec Ingestion, Python Automation Design, Local Runner Setup)
PHASE_2_STEPS = N / 2   (Steps 151 .. 300: Workflow Generation, Python Linter Verification, Green Gate Loop)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after the user sets them. Never change them mid-execution.

---

## Phase 0: Antigravity Skill Bootstrap (Memory Optimization)

Before any execution, check if this prompt is installed as a native Antigravity Skill.

1. Check if `.agents/skills/ci-cd-create/skill.md` exists in the workspace.
2. If it does NOT exist, create it now. Write the core instructions to `.agents/skills/ci-cd-create/skill.md` with frontmatter:
   ```yaml
   ---
   name: ci-cd-create
   description: >-
     Use this skill to autonomously design, create, and verify cross-platform Python CI/CD pipelines, linters, and workflows.
   ---
   ```
3. Once installed, load it on-demand via progressive disclosure for all future runs.

---

## 1. Specification Ingestion Checklist (Read Index / Overview and Subfiles)

For every specification folder below, AI agents MUST read `index.md` or `00-overview.md` (or both) first, then deeply internalize all referenced subfiles before authoring any CI/CD or automation files:

### A. CI/CD Pipeline Workflows (`spec/12-cicd-pipeline-workflows/`)

- [ ] Read `00-overview.md` or `index.md`
- [ ] `01-ci-pipeline.md`: Core CI triggers, matrix builds, artifact passing, and caching contracts.
- [ ] `01-shared-conventions.md`: Universal environment variables, exit codes, and cross-platform paths.
- [ ] `02-release-pipeline.md` & `02-github-release-standard.md`: Automated release tagging, checksums, and assets.
- [ ] `01-browser-extension-deploy/`: (`00-overview.md`, `01-ci-pipeline.md`, `02-release-pipeline.md`, `99-consistency-report.md`).
- [ ] `02-go-binary-deploy/`: (`00-overview.md`, `01-ci-pipeline.md`, `02-release-pipeline.md`, `03-complete-workflow-reference.md`).
- [ ] `03-reusable-ci-guards/`: (`00-overview.md`, `01-forbidden-name-guard.md`, `02-grandfather-baseline-naming.md`, `03-cross-file-collision-audit.md`, `04-baseline-diff-lint-gate.md`, `05-actionable-lint-suggestions.md`, `06-matrix-test-aggregator.md`, `07-shared-cli-wrapper.md`, `08-config-schema.md`, `09-workflow-templates.md`, `99-ai-implementation-guide.md`).
- [ ] `03-vulnerability-scanning.md`: Trivy, Snyk, and dependency vulnerability audits.
- [ ] `04-install-script-generation.md` & `04-installation-flow.md`: Cross-platform installer generation.
- [ ] `05-changelog-integration.md` & `07-release-body-and-changelog.md`: Automated changelog parsing and notes.
- [ ] `05-code-signing.md`: Binary signing for Windows (`signtool`/`osslsigncode`) and macOS (`codesign`).
- [ ] `06-self-update-mechanism.md` & `06-version-and-help.md`: Self-update validation in CI.
- [ ] `07-environment-variable-setup.md`: Secure secret injection and default environment fallbacks.
- [ ] `08-terminal-output-standards.md`: Clean, color-coded ANSI logging without clutter.
- [ ] `09-binary-icon-branding.md`: Resource embedding (`rsrc`, `windres`) in CI build steps.
- [ ] `10-release-pipeline-issues-rca.md`: 4-part RCA logging for failed release stages.
- [ ] `11-blue-green-deployment.md`: Zero-downtime deployment pipelines.
- [ ] `12-flaky-test-quarantine.md`: Quarantine strategies and automatic retry bounds.
- [ ] `13-contract-testing.md`: API schema validation and contract tests.
- [ ] `14-e2e-testing-pattern.md`: End-to-end integration and browser automated test flows.

### B. Coding Guidelines CI/CD Integration (`spec/02-coding-guidelines/06-cicd-integration/`)

- [ ] Read `00-overview.md` or `index.md`
- [ ] `01-sarif-contract.md`: Standard SARIF format for static analysis output.
- [ ] `02-plugin-model.md`: Extensible plugin architectures for linting.
- [ ] `04-ci-templates.md`: Reusable GitHub Actions / GitLab CI workflow templates.
- [ ] `05-distribution.md`: Packaging linters and CLI tools for multi-architecture distribution.
- [ ] `06-rules-mapping.md`: Mapping code-red rules to linter error codes.
- [ ] `07-performance.md`: Caching dependencies, build matrices, and sub-minute execution goals.
- [ ] `08-fix-repo-and-installers/`: (`00-overview.md`, `01-fix-repo-contract.md`, `02-installer-contract.md`, `03-visibility-change-contract.md`).

### C. Cross-Platform Automation & Update Architecture

- [ ] `spec/11-powershell-integration/`: (`00-overview.md`, `01-configuration-schema.md`, `02-script-reference.md`, `03-integration-guide.md`, `04-error-codes.md`).
- [ ] `spec/13-generic-cli/`: (`11-build-deploy.md`, `12-testing.md`, `18-batch-execution.md`, `20-terminal-output-design.md`, `22-self-update-gold-standard.md`).
- [ ] `spec/14-update/`: (`04-build-scripts.md`, `16-cross-compilation.md`, `17-release-pipeline.md`, `18-install-scripts.md`, `24-update-check-mechanism/`).
- [ ] `spec/15-distribution-and-runner/`: (`01-install-contract.md`, `02-runner-contract.md`, `03-release-pipeline.md`, `04-install-config.md`).
- [ ] `spec/16-generic-release/`: (`01-cross-compilation.md`, `02-release-pipeline.md`, `03-install-scripts.md`, `04-checksums-verification.md`, `05-release-assets.md`, `08-version-pinned-release-installers.md`).
- [ ] `spec/17-consolidated-guidelines/15-cicd-pipeline-workflows.md`: Master consolidated CI/CD reference.

---

## 2. Cross-Platform Python-First Mandate

> [!IMPORTANT]
> **PYTHON-FIRST AUTOMATION (NO FRAGILE SHELL SCRIPTS):**
>
> 1. All CI/CD build scripts, test runners, validation checks, and linters MUST be written in **Python 3** using standard library modules (`subprocess`, `sys`, `os`, `pathlib`, `concurrent.futures`, `json`, `shutil`).
> 2. Python ensures identical, deterministic execution across **Windows, Linux, and macOS** without platform-specific shell quirks (CRLF vs LF, PowerShell vs Bash, path separators).
> 3. Shell scripts (`.sh`, `.ps1`) must ONLY act as lightweight one-line entrypoints that invoke Python (e.g., `python scripts/build.py "$@"`).
> 4. All linter scripts (e.g. `linter-scripts/validate-guidelines.py`, `linter-scripts/check-*.py`) must be executable directly via Python without external wrapper dependencies.

### Standard Cross-Platform Python Scripts Architecture

```text
scripts/ or .lovable/ai-fix-scripts/
├── 01-file-manipulator.py       # File renaming, sequence renumbering, CRLF normalization
├── 02-guideline-autofixer.py    # Auto-formats return new lines and cleans booleans
├── 03-cicd-local-runner.py      # Master native host runner executing all CI/CD jobs
├── build.py                     # Cross-platform compilation & bundling script
├── test.py                      # Parallel test runner with coverage aggregation
└── lint.py                      # Multi-linter orchestrator (markdownlint, eslint, tsc, go, etc.)
```

---

## 3. Phase 1: Local Automation & Python Runner Setup (Steps 1 to PHASE_1_STEPS)

> [!IMPORTANT]
> **Build the local cross-platform foundation first.** Remote CI/CD workflows merely mirror the local Python runner.

### Step 1: Detect Tech Stack & Toolchains

1. Inspect project files (`package.json`, `go.mod`, `pyproject.toml`, `Cargo.toml`, `composer.json`, `version.json`).
2. Identify target compilers, linters, and test engines.
3. Record exact commands needed for:
   - Dependency installation (`npm ci`, `go mod download`, `pip install -r requirements.txt`, `composer install`).
   - Linting & static analysis (`golangci-lint`, `eslint`, `markdownlint`, `tsc --noEmit`, `phpcs`, `mypy`).
   - Build & compilation (`npm run build`, `go build`, `python -m build`, `cargo build`).
   - Automated testing (`npm test`, `go test -race ./...`, `pytest`, `cargo test`).

### Step 2: Implement Cross-Platform Python Linters

If custom checks or guideline validations are required:

1. Write or update Python scripts in `linter-scripts/` (e.g., `validate-guidelines.py`, `check-markdown-header-spacing.py`).
2. Ensure linters output standard error formats: `file:line:col: [RULE-CODE] message`.
3. Support `--fix` flag wherever deterministic AST/regex automated repair is possible.

### Step 3: Generate `.lovable/ai-fix-scripts/03-cicd-local-runner.py`

Create the master parallel local runner script that strips Docker wrappers and runs natively:

```python
#!/usr/bin/env python3
"""Auto-generated Cross-Platform CI/CD Local Runner."""
import os
import sys
import time
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

os.environ.setdefault("CI", "true")

BATCH_SIZE = 3
JOB_TIMEOUT_SEC = 120

# Populate JOBS dictionary from project requirements
JOBS = {
    "lint":      [sys.executable, "scripts/lint.py"],
    "typecheck": ["npx", "tsc", "--noEmit"],
    "build":     [sys.executable, "scripts/build.py"],
    "test":      [sys.executable, "scripts/test.py"],
}

def run_job(name: str, cmd: list):
    start_time = time.time()
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=JOB_TIMEOUT_SEC)
        elapsed = round(time.time() - start_time, 2)
        return name, res.returncode, res.stdout, res.stderr, elapsed
    except subprocess.TimeoutExpired:
        elapsed = round(time.time() - start_time, 2)
        return name, -1, "", f"Timed out after {JOB_TIMEOUT_SEC}s", elapsed
    except Exception as e:
        elapsed = round(time.time() - start_time, 2)
        return name, 1, "", str(e), elapsed

def main():
    print(f"🚀 Running CI/CD Local Runner ({len(JOBS)} jobs)...")
    job_items = list(JOBS.items())
    batches = [job_items[i:i + BATCH_SIZE] for i in range(0, len(job_items), BATCH_SIZE)]
    all_results = {}

    for batch in batches:
        with ThreadPoolExecutor(max_workers=BATCH_SIZE) as executor:
            futures = {executor.submit(run_job, name, cmd): name for name, cmd in batch}
            for future in as_completed(futures):
                name, code, out, err, elapsed = future.result()
                all_results[name] = (code, out, err, elapsed)

    all_passed = True
    for name, (code, out, err, elapsed) in all_results.items():
        if code == 0:
            print(f"✅ PASS [{name}] ({elapsed}s)")
        else:
            all_passed = False
            print(f"❌ FAIL [{name}] ({elapsed}s)\n{err or out}")

    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()
```

---

## 4. Phase 2: Workflow Generation & Green Gate Verification (Steps PHASE_1_STEPS+1 to N)

### Step 1: Generate GitHub Actions Workflows (`.github/workflows/`)

1. Create `.github/workflows/ci.yml` covering:
   - Matrix builds across OS platforms (`ubuntu-latest`, `windows-latest`, `macos-latest`) where applicable.
   - Cache steps (`actions/cache`, `actions/setup-node`, `actions/setup-python`, `actions/setup-go`).
   - Linting, typechecking, building, and testing jobs.
   - Invocation of native Python runner and scripts.
2. Create `.github/workflows/release.yml` covering:
   - Tagged release triggers (`v*`).
   - Multi-arch cross-compilation.
   - Checksum generation (`sha256sum`).
   - Release creation with `--notes-file` and Quick Install one-liners.

### Step 2: Autonomous Local Verification Loop

Execute the local runner and resolve every failure singly using self-looping turns:

```text
LOOP:
    1. Execute: python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    2. IF exit code == 0:
           SUCCESS -> Proceed to Stage & Commit.
    3. IF exit code != 0:
           Zero in on the first failing job.
           Document 4-part RCA in .lovable/memory/issues/XX-<slug>.md.
           Apply surgical fix to source code or python script.
           Re-verify with 03-cicd-local-runner.py.
           Repeat loop.
```

---

## STRICT AVOIDANCE: Never Disable CLI Linting or CI/CD Checks

> [!CAUTION]
> **TOTAL BAN ON DISABLING, SKIPPING, OR BYPASSING CLI LINTERS AND CI/CD GATES:**
>
> - **NEVER** disable, comment out, delete, or skip any CLI linting command (`golangci-lint`, `eslint`, `markdownlint`, `tsc`, `pytest`, `phpstan`, `mypy`, `check-*.py`), build step, or test suite.
> - **NEVER** add `|| true`, `continue-on-error: true`, `# nolint`, `// eslint-disable`, or ignore flags to "quickly win the race" or fake a pipeline pass.
> - **Your job is to legitimately fix the underlying source code and python scripts.** If resolving complex lint errors or test failures requires multiple sub-steps or nested self-looping turns, you MUST execute all necessary turns until the code is 100% clean and compliant.
> - Disabling or bypassing any CI/CD or CLI lint check is an automatic and immediate rejection.

---

## No Automatic Releases (Strict Policy)

> [!CAUTION]
> This prompt creates and verifies CI/CD infrastructure. You MUST NOT bump versions, update changelogs, or cut a release unless the user explicitly commands it in chat (e.g., "cut a release" or "bump the version"). All commits use `feat(ci): <description>` or `fix(ci): <description>`.

---

## Anti-Hallucination, Micro-Tasking, & Self-Looping

> [!CAUTION]
> **CRITICAL RULE: DO NOT ATTEMPT TO READ, PLAN, AND EXECUTE EVERYTHING AT ONCE.**
> If you try to consume a massive codebase and write all CI/CD pipelines in a single turn, you WILL hallucinate, drop requirements, and fail.

To survive massive checklists and complex codebases, you MUST operate using these three principles:

1. **Phase 1: Read & Understand (Isolated Loop):** Your very first action must be purely exploratory. Do NOT write code. Break down the task, read the specific files, trace the dependencies, and understand the architectural boundary. Once you understand the scope, end your turn and self-loop to begin execution.
2. **Phase 2: Bounded Micro-Tasking (Sequential Self-Looping):** Never attempt to execute the entire checklist in one response. Treat each checklist section or file as a strict, isolated boundary. Execute *only* the first small portion, verify it, end your turn, and self-loop to process the next portion.
3. **Phase 3: Multi-Agent Parallelization:** If tasks are independent, you MUST spawn dedicated sub-agents to handle them concurrently (up to 2-3 threads max). Give each sub-agent an extremely small, strictly defined bounding box (e.g., "Only write Python lint script for Go"). Never give a sub-agent a generic or multi-directory task.

---

## Pre-Reply / Loop Checklist (Must Verify Every Turn)

- [ ] **Specs Ingested:** Read `index.md` or `00-overview.md` and all subfiles across `spec/12-cicd-pipeline-workflows/` and `spec/02-coding-guidelines/06-cicd-integration/`.
- [ ] **Cross-Platform Python-First:** All automation, build, test, and linter scripts written in Python 3.
- [ ] **Local Runner Configured:** `.lovable/ai-fix-scripts/03-cicd-local-runner.py` created and tested with batching.
- [ ] **Workflows Generated:** `.github/workflows/ci.yml` and `.github/workflows/release.yml` created.
- [ ] **Zero Linting/CI/CD Bypass:** Confirmed NO linters, static analysis tools, or test scripts were disabled, commented out, or bypassed with `|| true`.
- [ ] **Local Runner 100% Green:** `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.
- [ ] **Strict Lowercase Filenames:** All generated files use strictly lowercase naming.
- [ ] **Stage, Commit & Push:** Grouped fixes into clean commit and pushed to remote branch.
