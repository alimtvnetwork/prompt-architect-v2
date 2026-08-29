#!/usr/bin/env bash
# Thin cross-platform delegator to Python smoke_installer.py
exec python3 "$(dirname "$0")/smoke_installer.py" "$@" || exec python "$(dirname "$0")/smoke_installer.py" "$@"
