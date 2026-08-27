Bump the PATCH version (MAJOR.MINOR.PATCH to MAJOR.MINOR.(PATCH+1)).

Only use this prompt when the user explicitly says "patch bump" or "patch release". Otherwise a release trigger defaults to MINOR.

## Required release action

1. Update root `version.json` only: set `version` to the new PATCH version and `releaseDate` to today's UTC date.

## Publish trigger

2. If publishing is requested, create the matching `vX.Y.Z` Git tag after the `version.json` change is present on the target branch. The tag triggers the release workflow.

## Mandatory Pinning & Changelog (Fatal if missed)

1. Changelog: You MUST read the `"changelog"` configuration from `version.json` (e.g. `file_path` and `format`) and append the proper changelog correctly according to that format.
2. Root README: You MUST pin the latest release version into the root `readme.md` file. It is FATAL if you do not update the version pins in the root README file!

You must update `version.json`, `changelog.md`, and `readme.md` at a minimum during any bump.

## Actionable Items & Checklist

- [ ] Read the overarching main task plan.
- [ ] Update version in `version.json`.
- [ ] Read `version.json` for Changelog formatting rules.
- [ ] Add the changelog properly to the targeted changelog file.
- [ ] Pin the latest version into the root `readme.md` file (FATAL IF MISSED).
- [ ] Ensure the git repository starts completely clean.
- [ ] Complete all work on the current branch only.
- [ ] Ensure `.gitignore` explicitly excludes test reports, artifacts, and compiled binaries.
- [ ] Group all completed work into a single logical commit.
- [ ] Push the commit to the remote repository.

### Execution Checklist

- Test File Ban: You MUST NOT read, scan, or modify test files (e.g., `*_test.*`, `*.spec.*`, `test/*`) when discovering or updating versions. Test files contain mock data, and updating mock data corrupts the tests.
- Release Architecture Memory: You must dynamically build a map of how the release works in this codebase (where the version lives, how it propagates) and write it to `.lovable/memory/release-architecture-map.md`. You must then enqueue this file inside `.lovable/memory/what-to-read.md` and link it in the root `readme.md`.
- [ ] Version Inheritance: If `version.json` contains components (e.g. `frontend`) set to `"inherit"`, DO NOT modify them. They automatically scale with the global version. Always bump the global root `"version"` property unless explicitly asked to bump a sub-component.
- [ ] Discover current version from disk.
- [ ] Determine new version according to SemVer rules.
- [ ] Explicitly state previous and new version in the reply.
- [ ] Update version in standard files (e.g., `package.json`, `version.json`, etc.).
- [ ] AVOID: Do NOT touch or modify any files inside the `.gitmap` folder.
- [ ] Execute `git add .`
- [ ] Execute `git commit -m "chore(release): bump version to <new_version>"`
- [ ] Execute `git push`
- [ ] AVOID: Do NOT create a git tag (e.g., `git tag`). Tags are managed externally by Git Map.
