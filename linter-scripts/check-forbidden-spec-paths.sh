#!/usr/bin/env bash
# Thin cross-platform delegator to Python
exec python3 "$(dirname "$0")/check-forbidden-spec-paths.py" "$@" || exec python "$(dirname "$0")/check-forbidden-spec-paths.py" "$@"
