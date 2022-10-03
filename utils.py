import os
import shutil
from software import neofetch, flameshot, vscode, backups

debug = True

def get_root_folder():
    for filename in os.listdir(os.getcwd()):
        if "-linuxconvert" in filename:
            return filename
            
def locate_application_path(name):
    """
    returns full path of application folder
    (folder should look like:

    app_name/\n
    --- app_name_application.json\n
    --- config/\n
            ...
    )
    """

    for filename in os.listdir(os.getcwd()):
        if "-linuxconvert" in filename:
            for application_folder in os.listdir(os.path.join(os.getcwd(), filename, "applications")):

                if application_folder == name:
                    return os.path.join(os.getcwd(), filename, "applications", application_folder)

def get_softwares():
    output = []

    output.append(neofetch.neofetch())
    output.append(flameshot.flameshot())
    output.append(vscode.vscode())
    output.append(backups.backups())

    return output

def dprint(message):
    """
    prints a debug message
    """

    if debug:
        print("DEBUG: " + str(message))

def eprint(message):
    """
    prints an error
    """

    if debug:
        print("ERROR: " + str(message))

def move_dirs_to_dir(dirs, output):
    try:
        os.mkdir(output)
    except FileExistsError as e:
        eprint(output + " already exists")
        return False # it didn't work
    
    try:
        for f in dirs:
            shutil.copytree(f, os.path.join(output, f))
    except FileNotFoundError as e:
        eprint(e.strerror)
        return False # it didn't work
    return True # it worked :)