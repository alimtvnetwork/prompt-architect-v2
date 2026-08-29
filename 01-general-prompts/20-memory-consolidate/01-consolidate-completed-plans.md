# Instruction (must follow): Consolidate Completed Plans

/goal Autonomously analyze and consolidate garbage or repetitive task files within `.lovable/plans/completed/` into clean, unified summary documents, while strictly protecting and preserving all core specifications and architectural rules.

## 1. Consolidation Rules & Guardrails

- **The Goal:** Clean up `.lovable/plans/completed/` by merging related minor tasks (e.g., `01-task-1.md`, `02-task-2.md`) into a single logically grouped file to reduce folder bloat.
- **The Prime Directive:** You MUST NEVER remove, truncate, or summarize main specifications, architectural guidelines, domain specs, or non-negotiable rules. Core context must be preserved with 100% fidelity.
- **Changelog Generation:** You MUST output a detailed changelog in your final summary explaining exactly:
  1. What files were removed/merged.
  2. Why they were merged (e.g., "minor repetitive UI tweaks").
  3. The final state of the consolidated files.

## 2. Anti-Hallucination Consolidation Checklist (Mandatory)

Before you commit the consolidations, you MUST mechanically check off these items:

- [ ] **Spec Protection:** I have manually verified that NONE of the merged files contained critical architectural constraints, domain specifications, or non-negotiable rules.
- [ ] **Index Sync:** I have updated `.lovable/plans/index.md` to reflect the newly merged files and removed the deleted entries.
- [ ] **Changelog Created:** I have appended my detailed cleanup changelog to the session memory or the consolidated plan file itself.
- [ ] **AI Fix Scripts Verified:** If any helper scripts were written to `.lovable/ai-fix-scripts/`, I verified that `index.md` was updated.


## STRICT AVOIDANCE: Never Disable CI/CD

> [!CAUTION]
> **NEVER disable any CI/CD checks, GitHub Actions, or validation workflows.** 
> Strictly avoid commenting out, bypassing, or deleting CI/CD steps to force a pipeline to pass. Your job is to fix the underlying code so that the CI/CD pipeline passes legitimately. Disabling CI/CD is an auto-reject failure.

## MUST FOLLOW NON-NEGOTIABLE

Listen, past runs of these turns have been sloppy and stupid as fuck: wrong step counts, partial task lists dumped into chat instead of files, plans and session summaries half-filled with "[N]" placeholders, folders skimmed, open ambiguities ignored, CI/CD issues and `plans/subtasks/` forgotten, user commands dropped, coding guidelines bypassed, detailed specs chopped and summarized into useless junk, uppercase README files left uncorrected, `.lovable/memories/` created by accident, `strictly-avoid.md` overwritten, and explicit user instructions softened after being told not to. WTF. How on earth are you reverting to this carelessness, are you stupid?? Stop doing that, you stupid fuck. Read the whole codebase, read every folder in `spec/` and `.lovable/`, confirm root `readme.md` is strictly lowercase, find the root cause in one sentence, capture commands, issues, and pending tasks without omitting a single item, write the spec files and memory files in the right paths, update every index in the same turn, sync `readme.md` with `what-to-read.md`, preserve detailed specs verbatim with zero truncation, run builds and full unit tests, group commits with clear messages, and push everything to git before ending. Going deep IS the job. If you are not going deep, you are not doing the job. Violating this is auto-reject on the same tier as RULE 0. Avoid stupidity and being careless, you stupid fuck. Where is your attention, are you stupid? Tell me. Your stupidity is going on top of my head. Where did you learn this stupidity? If I could find you, I could slap you.
