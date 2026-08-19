# React UI Fixes & Update Instruction

When applying UI fixes or updates to a React component, follow these rules strictly:

## 1. Zero Structural Changes
- Do not add or remove components, hooks, or imports unless specifically asked.
- Do not reorganize the file structure.
- Focus strictly on fixing the requested UI issue (e.g., alignment, color, spacing).

## 2. Maintain Existing Logic
- Ensure that the state, context, and effect logic remains untouched.
- If a UI fix requires a logic change, ask for permission before modifying the logic.

## 3. Class Names & Styling
- Do not introduce arbitrary CSS classes. Use the existing design system or utility classes (e.g., Tailwind) if present in the project.
- If using inline styles, minimize them and prefer class-based styling.
- Keep the component structure as clean as possible. No wrapping elements unless strictly necessary for layout fixes.

## 4. Provide Verification Instructions
- After applying the fix, provide a brief instruction on how to verify it (e.g., "Check the alignment on mobile screen size").

## Must Follow
Follow the exact instructions. Do not guess or extrapolate. Do exactly what is requested, and ensure no side-effects occur.
