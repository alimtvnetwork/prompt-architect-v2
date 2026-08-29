---
name: ci-cd-create
description: >-
  Use this skill to autonomously design, create, and verify cross-platform Python CI/CD pipelines, linters, and workflows.
---

# Instruction (must follow): CI/CD Pipeline & Cross-Platform Python Automation Creation

Trigger Keywords & Aliases: `create-ci-cd`, `cicd-create`, `create cicd`, `setup cicd pipeline`, `build ci-cd pipeline`, `cicd create python`, `05-cicd-pipeline-create`

/goal Autonomously design, create, and verify complete cross-platform Python CI/CD pipelines, local runners, and GitHub Actions workflows by following specifications in `spec/12-cicd-pipeline-workflows/` and `spec/02-coding-guidelines/06-cicd-integration/`, maintaining a continuous N-step self-loop until all jobs exit code 0.

/learn Ingest `spec/12-cicd-pipeline-workflows/`, `spec/02-coding-guidelines/06-cicd-integration/`, `spec/11-powershell-integration/`, `spec/14-update/`, `spec/15-distribution-and-runner/`, `spec/16-generic-release/`, `spec/17-consolidated-guidelines/15-cicd-pipeline-workflows.md`, and `.lovable/coding-guidelines/coding-guidelines.md` before writing code.

---

## Variables — Configurable at Runtime

```text
N = 300  (Total self-loop steps budget)

PHASE_1_STEPS = N / 2  (Steps 1 .. 150: Spec Ingestion, Python Automation Design, Local Runner Setup)
PHASE_2_STEPS = N / 2  (Steps 151 .. 300: Workflow Generation, Python Linter Verification, Green Gate Loop)
```

---

## Cross-Platform Python-First Mandate

1. All CI/CD runners, linters, test harnesses, and build orchestrators MUST be written in **Python 3**.
2. Python ensures identical, deterministic execution across **Windows, Linux, and macOS**.
3. Shell scripts (`.sh`, `.ps1`) are only thin wrappers or used when strictly required by the host OS environment.
4. Linter scripts in `linter-scripts/` must be native Python scripts.

---

## STRICT AVOIDANCE: Never Disable CLI Linting or CI/CD Checks

> [!CAUTION]
> **TOTAL BAN ON DISABLING, SKIPPING, OR BYPASSING CLI LINTERS AND CI/CD GATES:**
>
> - **NEVER** disable, comment out, delete, or skip any CLI linting command (`golangci-lint`, `eslint`, `markdownlint`, `tsc`, `pytest`, `phpstan`, `mypy`, `check-*.py`), build step, or test suite.
> - **NEVER** add `|| true`, `continue-on-error: true`, `# nolint`, `// eslint-disable`, or ignore flags to fake a pipeline pass.
> - Disabling or bypassing any CI/CD or CLI lint check is an automatic and immediate rejection.

---

## End of Tunnel Checklist

- [ ] All CI/CD specs (`spec/12-cicd-pipeline-workflows/`, `spec/02-coding-guidelines/06-cicd-integration/`) read and followed.
- [ ] Python cross-platform runner `.lovable/ai-fix-scripts/03-cicd-local-runner.py` created and verified.
- [ ] All linters in `linter-scripts/` verified and passing without bypass.
- [ ] GitHub Actions workflows created in `.github/workflows/`.
- [ ] Local runner exited with code 0 on all jobs.
- [ ] All changes committed and pushed to remote repository.
