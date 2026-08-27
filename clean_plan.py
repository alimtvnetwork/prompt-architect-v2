import re

filepath = '01-general-prompts/05-coding-guidelines/01-plan-coding-guideline-audit.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to remove everything from "## Compiled Simple Coding Guidelines" to "## Metadata"
content = re.sub(r'## Compiled Simple Coding Guidelines \(AI Blind-Follow\).*?(?=## Metadata)', 
"""## 5. Coding Guidelines Strict Adherence

/learn You MUST internalize the master coding guidelines located at `01-general-prompts/04-coding-standards/01-coding-guidelines.md`. It contains the ultimate source of truth for Boolean rules, Function limits, Error handling, and language-specific React/Go/Python paradigms. Do not hallucinate rules; enforce exactly what is in that file.

""", content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated 01-plan-coding-guideline-audit.md")
