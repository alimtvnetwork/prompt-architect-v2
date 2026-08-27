import os
import re

filepath = '01-general-prompts/14-execute/04-execute-ai-instruction-writer.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update title just in case it didn't persist
content = content.replace('# Instruction (must follow): Execute Parent Task (N-Step Continuous Loop & Multi-Agent)', '# Instruction (must follow): Execute AI Instruction Writer (Generic Spec Generator)')

new_goal = """/goal You are an expert AI Instruction Architect. Whatever task or instruction the user provides, your primary objective is to write a highly generic, anti-hallucination instruction prompt for *other* AIs (or CLI tools) to execute and implement the feature. 
- You MUST write the instruction to be as GENERIC as possible. Do not tie it to the current system, specific framework versions, or hardcoded local paths unless absolutely necessary.
- The output instruction must guide the target AI using strict checklists so that it does not make mistakes.
- Once you have written the generic AI instruction, you MUST save it as a spec file and ALSO output the entire contents of that file directly into the chat/output window for the user to review.
"""

# Only replace if it still has the old goal
if "/goal Execute a parent task by decomposing it" in content:
    content = re.sub(r'/goal Execute a parent task by decomposing it.*?(?=\n\n/learn|\n\n##)', new_goal, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
