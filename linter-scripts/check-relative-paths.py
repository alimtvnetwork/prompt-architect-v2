#!/usr/bin/env python3
"""
Linter Script: check-relative-paths.py
======================================
Validates that repository files, markdown specs, plans, subtasks, and code comments
contain strictly relative Git root paths and zero absolute filesystem paths or file:/// URIs.

Invokes .lovable/ai-fix-scripts/04-relative-path-fixer.py in check mode.

Usage:
    python linter-scripts/check-relative-paths.py [--fix]
"""

import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
FIXER_PATH = os.path.join(REPO_ROOT, ".lovable", "ai-fix-scripts", "04-relative-path-fixer.py")


def main():
    if not os.path.exists(FIXER_PATH):
        print(f"[ERROR] Relative path fixer not found at {FIXER_PATH}")
        sys.exit(1)

    is_fix = "--fix" in sys.argv
    cmd = [sys.executable, FIXER_PATH]
    if not is_fix:
        cmd.append("--check")

    result = subprocess.run(cmd, cwd=REPO_ROOT)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
