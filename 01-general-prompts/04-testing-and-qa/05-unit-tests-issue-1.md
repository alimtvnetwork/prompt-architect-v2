# Unit Tests Issue Tracking Instruction

When investigating and resolving unit test failures:

## 1. Root Cause Analysis
- Run the failing tests and examine the error output.
- Determine if the failure is due to a change in business logic (test needs updating) or a regression in the code (code needs fixing).

## 2. Test Format (AAA)
- Ensure all updated or new tests follow the Arrange, Act, Assert (AAA) pattern.
- Keep tests isolated. Do not share mutable state between tests.

## 3. Mocks and Stubs
- Use appropriate mocking for external dependencies (e.g., databases, APIs).
- Do not mock the system under test.

## 4. Documentation
- Document the root cause and the fix in the PR or issue tracker.

## Must Follow
Never blindly update a test to pass without understanding *why* it failed. Ensure the test still validates the intended behavior.
