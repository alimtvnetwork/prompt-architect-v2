# Instruction (must follow): Version Bump Docs Instruction

When instructed to bump the version in documentation:

## 1. Search and Replace

- Find all instances of the old version number in the docs (e.g., `README.md`, `installation.md`).
- Update them to the new version number provided.

## 2. Changelog

- If asked, add a new section in `CHANGELOG.md` for the new version.
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

### Execution Checklist

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
