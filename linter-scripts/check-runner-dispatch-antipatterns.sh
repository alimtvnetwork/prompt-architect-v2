#!/usr/bin/env bash
# Thin cross-platform delegator to Python
exec python3 "$(dirname "$0")/check-runner-dispatch-antipatterns.py" "$@" || exec python "$(dirname "$0")/check-runner-dispatch-antipatterns.py" "$@"
