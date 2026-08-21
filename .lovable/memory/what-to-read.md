# What To Read

> Authoritative routing map indicating which file an AI must open for what purpose.
> Last updated: 2026-08-21T17:47:00Z

## Changelog

- 2026-08-21T17:47:00Z, Updated Read and Write prompt specifications: enforced autonomous self-looping across all spec folders and the entire codebase; mandated root readme lowercase verification with immediate auto-fix, git commit, and git push; added conversation spec memory capture, task consolidation rules, and detailed spec protection.

## Reading Map

| Need | Read |
| --- | --- |
| Authoritative reading order (this file) | `.lovable/memory/what-to-read.md` |
| How prompts are stored, named, routed and formatted | `.lovable/memory/prompt-library.md` |
| Master institutional knowledge index | `.lovable/memory/index.md` |
| Execution plans roll-up & pending plans | `.lovable/plans/index.md` and `.lovable/plans/pending/` |
| Repo folder structure overview & casing rules | `readme.md` (repo root) |
| The archived prompts themselves | `<category>-prompts/` (e.g., `01-general-prompts/`, `02-pwsh-prompts/`) |
| Canonical prompt registry | `.lovable/prompts.md` |
| The original prompt library specification | `01-general-prompts/01-prompt-library-setup/01-prompt-library-setup.md` |
| Coding guidelines / standards | `spec/02` or `01-general-prompts/02-coding-standards/01-coding-guidelines.md` |
| Error management / handling conventions | `spec/03` |
| Database conventions & schema rules | `spec/04` |
| App specification & feature requirements | `spec/21` |
| Assets and images | `assets/` |

## Non-negotiable rules

1. **Autonomous Self-Looping & Full Codebase Survey**: Before touching the project, autonomously loop through the whole codebase, root `readme.md`, entire `.lovable/` folder (especially `what-to-read.md`), and every single spec folder in `spec/` (`spec/21`, `spec/02`, `spec/03`, `spec/04`, etc.).
2. **Root `readme.md` Lowercase Enforcement**: Both Read and Write times must verify that the root readme is strictly named lowercase `readme.md`. If uppercase `README.md` exists or casing is incorrect, fix it immediately, commit, and push to git without asking.
3. **Write Memory & Spec Protection**: All session conversations and directives must be captured in `.lovable/memory/specs/` or `.lovable/memory/learned/`. While simple tasks may be consolidated into summaries, **detailed, important, and architectural specs MUST NEVER be consolidated, summarized, or truncated**.
4. **Prompt Archiving**: Follow `.lovable/memory/prompt-library.md` exactly: proofread only (remove filler words, keep exact wording) unless marked "keep as is" (body verbatim), add action items checklist, save under `<category>-prompts/` with two-digit sequence prefix, lowercase slug.
5. **Code Standards**: Read `spec/02`, `spec/03`, `spec/04` before writing any code. Error management must be followed (never swallow errors, always log operation name and key inputs). Code must be DRY.
6. **Naming & Casing**: Two-digit sequence, hyphen, lowercase slug. Exactly one lowercase root `readme.md`, never create `README.md`. Empty folders keep a `.gitkeep`.
