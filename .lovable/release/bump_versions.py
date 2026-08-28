import os
import re
import json
import argparse

# Files that need to be bumped
FILES_TO_BUMP = [
    "package.json",
    "prompt-version.template.json",
    "readme.md",
    ".lovable/coding-guidelines/coding-guidelines.md",
    "linter-scripts/validate-guidelines.go",
    "linter-scripts/validate-guidelines.py",
    "spec/14-update/28-worker-push-instruction.md",
    "spec/17-consolidated-guidelines/31-compiled-simple-coding-guidelines.md",
    "spec/19-main-worker-service/diagrams/seq-push-update.mmd",
    "spec/19-main-worker-service/10-worker-bootstrap-protocol.md",
    "spec/19-main-worker-service/14-rbac-and-status-seed.md",
    "spec/19-main-worker-service/15-tunable-constants.md",
    "spec/19-main-worker-service/16-update-channels.md",
    "spec/19-main-worker-service/25-inherited-rules.md"
]

def get_current_version():
    with open("version.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("version", "1.0.0")

def set_current_version(new_version):
    with open("version.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        data["version"] = new_version
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def bump_version(current, bump_type):
    major, minor, patch = map(int, current.split("."))
    if bump_type == "major":
        return f"{major + 1}.0.0"
    elif bump_type == "minor":
        return f"{major}.{minor + 1}.0"
    elif bump_type == "patch":
        return f"{major}.{minor}.{patch + 1}"
    return current

def update_files(old_version, new_version):
    escaped_old = re.escape(old_version)
    regex_plain = re.compile(rf'\b{escaped_old}\b')
    regex_prefixed = re.compile(rf'v{escaped_old}\b')

    for file_path in FILES_TO_BUMP:
        if not os.path.exists(file_path):
            print(f"Warning: {file_path} not found. Skipping.")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = regex_plain.sub(new_version, content)
        new_content = regex_prefixed.sub(f"v{new_version}", new_content)

        if new_content != content:
            with open(file_path, "w", encoding="utf-8", newline='\n') as f:
                f.write(new_content)
            print(f"Bumped version in {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bump project versions safely.")
    parser.add_argument("--type", choices=["major", "minor", "patch"], help="Type of bump")
    parser.add_argument("--set", type=str, help="Explicitly set a specific version")
    args = parser.parse_args()

    current_version = get_current_version()
    
    if args.set:
        new_version = args.set
    elif args.type:
        new_version = bump_version(current_version, args.type)
    else:
        print("Error: Must specify --type or --set")
        exit(1)

    print(f"Bumping from {current_version} to {new_version}...")
    
    # 1. Update version.json
    set_current_version(new_version)
    print("Bumped version.json")
    
    # 2. Update all other files
    update_files(current_version, new_version)
    
    print(f"Successfully bumped to {new_version}!")
