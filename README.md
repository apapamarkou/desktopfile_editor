# Desktopfile editor 
![Screenshot_20240703_232813](https://github.com/apapamarkou/desktopfile_editor/assets/42995877/b639c158-d5af-41f1-9b7b-bb96b3dcc56a)
A simple and convenient utility to edit or create .desktop files. 

## Features

- Automatically add system edited .desktop files to your .local/share to override safely the system one.
- Easy setup and configuration.

## Dependencies

To run this application, you need the following dependencies:

- Python 3
- PyQt5

## Installation

## Installation Instructions

1. **Install dependencies:**

    - **Arch Linux, Manjaro, Garuda**
    ```bash
    sudo pacman -S python-pyqt5
    ```

    - **RedHat, Fedora**
    ```bash
    sudo dnf install python3-qt5
    ```

    - **OpenSUSE**
    ```bash
    sudo zypper install python3-qt5
    ```

    - **Solus**
    ```bash
    sudo eopkg install python3-qt5
    ```

     - **Debian, Ubuntu, Mint**
    ```bash
    sudo apt-get install python3-pyqt5
    ```

   - **Slackware**   
   You may need to compile PyQt5 from source or find packages suitable for Slackware.


2. **Install the script**:
    ```bash
    mkdir -p ~/Applications/appimage_manager
    git clone https://github.com/apapamarkou/desktopfile_editor.git ~/Applications/desktopfile_editor
    chmod +x ~/Applications/desktopfile_editor/desktopfile_editor.py
    chmod +x ~/Applications/desktopfile_editor/install.sh
    ~/Applications/desktopfile_editor/install.sh
    ```

## Usage

Right click on a .desktop file -> Open With -> Other Application -> Select the "Desktopfile Editor" application.

## Troubleshooting

- Ensure the `python3` package is installed and up to date.
- Verify that the `desktopfile_editor.py` script has executable permissions.

## License

This utility is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.


