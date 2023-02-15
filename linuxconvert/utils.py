import os
import shutil
from typing import NoReturn
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file as cp_file
from distutils.errors import DistutilsFileError
import logging
import subprocess

debug: bool = True

logging.basicConfig(
    format="%(asctime)-15s [%(levelname)s]: %(message)s",
    level=logging.DEBUG
)

def get_root_folder() -> str:
    """
    finds the root folder (produced by unzipping zip)
    exit()s if it can't find it
    """
    filename: str = ""
    for filename in os.listdir(os.getcwd()):
        if "-linuxconvert" in filename and ".zip" not in filename:
            return filename
    eprint("couldn't find root folder")
    exit(0)
            
def locate_application_path(name) -> str:
    """
    returns full path of application folder
    exit()s if it can't find the path

    (folder should look like:

    app_name/\n
    --- app_name_application.json\n
    --- config/\n
            ...
    )
    """

    root_folder: str = get_root_folder()

    for application_folder in os.listdir(os.path.join(root_folder, "applications")):

        if application_folder == name:
            return os.path.join(root_folder, "applications", application_folder)
    eprint("couldn't locate application path")
    exit(0)

def dprint(message):
    """
    prints a debug message
    """

    logging.debug(str(message))

def eprint(message):
    """
    prints an error
    """

    logging.error(str(message))

def copy_dir(src: str, dest: str):
    """
    copies a dir to another dir
    exit()s if any errors
    """
    try:
        copy_tree(src.replace("~", os.path.expanduser("~")), dest.replace("~", os.path.expanduser("~")))
    except OSError as e:
        eprint(e)
        exit(0)

def copy_dirs(dirs: list[str], dest: str):
    """
    copies a list of dirs to another dir
    uses copy_dir(), which exit()s if any errors occur
    """

    for d in dirs:
        copy_dir(d, os.path.join(dest, os.path.split(d)[1]))
        dprint(f"copied {d} to {dest}")

def copy_file(src: str, dest: str):
    """
    copies a file to a file
    exit()s if any errors
    """
    try:
        cp_file(src.replace("~", os.path.expanduser("~")), dest.replace("~", os.path.expanduser("~")))
        return True
    except OSError as e:
        eprint(e)
        exit(0)

def copy_files(files, dest):
    """
    copies files to a dir
    uses copy_file(), which exit()s if any errors
    """
    for f in files:
        copy_file(f, os.path.join(dest, os.path.split(f)[1]))
        dprint(f"copied {f} to {dest}")


def test_im():
    import InfoManager
    return InfoManager.InfoManager()

def cmd(command: list[str], sudo: bool = False) -> str:
        """
        cmd runs a command

        params:
            list[str] command -> the command to run (main command followed by args)
            bool sudo -> whether or not to run as sudo (default False)

        returns:
            str -> output of the command
        
        raises:
            Exception -> command fails
        """
        if sudo:
            command.insert(0, "sudo")
        
        output = subprocess.run(command, stdout=subprocess.PIPE)

        # catch errors!
        if output.returncode != 0:
            raise Exception("command " + str(command) + " failed...")

        return str(output.stdout)

def xfconf(channel: str, prop: str, value) -> None:
    os.system(f"xfconf-query -c {channel} -p {prop} -s {str(value)}")
