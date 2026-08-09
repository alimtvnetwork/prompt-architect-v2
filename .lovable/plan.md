# Store the "Read Memory (Enhanced)" prompt

Archive the pasted prompt next to the write-memory prompt, in the same folder, following the existing prompt-library rules.

## What gets created

One new file:

```text
01-prompts/01-general/03-read-write/02-read-memory-enhanced.md
```

Contents, in this order:

1. `# Read Memory (Enhanced)` title, with `slug: read-memory-enhanced` and `status: active` metadata lines, matching `01-write-antigravity.md`.
2. `## Prompt` — the pasted text stored VERBATIM. No proofreading, no filler removal, no softening of tone, nothing reordered or dropped.
3. `## Actionable Items & Checklist and non-negotiable must follow` — the trailing checklist restructured into execution phases (pre-flight reads, phase-by-phase reading order, anti-hallucination contract, memory update protocol, completion confirmation, code standards, delivery). Every rule preserved, none invented.
4. `## Folder Structure` — the `.lovable/` and `spec/` layout referenced by the prompt.
5. `## Before Writing Code` — standard footer: read `spec/02`, `spec/03`, `spec/04`; error management must be followed; code must be DRY.

## Note on the folder number

`01-general/` already has `03-dry-code/`, so `03-read-write/` is a second folder using the `03` prefix. It was created that way on your explicit instruction last turn and this file goes in the same place. Renumbering to `06-read-write/` is a separate one-line change if you want the sequence clean.

## Not in scope

No code changes, no commits, no other files touched.
