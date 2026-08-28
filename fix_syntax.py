import os

filepath = ".lovable/ai-fix-scripts/01-file-manipulator.py"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("r'\\\\?\\'", "'\\\\\\\\?\\\\'")
content = content.replace("r'\\\\?\\' + abs_path", "'\\\\\\\\?\\\\' + abs_path")

with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
