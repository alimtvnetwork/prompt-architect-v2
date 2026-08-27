# Important Instruction : Coding Guidelines v1.14

- [ ] /goal Blindly follow, enforce, and execute every coding guideline, error management architecture, function size cap, boolean principle, and type-safety rule across all languages in this repository. Zero hallucination, zero drive-by refactoring, zero tolerance for guideline violations.
- [ ] /learn Ingest, understand, and internalize all coding standards, cross-language rules, error philosophies, and project specifications from spec/02-coding-guidelines/, spec/03-error-manage/, and .lovable/ memory before reading, modifying, or creating any code.

This is a standalone file. Follow every rule below without consulting any other document. If a `spec/02-coding-guidelines/` folder or `spec/03-error-manage/` folder exists in this repository, treat those as strictly binding extensions to this file, but this file alone is enough to write compliant code.

## 1. Strict Anti-Garbage Naming (Zero Tolerance)

- NEVER generate arbitrary, generic, or sequential names like `comp_100.go`, `comp_100_test.go`, `Input100`, `data`, `temp`, `obj`, or `val`.
- Variables, functions, structs, classes, and file names MUST explicitly describe the domain concept they represent (e.g., `UpdateUserProfileInput` not `Input100`).
- Unit Tests: Unit test file names and test function names must explicitly define exactly what behavior is being tested. `TestHandleComp100` is garbage. `TestUpdateUserProfile_RejectsInvalidEmail` is required.
- If you generate sequential "ID-based" garbage names, the audit will fail you automatically. 

## 2. Boolean Naming & Logic

- All boolean variables/properties MUST begin with `is`, `has`, `can`, or `should` (e.g., `isReady`, `hasData`).
- Never use negative booleans (e.g., `isNotReady`, `disableCache`).
- Never invert success checks (e.g., `!response.isSuccess`). Use a direct failure check (`response.isFail`).

## 3. Function & Type Constraints

- Functions should ideally be <= 8 lines, and MUST never exceed 15 lines. Extract logic into named sub-functions.
- Group parameters into a struct/options object if there are >3 parameters or multiple adjacent parameters of the same type.
- Split long call arguments across multiple lines. No line should exceed 100 characters.
- No unused parameters. Remove them.
- No boolean positional parameters (e.g., `save(true)`). Use configuration objects (`save(SaveOptions{force: true})`).

## 4. Error Management & App Errors

- AppError vs Generic Error: Never throw or return generic base errors (e.g., `Error`, `Exception`). You MUST use a domain-specific AppError.
- Based on the language, create a strongly typed generic wrapper for application errors. For C# and similar OOP languages, this MUST be a custom Exception type (e.g., `AppException`, `DomainException`).
- Propagate and wrap EVERY error with context. Never swallow errors with generic `catch {}`.
- No magic literals as arguments; extract them into named constants or Enums.

## 5. Line-Gap and Whitespace Style

- R13: Blank line BEFORE `return` or `throw` (unless the function is 1 line).
- R14: Blank line AFTER a closing brace (e.g., after an `if` block).
- R15: Never use double blank lines.
- R16: No padded braces (e.g., `function() { \n\n }`).
- R17: Blank line between top-level declarations.
- R18: Group imports logically.
- R19: No trailing whitespace, always end with a single trailing newline.

## 6. Acronyms & Serialization

- R1: Acronym casing is PascalCase, NEVER all-caps (e.g., `SwapIpWindows`, not `SwapIPWindows`).
- R2: JSON / serialization keys must be PascalCase.

## 7. Method Documentation

- Simple methods do NOT require documentation. Do not restate the signature.
- ONLY write docs if the method performs complex transformations or requires external citation.

## 8. Workflow & Execution

- Read the code, find the root cause in one sentence, apply the minimum correct fix, and verify it in the logs.
- List EVERY remaining task. Bump the version, update changelog.
- Do the job properly. Going deep IS the job. Violating this is auto-reject on the same tier as RULE 0.
