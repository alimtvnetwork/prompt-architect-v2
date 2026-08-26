import os
import re

files_to_update = [
    '01-general-prompts/17-release-management/01-major-bump.md',
    '01-general-prompts/17-release-management/02-minor-bump.md',
    '01-general-prompts/17-release-management/03-patch-bump.md'
]

# We need to aggressively rewrite the "Release trigger rule..." paragraph.
new_rule = """## Mandatory Pinning & Changelog (Fatal if missed)
1. **Changelog:** You MUST read the `"changelog"` configuration from `version.json` (e.g. `file_path` and `format`) and append the proper changelog correctly according to that format.
2. **Root README:** You MUST pin the latest release version into the root `readme.md` file. It is FATAL if you do not update the version pins in the root README file!

You must update `version.json`, `changelog.md`, and `readme.md` at a minimum during any bump."""

for file_path in files_to_update:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex replace the bad old rule
        content = re.sub(r"Release trigger rule:.*?Do not edit `readme\.md`, `changelog\.md`.*?checkers\.", new_rule, content, flags=re.DOTALL)
        
        # Make sure the Checklist reflects this
        checklist_items = """- [ ] Update version in `version.json`.
- [ ] Read `version.json` for Changelog formatting rules.
- [ ] Add the changelog properly to the targeted changelog file.
- [ ] Pin the latest version into the root `readme.md` file (FATAL IF MISSED)."""
        
        # Replace "- [ ] Read the overarching main task plan." to anchor our new checklist items
        if "- [ ] Pin the latest version" not in content:
            content = content.replace("- [ ] Read the overarching main task plan.", f"- [ ] Read the overarching main task plan.\n{checklist_items}")
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
