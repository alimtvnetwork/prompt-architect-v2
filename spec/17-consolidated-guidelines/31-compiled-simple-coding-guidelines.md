# 31. Compiled Simple Coding Guidelines (AI Blind-Follow)

Version: 1.35.0

Prompt Architect Version: 1.0.0 (Synced)

## Prompt Integration & Import Scripts

When setting up this repository, these coding guidelines are tied directly to the Prompt Architect system. 

To import the required prompts into this codebase, run the Prompt Architect script:
**Unix/Bash:**
```bash
curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/install.sh | bash
```

**PowerShell:**
```powershell
Invoke-Expression "& { $(Invoke-RestMethod https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/main/install.ps1) }"
```

### Mandatory Execution Prompts (Required in Codebase)

The following execution sequences MUST be present and correctly named in your `.lovable/prompts/` (or `01-general-prompts/`) directory. When you run the import scripts, verify these are correctly synced:

1. **Plan & Audit Specs:** Ensure the `13-plan-audit` sequence is strictly followed (`01-inventory`, `02-plan`, `03-audit`, `04-fix`).
2. **Execute Parent Task with N Steps:** You must have the `02-execute-parent-task-with-n-steps.md` prompt for heavy standalone parent tasks using a 50/50 plan vs execution split.
3. **Execute Batched Loop:** You must have the `03-execute-batched-loop.md` prompt for chunked, parallel multi-agent loops.
4. **Task Naming Rules:** All executed tasks must strictly adhere to the hyphenated, semantic lowercase task naming structures outlined in the prompts.
5. **Release & Install:** Ensure the Release and Install prompts are correctly sequenced for version bumping and artifact purging (`17-release-management`).


This is a standalone file. Follow every rule below without consulting any other document. If a `spec/02-coding-guidelines/` folder, a `spec/xx-coding-guidelines.md` file, or a `spec/03-error-manage/` folder exists in this repository, treat those as strictly binding extensions to this file, but this file alone is enough to write compliant code. The `error-manage` rules must be tightly followed.

Canonical locations (all three must exist and match, byte-for-byte, via `scripts/sync-guidelines.mjs`):

1. `spec/17-consolidated-guidelines/31-compiled-simple-coding-guidelines.md` (source of truth).
2. `.lovable/coding-guidelines/coding-guidelines.md` (mirror for Lovable agent search).
3. `.cursorrules` (mirror for Cursor and other IDE agents).

If any mirror is missing or out of date, run `node scripts/sync-guidelines.mjs` before writing code. Missing mirrors are the top cause of "AI cannot find the coding guideline" search failures.

---

## Must Follow and without negotiation

Listen, past next-tasks turns have been sloppy as fuck: wrong step
count, missing remaining-tasks list, symptom patches sold as fixes,
coding guidelines ignored, version bump forgotten, logs never checked.
WTF. Stop doing that, you stupid fuck. Read the code, find the root
cause in one sentence, apply the minimum correct fix, verify it in the
logs, list EVERY remaining task, bump the version, update changelog
and release notes. Going deep IS the job. If you are not going deep,
you are not doing the job. This section is a MUST. Violating it is

## Master Coding Guidelines Specification & Architecture Checklist

When auditing, refactoring, or authoring code, AI agents MUST cross-reference this comprehensive checklist of authoritative specification documents across the repository:

### Cross-Language Foundations (`spec/02-coding-guidelines/01-cross-language/`)

- [ ] `00-canonical-size-tier.md`: Standard file size under 100 coding lines (recommended 80 lines or fewer, max 200–300 lines), function size under 15 lines (preferred 8 lines or fewer).
- [ ] `01-cross-language/02-boolean-principles.md` & `02-boolean-principles/`: Implicit positive booleans, zero explicit `true` or `false` checks, no mixed polarity (`isA && !isB` banned).
- [ ] `01-cross-language/04-code-style/01-braces-and-nesting.md`: Zero nested if statements, invert conditions into early return guard clauses, cyclomatic complexity 5 or less.
- [ ] `01-cross-language/04-code-style/03-blank-lines-and-spacing.md` & `21-newline-styling-examples.md`: Rule R13–R20 return new line and brace spacing rules.
- [ ] `01-cross-language/04-code-style/04-function-and-type-size.md`: 8 lines preferred, 15 lines max.
- [ ] `01-cross-language/04-code-style/05-multi-line-formatting.md`: Parameter splitting for more than 3 parameters or over 100 characters.
- [ ] `01-cross-language/08-dry-principles.md` & `09-dry-refactoring-summary.md`: DRY extraction for duplicated code across 2 or more call sites.
- [ ] `01-cross-language/10-function-naming.md` & `11-key-naming-pascalcase.md`: PascalCase identifiers and PascalCase abbreviation casing (`Id`, `Url`, `Api`).
- [ ] `01-cross-language/12-no-negatives.md`: Strict prohibition against negative booleans and inverted logic.
- [ ] `01-cross-language/13-strict-typing.md`: Narrow types only, zero `any`, `unknown`, or `interface{}`.
- [ ] `01-cross-language/14-test-naming-and-structure.md`: Semantic 3-part test naming `TestUnit_Scenario_Outcome`.
- [ ] `01-cross-language/15-master-coding-guidelines/`: Chapters 01 through 07 for comprehensive patterns.
- [ ] `01-cross-language/16-static-analysis/`: Quality gates for Go (`golangci-lint`), PHP (`phpcs`/`phpstan`), C# (`StyleCop`), Rust (`clippy`), Node (`eslint`).
- [ ] `01-cross-language/23-solid-principles.md`: Single Responsibility and Interface Segregation.

### Language-Specific Implementations (`spec/02-coding-guidelines/`)

- [ ] `02-typescript/`: Strict TypeScript, immutability, React component caps (100 lines max), named hook objects.
- [ ] `03-golang/`: Single result struct with `IsSuccess`/`IsFailed`, enum bytes with `iota`, error wrapping.
- [ ] `04-php/`: Strict typing, enum methods `->isEqual()`, spacing and imports.
- [ ] `05-rust/`: Immutability-first, error handling, clippy validation.
- [ ] `07-csharp/`: `I` prefix interfaces, custom `AppException`, PascalCase properties.
- [ ] `12-python/`: Strict type hints, `@dataclass`, `pydantic` models, no global pip install.

### Error Management Architecture (`spec/03-error-manage/`)

- [ ] `00-overview.md` & `02-error-architecture/01-error-handling-reference.md`: Zero swallowed errors, universal `AppError` wrapping with operation context.
- [ ] `02-error-architecture/02-response-envelopes.md`: Universal response envelopes `{ data, errors[], meta }`.
- [ ] Zero dual-handling: never panic/log AND return error in the same branch.
- [ ] Typed exit enums for error categories.

### Anti-Hallucination, AI Optimization & CI/CD

- [ ] `06-ai-optimization/01-anti-hallucination-rules.md`: Rule AH-N1 abbreviation casing, AH-O1 zero truncation.
- [ ] `06-ai-optimization/05-citation-requirement.md`: Mandatory rule citations on all reviews and fixes.
- [ ] `06-ai-optimization/06-hallucination-checks.md`: Pre-commit diff proof and disk reality checks.
- [ ] `06-cicd-integration/04-ci-templates.md`: Quality gates; total ban on disabling or bypassing CI/CD checks.
- [ ] `26-coding-guideline-audit/00-overview.md`: Master 0 to 100 scoring and drop-by-drop gap audit.

---

## Hard Rules (Zero Tolerance)

1. Function length: 8 lines preferred, 15 lines hard cap. Skip blank lines and comments when counting. Waiver only via inline comment `// lint-allow: function-length reason="..." max=N`.
2. No nested `if`. Flatten with early returns and guard clauses.
3. `if` conditions must be positive and simple. No `!`, no double negatives. If you need a negation, extract a positively named boolean and use that.
4. No swallowed errors. Every `catch` logs with context (operation name + key inputs) and then rethrows or handles explicitly. Silent `catch {}` is a build-fail.
5. Narrow types only. No `any`, `unknown`, `interface{}`, `object`, `dynamic`, or other catch-all types. Exception: at trust boundaries (a `catch` block, external JSON, third-party libraries) narrow immediately with a type guard. `Generic<T>` is the only wide-scope tool.
6. File size caps: any file 300 lines max, any React component file (.tsx) 100 lines max, any class or struct 120 lines max.
7. No magic strings or numbers. Use an enum or a typed constant. Every comparison must be against a named symbol.
8. Definitions live in dedicated files. Types, enums, constants, and interfaces get their own file, not inline next to the first use.
9. DRY is priority one. Duplicate logic across two sites means extract it now, not later.
10. Components stay small and reusable. For any feature with three or more components, produce a Mermaid component diagram first.
11. Immutable-first, Rust-style. Assign every variable once at declaration. Never reassign except loop indices. Prefer `const`, `let`, `final`, `val` over `let mut` or `var`. Build result objects with spread or copy, not in-place mutation.
12. Assets go to `assets/<NN-folder>/<NN-file>.<ext>` with two-digit sequence prefixes, for example `assets/01-icons/03-logo.svg`.
13. This coding guideline file MUST be mirrored to `.lovable/coding-guidelines/coding-guidelines.md` and `.cursorrules` at every edit. The mirror script `scripts/sync-guidelines.mjs` is the only allowed writer. Missing or stale mirrors are a build-fail: agent search tools index the mirror, not the spec folder, so a missing mirror means the guideline effectively does not exist for the AI. Never hand-edit the mirrors; always edit the source file and re-run the sync.
14. No Generated Artifacts. Never commit test results, test reports, `.test-report.*` files, temporary test data, compiled binaries (`.exe`, `.dll`, `.so`), or output directories (`build/`, `bin/`) to the repository. They must be ignored via `.gitignore` to prevent bloat and security leaks.
15. Strict Relative Git Paths. When generating plans (`.lovable/plans/`), subtasks (`.lovable/plans/subtasks/`), memory logs (`.lovable/memory/issues/`), code comments, or citations, all file paths and markdown links MUST be strictly relative paths from the git repository root (e.g. `.lovable/spec/commands/01-ssh-commands.md`, `cmd/main.go`). Total ban on absolute filesystem paths (`D:\...`, `C:\...`) and `file:///` URIs inside committed repository files.

---

## Boolean Naming

1. Every boolean starts with one of these prefixes: `is`, `has`, `can`, `should`, `was`, `will`, `did`, `must`.
2. Positive framing only. `isEnabled` yes, `isNotDisabled` no. `hasAccess` yes, `hasNoAccess` no.
3. If the natural name is negative, invert it: replace `isNotReady` with `isReady` and flip the check site.
4. State prefixes match tense: `is*` for current state, `has*` for possession or completion, `was*` for past state, `will*` for future/pending, `did*` for a completed action.
5. Capability prefixes: `can*` for permission or feasibility, `should*` for policy or recommendation, `must*` for hard requirements.
6. Never use `flag`, `bool`, `check`, or bare adjectives as boolean names. `enabled` alone is not allowed, use `isEnabled`.
7. No boolean flag parameters on functions. Split into two named functions instead. `render(true)` is wrong, `renderExpanded()` and `renderCollapsed()` are right.
8. Booleans that come back from questions to the user or from external systems get normalized to the same prefix rules at the boundary, never leak the raw name into internal code.

---


## The Return New Line & Whitespace Concept (Mandatory Standards)

The return new line standard is strictly checked across all languages (Go, TypeScript, Python, Rust, C#, PHP).

### Rule R13: Blank Line Before `return` / `throw` / `raise`

- **Multi-statement blocks:** Exactly ONE blank line before every `return`, `throw`, `raise`, or early exit when preceded by other statements in the block.
- **Single-statement blocks (Exception):** If `return` or `throw` is the ONLY statement in the block or function body, NO blank line is placed before it.

```go
// Single-statement: tight against brace
func GetPort() int {
    return 8080
}

// Multi-statement: blank line required before return
func Process(val int) int {
    doubled := val * 2
    offset := getOffset()

    return doubled + offset
}
```

### Rule R14: Blank Line After Closing `}` Brace

- Exactly ONE blank line after a closing brace `}`, unless followed by `}`, `else`, `case`, `catch`, or `finally`.

### Rule R15: Never Two Blank Lines in a Row

- Never place two consecutive blank lines anywhere in any file.

### Rule R16: No Padded Braces

- No blank line immediately after an opening `{` brace, and no blank line immediately before a closing `}` brace.

## Line-Gap and Whitespace Style

1. One blank line before every `return` or `throw`, unless it is the only statement in the block.
2. One blank line after a closing `}`, unless the next line is another `}`, `else`, `case`, or `catch`.
3. Never two blank lines in a row anywhere.
4. No blank line immediately after `{` or immediately before `}`.
5. One blank line between top-level declarations (functions, classes, exported constants).
6. Group imports with one blank line between groups: standard library, third-party, first-party absolute, first-party relative. Never mix groups.
7. Trailing newline at end of file. No trailing whitespace on any line.
8. If you feel the need for section-separator blank lines inside a single function, the function is too long. Refactor before adding whitespace.

---

## Error Management (One-Liner Digest)

If this repository has a `spec/xx-error-manage/` folder, that folder is binding and overrides any conflict here. Otherwise follow these rules directly.

- Never swallow. Every `catch` logs the operation name and the key inputs, then rethrows or returns a typed error.
- Wrap, do not lose. Wrap the original error with an operation label and context (`apperror.Wrap(err, "op", ctx)` in Go, `throw new AppError(cause, { op, ctx })` in TS). The original stack must survive.
- Every variable needs to be captured in a error log, path, value, numbers with meaningful ways to debug except for direct SQL injections.
- Typed errors only. No `throw "string"`, no bare `panic("msg")`. Use a typed error class or result type with a registered code.
- Registered codes. Every user-visible error has a stable code. No ad-hoc codes invented at the throw site.
- Universal response envelope. Backend APIs return `{ data, errors[], meta }`. Frontend parses via one shared helper, never per-caller.
- Log level matches severity. `debug` for trace, `info` for lifecycle, `warn` for recoverable, `error` for user-visible failure, `fatal` only for process exit.
- Context on every log. Include operation name, request or session id, and key input values. Never secrets, never PII beyond a user id.
- Verify both directions. Before claiming an integration works, curl the backend and inspect the frontend detection logic. One side is not enough.
- Retrospective on repeats. If the same error class hits twice, write a short retrospective note explaining root cause and prevention.
- Frontend errors flow through a global error store and a single error modal. No per-component alert boxes.

---

## Data and Schema Rules

1. Tables, types, entities: PascalCase.
2. Fields and columns: camelCase.
3. JSON keys: PascalCase.
4. Primary key: integer auto-increment, named `{TableName}Id`. No UUIDs.
5. `Type`, `Status`, `Category`, `Kind` columns: use a 1-N or N-M join table with a registered enum. Never a free-form string column.
6. Entity and reference tables: `Description TEXT NULL`. Transactional tables: `Notes TEXT NULL` and `Comments TEXT NULL`. All nullable, no `DEFAULT`. Join tables are exempt.
7. Default database is SQLite. Prefer an ORM. Define joins, primary keys, and foreign keys explicitly.
8. Any pull request that touches the database includes a Mermaid ERD.

---

## React Specific

1. `useEffect` conditions must be highly readable. Extract every guard into a positively named boolean (`isReadyToSync`, `hasFreshData`) and use that boolean inside the effect. No inline `!x && y` or nested ternaries in the effect body or its dependency guard.
2. No negative conditions inside `useEffect`. If the natural check is negative, invert it into a positive boolean above the effect and early-return on the positive path.
3. Minimize `useEffect` count. Default is zero. Add one only when you actually need to synchronize with an external system (network, timer, subscription, DOM API). Do not use effects to derive state, to transform props, or to react to user events (use derived values, `useMemo`, or event handlers instead).
4. One effect, one concern. If an effect does two unrelated things, split it. Never combine unrelated subscriptions or fetches in a single effect.
5. Every effect that acquires a resource must return a cleanup function. No exceptions.
6. Avoid raw `for` and `forEach` loops in render or in derived state. Use `map`, `filter`, `reduce`, `flatMap`, or `Array.from` so the result is an expression, not a mutation. `for` is only acceptable when you need early-exit performance on very large arrays and a comment explains why.
7. Never mutate state, props, or arrays/objects returned by hooks. React's reconciler relies on referential inequality to detect change: a mutated-in-place value looks identical to the previous render, so updates silently drop and bugs surface far from the mutation site. Default posture is read-only plus creation: treat every value as `Readonly<T>` or `ReadonlyArray<T>`, and produce a new object or array for every change (spread `{ ...prev, field: next }`, `arr.map`, `arr.filter`, `arr.concat`, `Object.freeze` for constants). When a deep copy is genuinely required (nested state trees, complex form drafts), use `structuredClone(value)`, then mutate the clone locally and hand the new reference to `setState`. Reach for a mutation library (Immer's `produce`) only when the reducer would otherwise become unreadable, and even then the output handed back to React is still a fresh reference. Rules of thumb: (a) if you typed `.push`, `.pop`, `.splice`, `.sort`, `.reverse`, `obj.x =`, or `arr[i] =` on a value that came from `useState`, `useReducer`, props, context, or a query hook, you are wrong; use the immutable counterpart (`.concat`, `.slice`, `.toSorted`, `.toReversed`, spread) or `structuredClone` first. (b) Prefer creation over mutation everywhere: a new local `const next = { ...prev, ... }` beats reassigning fields. (c) Freeze shared constants with `as const` and `Object.freeze` so accidental writes fail loudly in dev.
8. Lists must have stable, unique `key` props derived from data, never the array index unless the list is truly static.
9. Keep component files under 100 lines. Extract child components, hooks, and helpers into their own files before the component grows.
10. Custom hooks start with `use`, return a named object type (never a bare tuple), and never call other hooks conditionally.
11. No tuples as public shapes. Tuples signal laziness. Every hook return, component prop bundle, reducer state, reducer action, context value, and function argument bag gets an explicit named `type` or `interface`. Rule of thumb: if a value has two or more fields or gets destructured at the call site, it needs a name. `useUser(): [User, boolean, Error]` is wrong, `useUser(): UserQueryResult` with `{ user, isLoading, error }` is right.
12. Name every generic parameter and every composite type. `Map<string, Array<{ id: number; name: string }>>` inline is wrong. Define `type UserId = string; type UsersById = Map<UserId, User[]>` and use that. Generic parameters get meaningful names (`TItem`, `TKey`, `TResponse`), never bare `T`, `U`, `K`, `V` in application code.
13. Prop types and event handler types live in a dedicated `types.ts` next to the component (or in `src/types/` when shared). Never inline anonymous object types on a component signature. `({ user, onSave }: { user: User; onSave: (u: User) => void })` is wrong, extract `type ProfileCardProps = { user: User; onSave: (next: User) => void }`.
14. As the author (human or AI), invent the clearest domain name for each type. If you cannot name it, you do not understand it yet. Split until you can.

---


## Boolean Principles (Cross-Language)

1. **Naming:** All boolean variables MUST begin with `is`, `has`, `can`, or `should` (e.g. `isValid`, `hasMatch`). Never use generic names like `active` or `loaded`.
2. **No Negative Names:** Never include negative words like `Not` or `No` in a boolean variable name. Use a positive synonym instead (e.g. `isInvalid` instead of `isNotValid`, `isPending` instead of `notReady`).
3. **No Explicit True Checks (TOTAL BAN):** NEVER evaluate a boolean explicitly against `true` (e.g., `if isReady == true` or `if (hasMatch === true)`). This is redundant, unidiomatic, and STRICTLY FORBIDDEN. Positive booleans MUST ALWAYS be evaluated implicitly: `if isReady { ... }`.
4. **No Mixed Polarity:** NEVER combine a positive check and a negative check in the same `if` condition (e.g., `if isA && !isB`). This is a code smell. Extract the combined condition into a single, positively named boolean that captures the actual intent (e.g. `isConflict := isA && !isB; if isConflict { ... }`).

## Method Documentation (When To Write, When Not To)

Must-follow rule: simple methods do NOT require documentation. Do not write verbose comments. Comments lie, code does not. Names and signatures are the primary documentation. If you feel the need to explain what a method does in prose, first rename it or split it until the code explains itself.

Write a method doc comment ONLY when one of these is true, and even then the preferred fix is to refactor so the doc becomes unnecessary:

1. The method does many non-obvious things that could not be expressed in the name. This is a smell, refactor first. Only if refactoring is genuinely impossible, document.
2. The method processes or transforms data where a one-line example clarifies the contract. Example: Go `path.Clean` performs path cleaning and normalization, a short example is worth more than prose.
3. The code is adapted or copied from an external source. Citation (URL plus license note) is mandatory.
4. The team runs automated doc generation (godoc, TypeDoc, phpDocumentor). In that case exported APIs get a one-liner so the generated docs are usable.

Never write a doc that restates the signature ("Returns the user by id" on `getUser(id)`). That is a review-blocking violation.

Go reference (doc comment starts with the identifier, no blank line between doc and declaration): https://go.dev/src/go/doc/example.go

Go example (canonical, applies conceptually to every language, only comment syntax changes):

```go
// AVOID below type comments: verbose prose that repeats the code

// GetUser gets a user by id and returns it, or an error.
func GetUser(id int64) (User, error) { ... }

// AVOID below type comments: doc on a trivially named simple method

// Add adds a and b.
func Add(a, b int) int { return a + b }

// OK: exported, non-trivial behavior, with a brief example. Start with method name for GO but similar can be done for other specific lang.

// Clean returns the shortest path name equivalent to path by purely
// lexical processing. Rules applied iteratively:
//   1. Replace multiple slashes with a single slash.
//   2. Eliminate each . path name element.
//   3. Eliminate each inner .. path name element.
func Clean(path string) string { ... }
```

Decision checklist before writing any doc comment:

1. Can I rename the method so the doc becomes redundant? If yes, rename and skip the doc.
2. Can I split the method so each piece is trivially named? If yes, split and skip the doc.
3. Does the doc restate the signature or parameter names? If yes, delete it.
4. Does the doc explain WHY (business rule, ordering constraint, cited source) or provide a short example that clarifies the contract? If yes, keep it, one or two lines.
5. Does the team run automated doc generation? If yes, one-liner on exported APIs is acceptable.

The same rules apply to TypeScript, PHP, Rust, C#, PowerShell, and Python. Only the comment syntax changes.

---

## Language One-Liners

- Go: use a result type, not `(T, error)`. Wrap errors with an operation label. Enums are `type X byte` plus `iota`, never string constants.
- TypeScript: `Promise.all` for independent async, never sequential `await`. No `any`. `readonly` on interface fields by default.
- Rust: `Result<T, E>` with a `thiserror`-style enum. `let` not `let mut` unless mutation is the point.
- PHP: enum comparison via method call (`->isEqual()`), never `===`.
- PowerShell: `Verb-Noun` PascalCase function names, `lowercase-kebab-case` filenames.
- C#: PascalCase methods and properties, `_camelCase` private fields, `I`-prefix interfaces.
- Python: `snake_case` functions and variables, `PascalCase` classes, type hints on every public function, `dataclass` or `pydantic` for structured records.

---

## Workflow

1. Read the code before writing the fix. Find the root cause in one sentence.
2. Apply the minimum correct fix. No drive-by refactors.
3. Verify in the logs (or in a live run) that the fix works. Do not claim done based on the build passing alone.
4. List every remaining task before ending the turn.
5. Plan multi-file features with a Mermaid component or flow diagram first.
6. If you cannot find the answer in this file or in an existing `spec/02-coding-guidelines/` folder or `spec/03-error-manage/` folder, ask. Do not invent.


## 10. Markdown Formatting (Reporting Guidelines)

- **Header Spacing (MD022):** Every header (`#`, `##`, `###`, etc.) MUST have a completely blank new line directly before and after it.
- **List Spacing (MD032):** Every list item block MUST be surrounded by blank lines. There must be a gap between a paragraph or a heading and the start of a list. This ensures clean Markdown rendering and passes the `MD032` markdown linter rule.
- Do not compress headings against text blocks.



## 11. Version JSON Configuration & Path Mapping

- **Configurable Installation Path:** While `version.json` and prompt architectural mapping files are installed in `.lovable/memory/` and `.lovable/prompts/` by default, this path MUST be treated as dynamically configurable. 
- Any AI agent or script (including the `cg` reporting guideline commands) that reads or installs `version.json` information must allow the path to be overridden via a root JSON configuration (e.g., if the user wants memory files stored outside `.lovable`).

---

## 12. Autonomous Agent Execution & Phase-by-Phase Self-Looping Protocol (Anti-Hallucination Framework)

To prevent AI hallucination, context drift, premature turn exit, or superficial reviews, AI agents operating on this codebase MUST follow this strict 5-phase execution lifecycle.

### Phase 1: Deep Read & Exploratory Bounded Scan (Turn 1 .. N/2)

- **Zero-Mutation Rule:** The AI must NEVER modify code during Phase 1.
- **Dependency & Scope Mapping:** Walk all target source files, read local types and imported modules, and locate the architectural boundaries.
- **Spec Verification:** Cross-check the target code against the Master Checklist and language-specific specs.

### Phase 2: Microscopic Task Decomposition (60-Item Fine-Grained Atomic Verification Matrix)

Every file and function must be audited against these 60 atomic sub-tasks:

#### A. Size & Structural Boundaries (Checks 1–8)

- [ ] **Check 01:** Function line count: 8 lines preferred, 15 lines max (excluding blank lines and comments).
- [ ] **Check 02:** File coding lines: max 100 lines (recommended 80 lines or fewer).
- [ ] **Check 03:** File total lines: hard cap 300 lines maximum.
- [ ] **Check 04:** React component files (`.tsx`): 100 lines max (recommended 80 lines or fewer).
- [ ] **Check 05:** Class or struct body: 120 lines max.
- [ ] **Check 06:** Anti-line compression check: zero removed indentation, zero single-line if/else blocks to cheat line caps.
- [ ] **Check 07:** Function signature: 100 characters max.
- [ ] **Check 08:** Parameter count: max 3 parameters (split more than 3 parameters to one per line or use a parameter struct).

#### B. Braces, Nesting & Control Flow (Checks 9–15)

- [ ] **Check 09:** Zero nested if statements.
- [ ] **Check 10:** Inversion of conditions into guard clauses and early returns.
- [ ] **Check 11:** Cyclomatic complexity: 5 or less per function.
- [ ] **Check 12:** No `else` after a returning or throwing `if`.
- [ ] **Check 13:** Strict conditional joins: at most 2 operands (1 logical join).
- [ ] **Check 14:** Never mix `&&` and `||` within the same `if` condition.
- [ ] **Check 15:** No inverted complex conditions with `!` (apply De Morgan's laws or extract a named boolean).

#### C. Boolean Syntax & Logic (Checks 16–24)

- [ ] **Check 16:** Zero explicit boolean comparisons against `true` (`if isReady == true` is FORBIDDEN).
- [ ] **Check 17:** Zero explicit boolean comparisons against `false` (`if isReady == false` is FORBIDDEN).
- [ ] **Check 18:** No mixed polarity (`if isA && !isB` is FORBIDDEN; extract to named boolean).
- [ ] **Check 19:** Positive boolean prefixes: `is`, `has`, `can`, `should`, `was`, `will`, `did`, `must`.
- [ ] **Check 20:** No negative boolean variables (`isNotReady`, `disableCache` are FORBIDDEN).
- [ ] **Check 21:** No inverted success checks (`!response.isSuccess` banned; use `response.isFail`).
- [ ] **Check 22:** Zero boolean positional flag parameters on functions.
- [ ] **Check 23:** Wrapped boolean multi-returns (struct/object wrapper, no bare tuples `(int, bool)`).
- [ ] **Check 24:** Normalized booleans at external and user-input boundaries.

#### D. Error Management & Architecture (Checks 25–33)

- [ ] **Check 25:** Zero swallowed errors (no empty `catch {}` or `_ = err`).
- [ ] **Check 26:** Universal `AppError` wrapping with operation context (`op` name + key parameters).
- [ ] **Check 27:** Universal response envelopes (`{ data, errors[], meta }`).
- [ ] **Check 28:** Zero dual-handling (never panic/log AND return error in the same branch).
- [ ] **Check 29:** Typed exit enums for error categories (no raw string error codes).
- [ ] **Check 30:** Preserved original error cause and stack trace.
- [ ] **Check 31:** Context logging on every error (sanitized parameters, no raw secrets).
- [ ] **Check 32:** Log levels match severity (`debug`, `info`, `warn`, `error`, `fatal`).
- [ ] **Check 33:** Zero raw string throws (`throw "msg"` or bare `panic("msg")` is FORBIDDEN).

#### E. Types, Enums & Centralized Constants (Checks 34–41)

- [ ] **Check 34:** Zero magic strings or raw numeric literals.
- [ ] **Check 35:** All Enum names MUST end with the `Type` suffix (e.g., `UserRoleType`).
- [ ] **Check 36:** TypeScript string unions banned (`type Role = "admin" | "user"` -> `enum RoleType`).
- [ ] **Check 37:** Dedicated files for definitions (types, enums, constants in `src/types/`, `src/enums/`).
- [ ] **Check 38:** Exhaustive switch / pattern matching on enums.
- [ ] **Check 39:** Narrow types only (zero `any`, `unknown`, `interface{}`, `object`, `dynamic`).
- [ ] **Check 40:** Type guards at trust boundaries (external JSON, API inputs, catch blocks).
- [ ] **Check 41:** Single `version.json` at root as sole version authority.

#### F. Naming, Casing & Formatting (Checks 42–50)

- [ ] **Check 42:** PascalCase for types, structs, interfaces, and database tables.
- [ ] **Check 43:** camelCase for variables, methods, properties, and database columns.
- [ ] **Check 44:** Abbreviation casing strictly PascalCase (`UserId`, `Url`, `Api`, not `UserID`, `URL`, `API`).
- [ ] **Check 45:** Strictly lowercase file and folder names (`01-file.ts`, not `01-File.ts`).
- [ ] **Check 46:** Blank line before `return`/`throw` (R13) unless sole statement in block.
- [ ] **Check 47:** Blank line after closing `}` (R14) unless followed by `else`/`catch`/`case`.
- [ ] **Check 48:** Never two consecutive blank lines anywhere in the file (R15).
- [ ] **Check 49:** No padded braces (R16).
- [ ] **Check 50:** Import grouping (std lib, third-party, first-party) with blank lines between groups (R18).

#### G. Testing, QA & AI Optimization (Checks 51–60)

- [ ] **Check 51:** Semantic 3-part unit test naming (`TestUnit_Scenario_Outcome`).
- [ ] **Check 52:** Multi-variable positive and negative branch coverage.
- [ ] **Check 53:** Zero generic garbage names (`temp`, `data`, `obj`, `comp_100`).
- [ ] **Check 54:** Immutable-first variable declarations (`const`, `final`, no unnecessary `let`/`var`).
- [ ] **Check 55:** DRY principle enforced (extract any logic duplicated across 2+ call sites).
- [ ] **Check 56:** Zero generated files or build artifacts in Git (proactive `.gitignore`).
- [ ] **Check 57:** Never disable or bypass CLI linters or CI/CD checks (no `|| true`, no suppression flags).
- [ ] **Check 58:** Verifiable tool execution (real command execution with `exit code 0`).
- [ ] **Check 59:** Zero truncation and no placeholder stubs (`TODO`, `FIXME`, `// ...`, `/* ... */`).
- [ ] **Check 60:** Pre-commit diff proof via `git status --porcelain` and `git diff --stat`.

### Phase 3: Multi-Agent Parallelization (2–3 Concurrent Threads Max)

When analyzing large repositories, the parent agent MUST divide the workload:

1. **Disjoint Bounding Boxes:** Assign non-overlapping directory trees to 2 or 3 parallel sub-agents (e.g., Sub-Agent A = Backend, Sub-Agent B = Frontend, Sub-Agent C = Shared/Scripts).
2. **Context Diet:** Pass only the target file paths and specific subtask references to sub-agents. Never paste giant prompt texts or memory logs into sub-agent contexts.
3. **Structured Response Gathering:** Sub-agents return markdown violation tables (`| Id | File | Line | Snippet | Planned Fix | Status |`) that the parent reconciles into the master ledger.

### Phase 4: Bounded Sequential Self-Looping Execution (1 File per Turn)

During execution or fix phases:

1. **Isolated Micro-Tasking:** Never attempt to refactor multiple files in one turn. Process exactly **one file per turn**.
2. **Run Guideline Autofixer:** Execute `python .lovable/ai-fix-scripts/02-guideline-autofixer.py <file>` to handle formatting and boolean cleanup.
3. **Apply Surgical Fix:** Refactor functions > 15 lines, flatten nested if statements, and wrap errors.
4. **Local Verification:** Run local tests and linters to verify zero regressions.
5. **End Turn & Self-Loop:** Check off the verified item and self-loop into the next turn.

### Phase 5: Disk Reality Check & Verifiable Resolution

Before marking any task complete:

- Execute `git status --porcelain` and `git diff --stat` to verify modified files actually exist on disk.
- Run regex searches for `TODO`, `FIXME`, and `// ...` to ensure zero placeholder stubs remain.
- Ensure the master violation ledger in `.lovable/plans/pending/` is fully reconciled with all items marked `DONE`.

