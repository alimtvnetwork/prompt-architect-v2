# What To Read

> Authoritative routing map indicating which file an AI must open for what purpose.
> Last updated: 2026-08-22T03:16:00Z

## Changelog

- 2026-08-22T03:16:00Z, Consolidated pending tasks architecture to `.lovable/plans/pending/` with strict `01-` two-digit sequence prefixes, eradicated legacy `.lovable/spec/tasks/` references, and enforced anti-hallucination verification protocols.
- 2026-08-21T18:20:00Z, Preserved and structured all Read & Write prompts in `01-general-prompts/03-read-write/` (`01-write-antigravity.md`, `02-read-memory-enhanced.md`, `03-write-memory.md`).

## Reading Map

| Need | Read |
| --- | --- |
| Authoritative reading order (this file) | `.lovable/memory/what-to-read.md` |
| How prompts are stored, named, routed and formatted | `.lovable/memory/prompt-library.md` |
| Master institutional knowledge index | `.lovable/memory/index.md` |
| Execution plans roll-up & pending plans | `.lovable/plans/index.md` and `.lovable/plans/pending/` |
| Repo folder structure overview & casing rules | `readme.md` (repo root) |
| Authoritative Write Memory (Antigravity) prompt | `01-general-prompts/03-read-write/01-write-antigravity.md` |
| Authoritative Read Memory prompt | `01-general-prompts/03-read-write/02-read-memory-enhanced.md` |
| Standard Write Memory prompt | `01-general-prompts/03-read-write/03-write-memory.md` |
| Canonical prompt registry | `.lovable/prompts.md` |
| The original prompt library specification | `01-general-prompts/01-prompt-library-setup/01-prompt-library-setup.md` |
| Pending tasks read-only scan & inventory | `01-general-prompts/07-execute/04-inventory-pending-tasks.md` |
| Continuous loop & multi-agent execution | `01-general-prompts/07-execute/01-execute-pending-tasks.md` |
| Resilient 3-agent maximum execution loop | `01-general-prompts/07-execute/02-execute-robust-loop.md` |
| Coding guidelines / standards | `spec/02-coding-guidelines/` or `01-general-prompts/02-coding-standards/01-coding-guidelines.md` |
| Error management / handling conventions | `spec/03-error-manage/` |
| Database conventions & schema rules | `spec/04-database-conventions/` |
| App specification & feature requirements | `spec/21-app/` |
| Artifact detection & Git history purge | `01-general-prompts/05-commit-and-multi-agent-code-fix/09-clean-artifacts-and-git-history.md` |
| Unified MUST FOLLOW NON-NEGOTIABLE enforcement text (V2) | `01-general-prompts/09-insults/02-consolidated-insults-v2.md` |
| Raw insults compilation (V1) | `01-general-prompts/09-insults/01-raw-insults.md` |
| Assets and images | `assets/` |

## Non-negotiable rules

1. **Authoritative Read & Write Location**: Read Memory and Write Memory prompts live in `01-general-prompts/03-read-write/` (`01-write-antigravity.md`, `02-read-memory-enhanced.md`, `03-write-memory.md`).
2. **Autonomous Self-Looping & Full Codebase Survey**: Before touching the project, autonomously loop through the whole codebase, root `readme.md`, entire `.lovable/` folder (especially `what-to-read.md`), and every single spec folder in `spec/` (`spec/01-spec-authoring-guide/`, `spec/02-coding-guidelines/`, `spec/03-error-manage/`, `spec/04-database-conventions/`, `spec/21-app/`, etc.), reading and listing all pending tasks.
3. **Single Canonical Pending Tasks Queue & Sequential Numbering**: All active execution plans and pending tasks are consolidated strictly under `.lovable/plans/pending/01-<slug>.md` (with two-digit sequence prefixes `01-`, `02-`, `03-`) and `.lovable/plans/subtasks/01-<slug>/01-<subslug>.md`. The legacy `.lovable/spec/tasks/` path is eliminated.
4. **Anti-Hallucination & Clarifying Questions**: If files, specs, or requirements are missing or ambiguous, the AI MUST NOT guess, assume, or invent rules. It must stop and ask clarifying questions or file an open question in `01-new-ambiguity/01-<slug>.md` before proceeding.
5. **Root `readme.md` Lowercase Enforcement**: Both Read and Write times must verify that the root readme is strictly named lowercase `readme.md`. If uppercase `README.md` exists or casing is incorrect, fix it immediately, commit, and push to git without asking.
6. **Artifact Cleanup & Git History Purge**: Prevent artifact zips, test data, temporary scripts, and unwanted code from bloating the repository. Present candidate files with positive question framing, and on removal execute dual removal (filesystem + Git history purge).
7. **Write Memory & Spec Protection**: All session conversations and directives must be captured in `.lovable/memory/specs/` or `.lovable/memory/learned/`. While simple tasks may be consolidated into summaries, **detailed, important, and architectural specs MUST NEVER be consolidated, summarized, or truncated**.
8. **Prompt Archiving**: Follow `.lovable/memory/prompt-library.md` exactly: proofread only (remove filler words, keep exact wording) unless marked "keep as is" (body verbatim), add action items checklist, save under `<category>-prompts/` with two-digit sequence prefix, lowercase slug.
9. **Code Standards**: Read `spec/02-coding-guidelines/`, `spec/03-error-manage/`, `spec/04-database-conventions/` before writing any code. Error management must be followed (never swallow errors, always log operation name and key inputs). Code must be DRY.
10. **Naming & Casing**: Two-digit sequence, hyphen, lowercase slug. Exactly one lowercase root `readme.md`, never create `README.md`. Empty folders keep a `.gitkeep`.

