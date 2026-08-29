# Strictly Avoided Patterns & Anti-Patterns Memory

This document is the authoritative registry of strictly avoided mistakes, anti-patterns, and fragile configurations discovered across CI/CD and coding tasks.

## 1. Shell Script Brittleness in CI/CD (RCA: 2026-08-29)

- **Anti-Pattern:** Writing complex smoke installers, test runners, or linter quality gates in `.sh` Bash scripts (e.g. `bash .github/scripts/smoke-installer.sh release`).
- **Why It Fails:** Shell scripts fail under `bash -e -o pipefail`, break across Windows and Linux GitHub runner VMs due to path separators (`\` vs `/`), and suffer from permission mismatches.
- **Strict Rule:** ALWAYS implement CI/CD scripts, linters, and installer verifications in **Python 3** (`.py`) with standard library utilities.

## 2. Total Ban on Absolute Paths & `file:///` URIs

- **Anti-Pattern:** Writing hardcoded system paths (e.g., `D:\...`, `C:\...`, `/home/...`) or `file:///` URIs in plans, subtasks, specs, memory logs, or code comments.
- **Why It Fails:** Destroys portability and breaks markdown cross-references across team members and CI runners.
- **Strict Rule:** ALL repository references and links MUST use strictly relative paths starting from the Git root.

## 3. Total Ban on Explicit True Checks & Mixed Polarity

- **Anti-Pattern:** `if isReady == true` or `if isA && !isB`.
- **Strict Rule:** Evaluate positive booleans implicitly: `if isReady { ... }`.

## 4. Total Ban on Disabling CI/CD

- **Anti-Pattern:** Bypassing, commenting out, or deleting linter/test steps to force a pipeline to pass.
- **Strict Rule:** Fix the underlying code so that CI/CD passes legitimately.
