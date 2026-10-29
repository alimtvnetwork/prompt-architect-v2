# Recent session — 2026-10-29

This note records what was created and shipped on 2026-10-29. Paths below are relative git paths.

## go-email-reader

- Specifications for warm-up sequences 08 through 13 are in `02-spec/21-app/08-ui-and-warm-up-algorithm-improvements/` through `02-spec/21-app/13-ui-and-warm-up-algorithm-improvements/`.
- Plans are in `.ai-memory/plans/pending/08-ui-and-warm-up-algorithm-improvements.md` through `.ai-memory/plans/pending/13-ui-and-warm-up-algorithm-improvements.md`.
- Sequence 08 is the connector and gate map. Sequence 09 is brakes. Sequence 10 is the send lease and cool-down. Sequence 11 is the shadow compare. Sequence 12 is the pace envelope. Sequence 13 is the shared quiet window.
- The live tick now consults `internal/warmup/gatefeed.go`. A peer can tighten the remaining-send cap and cannot raise it. An absent or stale peer does not stop local warm-up. Local quiet hours hold. A quiet skip does not send. A dry run does not spend the cap. The gate order is health, cadence, connector, theme.
- The reader UI gate map reads `GET /api/warmup/gates`.
- Commit `f3864ee` is on `main` and is pushed. The remote uses SSH.
- Sequences 08 through 13 stay pending as catalogs. Only the gate engine is implemented.
- `user.email` is `local@gitmap`. The name is `gitmap automation`.

## gitmap-v28

- Cursor-like IDE setup landed in `cli/cmdide/ide_setup.go`, `cli/cmdide/setup/`, and `cli/cmdui/ui_server_ide_setup.go`.
- The spec is `02-spec/21-app/352-cursor-like-ide-setup-from-gitmap/`.
- Pushed commits include `3229df9b4`, `864012968`, and `04690b952`.
- `cli/cov` is a coverage profile and was not committed.

## repo-cache

- Commit `f474298` stores heatmap databases, including `.heatmap/06-cursor/go-email-reader/heatmap.db`.
- SQLite `-shm` and `-wal` sidecars were not committed.

## Push denied

These local commits are still unpushed because GitHub denied `alimtvnetwork`:

- `alim.karim.profile` (19 commits)
- `kubernetes-training-v1` (19 commits)
- `common-linux-installer` (1 commit)

## Rules learned

- Do not put a personal access token in a git remote URL. Use SSH.
- Do not commit coverage profiles or SQLite sidecar files.

## Last 30 commits in this repo

```text
03be798 updates
c0b3604 feat(prompts): upgrade read/write memory prompts with modern folder structure, skill/rule auto-generation, and release v1.39.0
0e54bd9 docs(readme): add author and lead architect section and release v1.38.0
e5df923 docs(readme): add author biography, origin story, and release v1.37.0
c97830f chore(release): bump version to v1.36.0 (migration to coding-guidelines)
a9e846b docs(cg-execute): add AI diagnostic guide, mandatory 5-8 file batching, and unstoppable self-loop protocol to style prompt
52cc493 docs(cg-execute): add Rule 2d for struct instantiations and sequential function calls, enforce 5-8 files micro-batching
c11af3d docs(cg-execute): add multiline map/loop spacing and extracted boolean condition examples to style and boolean prompts
feb8498 docs(guidelines): standardize boolean prefix statement to explicit is/has only acceptance phrasing
e477f55 docs(guidelines): enforce strictly is or has boolean prefixes across all prompts, skills, and specs
683b694 feat(cg-execute): add prompt 18 (Argument Reduction, Parameter Structs & Return Architecture)
1d17207 feat(cg-execute): add comprehensive Result[T] and AppError methods, type interrogation, and multi-language wrappers
b179612 style(prompts): standardize numbered checklists to N. [ ] format without redundant hyphens
5660215 feat(prompts): integrate continuous 2-agent auto-looping execution architecture and failure memory recovery
a94ffda docs(prompts): decompose compound tasks and multi-file ingestion into atomic numbered steps
b40502c docs(prompts): enforce unique topic-first first-word titles across all 98 prompts
7a9198f docs(prompts): standardize prompt titles with topic-first naming and version 2.1.0 synchronization metadata
d7b7d6b feat(cg-execute): add multi-line parameter and invocation formatting rules (Rule 9a/9b) to prompt 14
dbe3794 feat(cg-execute): add prompts 15 (TypeScript Types), 16 (Multi-Language Enums/Traits), and 17 (Terminal UI/Lipgloss)
519b13b feat(cg-execute): add 14-function-signatures-and-return-types.md prompt for Result[T] envelope and AppError enforcement
152a17c docs(memory-consolidate): add mandatory pre-consolidation timestamped backup branch protocol to 01-consolidate-completed-plans.md
a84feee docs: enrich 01-consolidate-completed-plans.md and 13-cli-commands-and-help.md with exhaustive checklists and nested subcommand examples
39c2656 docs(memory-consolidate): upgrade 01-consolidate-completed-plans.md with actionable checklists and resequencing architecture
71ce623 feat(cg-execute): add 13-cli-commands-and-help.md prompt and 06-cli-help-auditor.py script for CLI help parity
7c49228 feat(cg-execute): eliminate magic runes and expand 06-constants-and-enums.md with multi-language enum and trait patterns
3753036 docs(cg-execute): add strict LF line endings, UTF-8 no BOM, EOF trailing newline, and header spacing rules to style and hygiene prompts
a84ae68 docs(cg-execute): expand 10-style-guidelines.md with comprehensive multi-language before/after examples for newlines, line-gaps, and style rules
3cd4ba8 docs(cg-execute): enrich 10-style-guidelines.md with before/after newline and style gallery
c7ffd20 feat(cg-execute): add prompt 05-naming-conventions-and-boolean-prefixes.md, register 05-naming-autofixer.py, and update specs
1a58bba fix(ci-cd): migrate shell scripts to Python-first harness, create smoke_installer.py, and document RCA in memory
```
