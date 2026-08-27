import os
import glob

files = [
    ".lovable/coding-guidelines/coding-guidelines.md",
    "spec/17-consolidated-guidelines/31-compiled-simple-coding-guidelines.md"
]

target = "- **Header Spacing:** Every header (`#`, `##`, `###`, etc.) MUST have a completely blank new line directly before and after it. This ensures clean Markdown rendering and passes the `MD022` markdown linter rule."
replacement = """- **Header Spacing (MD022):** Every header (`#`, `##`, `###`, etc.) MUST have a completely blank new line directly before and after it.
- **List Spacing (MD032):** Every list item block MUST be surrounded by blank lines. There must be a gap between a paragraph or a heading and the start of a list. This ensures clean Markdown rendering and passes the `MD032` markdown linter rule."""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if target in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
