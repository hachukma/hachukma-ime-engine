#!/bin/bash
# create_dmg_macos.sh
# Creates a professional DMG installer for macOS
# Run: bash create_dmg_macos.sh

set -e

echo "=== Creating Hachukma IME DMG Installer ==="

# Configuration
APP_NAME="Hachukma IME"
APP_BUNDLE="dist/Hachukma IME.app"
DMG_NAME="Hachukma-IME-Installer.dmg"
DMG_TEMP="Hachukma-IME-temp.dmg"
DMG_BACKGROUND="background.png"

# Check if app bundle exists
if [ ! -d "$APP_BUNDLE" ]; then
    echo "Error: App bundle not found at $APP_BUNDLE"
    echo "Please run: python setup_macos.py py2app"
    exit 1
fi

# Create temporary DMG (150 MB)
echo "Creating temporary DMG..."
hdiutil create -srcfolder dist -volname "$APP_NAME" -fs HFS+ -fsargs "-c c=64,a=16,e=16" \
    -format UDRW -size 150M "$DMG_TEMP"

# Mount the temporary DMG
echo "Mounting temporary DMG..."
MOUNT_DIR=$(mktemp -d)
hdiutil attach "$DMG_TEMP" -mountpoint "$MOUNT_DIR"

# Set folder properties
echo "Customizing DMG appearance..."

# Create symlink to Applications folder
ln -s /Applications "$MOUNT_DIR/Applications" || true

# Set background image if it exists
if [ -f "$DMG_BACKGROUND" ]; then
    mkdir -p "$MOUNT_DIR/.background"
    cp "$DMG_BACKGROUND" "$MOUNT_DIR/.background/background.png"
fi

# Set DMG icon view properties using AppleScript
osascript << EOF
tell application "Finder"
    set current view of container window of disk "$APP_NAME" to icon view
    set toolbar visible of container window of disk "$APP_NAME" to false
    set statusbar visible of container window of disk "$APP_NAME" to false
    
    set the bounds of container window of disk "$APP_NAME" to {100, 100, 640, 480}
    set theViewOptions to the icon view options of container window of disk "$APP_NAME"
    set arrangement of theViewOptions to not arranged
    set icon size of theViewOptions to 72
    
    if file ".background:background.png" of disk "$APP_NAME" exists then
        set background picture of theViewOptions to file ".background:background.png" of disk "$APP_NAME"
    end if
    
    set position of item "$APP_NAME.app" of container window of disk "$APP_NAME" to {150, 150}
    set position of item "Applications" of container window of disk "$APP_NAME" to {450, 150}
end tell

delay 2
EOF

# Unmount the temporary DMG
echo "Finalizing DMG..."
hdiutil detach "$MOUNT_DIR"

# Convert to compressed DMG
hdiutil convert "$DMG_TEMP" -format UDZO -o "$DMG_NAME"

# Clean up
rm -f "$DMG_TEMP"
rm -rf "$MOUNT_DIR"

echo "=== DMG Created Successfully ==="
echo "Output: $DMG_NAME"
echo "Ready to distribute!"
