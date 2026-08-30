# Repository Guide (Transition Notice: Moving to Coding Guidelines)

> [!IMPORTANT]
> **REPOSITORY STATUS: MIGRATION & TRANSITION TO `coding-guidelines`**
>
> Active development, maintenance, and the authoritative versions of all prompts, coding standards, and AI runbooks have **moved to the `coding-guidelines` meta-repository**.
>
> Work in this repository (`prompt-architect`) is now finalized. To adopt or sync the latest prompts, coding standards, and automation scripts, refer directly to the `coding-guidelines` repository.

One readme only, always lowercase `readme.md`. Never create `README.md`.

## AI entry point

1. `.lovable/memory/what-to-read.md` — routing table: which file to read for what.
2. `.lovable/memory/prompt-library.md` — full prompt storage and formatting rules.
3. `01-general-prompts/             library of all general reusable prompts
  00-folder-structure/          prompts regarding folder layout
  01-prompt-library-setup/      prompts for setting up prompt indexing and architecture
  02-core-workflow/             general lifecycle prompts (initial unified prompt, plan/next steps)
  03-read-write/                canonical Read Memory & Write Memory prompts
  04-coding-standards/          actual master coding guidelines and theming rules
  05-coding-guidelines/         prompts for auditing/executing against guidelines
  06-testing-and-qa/            prompts for unit tests, code coverage, issues
  07-bug-fix/                   prompts for fixing specific issues
  08-dry-code/                  prompts enforcing DRY code
  09-commit-and-multi-agent-code-fix/ prompts for commit fixes and git history cleanups
  10-ui-and-design/             prompts for UI components, SVG, logo creation
  11-content-and-seo/           prompts for README, SEO, social media, jokes
  12-old-plan-prompts/          archive of legacy planning prompts
  13-plan-audit/                prompts for auditing specs and generating strict plans
  14-execute/                   prompts for pending task execution & self-looping agents
  15-cg-execute/                prompts for coding guideline execution suite
  16-prompt-engineering/        prompts for proofreading and prompt creation
  17-ci-cd/                     prompts for CI/CD workflow & script fixes
  18-release-management/        prompts for version bumps and releases
  19-insults/                   consolidated unsoftened stance and enforcement texts
  20-memory-consolidate/        prompts for safe memory & completed plans consolidation
  21-old-execute-prompts/       archive of legacy execution prompts
  22-ai-fix-script-prompts/     prompts for reusable AI automation tools
02-pwsh-prompts/                PowerShell specific prompts
<project-name>-prompts/         prompts that name a project
  01-<prompt-slug>.md
.agents/                        Antigravity Skills & Rules for progressive disclosure
  skills/                       modular runbook skills for the AI
assets/                         images and assets supplied with prompts
spec/                           specifications (hyphenated: spec/<NN>-<slug>/)
  01-spec-authoring-guide/      spec authoring standards
  02-coding-guidelines/         coding standards & rules
  03-error-manage/              error management conventions
  04-database-conventions/      database schema & query rules
  21-app/                       app domain specifications & routes
.lovable/                       configuration, memory, and indexes
  ai-fix-scripts/               Automated scripts (e.g. 02-guideline-autofixer.py)
  memory/                       what-to-read.md, prompt-library.md, naming-conventions.md
  temp-scripts/                 scratch space for automation scripts (gitignored)
  temp-agents/                  scratch space for active sub-agent states (gitignored)
  release/                      automation scripts for git releases
  prompts.md                    canonical index of all saved prompts
agents.md                       global configuration rules for Antigravity agents
readme.md                       this file
src/                            application code

```

*(Note: Spec folder sequence numbers and placements follow `spec/<NN>-<slug>/` but can switch between projects; AI agents dynamically discover and read all nested markdown files).*

## Naming rules

- Two-digit sequence + hyphen + lowercase slug: `01-prompt-library-setup.md`.
- Lowercase and hyphens only — no spaces, uppercase or camelCase.
- All readme files are lowercase `readme.md`, and the root has exactly one.
- Every empty folder keeps a `.gitkeep`.

## Where a prompt goes

- Project name mentioned -> `<project-name>-prompts/<NN>-<slug>.md`.
- General reusable prompt -> `01-general-prompts/<NN>-<category>/<slug>.md`.
- Read and Write memory prompts belong strictly in `01-general-prompts/03-read-write/`.
- Use the next free sequence number when generating a new category or new project folder.
- All prompts must be indexed in `.lovable/prompts.md` per the canonical prompt architecture.

## Prompt file format

Proofread only: remove filler words, keep the exact wording. Sections in order:

1. `## Prompt` — the proofread text.
2. `## Action Items — Must Follow (Non-Negotiable)` — checklist of every stated rule.
3. `## Folder Structure` — only if discussed.
4. `## Database` — only if discussed.
5. `## Before Writing Code` — code prompts only: read `spec/02-coding-guidelines/`, `spec/03-error-manage/`, `spec/04-database-conventions/`; error management must be followed; code must be DRY.

If the user says to keep a prompt as is, store the body verbatim — only the checklist
section may be enhanced (formatting, phase grouping, sharper wording; never drop a rule).

## Supplied files and links

Assets/images -> `assets/`. Specs -> `spec/` (app spec in `spec/21-app/`). Ask if unclear.

## 📖 About Prompt Architect & Why It Was Invented

Prompt Architect was created by **[Md. Alim Ul Karim](https://alimkarim.com/)** out of a deep and relatable frustration: while modern AI coding assistants are immensely powerful, software engineers were spending an exhausting amount of time **babysitting, hand-holding, and constantly correcting AI agents** instead of focusing on high-level system architecture and solving core business problems.

Left unconstrained, AI coding models frequently:
- **Produce compressed, dense code** that skips necessary vertical line gaps around control structures (`if`, `for`, `return`) and parameter struct instantiations.
- **Hallucinate completion** by running superficial checks or creating planning documents without refactoring actual source code files.
- **Scatter magic literals and loose booleans** across the codebase instead of using type-safe enums (`*Type`) and affirmative prefixes (`is`, `has`).
- **Swallow errors or return raw generic tuples** `(T, error)` instead of structured, predictable `Result[T]` envelopes and contextual `*AppError` wrappers.
- **Overload function signatures** with 4–6 loose arguments instead of clean, value-based parameter structs.

### How Prompt Architect Empowers Software Engineers

Prompt Architect bridges the gap between AI speed and enterprise-grade software engineering standards. It provides a complete meta-framework of:
1. **Deterministic, Self-Looping AI Runbooks:** Guides agents through structured phases (Phase 1: Deep Inventory & Spec Writing, Phase 2: Parallel Batch Execution) with strict 5–8 file micro-batching to prevent context exhaustion and hallucination.
2. **Ironclad Cross-Language Coding Standards:** Enforces zero nested `if` statements (flattened to depth 0), implicit positive booleans (`is`/`has` ONLY), single return types, <= 8–15 line function caps, and clean Git diff readability.
3. **Automated AI Quality Gates & Autofixers:** Pre-packaged with Python linters and autofixers (`.lovable/ai-fix-scripts/`) that automatically verify and repair formatting, line endings, error codes, and relative paths.
4. **Complete Multi-Language Error & Envelope System:** Production-grade `Result[T]` and `*AppError` implementations across Go, TypeScript, Python, PHP, C#, and Rust.

---

## 👤 Author & Lead Architect

**Md. Alim Ul Karim**  
*Creator & Lead Architect • Chief Software Engineer • Top 1% Crossover Status*

- 🌐 **Personal Website:** [alimkarim.com](https://alimkarim.com/)
- 💼 **LinkedIn:** [linkedin.com/in/alimkarim](https://www.linkedin.com/in/alimkarim)
- 💻 **Stack Overflow:** [stackoverflow.com/users/513511/md-alim-ul-karim](https://stackoverflow.com/users/513511/md-alim-ul-karim)
- 🔍 **Google Profile:** [Alim Ul Karim on Google](https://www.google.com/search?q=Alim+Ul+Karim)

Alim is a veteran system architect with 20+ years of professional software engineering experience across enterprise systems, fintech, distributed cloud infrastructures, and developer tooling. His core philosophy — **consistency over cleverness, convention over configuration, and deterministic constraints over manual babysitting** — is the foundational bedrock behind Prompt Architect and the `coding-guidelines` ecosystem.

---

## Installation & Import

You can instantly import the Prompt Architect directly into your own codebase using our automated scripts. The scripts will download the prompts into `.lovable/prompts` (or a folder of your choice) and track the version in `prompt-version.json`.

**Using PowerShell (Windows):**
```powershell
# Import the latest version
Invoke-Expression "& { $(Invoke-RestMethod https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/install.ps1) }"

# Import a specific version into a specific folder
Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/install.ps1 -OutFile install.ps1
.\install.ps1 -TargetDir ".lovable/prompts" -Version "v1.38.0"
```

**Using Bash (macOS/Linux):**
```bash
# Import the latest version
curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/install.sh | bash

# Import a specific version into a specific folder
curl -sO https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/install.sh
chmod +x install.sh
./install.sh ".lovable/prompts" "v1.38.0"
```


### Git Map / CT CLI Integration

If you are using the `git map` ecosystem or a `ct` CLI wrapper, you can embed this installation seamlessly into your toolchain as `ct install-prompts`.

Example CLI wrapper implementation (Node.js/Bash/PowerShell):

1. Create a `ct install-prompts` command.
2. The command should detect the host OS.
3. If Windows, spawn: `Invoke-Expression "& { $(Invoke-RestMethod https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/install.ps1) }"`
4. If macOS/Linux, spawn: `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/install.sh | bash`
5. The install script will automatically populate your repository's `version.json` with the rich `promptArchitectByRiseupAsia` metadata block containing the imported file mappings and author attributions.

## Prompt Library Reference

Below is a complete list of all prompts available in the `01-general-prompts` directory. You can view them directly on GitHub or copy the raw markdown text.

| Category / Prompt | Description / Usage | View in Repo | Raw URL |
|---|---|---|---|
| **00-folder-structure**<br>`01-canonical-folder-structure.md` | 01 Canonical Folder Structure | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/00-folder-structure/01-canonical-folder-structure.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/00-folder-structure/01-canonical-folder-structure.md) |
| **01-prompt-library-setup**<br>`01-prompt-library-setup.md` | 01 Prompt Library Setup | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/01-prompt-library-setup/01-prompt-library-setup.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/01-prompt-library-setup/01-prompt-library-setup.md) |
| **02-core-workflow**<br>`01-next-steps.md` | 01 Next Steps | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/02-core-workflow/01-next-steps.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/02-core-workflow/01-next-steps.md) |
| **02-core-workflow**<br>`02-pending-tasks.md` | 02 Pending Tasks | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/02-core-workflow/02-pending-tasks.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/02-core-workflow/02-pending-tasks.md) |
| **02-core-workflow**<br>`05-unified-ai-prompt-v4.md` | 05 Unified Ai Prompt V4 | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/02-core-workflow/05-unified-ai-prompt-v4.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/02-core-workflow/05-unified-ai-prompt-v4.md) |
| **03-read-write**<br>`01-write-antigravity.md` | 01 Write Antigravity | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/03-read-write/01-write-antigravity.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/03-read-write/01-write-antigravity.md) |
| **03-read-write**<br>`02-read-memory-enhanced.md` | 02 Read Memory Enhanced | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/03-read-write/02-read-memory-enhanced.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/03-read-write/02-read-memory-enhanced.md) |
| **03-read-write**<br>`03-write-memory.md` | 03 Write Memory | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/03-read-write/03-write-memory.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/03-read-write/03-write-memory.md) |
| **04-coding-standards**<br>`01-coding-guidelines.md` | 01 Coding Guidelines | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/04-coding-standards/01-coding-guidelines.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/04-coding-standards/01-coding-guidelines.md) |
| **04-coding-standards**<br>`02-theming-guidelines.md` | 02 Theming Guidelines | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/04-coding-standards/02-theming-guidelines.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/04-coding-standards/02-theming-guidelines.md) |
| **04-coding-standards**<br>`03-update-theming.md` | 03 Update Theming | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/04-coding-standards/03-update-theming.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/04-coding-standards/03-update-theming.md) |
| **05-coding-guidelines**<br>`01-plan-coding-guideline-audit.md` | 01 Plan Coding Guideline Audit | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/05-coding-guidelines/01-plan-coding-guideline-audit.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/05-coding-guidelines/01-plan-coding-guideline-audit.md) |
| **05-coding-guidelines**<br>`02-execute-coding-guideline-fix.md` | 02 Execute Coding Guideline Fix | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/05-coding-guidelines/02-execute-coding-guideline-fix.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/05-coding-guidelines/02-execute-coding-guideline-fix.md) |
| **05-coding-guidelines**<br>`03-cg-audit-gap-n-steps.md` | 03 Cg Audit Gap N Steps | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/05-coding-guidelines/03-cg-audit-gap-n-steps.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/05-coding-guidelines/03-cg-audit-gap-n-steps.md) |
| **06-testing-and-qa**<br>`01-autonomous-qa-and-testing-v4.md` | 01 Autonomous Qa And Testing V4 | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/06-testing-and-qa/01-autonomous-qa-and-testing-v4.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/06-testing-and-qa/01-autonomous-qa-and-testing-v4.md) |
| **09-commit-and-multi-agent-code-fix**<br>`01-boolean-improvements.md` | 01 Boolean Improvements | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/09-commit-and-multi-agent-code-fix/01-boolean-improvements.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/09-commit-and-multi-agent-code-fix/01-boolean-improvements.md) |
| **09-commit-and-multi-agent-code-fix**<br>`02-execute-pending-tasks.md` | 02 Execute Pending Tasks | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/09-commit-and-multi-agent-code-fix/02-execute-pending-tasks.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/09-commit-and-multi-agent-code-fix/02-execute-pending-tasks.md) |
| **09-commit-and-multi-agent-code-fix**<br>`03-commit-fix-v2.md` | 03 Commit Fix V2 | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/09-commit-and-multi-agent-code-fix/03-commit-fix-v2.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/09-commit-and-multi-agent-code-fix/03-commit-fix-v2.md) |
| **09-commit-and-multi-agent-code-fix**<br>`04-execute-pending-tasks-v2.md` | 04 Execute Pending Tasks V2 | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/09-commit-and-multi-agent-code-fix/04-execute-pending-tasks-v2.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/09-commit-and-multi-agent-code-fix/04-execute-pending-tasks-v2.md) |
| **09-commit-and-multi-agent-code-fix**<br>`05-boolean-improvements-v2.md` | 05 Boolean Improvements V2 | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/09-commit-and-multi-agent-code-fix/05-boolean-improvements-v2.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/09-commit-and-multi-agent-code-fix/05-boolean-improvements-v2.md) |
| **09-commit-and-multi-agent-code-fix**<br>`06-insult-code-fix.md` | 06 Insult Code Fix | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/09-commit-and-multi-agent-code-fix/06-insult-code-fix.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/09-commit-and-multi-agent-code-fix/06-insult-code-fix.md) |
| **09-commit-and-multi-agent-code-fix**<br>`07-clean-artifacts-and-git-history.md` | 07 Clean Artifacts And Git History | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/09-commit-and-multi-agent-code-fix/07-clean-artifacts-and-git-history.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/09-commit-and-multi-agent-code-fix/07-clean-artifacts-and-git-history.md) |
| **10-ui-and-design**<br>`01-logo-create.md` | 01 Logo Create | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/10-ui-and-design/01-logo-create.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/10-ui-and-design/01-logo-create.md) |
| **10-ui-and-design**<br>`02-react-ui-fixes-update.md` | 02 React Ui Fixes Update | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/10-ui-and-design/02-react-ui-fixes-update.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/10-ui-and-design/02-react-ui-fixes-update.md) |
| **10-ui-and-design**<br>`03-svg-logo.md` | 03 Svg Logo | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/10-ui-and-design/03-svg-logo.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/10-ui-and-design/03-svg-logo.md) |
| **11-content-and-seo**<br>`01-jokes-ideas-generate.md` | 01 Jokes Ideas Generate | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/11-content-and-seo/01-jokes-ideas-generate.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/11-content-and-seo/01-jokes-ideas-generate.md) |
| **11-content-and-seo**<br>`02-lowercase-readme-and-sequence.md` | 02 Lowercase Readme And Sequence | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/11-content-and-seo/02-lowercase-readme-and-sequence.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/11-content-and-seo/02-lowercase-readme-and-sequence.md) |
| **11-content-and-seo**<br>`03-seo-optimization.md` | 03 Seo Optimization | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/11-content-and-seo/03-seo-optimization.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/11-content-and-seo/03-seo-optimization.md) |
| **11-content-and-seo**<br>`04-social-media-post.md` | 04 Social Media Post | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/11-content-and-seo/04-social-media-post.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/11-content-and-seo/04-social-media-post.md) |
| **11-content-and-seo**<br>`05-update-readme.md` | 05 Update Readme | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/11-content-and-seo/05-update-readme.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/11-content-and-seo/05-update-readme.md) |
| **12-old-plan-prompts**<br>`01-plan-maximum-enforcement.md` | 01 Plan Maximum Enforcement | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/12-old-plan-prompts/01-plan-maximum-enforcement.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/12-old-plan-prompts/01-plan-maximum-enforcement.md) |
| **12-old-plan-prompts**<br>`03-plan-steps.md` | 03 Plan Steps | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/12-old-plan-prompts/03-plan-steps.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/12-old-plan-prompts/03-plan-steps.md) |
| **12-old-plan-prompts**<br>`04-plan-steps-by-groups.md` | 04 Plan Steps By Groups | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/12-old-plan-prompts/04-plan-steps-by-groups.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/12-old-plan-prompts/04-plan-steps-by-groups.md) |
| **12-old-plan-prompts**<br>`05-plan-maximum-enforcement-v5.md` | 05 Plan Maximum Enforcement V5 | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/12-old-plan-prompts/05-plan-maximum-enforcement-v5.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/12-old-plan-prompts/05-plan-maximum-enforcement-v5.md) |
| **12-old-plan-prompts**<br>`06-plan-spec-steps.md` | 06 Plan Spec Steps | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/12-old-plan-prompts/06-plan-spec-steps.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/12-old-plan-prompts/06-plan-spec-steps.md) |
| **13-plan-audit**<br>`01-inventory-pending-tasks.md` | 01 Inventory Pending Tasks | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/13-plan-audit/01-inventory-pending-tasks.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/13-plan-audit/01-inventory-pending-tasks.md) |
| **13-plan-audit**<br>`02-plan-spec-steps-v2.md` | 02 Plan Spec Steps V2 | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/13-plan-audit/02-plan-spec-steps-v2.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/13-plan-audit/02-plan-spec-steps-v2.md) |
| **13-plan-audit**<br>`03-audit-app-spec.md` | 03 Audit App Spec | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/13-plan-audit/03-audit-app-spec.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/13-plan-audit/03-audit-app-spec.md) |
| **13-plan-audit**<br>`04-fix-spec-from-audit.md` | 04 Fix Spec From Audit | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/13-plan-audit/04-fix-spec-from-audit.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/13-plan-audit/04-fix-spec-from-audit.md) |
| **14-execute**<br>`01-execute-pending-tasks.md` | 01 Execute Pending Tasks | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/14-execute/01-execute-pending-tasks.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/14-execute/01-execute-pending-tasks.md) |
| **14-execute**<br>`02-execute-parent-task-with-n-steps.md` | 02 Execute Parent Task With N Steps | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/14-execute/02-execute-parent-task-with-n-steps.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/14-execute/02-execute-parent-task-with-n-steps.md) |
| **14-execute**<br>`03-execute-batched-loop.md` | 03 Execute Batched Loop | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/14-execute/03-execute-batched-loop.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/14-execute/03-execute-batched-loop.md) |
| **15-cg-execute**<br>`01-index.md` | 01 Index | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/15-cg-execute/01-index.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/15-cg-execute/01-index.md) |
| **15-cg-execute**<br>`02-error-management.md` | 02 Error Management | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/15-cg-execute/02-error-management.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/15-cg-execute/02-error-management.md) |
| **15-cg-execute**<br>`03-nested-if-and-guard-clauses.md` | 03 Nested If And Guard Clauses | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/15-cg-execute/03-nested-if-and-guard-clauses.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/15-cg-execute/03-nested-if-and-guard-clauses.md) |
| **15-cg-execute**<br>`04-booleans-and-complex-conditions.md` | 04 Booleans And Complex Conditions | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/15-cg-execute/04-booleans-and-complex-conditions.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/15-cg-execute/04-booleans-and-complex-conditions.md) |
| **15-cg-execute**<br>`05-constants-and-enums.md` | 05 Constants And Enums | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/15-cg-execute/05-constants-and-enums.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/15-cg-execute/05-constants-and-enums.md) |
| **15-cg-execute**<br>`06-data-and-schema.md` | 06 Data And Schema | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/15-cg-execute/06-data-and-schema.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/15-cg-execute/06-data-and-schema.md) |
| **15-cg-execute**<br>`07-react-frontend-guidelines.md` | 07 React Frontend Guidelines | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/15-cg-execute/07-react-frontend-guidelines.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/15-cg-execute/07-react-frontend-guidelines.md) |
| **15-cg-execute**<br>`08-code-hygiene.md` | 08 Code Hygiene | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/15-cg-execute/08-code-hygiene.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/15-cg-execute/08-code-hygiene.md) |
| **15-cg-execute**<br>`09-style-guidelines.md` | 09 Style Guidelines | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/15-cg-execute/09-style-guidelines.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/15-cg-execute/09-style-guidelines.md) |
| **15-cg-execute**<br>`10-testing-and-coverage.md` | 10 Testing And Coverage | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/15-cg-execute/10-testing-and-coverage.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/15-cg-execute/10-testing-and-coverage.md) |
| **16-prompt-engineering**<br>`01-conversation-log.md` | 01 Conversation Log | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/16-prompt-engineering/01-conversation-log.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/16-prompt-engineering/01-conversation-log.md) |
| **16-prompt-engineering**<br>`02-proofread.md` | 02 Proofread | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/16-prompt-engineering/02-proofread.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/16-prompt-engineering/02-proofread.md) |
| **17-ci-cd**<br>`01-ci-cd-fix.md` | 01 Ci Cd Fix | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/17-ci-cd/01-ci-cd-fix.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/17-ci-cd/01-ci-cd-fix.md) |
| **17-ci-cd**<br>`02-cicd-run-ps1.md` | 02 Cicd Run Ps1 | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/17-ci-cd/02-cicd-run-ps1.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/17-ci-cd/02-cicd-run-ps1.md) |
| **17-ci-cd**<br>`03-fix-ci-cd-and-run-scripts.md` | 03 Fix Ci Cd And Run Scripts | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/17-ci-cd/03-fix-ci-cd-and-run-scripts.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/17-ci-cd/03-fix-ci-cd-and-run-scripts.md) |
| **17-ci-cd**<br>`04-ci-cd-fix-with-release.md` | 04 Ci Cd Fix With Release | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/17-ci-cd/04-ci-cd-fix-with-release.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/17-ci-cd/04-ci-cd-fix-with-release.md) |
| **17-ci-cd**<br>`05-cicd-pipeline-create.md` | 05 Cicd Pipeline Create | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/17-ci-cd/05-cicd-pipeline-create.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/17-ci-cd/05-cicd-pipeline-create.md) |
| **18-release-management**<br>`01-major-bump.md` | 01 Major Bump | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/18-release-management/01-major-bump.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/18-release-management/01-major-bump.md) |
| **18-release-management**<br>`02-minor-bump.md` | 02 Minor Bump | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/18-release-management/02-minor-bump.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/18-release-management/02-minor-bump.md) |
| **18-release-management**<br>`03-patch-bump.md` | 03 Patch Bump | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/18-release-management/03-patch-bump.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/18-release-management/03-patch-bump.md) |
| **18-release-management**<br>`04-release.md` | 04 Release | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/18-release-management/04-release.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/18-release-management/04-release.md) |
| **18-release-management**<br>`05-version-bump-docs.md` | 05 Version Bump Docs | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/18-release-management/05-version-bump-docs.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/18-release-management/05-version-bump-docs.md) |
| **19-insults**<br>`01-raw-insults.md` | 01 Raw Insults | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/19-insults/01-raw-insults.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/19-insults/01-raw-insults.md) |
| **19-insults**<br>`02-consolidated-insults-v2.md` | 02 Consolidated Insults V2 | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/19-insults/02-consolidated-insults-v2.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/19-insults/02-consolidated-insults-v2.md) |
| **20-memory-consolidate**<br>`01-consolidate-completed-plans.md` | 01 Consolidate Completed Plans | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/20-memory-consolidate/01-consolidate-completed-plans.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/20-memory-consolidate/01-consolidate-completed-plans.md) |
| **21-old-execute-prompts**<br>`02-execute-robust-loop.md` | 02 Execute Robust Loop | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/21-old-execute-prompts/02-execute-robust-loop.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/21-old-execute-prompts/02-execute-robust-loop.md) |
| **21-old-execute-prompts**<br>`04-fix-subtask-naming-convention.md` | 04 Fix Subtask Naming Convention | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/21-old-execute-prompts/04-fix-subtask-naming-convention.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/21-old-execute-prompts/04-fix-subtask-naming-convention.md) |
| **22-ai-fix-script-prompts**<br>`01-python-file-manipulator.md` | 01 Python File Manipulator | [View](https://github.com/alimtvnetwork/prompt-architect-v2/blob/main/01-general-prompts/22-ai-fix-script-prompts/01-python-file-manipulator.md) | [Raw Text](https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/01-general-prompts/22-ai-fix-script-prompts/01-python-file-manipulator.md) |

---

## 👤 Author & Lead Architect

**Md. Alim Ul Karim**  
*Creator & Lead Architect • Chief Software Engineer • Top 1% Crossover Status*

- 🌐 **Personal Website:** [alimkarim.com](https://alimkarim.com/)
- 💼 **LinkedIn:** [linkedin.com/in/alimkarim](https://www.linkedin.com/in/alimkarim)
- 💻 **Stack Overflow:** [stackoverflow.com/users/513511/md-alim-ul-karim](https://stackoverflow.com/users/513511/md-alim-ul-karim)
- 🔍 **Google Profile:** [Alim Ul Karim on Google](https://www.google.com/search?q=Alim+Ul+Karim)

Alim is a veteran system architect with 20+ years of professional software engineering experience across enterprise systems, fintech, distributed cloud infrastructures, and developer tooling. His core philosophy — **consistency over cleverness, convention over configuration, and deterministic constraints over manual babysitting** — is the foundational bedrock behind Prompt Architect and the `coding-guidelines` ecosystem.

