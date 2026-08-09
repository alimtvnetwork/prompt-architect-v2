# What To Read

Start here. This file tells any AI which file to open for what.

| Need | Read |
| --- | --- |
| How prompts are stored, named, routed and formatted | `.lovable/memory/prompt-library.md` |
| Repo folder structure overview | `readme.md` (repo root) |
| The archived prompts themselves | `<category>-prompts/` (e.g., `01-general-prompts/`, `02-pwsh-prompts/`) |
| The original prompt library specification | `01-general-prompts/01-prompt-library-setup/01-prompt-library-setup.md` |
| Coding guidelines / error management / mandatory rules | `spec/02`, `spec/03`, `spec/04` |
| App specification | `spec/21` |
| Assets and images | `assets/` |

## Non-negotiable rules

1. When the user gives a prompt to store ("next prompt", "proofread prompt", or any
   prompt handed over for archiving), follow `.lovable/memory/prompt-library.md`
   exactly: proofread only (remove filler words, keep the exact wording), add the
   action-item checklist, add folder-structure and database sections only when those
   were discussed, save under the respective `<category>-prompts/` folder, then commit.
2. Before writing any code, read `spec/02`, `spec/03` and `spec/04`. Error management
   must be followed. Code must be DRY.
3. Naming everywhere: two-digit sequence, hyphen, lowercase slug. Readme files are
   lowercase `readme.md`. Empty folders keep a `.gitkeep`.
