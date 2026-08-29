# Instruction (must follow): Version Bump Docs Instruction

When instructed to bump the version in documentation:

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.

## 1. Search and Replace

- Find all instances of the old version number in the docs (e.g., `README.md`, `installation.md`).
- Update them to the new version number provided.

## 2. Changelog

- If asked, add a new section in `changelog.md` for the new version.
- Format: `## [Version] - YYYY-MM-DD`.

## Must Follow

Ensure consistency across all documentation files. Do not miss any version references in installation snippets or download links.

## Actionable Items & Checklist

- [ ] Read the overarching main task plan.
- [ ] Ensure the git repository starts completely clean.
- [ ] Complete all work on the current branch only.
- [ ] Ensure `.gitignore` explicitly excludes test reports, artifacts, and compiled binaries.
- [ ] Group all completed work into a single logical commit.
- [ ] Push the commit to the remote repository.

#

## Anti-Hallucination & Checklist Execution (Strict Sequential Self-Looping)

> [!CAUTION]
> **CRITICAL RULE: DO NOT ATTEMPT TO DO EVERYTHING AT ONCE.**
> You have massive checklists and strict architectural guidelines. If you try to execute all tasks in a single response, you WILL hallucinate, drop requirements, and fail the task. 

To solve this, you MUST operate using these two principles:

1. **Sequential Self-Looping:** Break the instructions down. Treat each checklist section or task as a completely separate execution step. Complete *only* the first section, verify it, end your turn, and self-loop (continue execution) to process the next checklist item one by one.
2. **Multi-Agent Parallelization:** To solve tasks faster, you are highly encouraged to spawn 2 or more sub-agents concurrently to handle independent tasks. If tasks are dependent on one another (e.g., sequential coding guideline audits), you must process them strictly one by one in your self-loop.

## Execution Checklist

- [ ] **Go Generate Sync:** If you modify Go constants, enums, or stringers, you MUST run `go generate ./...` in the relevant directory (e.g., `cd gitmap && go generate ./...`) and commit the resulting generated files to prevent CI drift.
- [ ] I have successfully pinned the new version in the root `readme.md` (FATAL IF MISSED).
- [ ] I have successfully updated the changelog.
- [ ] Discover current version from disk.
- [ ] Determine new version according to SemVer rules.
- [ ] Explicitly state previous and new version in the reply.
- [ ] Update version in standard files (e.g., package.json, version.json, etc.).
- [ ] AVOID: Do NOT touch or modify any files inside the .gitmap folder.
- [ ] Execute git add .
- [ ] Execute git commit -m 'chore(release): bump version to <new_version>'
- [ ] Execute git push
- [ ] AVOID: Do NOT create a git tag (e.g., git tag). Tags are managed externally by Git Map.
