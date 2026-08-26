#!/bin/bash
TARGET_DIR="${1:-.lovable/prompts}"
VERSION="${2:-main}"

echo "Installing Prompt Architect v$VERSION into $TARGET_DIR..."

REPO_ROOT=$(pwd)
VERSION_JSON="$REPO_ROOT/version.json"

if [ -d "$TARGET_DIR" ]; then
    rm -rf "$TARGET_DIR"/*
else
    mkdir -p "$TARGET_DIR"
fi

TEMP_DIR=$(mktemp -d)

echo "Cloning version $VERSION..."
git clone -q --depth 1 --branch "$VERSION" https://github.com/alimtvnetwork/prompt-architect-v2.git "$TEMP_DIR"

if [ $? -eq 0 ]; then
    echo "Copying prompts..."
    cp -r "$TEMP_DIR"/01-general-prompts/* "$TARGET_DIR"/
    
    NOW=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    
    python3 -c "
import json, os, sys

version_file = '$VERSION_JSON'
target_dir = '$TARGET_DIR'

# Traverse target_dir and build relative paths
files_imported = []
for root, dirs, files in os.walk(target_dir):
    for f in files:
        full_path = os.path.join(root, f)
        # We want the path relative to REPO_ROOT (which is the current working directory)
        rel_path = os.path.relpath(full_path, start='.')
        files_imported.append(rel_path.replace('\\\\', '/'))

prompt_data = {
    'version': '$VERSION',
    'installed_at': '$NOW',
    'author': {
        'name': 'Md. Alim Ul Karim',
        'title': 'Chief Software Engineer',
        'url': 'https://github.com/alimtvnetwork/prompt-architect-v2'
    },
    'mapping': {
        'source_repository': 'alimtvnetwork/prompt-architect-v2',
        'source_directory': '01-general-prompts',
        'target_directory': target_dir,
        'files_imported': files_imported
    }
}

data = {}
if os.path.exists(version_file):
    try:
        with open(version_file, 'r') as f:
            data = json.load(f)
    except Exception:
        data = {'name': 'unknown-project', 'version': '0.0.0'}
else:
    data = {'name': 'unknown-project', 'version': '0.0.0'}

data['promptArchitectByRiseupAsia'] = prompt_data

with open(version_file, 'w') as f:
    json.dump(data, f, indent=2)
"
    
    echo "Successfully installed Prompt Architect $VERSION! Metadata written to version.json"
else
    echo "Failed to clone repository. Check version tag."
    rm -rf "$TEMP_DIR"
    exit 1
fi

rm -rf "$TEMP_DIR"
