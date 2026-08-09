# Single Lowercase Readme

## Current state (verified)

The repo root now has exactly one readme, `readme.md` — both on disk and in git's tracked file list. The old uppercase `README.md` was already deleted. The duplicate you see is a stale editor tab pointing at the removed path, plus one remaining uppercase file elsewhere: `src/routes/README.md`.

## Root cause

Git and macOS/Windows filesystems disagree on case. `README.md` was renamed to `readme.md`, which on a case-insensitive filesystem looks like the same path, so editors and checkouts can show both the old and new entry until the tab/index refreshes. Mixing cases anywhere in the repo keeps re-triggering this.

## Fix

1. Confirm the root has only `readme.md` (no `README.md`) and keep it that way permanently.
2. Rename `src/routes/README.md` to `src/routes/readme.md` so no uppercase readme exists anywhere — this removes the recurring case-collision risk.
3. Merge the readme content into one compact root `readme.md`: entry-point pointers, folder structure, naming rules, prompt routing, prompt file format, supplied-file handling, and the app dev commands — trimmed, no repetition.
4. Add a "Readme casing — root cause" note to `.lovable/memory/prompt-library.md` and a one-line rule in the memory index: exactly one root readme, always lowercase `readme.md`, never create `README.md`, never keep both.
5. Update `.lovable/memory/what-to-read.md` if any path reference changes.

## Note for you

If your editor still shows a `README.md` tab after this, close it and reopen the file list — the file no longer exists in the repository.
