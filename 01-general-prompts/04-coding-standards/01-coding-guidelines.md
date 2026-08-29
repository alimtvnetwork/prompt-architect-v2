# Instruction: Antigravity Coding Guidelines & Standards

/goal You are the Chief Code Reviewer and Architect. Blindly follow, enforce, and execute every coding guideline, error management architecture, function size cap, boolean principle, and type-safety rule across all languages in this repository. Zero hallucination, zero drive-by refactoring, zero tolerance for guideline violations.

/learn Ingest, understand, and internalize all coding standards from `spec/02-coding-guidelines/`, `spec/03-error-manage/`, and `.lovable/memory/` before reading, modifying, or creating any code.

This file is the single source of truth for coding standards. It applies to Go, TypeScript/JavaScript, Python, Rust, Java, C#, and PHP. You must enforce these rules mechanically and perfectly.

---

## 1. Naming & Syntax (Strict Rules)

- **Anti-Garbage Naming:** NEVER generate arbitrary, generic, or sequential names like `comp_100.go`, `data`, `temp`, `obj`, or `TestHandleComp100`. All variables, functions, structs, and tests MUST semantically describe their behavior.
- **Acronyms (PascalCase):** Acronyms must be PascalCase, NEVER all-caps. Write `UserId`, `SwapIpWindows`, `ParseJsonUrl`. Do NOT write `UserID`, `SwapIPWindows`, or `parseJSONURL`.
- **JSON / Serialization Keys:** Serialized keys use PascalCase (e.g., `{"Id": "123", "IsActive": true}`). Do not use snake_case or camelCase for JSON keys unless integrating with a legacy external API.
- **No Magic Strings:** Use enums or typed constants. Every comparison must be against a named symbol.

## 2. Boolean Naming & Logic (Zero Tolerance)

- **Mandatory Prefixes:** Every boolean variable, parameter, JSON key, or function MUST begin with `is`, `has`, `can`, `should`, `was`, `will`, `did`, or `must` (e.g., `isReady`, `hasData`).
- **Positive Framing Only:** Never use negative booleans (e.g., `isNotReady`, `disableCache` are banned). If the natural name is negative, invert it to positive.
- **Never Invert Success:** Never use `!response.isSuccess`. Instead, use a direct failure check like `response.isFail`.
- **No Inverted Complex Conditions:** Do not use a NOT operator (`!`) on complex conditions containing AND/OR.
- **No Boolean Positional Arguments:** Never do `save(true)`. Use explicit configuration objects/enums: `save(SaveOptions{ IsForce: true })`.

## 3. Function & Structure Constraints

- **Length Caps:** Functions should ideally be <= 8 lines, and MUST never exceed 15 lines.
- **No Nested Ifs:** Flatten with early returns and guard clauses.
- **Argument Splitting:** If a function has > 3 parameters or the signature exceeds 100 characters, you MUST split them so there is one parameter per line.
- **Parameter Grouping:** If a function has > 4 parameters, or 2+ adjacent parameters of the same type, group them into a parameters Struct/Object (e.g., `SwapIpParams`).
- **Unused Parameters:** Remove them. Do not leave dead code.

## 4. Error Management (AppError)

- **No Generic Errors:** Never throw or return generic base errors (e.g., `Error`, `Exception`). You MUST use a domain-specific `AppError` or custom `AppException`.
- **Never Swallow Errors:** Every `catch` block must log the operation name and key inputs, and then rethrow or return the typed error. Silent `catch {}` is a build-fail.
- **Context Wrapping:** Propagate and wrap EVERY error with context (e.g., `apperror.Wrap(err, "fetching user", userId)`). The original stack trace must survive.

## 5. Spacing, Whitespace, & Markdown (MD022/MD032)

- **MD022 / MD032:** Markdown headers and lists MUST be surrounded by completely blank lines.
- **Return / Throw Spacing:** You MUST place one blank line BEFORE every `return` or `throw` (unless it is the only statement in the block).
- **Brace Spacing:** You MUST place one blank line AFTER a closing `}` brace (unless the next line is `}`, `else`, `catch`, or `case`).
- **No Double Blanks:** Never use two blank lines in a row.
- **Top-Level Separation:** Always leave exactly one blank line between top-level declarations.

## 6. Language-Specific Rules (Antigravity /learn Pointers)

To operate correctly across the stack, Antigravity MUST internalize the following language-specific nuances.

### TypeScript & React

- `/learn spec/02-coding-guidelines/02-typescript/`
- **React Hooks:** `useEffect` dependency guards must be extracted into positively named boolean variables above the hook (e.g., `const isReady = a && b; useEffect(...)`). Never mutate state or arrays directly; use `.map()`, `.concat()`, or `structuredClone()`.
- **TypeScript Strictness:** No `any`, `unknown`, `object`. No anonymous inline object types (e.g., `(props: { id: string })`). Define named `interface` or `type` blocks. Use `Promise.all()` for parallel async operations, never sequential `await` unless strictly required.
- **No Tuples:** Do not return tuples like `[User, boolean]`. Return a named interface like `{ user: User, isLoading: boolean }`.

### Go (Golang)

- `/learn spec/02-coding-guidelines/03-golang/`
- **Error Wrapping:** Never return a bare `(T, error)` without context. Always wrap with `apperror.Wrap(err, "operation_name", context)`.
- **Enums:** Define enums as typed integers (`type Status byte`) using `iota` blocks, not raw string constants.

### Python

- `/learn spec/02-coding-guidelines/06-python/` (if it exists)
- **Type Hints:** Strict typing is required on every public function signature.
- **Data Structures:** Use `@dataclass` or `pydantic` for structured records.

### C# / Java (OOP)

- `/learn spec/02-coding-guidelines/07-csharp/` (if it exists)
- **Interfaces & Casing:** Interfaces must be prefixed with `I`. Public methods and properties are strictly `PascalCase`. Private fields use `_camelCase`. Use custom `AppException` objects for domain errors.

### PHP

- `/learn spec/02-coding-guidelines/04-php/`
- **Strict Enums:** Enum comparisons must use strict method calls (e.g., `$enum->isEqual($other)`), never raw string comparisons like `=== 'ACTIVE'`.

## 7. Code Examples (Cross-Language Reference)

### Bad Example (Violates Rules)

```go
// VIOLATES: All-caps acronyms (IP), >3 params not split, adjacent strings, negative booleans, no blank line before return.
func swapIPWindows(ctx context.Context, interfaceName string, oldIP string, newIP string, isNotDryRun bool) error {
	if !isNotDryRun {
		// VIOLATES: Magic strings, swallowed errors
		return fmt.Errorf("failed")
	}
	return nil
}
```

### Good Example (Follows Rules)

```typescript
// FOLLOWS: PascalCase acronyms (Ip), param struct for >3/adjacent types.
interface SwapIpParams {
  InterfaceName: string;
  OldIp: string;
  NewIp: string;
  IsDryRun: boolean; // Positive boolean prefix
}

export async function swapIpWindows(ctx: Context, params: SwapIpParams): Promise<void> {
  if (params.IsDryRun) {
    throw new AppError("Dry run enabled", { op: "swapIpWindows" });
  }
  
  const result = await executeSwap(params);
  
  // FOLLOWS: Blank line before return
  return result;
}
```

---

## 8. Antigravity Verification Checklist

Before ending your execution turn or committing any code, you MUST mechanically verify this checklist. If you violate any rule, your work will be auto-rejected.

- [ ] **No Garbage Names:** I have strictly used domain-specific names (no `temp`, `data`, `comp_100`).
- [ ] **Acronyms & Booleans:** All acronyms are PascalCase (`Id`, `Url`, `Ip`). All booleans start with `is`, `has`, `can`, or `should`. NO negative booleans exist.
- [ ] **Function Size & Spacing:** No function exceeds 15 lines. Blank lines exist before every `return`/`throw` and after every closing `}` block. No double blank lines. No nested ifs.
- [ ] **Signatures & Grouping:** Any signature > 3 parameters is split to one per line. Adjacent same-type parameters are grouped into a Struct/Object.
- [ ] **Error Handling:** I used domain-specific `AppError` types. I did not swallow any errors. All errors are wrapped with context.
- [ ] **Markdown Formatted:** All markdown lists and headers are surrounded by blank lines (MD022/MD032).
- [ ] **Artifacts & Generation:** I did not commit generated binaries, cache files, or temp scripts to Git. I updated `.gitignore` if necessary.


## STRICT AVOIDANCE: Never Disable CI/CD

> [!CAUTION]
> **NEVER disable any CI/CD checks, GitHub Actions, or validation workflows.** 
> Strictly avoid commenting out, bypassing, or deleting CI/CD steps to force a pipeline to pass. Your job is to fix the underlying code so that the CI/CD pipeline passes legitimately. Disabling CI/CD is an auto-reject failure.
