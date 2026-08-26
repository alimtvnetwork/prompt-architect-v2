import sys

files = ['install.sh', 'install.ps1']

for f_path in files:
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if f_path == 'install.sh':
        old_stub = "data = {'name': 'unknown-project', 'version': '0.0.0', 'frontend': {'version': 'inherit'}, 'backend': {'version': 'inherit'}}"
        new_stub = "data = {'name': 'unknown-project', 'version': '0.0.0', 'frontend': {'version': 'inherit'}, 'backend': {'version': 'inherit'}, 'changelog': {'file_path': 'changelog.md', 'format': '## [v{version}] {date} {headline}'}}"
        content = content.replace(old_stub, new_stub)
    elif f_path == 'install.ps1':
        old_ps_stub = """        $newJson = @{
            name = "unknown-project"
            version = "0.0.0"
            frontend = @{ version = "inherit" }
            backend = @{ version = "inherit" }
            promptArchitectByRiseupAsia = $promptData
        }"""
        new_ps_stub = """        $newJson = @{
            name = "unknown-project"
            version = "0.0.0"
            frontend = @{ version = "inherit" }
            backend = @{ version = "inherit" }
            changelog = @{ file_path = "changelog.md"; format = "## [v{version}] {date} {headline}" }
            promptArchitectByRiseupAsia = $promptData
        }"""
        content = content.replace(old_ps_stub, new_ps_stub)

    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {f_path}")
