# Instruction (must follow): SVG Logo Generation

> This instruction provides guidelines and directives for svg logo generation.

When generating an SVG logo from a text description:

## 1. Clean SVG Code

- Ensure the output is valid XML and SVG.
- Do not use unnecessary grouping (`<g>`) or inline styles unless required. Prefer presentation attributes or minimal CSS.
- Ensure `viewBox` is set appropriately, and remove fixed `width` and `height` attributes to make the SVG responsive.

## 2. Accessibility

- Add a `<title>` and `<desc>` element for screen readers.

## 3. Colors and Theming

- Use `currentColor` for monochrome icons so they inherit text color.
- If it's a multi-color logo, use standard hex codes or CSS variables if specified.

## 4. Output

- Provide only the raw SVG code within an `xml` or `svg` code block. Do not wrap it in HTML unless requested.

## Must Follow

Generate clean, scalable, and responsive SVGs. No base64 embedded images inside the SVG.

## Actionable Items & Checklist

- [ ] Read the overarching main task plan.
- [ ] Ensure the git repository starts completely clean.
- [ ] Complete all work on the current branch only.
- [ ] Ensure `.gitignore` explicitly excludes test reports, artifacts, and compiled binaries.
- [ ] Group all completed work into a single logical commit.
- [ ] Push the commit to the remote repository.
