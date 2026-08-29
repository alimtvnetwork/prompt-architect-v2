# Root Cause Analysis (RCA): Shell-to-Python CI/CD & Smoke Installer Migration

## Incident Overview

- **Timestamp:** 2026-08-29
- **Failed Job:** `Run bash .github/scripts/smoke-installer.sh release`
- **Failing Command Signature:**
  ```text
  Run bash .github/scripts/smoke-installer.sh release
    bash .github/scripts/smoke-installer.sh release
    shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
  ```
- **Resolution:** Replaced standalone `.sh` shell scripts with cross-platform Python scripts (`smoke_installer.py`, `check-axios-version.py`, `check-forbidden-spec-paths.py`, `check-runner-dispatch-antipatterns.py`).

---

## 4-Part Root Cause Analysis

### 1. Symptom

In GitHub Actions pipelines, running `bash .github/scripts/smoke-installer.sh release` failed with unexpected exit codes under the runner's default shell execution (`/usr/bin/bash --noprofile --norc -e -o pipefail`).

### 2. Root Cause

1. **Shell Script Brittleness & Non-Portability:** Shell scripts (`.sh`) assume a POSIX environment and frequently break across operating systems (especially Windows GitHub runner VMs where Git-Bash/MSYS2 path translation `C:\` vs `/c/` causes silent failures).
2. **Pipefail Fragility (`-e -o pipefail`):** In bash, minor subshell warnings, pipe commands, or environment variable checks exit with non-zero codes, causing CI pipelines to abort abruptly without informative diagnostic error messages.
3. **Execution Permissions & Shell Invocation Mismatches:** Windows runners often fail on executable bits (`chmod +x`), requiring awkward `bash script.sh` overrides that behave inconsistently with local environments.

### 3. Permanent Fix

1. **Python-First Automation:** Rewrote `.github/scripts/smoke_installer.py` (and all linter scripts in `linter-scripts/`) in **Python 3**, ensuring identical execution semantics across Windows, Linux, and macOS.
2. **UTF-8 Output Encoding:** Configured `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` to eliminate `UnicodeEncodeError` on Windows `cp1252` terminal consoles.
3. **Thin Wrapper Compatibility:** Kept `.sh` files as 2-line delegators that forward arguments to `python script.py`, ensuring backwards compatibility for any external tools.

### 4. Prevention & Strictly Avoided Anti-Patterns

- **NEVER** write standalone complex CI/CD quality gates, linter rules, or smoke testers in Bash/Shell scripts.
- **ALWAYS** implement automation in Python 3 (`.py`), using standard library tools (`os`, `subprocess`, `sys`, `json`).
- **ALWAYS** wire GitHub Actions workflows to execute `python <script>.py` directly.
