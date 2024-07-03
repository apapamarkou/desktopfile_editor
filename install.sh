 
#!/bin/bash

# Define the file path
DESKTOP_FILE="$HOME/.local/share/applications/Desktopfile.desktop"

# Create the directory if it doesn't exist
mkdir -p "$HOME/.local/share/applications"

# Write the desktop entry to the file
cat <<EOL > "$DESKTOP_FILE"
[Desktop Entry]
Name=Desktopfile
Exec=$HOME/Applications/desktopfile_editor/desktopfile_editor.py
Icon=$HOME/Applications/desktopfile_editor/desktopfile_editor.png
Categories=Utilities;
Terminal=false
Type=Application
EOL

# Make the desktop file executable
chmod +x "$DESKTOP_FILE"

echo "Desktop entry created at $DESKTOP_FILE"
