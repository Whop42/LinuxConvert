import os
import shutil
from software import neofetch, flameshot, vscode, backups
from distutils.dir_util import copy_tree
from distutils.errors import DistutilsFileError

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

def copy_dir(src, dest):
    """
    copies a dir to another dir
    returns false if any errors, true otherwise
    """
    try:
        copy_tree(src.replace("~", os.path.expanduser("~")), dest.replace("~", os.path.expanduser("~")))
        return True
    except FileNotFoundError as e:
        eprint(e)
    except DistutilsFileError as e:
        eprint(e)
    return False

def copy_dirs(dirs, dest):
    """
    copies a list of dirs to another dir
    returns false if any errors, true otherwise
    """

    for d in dirs:
        if copy_dir(d, os.path.join(dest, os.path.split(d)[1])):
            dprint(f"copied {d} to {dest}")
        else:
            return False
    return True