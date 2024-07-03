#!/usr/bin/env python3

#  ____            _    _               __ _ _        _____    _ _ _
# |  _ \  ___  ___| | _| |_ ___  _ __  / _(_) | ___  | ____|__| (_) |_ ___  _ __
# | | | |/ _ \/ __| |/ / __/ _ \| '_ \| |_| | |/ _ \ |  _| / _` | | __/ _ \| '__|
# | |_| |  __/\__ \   <| || (_) | |_) |  _| | |  __/ | |__| (_| | | || (_) | |
# |____/ \___||___/_|\_\\__\___/| .__/|_| |_|_|\___| |_____\__,_|_|\__\___/|_|
#
# A simple Desktopfile editor for linux users
# Author: Andrianos Papamarkou


import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QWidget, QHBoxLayout, QComboBox, QSpacerItem, QSizePolicy, QCheckBox, QShortcut
)
from PyQt5.QtGui import QIcon, QPixmap, QKeySequence
from PyQt5.QtCore import Qt

class DesktopFileEditor(QMainWindow):
    def __init__(self, desktop_file=None):
        super().__init__()
        icon_path = os.path.expanduser('~/Applications/desktopfile_editor/desktopfile_editor.png')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle("Desktop File Editor")
        self.default_icon_path = 'default_icon.png'
        self.icon_path = self.default_icon_path
        self.original_content = ""
        self.desktop_file_path = None
        self.initUI()
        if desktop_file:
            self.loadDesktopFile(desktop_file)
        self.adjustSize()
        self.setMinimumWidth(385)


    def initUI(self):
        layout = QVBoxLayout()

        # Icon Field
        self.icon_label = QLabel("Icon:")
        self.icon_button = QPushButton()
        self.icon_button.setFixedSize(64, 64)
        self.icon_button.clicked.connect(self.browseIcon)
        icon_layout = QVBoxLayout()
        icon_layout.setContentsMargins(0, 0, 0, 0)
        icon_layout.addWidget(self.icon_label)
        icon_layout.addWidget(self.icon_button)
        icon_widget = QWidget()
        icon_widget.setLayout(icon_layout)
        layout.addWidget(icon_widget)

        # Name Field
        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        name_layout = QHBoxLayout()
        name_layout.setContentsMargins(5, 2, 5, 2)
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_edit)
        name_widget = QWidget()
        name_widget.setLayout(name_layout)
        layout.addWidget(name_widget)

        # Comment Field
        self.comment_label = QLabel("Comment:")
        self.comment_edit = QLineEdit()
        comment_layout = QHBoxLayout()
        comment_layout.setContentsMargins(5, 2, 5, 2)
        comment_layout.addWidget(self.comment_label)
        comment_layout.addWidget(self.comment_edit)
        comment_widget = QWidget()
        comment_widget.setLayout(comment_layout)
        layout.addWidget(comment_widget)

        # Executable Field
        self.exec_label = QLabel("Executable:")
        self.exec_edit = QLineEdit()
        exec_layout = QHBoxLayout()
        exec_layout.setContentsMargins(5, 2, 5, 2)
        exec_layout.addWidget(self.exec_label)
        exec_layout.addWidget(self.exec_edit)
        exec_widget = QWidget()
        exec_widget.setLayout(exec_layout)
        layout.addWidget(exec_widget)

        # Browse Button for Executable Field
        self.exec_button = QPushButton("Browse")
        self.exec_button.clicked.connect(self.browseExecutable)
        browse_layout = QHBoxLayout()
        browse_layout.setContentsMargins(5, 2, 5, 20)
        browse_layout.addWidget(self.exec_button)
        browse_widget = QWidget()
        browse_widget.setLayout(browse_layout)
        layout.addWidget(browse_widget)

        # Category Field
        self.category_label = QLabel("Category:")
        self.category_combo = QComboBox()
        self.category_combo.addItems(["Development", "Games", "Graphics", "Multimedia", "Office", "Settings", "System", "Utilities", "Network"])
        category_layout = QHBoxLayout()
        category_layout.setContentsMargins(5, 2, 5, 2)
        category_layout.addWidget(self.category_label)
        category_layout.addWidget(self.category_combo)
        category_widget = QWidget()
        category_widget.setLayout(category_layout)
        layout.addWidget(category_widget)

        # Terminal Checkbox
        self.terminal_checkbox = QCheckBox("Run in terminal")
        layout.addWidget(self.terminal_checkbox)

        # Type Field
        self.type_label = QLabel("Type:")
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Application", "Link", "Directory", "File", "Other"])
        type_layout = QHBoxLayout()
        type_layout.setContentsMargins(5, 2, 5, 2)
        type_layout.addWidget(self.type_label)
        type_layout.addWidget(self.type_combo)
        type_widget = QWidget()
        type_widget.setLayout(type_layout)
        layout.addWidget(type_widget)

        # Spacer
        spacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Save Button
        self.save_button = QPushButton("Save .desktop file")
        self.save_button.clicked.connect(self.saveDesktopFile)
        layout.addWidget(self.save_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Add shortcuts
        self.addShortcuts()
        icon_path = os.path.expanduser('~/Applications/disktopfile_editor/desktopfile_editor.png')
        self.setWindowIcon(QIcon(icon_path))
        self.show()

    def addShortcuts(self):
        save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        save_shortcut.activated.connect(self.saveDesktopFile)

        quit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        quit_shortcut.activated.connect(self.quitApp)

    def browseExecutable(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Executable")
        if file_name:
            self.exec_edit.setText(file_name)

    def browseIcon(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Icon", filter="Images (*.png *.xpm *.jpg *.svg)")
        if file_name:
            self.updateIconPreview(file_name)

    def updateIconPreview(self, icon_path):
        self.icon_path = icon_path
        pixmap = QPixmap(icon_path).scaled(self.icon_button.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.icon_button.setIcon(QIcon(pixmap))
        self.icon_button.setIconSize(self.icon_button.size())

    def updateIconFromName(self, icon_name):
        icon = QIcon.fromTheme(icon_name)
        if not icon.isNull():
            pixmap = icon.pixmap(self.icon_button.size())
            self.icon_button.setIcon(QIcon(pixmap))
        else:
            self.updateIconPreview(self.default_icon_path)

    def loadDesktopFile(self, file_name):
        self.desktop_file_path = file_name
        if file_name:
            with open(file_name, 'r') as file:
                self.original_content = file.read()
                lines = self.original_content.splitlines()
                for line in lines:
                    if line.startswith('Name='):
                        self.name_edit.setText(line.split('=', 1)[1].strip())
                    elif line.startswith('Comment='):
                        self.comment_edit.setText(line.split('=', 1)[1].strip())
                    elif line.startswith('Exec='):
                        self.exec_edit.setText(line.split('=', 1)[1].strip())
                    elif line.startswith('Icon='):
                        icon_path = line.split('=', 1)[1].strip()
                        if os.path.isfile(icon_path):
                            self.updateIconPreview(icon_path)
                        else:
                            self.updateIconFromName(icon_path)
                    elif line.startswith('Categories='):
                        categories = line.split('=', 1)[1].strip().split(';')
                        if categories:
                            self.category_combo.setCurrentText(categories[0])
                    elif line.startswith('Terminal='):
                        self.terminal_checkbox.setChecked(line.split('=', 1)[1].strip() == 'true')
                    elif line.startswith('Type='):
                        self.type_combo.setCurrentText(line.split('=', 1)[1].strip())
                self.original_content = '\n'.join(lines)

    def saveDesktopFile(self):
        # Save to the default location
        default_dir = os.path.expanduser("~/.local/share/applications/")
        if not os.path.exists(default_dir):
            os.makedirs(default_dir)

        # Get base name of the desktop file
        base_name = os.path.basename(self.desktop_file_path) if self.desktop_file_path else "new_application.desktop"
        file_name = os.path.join(default_dir, base_name)

        # Create the new content
        new_content = []

        # Ensure [Desktop Entry] header is included
        new_content.append("[Desktop Entry]")

        for line in self.original_content.splitlines():
            if line.startswith('Name='):
                new_content.append(f"Name={self.name_edit.text()}")
            elif line.startswith('Comment='):
                new_content.append(f"Comment={self.comment_edit.text()}")
            elif line.startswith('Exec='):
                new_content.append(f"Exec={self.exec_edit.text()}")
            elif line.startswith('Icon='):
                new_content.append(f"Icon={self.icon_path}")
            elif line.startswith('Categories='):
                new_content.append(f"Categories={self.category_combo.currentText()};")
            elif line.startswith('Terminal='):
                new_content.append(f"Terminal={'true' if self.terminal_checkbox.isChecked() else    'false'}")
            elif line.startswith('Type='):
                new_content.append(f"Type={self.type_combo.currentText()}")
            else:
                new_content.append(line)

        # Add entries if not present
        if not any(line.startswith('Name=') for line in new_content):
            new_content.append(f"Name={self.name_edit.text()}")
        if not any(line.startswith('Comment=') for line in new_content):
            new_content.append(f"Comment={self.comment_edit.text()}")
        if not any(line.startswith('Exec=') for line in new_content):
            new_content.append(f"Exec={self.exec_edit.text()}")
        if not any(line.startswith('Icon=') for line in new_content):
            new_content.append(f"Icon={self.icon_path}")
        if not any(line.startswith('Categories=') for line in new_content):
            new_content.append(f"Categories={self.category_combo.currentText()};")
        if not any(line.startswith('Terminal=') for line in new_content):
            new_content.append(f"Terminal={'true' if self.terminal_checkbox.isChecked() else    'false'}")
        if not any(line.startswith('Type=') for line in new_content):
            new_content.append(f"Type={self.type_combo.currentText()}")

        # Write the updated content back to the file
        with open(file_name, 'w') as file:
            file.write('\n'.join(new_content))


    def quitApp(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    editor = DesktopFileEditor()
    if len(sys.argv) > 1:
        editor.loadDesktopFile(sys.argv[1])
    sys.exit(app.exec_())
