import os
import glob
import re

execute_files = glob.glob('01-general-prompts/14-execute/*.md')

release_checklist = """
## End of Tunnel Release (Anti-Hallucination Checklist)
Past execution turns were sloppy and failed to pin READMEs or bump versions. To prevent this hallucination, when EVERYTHING is completely finished (at the very end of the tunnel), you MUST trigger a release and physically check off these items in your final report:
- [ ] **Minor Bump:** I have bumped the MINOR version in the canonical `version.json` file.
- [ ] **Test File Ban:** I have strictly excluded all test files (`*test*`, `*.spec.*`) from version scanning.
- [ ] **Root README Pinning (FATAL):** I have pinned the latest release version into the root `readme.md` file! I have verified badges and install snippets match the new version.
- [ ] **Changelog Formatting:** I have updated the changelog exactly according to the `version.json` format.
- [ ] **Release Architecture Map:** I have maintained `.lovable/memory/release-architecture-map.md`, enqueued it in `what-to-read.md`, and linked it in the root `readme.md`.
"""

summary_checklist = "\n     - [x] **Action Summary Checklist (Anti-Hallucination):** I have output a detailed `- [x]` checklist summarizing exactly what I accomplished this turn to ensure no steps were hallucinated or skipped (e.g. `- [x] Created schema`, `- [x] Pinned README`)."

for filepath in execute_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the bad giant block at the top if it exists
    if "## Anti-Hallucination & Carelessness Stance (MUST READ)" in content:
        content = re.sub(r'\n*## Anti-Hallucination & Carelessness Stance \(MUST READ\).*?(?=\n```text)', '\n\n', content, flags=re.DOTALL)
        
    # Remove the floating text if my previous fix_executes.py left it
    content = re.sub(r'Past execution turns were sloppy: skipping checklists.*?Your carelessness is unacceptable\. You must follow the exact rules\.', '', content, flags=re.DOTALL)

    # Rewrite End of Tunnel
    content = re.sub(r'(?:> )?3\. End of Tunnel Release.*?(?=\n## 4\.|\n## |\Z)', release_checklist, content, flags=re.DOTALL)
    content = re.sub(r'## End of Tunnel Release \(Strict Checklist\).*?(?=\n## 4\.|\n## |\Z)', release_checklist, content, flags=re.DOTALL)
    
    # Inject Summary Checklist requirement
    if "Action Summary Checklist" not in content:
        if "Execution Reporting (Mandatory Output Format)" in content:
            target = "- [x] Magic strings/numbers extracted to constants."
            if target in content:
                content = content.replace(target, target + summary_checklist)
            else:
                target2 = "- [x] Error management protocols followed"
                if target2 in content:
                    content = content.replace(target2, target2 + summary_checklist)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {filepath}")

