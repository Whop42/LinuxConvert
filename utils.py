import os
from software import neofetch, flameshot, vscode

debug = True

def locate_application_path(name):
    """
    returns full path of application folder
    (folder should look like:

    app_name/
        app_name_application.json
        config (optional)/
            ...
    )
    """

    for filename in os.listdir(os.getcwd()):
        if "-linuxconvert" in filename:
            for application_folder in os.listdir(os.path.join(os.getcwd(), filename, "applications")):

                if application_folder == name:
                    return os.path.join(os.path.join(os.getcwd(), filename, "applications", application_folder))

def locate_backup_folder():
    """
    returns file backup folder (contains Documents, Desktop, etc.)
    """
    for filename in os.listdir(os.getcwd()):
        if "-linuxconvert" in filename:
            return os.path.join(os.get_cwd(), "file_backups")

def get_softwares():
    output = []

    output.append(neofetch.neofetch())
    output.append(flameshot.flameshot())
    output.append(vscode.vscode())

    return output

def dprint(message):
    """
    prints a debug message
    """

    if debug:
        print("DEBUG: " + message)