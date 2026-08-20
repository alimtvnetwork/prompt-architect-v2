# Store Two Prompts: Commit & Multi-Agent Code Fix

## New category folder

`01-prompts/01-general/05-commit-and-multi-agent-code-fix/`

Existing general categories are `01-prompt-library-setup`, `02-bug-fix`, `03-dry-code`, `04-coding-guidelines`, so this takes the next free sequence, `05`.

## Files

```text
01-prompts/01-general/05-commit-and-multi-agent-code-fix/
  01-commit-fix.md
  02-boolean-improvements.md
```

## Content rules for these two files

- The prompt body is stored **verbatim** — no proofreading, no filler-word removal, no rewording, no reordering, nothing added or removed above the checklist.
- Only the "Actionable Items & Checklist and non-negotiable must follow" section is enhanced: turned into a proper markdown checklist, deduplicated where a line is literally repeated, and each item sharpened into an unambiguous instruction an AI can act on (explicit verbs, explicit targets). No rule is dropped and no new rule is invented.
- Each file gets an `## Enhanced Checklist Notes` marker only if needed to explain grouping; otherwise the checklist keeps the original heading text.

## Checklist enhancements applied to both files

Group the items so the AI executes in order, while keeping every original line:

- Pre-flight: fix git status, write the task/spec into `.lovable`, enqueue tasks.
- Planning: big plan, self-loop, spawn sub-agents and run them in parallel.
- Investigation: find and record the root cause in memory and `.lovable`.
- Standards: aspect-folder code review guidelines, error-manage logging on every catch,
  query wrapper for PHP/Python/TS, no magic strings/numbers except logging,
  enums instead of string unions, all enum names end with `Type`,
  explicit `isFail` instead of `!isSuccess`, DRY and reused constants.
- Verification: local build, CI/CD, full unit test pass.
- Delivery: grouped commits with good messages, push every commit, minor release bump
  following this repo's release guidelines, git as source of truth.

## Also updated

- `readme.md` and `.lovable/memory/prompt-library.md` gain one line: prompts explicitly
  marked "keep as is" are stored verbatim; only the checklist may be enhanced.
