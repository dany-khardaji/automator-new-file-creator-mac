import os                                                      # Navigates files and folders on the os.
import sys                                                     # Accesses system info like arguments, exit codes, and platform details; used here for sys.argv.
import shutil                                                  # Copy, move, and delete files.
import subprocess                                              # Runs terminal commands from inside Python; used here to run osascript for the Mac dialog.

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")  # Find the folder this script lives in, then point to the templates subfolder inside it.

FILE_TYPES = {                                                 # Dictionary structure for the menu and program.
    "1": ("Text File", "blank.txt"),
    "2": ("Markdown File", "blank.md"),
    "3": ("Python File", "blank.py"),
    "4": ("Pages File", "blank.pages"),
}

# Dynamically builds a native macOS dialog using osascript (AppleScript).
# Formats the FILE_TYPES dictionary into AppleScript's list syntax,
# Runs it via subprocess, and returns the matching key from the user's selection.
# Note: AppleScript requires curly braces {} for lists, not Python's square brackets [].
def get_user_choice():
    options = ", ".join([f'"{key}. {name}"' for key, (name, _) in FILE_TYPES.items()])
    script = f'choose from list {{{options}}} with prompt "What type of file do you want to create?"'
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    selected = result.stdout.strip()
    for key, (name, _) in FILE_TYPES.items():
        if selected.startswith(key):
            return key
        
def get_destination():
    if len(sys.argv) < 2:                                      # Failsafe - If no folder path is passed in from Automator, fall back to the Desktop as the destination.
        return os.path.expanduser("~/Desktop")
    return sys.argv[1]                                         # Grabs the folder path passed in via sys.argv sent by Automator when right-clicking in Finder.

def create_file(choice, destination):
    _, blank_file = FILE_TYPES[choice]                         # Unpack the tuple from FILE_TYPES — ignore the display name, keep the template filename.
    template_path = os.path.join(TEMPLATES_DIR, blank_file)    # Build the full path to the template file.
    shutil.copy(template_path, destination)                    # Copy the template to the destination folder.

def main():                                                    # Runs each function in order, created choice/destination variables to link the create_file function.
    choice = get_user_choice()
    destination = get_destination()
    create_file(choice, destination)

if __name__ == "__main__":                                     # This tells the code to run only when triggered. Not automatically when imported.
    main()