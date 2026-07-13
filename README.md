# mac-new-file-creator
This is a local macOS utility using Automator and Python to right click a folder anywhere in Finder
and instantly create a blank file such as `.txt`, `.md`, `.py`, and `.pages`.

## Why I built it
Coming from Windows to Mac, I've always loved being able to right click in File
Explorer and create new files on the go. With Mac, it isn't possible by default.

## Known Limitations
- Quick Actions do not appear when right-clicking empty space in Finder
- Right-click an existing file or folder inside your target directory instead


## How to install
1. Clone the repo to directory of your choice

2. Make sure python3 is installed

3. Open Automator and create a new Quick Action

4. In Library under actions, search for `Run Shell Script` and drag it into the workflow

5. Set `Workflow receives current` to `folder` in `finder`

6. In the script box, type `python3 /path/to/main.py "$1"`

7. Replace `/path/to/main.py` with the actual path to `main.py` on your machine

8. Optional: set the Quick Action image to `+` in Automator for a cleaner look

9. Right-click any file or folder in your target directory, select 
   `Quick Actions` → `New File Creator`


## Built with
- Python3
- macOS Automator (Quick Actions)
- osascript / AppleScript for GUI dialog
