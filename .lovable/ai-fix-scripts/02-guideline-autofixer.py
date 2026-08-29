import os
import sys
import glob
import re

def process_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
        return False

    original = content

    # 1. Remove == true and === true
    content = re.sub(r'\s*===\s*true', '', content)
    content = re.sub(r'\s*==\s*true', '', content)
    content = re.sub(r'\s*!==\s*false', '', content)
    content = re.sub(r'\s*!=\s*false', '', content)

    # 2. Remove == false (replace with ! condition is trickier for regex without AST, but we can do simple ones)
    # Actually, replacing `foo == false` with `!foo` is dangerous in regex. We'll skip complex inversions and let the AI do them.

    # 3. Fix double blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # 4. Ensure one blank line before return (if not at start of block)
    # regex: look for newline, then some non-whitespace code, then newline, then spaces, then return
    # This is slightly complex in regex. Let's do a line-by-line pass.
    lines = content.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("return ") or stripped == "return":
            # Check if previous line is not empty and not a { or comment
            if i > 0:
                prev_stripped = lines[i-1].strip()
                if prev_stripped != "" and not prev_stripped.endswith("{") and not prev_stripped.startswith("//") and not prev_stripped.startswith("/*") and not prev_stripped.startswith("*"):
                    new_lines.append("")
        
        # Blank line after closing bracket (if next line is not closing bracket or else)
        if stripped == "}" and i < len(lines) - 1:
            next_stripped = lines[i+1].strip()
            new_lines.append(line)
            if next_stripped != "" and next_stripped != "}" and not next_stripped.startswith("else") and not next_stripped.startswith("catch") and not next_stripped.startswith("finally"):
                new_lines.append("")
            continue

        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # 5. Remove consecutive blank lines again if we created any
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original:
        with open(filepath, "w", encoding="utf-8", newline='\n') as f:
            f.write(content)
        print(f"[FIXED] {filepath}")
        return True
    return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 02-guideline-autofixer.py <file-or-dir>")
        sys.exit(1)

    target = sys.argv[1]
    
    if os.path.isfile(target):
        process_file(target)
    elif os.path.isdir(target):
        # Scan for supported languages
        exts = [".go", ".ts", ".tsx", ".js", ".jsx", ".py"]
        fixed = 0
        for root, _, files in os.walk(target):
            if "node_modules" in root or ".git" in root or "vendor" in root:
                continue
            for file in files:
                if any(file.endswith(ext) for ext in exts):
                    if process_file(os.path.join(root, file)):
                        fixed += 1
        print(f"Autofix complete. Fixed {fixed} files.")
    else:
        print(f"Target not found: {target}")

