#!/bin/bash
TARGET_DIR="${1:-.lovable/prompts}"
VERSION="${2:-main}"

echo "Installing Prompt Architect v$VERSION into $TARGET_DIR..."

if [ -d "$TARGET_DIR" ]; then
    if [ -f "$TARGET_DIR/prompt-version.json" ]; then
        OLD_VERSION=$(grep -o '"version": *"[^"]*"' "$TARGET_DIR/prompt-version.json" | cut -d'"' -f4)
        echo "Removing old version: $OLD_VERSION"
    fi
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
    
    cat <<EOF > "$TARGET_DIR/prompt-version.json"
{
  "version": "$VERSION",
  "installed_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF
    echo "Successfully installed Prompt Architect $VERSION!"
else
    echo "Failed to clone repository. Check version tag."
    exit 1
fi

rm -rf "$TEMP_DIR"
