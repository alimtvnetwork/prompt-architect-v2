import os
import glob

files = glob.glob('**/*.md', recursive=True) + glob.glob('**/*.json', recursive=True)

for filepath in files:
    if 'node_modules' in filepath or '.git' in filepath:
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Ensure it ends with a single newline to normalize it
        content = content.rstrip('\r\n') + '\n'
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Failed on {filepath}: {e}")

print("Normalized all files with clean UTF-8 and trailing newlines.")
