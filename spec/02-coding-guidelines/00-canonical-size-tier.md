# Canonical Size Tier (Single Source of Truth)

> **This file is the ONLY authoritative source for function-length, file-length, and component-size limits.**
> All other locations (`.cursorrules`, `eslint.config.js`, `linters-cicd/`, `spec/13-generic-cli/08-code-style.md`, `spec/17-consolidated-guidelines/31-compiled-simple-coding-guidelines.md`) mirror this table and MUST reference it. If any of those drift, this file wins and the others get patched.

## Tier

| Metric                    | Limit         | Enforcement           | Rule ID       |
|---------------------------|---------------|-----------------------|---------------|
| Function body (preferred) | ≤ 8 lines     | warn                  | CODE-RED-005  |
| Function body (hard cap)  | ≤ 15 lines    | error (build-fails)   | CODE-RED-004  |
| File length (standard max)| ≤ 100 lines   | error (coding lines)  | CODE-RED-006  |
| File length (recommended) | ≤ 80 lines    | info                  | CODE-RED-006A |
| React component file      | ≤ 80–100 lines| error (max 100 lines) | CODE-RED-006R |
| Struct / class            | ≤ 120 lines   | error                 | CODE-RED-017  |
| Nested `if` statements    | 0 (No nesting)| error (flatten depth) | CODE-RED-002  |
| Parameters per function   | ≤ 3           | error                 | CODE-RED-008  |
| Cognitive complexity      | ≤ 10          | error                 | CODE-RED-CC10 |

## Counting & Anti-Compression Rules (Strictly Enforced)

- **Standard File Size:** Every code file MUST stay under 100 coding lines (recommended <= 80 lines).
- **Functions:** Target <= 8 lines of body logic; hard cap of <= 15 lines.
- **NO Line-Compression Cheating (TOTAL BAN):**
  - **NEVER** collapse `if/else`, return statements, or blocks into a single line to artificially reduce line count (e.g. `if (x) return y;` or `if (x) { y(); }` are strictly forbidden).
  - **NEVER** delete required blank lines (R13-R16: blank line before `return`/`throw`, blank line after `}`) to cram code into fewer lines.
  - **NEVER** remove code formatting, indentation, or comments to cheat line limits.
  - Sizing MUST be achieved legitimately through **modular decomposition**: extracting helper functions, splitting files into smaller focused modules, and creating dedicated components.

## Waivers

Use only when a genuine domain reason exists (e.g. exhaustive switch on a codegen enum).

```ts
// lint-allow: function-length reason="exhaustive switch over generated enum" max=42
function mapKind(k: Kind): Label { ... }
```

- `reason="..."` is **required** and must be human-readable.
- `max=N` bounds the waiver; the function still fails if it grows past `N`.
- Waivers apply to both `max-function-lines` (15 cap) and `prefer-function-lines` (8 warn).

## Cross-references (must match this tier)

| File | Role |
|------|------|
| `.cursorrules` (Quick Rule 4) | Editor / AI reminder |
| `eslint.config.js` | JS/TS enforcement (`max-lines`, `max-function-lines`, `prefer-function-lines`, `.tsx` override) |
| `linters-cicd/checks/file-length/` | Language-agnostic CI check |
| `linters-cicd/checks/function-length-prefer8/` | Language-agnostic prefer-8 check |
| `spec/13-generic-cli/08-code-style.md` | CLI code-style ref |
| `spec/17-consolidated-guidelines/31-compiled-simple-coding-guidelines.md` §"File Size Limits" | Consolidated guidelines mirror |

## Change protocol

1. Edit this file first.
2. Update the mirrors above in the **same commit**.
3. Bump patch version and add an entry to `changelog.md` under "Canonical tier change".
