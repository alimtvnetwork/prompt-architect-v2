# Update Theming Instruction

When updating the theming configuration:

## 1. Token Updates
- Update the central theme file (e.g., `tailwind.config.js`, `theme.json`, or root CSS variables).
- Do not scatter hardcoded colors or spacing values across components.

## 2. Consistency
- Ensure new colors have appropriate shades (e.g., 50-900) if using a scale-based system.
- Ensure semantic names (e.g., `primary`, `danger`, `success`) are used correctly.

## Must Follow
All theming changes must be centralized in the configuration files. No inline styles or hardcoded values in UI components.
