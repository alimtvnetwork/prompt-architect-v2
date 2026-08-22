Bump the MINOR version (MAJOR.MINOR.PATCH to MAJOR.(MINOR+1).0, PATCH resets to 0).

## Required release action

1. Update root `version.json` only: set `version` to the new MINOR version and `releaseDate` to today's UTC date.

## Publish trigger

2. If publishing is requested, create the matching `vX.Y.0` Git tag after the `version.json` change is present on the target branch. The tag triggers the release workflow.

Release trigger rule: the user phrase "bump version", "release", or old variants such as "bump version + add changelog + pin that version to root readme" means update `version.json` only unless publishing is explicitly requested. Do not edit `readme.md`, `changelog.md`, `manifest.json`, constants, instruction files, or fallback copies only to propagate a version. Do not run stale-version, version-sync, release-readiness, or asset-manifest checkers.

## Actionable Items & Checklist

- [ ] Read the overarching main task plan.
- [ ] Ensure the git repository starts completely clean.
- [ ] Complete all work on the current branch only.
- [ ] Ensure `.gitignore` explicitly excludes test reports, artifacts, and compiled binaries.
- [ ] Group all completed work into a single logical commit.
- [ ] Push the commit to the remote repository.

### Execution Checklist

- [ ] Discover current version from disk.
- [ ] Determine new version according to SemVer rules.
- [ ] Explicitly state previous and new version in the reply.
- [ ] Update version in standard files (e.g., `package.json`, `version.json`, etc.).
- [ ] **AVOID**: Do NOT touch or modify any files inside the `.gitmap` folder.
- [ ] Execute `git add .`
- [ ] Execute `git commit -m "chore(release): bump version to <new_version>"`
- [ ] Execute `git push`
- [ ] **AVOID**: Do NOT create a git tag (e.g., `git tag`). Tags are managed externally by Git Map.
