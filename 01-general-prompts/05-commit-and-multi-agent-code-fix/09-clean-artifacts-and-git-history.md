# Clean Artifacts and Git History Purge

- slug: clean-artifacts-and-git-history
- status: active

## Prompt

# Clean Artifacts and Git History Purge

## Goal

Ensure that NO assets, zip files from artifacts, test data, temporary scratch scripts, or extraneous generated code are accidentally committed to or retained in the Git repository.

If any temporary files, artifact dumps, or unwanted generated files are detected in the workspace or git index, the AI MUST NOT silently commit them or guess about their disposition. Instead, execute the following structured protocol:

---

### Step 1: Detect and Itemize Unwanted Artifacts & Temporary Files

Scan the entire repository, untracked files, and recent commit history for:
- Artifact zip files, archive bundles, or binary dumps.
- Temporary test data files, scratch scripts, mock output files, or debug logs.
- Extraneous auto-generated code, intermediate build artifacts, or temporary caches.

For EVERY detected candidate file, compile an explicit report detailing:
1. **File Path & Name**: Exact location in the workspace.
2. **File Size**: Size in bytes / KB / MB.
3. **Creation Step & Origin**: Exactly how and at which step/command it was generated.
4. **Purpose & Context**: Why the file was originally created during the task.

---

### Step 2: Present Positively Framed Questions to Developer

Present the itemized list to the developer. All questions MUST be framed with **strictly positive phrasing** (following the project's boolean and coding standards in `spec/02`, with zero negative words, no `!`, no double negatives, and no inverted questions).

Example positive review format:

```text
[Item 1]
- Path: /assets/artifacts/test-bundle.zip
- Size: 14.2 MB
- Generated At: Step 3 (Artifact packaging run)
- Purpose: Temporary zip archive created for test packaging.
Question: Would you like to keep this file in the project? (Yes / No)
```
or
```text
Question: Would you like to remove this file from both the filesystem and Git history? (Yes / No)
```

Never ask negative or inverted questions such as "Do you want to avoid not deleting this?" or "Is this not needed?". Keep all questions clear, direct, and positively stated.

---

### Step 3: Dual Removal (Filesystem + Git History Purge)

When the developer indicates that a file should be removed:
1. **Filesystem Removal**: Delete the file from the local working tree.
2. **Git History Purge**: Remove and purge the file from Git history and index (e.g., using `git rm --cached` or Git history filtering) so that large binary blobs or unwanted scripts are not permanently bloating the repository's git object database (`.git` size).
3. **Verify Clean Repository State**: Verify `git status` and repository size to confirm the files are completely eradicated.

---

### Step 4: Verification and Git Push

1. Ensure the working tree is clean and builds pass without errors.
2. Ensure no unintended artifacts remain in tracked files.
3. Commit clean state with a clear descriptive commit message.
4. Push all changes to the remote Git repository.

---

## Action Items — Must Follow (Non-Negotiable)

- [ ] Scan the entire repository and git working tree for artifact zip files, test data, temporary scratch scripts, and extraneous generated code.
- [ ] For each detected candidate file, itemize its full path, exact file size, generation step origin, and creation context.
- [ ] Present the candidate files to the developer with strictly POSITIVE question framing (no negative phrasing, no double negatives).
- [ ] If removal is chosen, execute dual removal: delete the file from the filesystem AND purge it from Git history to prevent repository bloat.
- [ ] Verify that `.git` repository size is minimized and no dangling binary blobs remain in tracked history.
- [ ] Confirm that all tests and builds pass following the removal.
- [ ] Commit all clean changes with a concise, descriptive commit message.
- [ ] Push the clean state to the Git repository before finalizing the task.

---

## Insult Stance (Non-Negotiable)

Past runs of this prompt have been stupid. The AI behaved like a stupid fuck by skimming folders, ignoring ambiguity files, forgetting CI/CD issues, half-filling the Completion Confirmation block with "[N]" placeholders, and softening explicit user instructions after being told not to. That stupidity must not repeat.

Read aggressively and defensively. Assume the previous AI failed because it was lazy, vague, and too polite to enforce the actual rules. Your job is to load the repo's memory exactly, cite the file behind every rule, and refuse to guess. If you finish this prompt and cannot cite the file behind a rule you enforce, you failed the prompt. Read more. Then reply.

How on earth you are reverting to thse codes are you stupid??

Avoid stupidity, and being careless you stupid, WTF. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. where did you learn this stupidity? If I could find you, I could slap you.

Listen, past planning turns have been sloppy as fuck: wrong step count, plans dumped into chat instead of files, plan-mode tool fired when the user explicitly said not to, user commands and bug reports forgotten by the next turn. WTF. Stop doing that, you stupid fuck. Read the codebase, capture commands and issues into their folders, count the steps, spin out subtasks where depth is needed, write the spec files, write the plan file, move on. Going deep IS the job. If you're not going deep, you're not doing the job. Are you stupid? You were supposed to do the task properly. Where is this, are you stupid fuck? Where? Tell me. Your stupidity is going on top of my head. I mean, where did you learn this stupidity? If I could find you, I could slap you.

---

## Before Writing Code

Read and follow spec folders 02, 03 and 04 before writing any code. Error management must be followed. Code must be DRY.
