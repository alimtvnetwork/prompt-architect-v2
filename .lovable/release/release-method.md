# Release Method Blueprint

This document defines exactly where and how versions are tracked and updated in this repository. Any AI performing a release MUST refer to this file to understand the architecture before modifying version strings.

## Versioning Scheme
The project follows Semantic Versioning (Major.Minor.Patch).
The **canonical** source of truth for the current version is ersion.json.

## Files Requiring Version Bumps
When a release occurs, the version string (both plain 1.X.X and prefixed 1.X.X) MUST be updated in the following explicit file paths. **Do NOT run global unbounded searches.**

- ersion.json
- package.json
- prompt-version.template.json
- eadme.md
- .lovable/coding-guidelines/coding-guidelines.md
- linter-scripts/validate-guidelines.go
- linter-scripts/validate-guidelines.py
- spec/14-update/28-worker-push-instruction.md
- spec/17-consolidated-guidelines/31-compiled-simple-coding-guidelines.md
- spec/19-main-worker-service/diagrams/seq-push-update.mmd
- spec/19-main-worker-service/10-worker-bootstrap-protocol.md
- spec/19-main-worker-service/14-rbac-and-status-seed.md
- spec/19-main-worker-service/15-tunable-constants.md
- spec/19-main-worker-service/16-update-channels.md
- spec/19-main-worker-service/25-inherited-rules.md

## Automation Script
The python script .lovable/release/bump_versions.py automates this process. It reads ersion.json, calculates the next semantic version, and safely applies regex replacements only to the files listed above.
