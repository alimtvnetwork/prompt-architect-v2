import os
import re

files_with_issues = []

# Regex to find headings that don't have a blank line before or after them
# A blank line is just whitespace or empty
heading_pattern = re.compile(r'^(#{1,6}\s+.*)$')

for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for i, line in enumerate(lines):
                if heading_pattern.match(line):
                    # Check line before
                    if i > 0 and lines[i-1].strip() != '':
                        files_with_issues.append((filepath, i+1, 'No blank line BEFORE'))
                    # Check line after
                    if i < len(lines) - 1 and lines[i+1].strip() != '':
                        files_with_issues.append((filepath, i+1, 'No blank line AFTER'))

for issue in files_with_issues:
    print(f"{issue[0]}:{issue[1]} - {issue[2]}")
