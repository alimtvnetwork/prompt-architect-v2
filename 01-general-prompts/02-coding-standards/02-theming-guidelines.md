# Instruction (must follow): Theming Guidelines

When implementing or updating theming (colors, typography, spacing):

## 1. CSS Variables / Design Tokens

- Always use CSS variables (custom properties) or the project's design token system (e.g., Tailwind config).
- Do not hardcode hex codes or pixel values in components.

## 2. Dark Mode Support

- Ensure all color variables have a dark mode equivalent.
- Test contrast ratios for accessibility in both light and dark modes.

## 3. Consistency

- Follow the existing naming convention for variables (e.g., `--color-primary-500`, `--spacing-md`).
- Do not invent new token names if an existing one fits the purpose.

## Must Follow

Strict adherence to the design token system. No hardcoded styles.

## Actionable Items & Checklist

- [ ] Read the overarching main task plan.
- [ ] Ensure the git repository starts completely clean.
- [ ] Complete all work on the current branch only.
- [ ] Ensure `.gitignore` explicitly excludes test reports, artifacts, and compiled binaries.
- [ ] Group all completed work into a single logical commit.
- [ ] Push the commit to the remote repository.
