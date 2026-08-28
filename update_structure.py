filepath = ".lovable/lovable-folder-structure.md"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Check where ai-fix-scripts is documented
old_text = "### `.lovable/ai-fix-scripts/`"
new_text = """### `.lovable/ai-fix-scripts/`
A persistent toolkit of reusable AI helper scripts.
*   **Shipped Globally:** This folder and its scripts (like `01-file-manipulator.py`) are shipped out-of-the-box via the prompt architect installer.
*   **`01-file-manipulator.py`**: The canonical Python tool for mass lowercasing, file sequencing, and aggressive encoding/line-ending normalizations. AIs should use this instead of writing new scripts."""

if old_text in content and "Shipped Globally" not in content:
    import re
    # We want to replace the current text under the header.
    # We will just do a regex replace of the header and its bullets up to the next ### or end of file
    pattern = re.compile(r'### \.lovable/ai-fix-scripts/.*?(\n### |\Z)', re.DOTALL)
    content = pattern.sub(new_text + r'\1', content)
    
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print("Updated folder structure docs.")
else:
    print("Could not find ai-fix-scripts header to replace.")
