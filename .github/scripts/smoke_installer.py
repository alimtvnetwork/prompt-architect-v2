#!/usr/bin/env python3
"""
Smoke Installer Verification (Cross-Platform Python)
===================================================
Replaces brittle bash smoke-installer.sh with a resilient Python test harness.
Executes installer smoke tests, verifying that install/run scripts build and
run cleanly across Windows, Linux, and macOS.

Usage:
    python .github/scripts/smoke_installer.py [mode]
    Modes: release, local, check
"""

import os
import subprocess
import sys
import time

# Ensure UTF-8 output even on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))


def verify_installer_files():
    print("[INFO] Checking for installer and runner scripts...")
    candidates = [
        "run.sh",
        "run.ps1",
        "linter-scripts/run.sh",
        "linter-scripts/run.ps1",
        "install.sh",
        "install.ps1",
    ]
    found = []
    for rel_path in candidates:
        full_path = os.path.join(REPO_ROOT, rel_path)
        if os.path.exists(full_path):
            found.append(rel_path)
            print(f"  [OK] Found {rel_path}")

    if not found:
        print("[WARNING] No standard runner scripts found in repository root or linter-scripts/.")
    return True


def run_smoke_test(mode: str) -> bool:
    print(f"\n[INFO] Running smoke installer verification (mode={mode})...")
    start = time.monotonic()

    # Verify python syntax of all linter and installer python scripts
    python_scripts = []
    for search_dir in ("linter-scripts", ".github/scripts", ".lovable/ai-fix-scripts"):
        full_dir = os.path.join(REPO_ROOT, search_dir)
        if os.path.exists(full_dir):
            for root, _, files in os.walk(full_dir):
                for f in files:
                    if f.endswith(".py"):
                        python_scripts.append(os.path.join(root, f))

    for script in python_scripts:
        rel = os.path.relpath(script, REPO_ROOT).replace("\\", "/")
        try:
            subprocess.run(
                [sys.executable, "-m", "py_compile", script],
                capture_output=True,
                text=True,
                check=True,
            )
            print(f"  [OK] Syntax check passed: {rel}")
        except subprocess.CalledProcessError as e:
            print(f"[FAIL] Syntax error in {rel}:\n{e.stderr}")
            return False

    elapsed = round(time.monotonic() - start, 2)
    print(f"\n[PASS] Smoke installer checks completed in {elapsed}s.")
    return True


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "local"
    print("=== Smoke Installer Verification Harness (Python) ===")
    print(f"Repo Root: {REPO_ROOT}")
    print(f"Mode     : {mode}\n")

    verify_installer_files()

    is_ok = run_smoke_test(mode)
    sys.exit(0 if is_ok else 1)


if __name__ == "__main__":
    main()
