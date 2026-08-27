import os
import glob

prompts = glob.glob('01-general-prompts/17-release-management/*.md') + glob.glob('.lovable/prompts/*.md')

dynamic_instructions = """### Install <Project Name> vX.Y.Z
   To pin your repository to this exact version, run the following one-liner:
   Unix/Bash: `curl -sL https://raw.githubusercontent.com/<owner>/<repo>/vX.Y.Z/install.sh | bash -s -- ".lovable/prompts" "vX.Y.Z"`
   PowerShell: `Invoke-WebRequest -Uri https://raw.githubusercontent.com/<owner>/<repo>/vX.Y.Z/install.ps1 -OutFile install.ps1; .\\install.ps1 -TargetDir ".lovable/prompts" -Version "vX.Y.Z"`

   *(Note: You MUST dynamically discover the `<owner>/<repo>` by running `git config --get remote.origin.url`. Do not hardcode Prompt Architect URLs unless you are actually in the Prompt Architect repository.)*
"""

old_block = """### Install Prompt Architect vX.Y.Z
   To pin your repository to this exact version, run the following one-liner:
   Unix/Bash: `curl -sL https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/vX.Y.Z/install.sh | bash -s -- ".lovable/prompts" "vX.Y.Z"`
   PowerShell: `Invoke-WebRequest -Uri https://raw.githubusercontent.com/alimtvnetwork/prompt-architect-v2/vX.Y.Z/install.ps1 -OutFile install.ps1; .\\install.ps1 -TargetDir ".lovable/prompts" -Version "vX.Y.Z"`"""

for filepath in prompts:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_block in content:
        content = content.replace(old_block, dynamic_instructions)
        content = content.replace("`### Install Prompt Architect` block exactly as shown above", "`### Install <Project Name>` block, dynamically filling in the GitHub owner and repo parsed from the git config")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
