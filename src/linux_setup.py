import subprocess
from install_software import Install_Software
import os
import shutil
import sys
from utils import eprint, dprint
import logging

logger: logging.Logger = logging.getLogger(__name__ + "::" + __file__)

def main() -> None:
    if not sys.argv[1]:
        logger.error("no CLI argument for zip file...")
        exit()

    final_conf_path: str = unzip(sys.argv[1])
    
    install_software: Install_Software = Install_Software()
    config: dict = install_software.load_files(final_conf_path)
    logger.info("loaded config from " + final_conf_path)

    install_software.install_from_list()

    config: dict = {"original_os": "assads"}

    theme(config)

    logger.info("LinuxConvert install completed!")

def unzip(zipfile: str) -> str:
    """
    unzips the file provided to it to a folder in os.getcwd
    of the same name

    returns: final path of folder
    """
    logger.info("unzipping config folder...")

    # move entire config folder to <cwd>/<zipfile_name_without_.zip>/
    conf_path: str = zipfile.removesuffix(".zip")
    final_conf_path: str = os.path.join(os.getcwd(), os.path.split(conf_path)[1])

    try:
        shutil.unpack_archive(zipfile, final_conf_path)
    except OSError as e:
        logger.error(str(e))
        exit()
    logger.info("unzipped config folder to " + final_conf_path)
    return final_conf_path

def theme(config: dict) -> None:
    """
    chooses and calls the appropriate setup function for
    each possible value of config["original_os"]

    returns: nothing
    """
    original_os: str = config["original_os"]
    if(original_os == "win10"):
        win10(config)
    elif(original_os == "win11"):
        win11(config)
    elif(original_os == "none"):
        pass
    else:
        logger.error("config doesn't specify OS (may be corrupt)")

        theme_choice: str = input("which theme would you like? (win10/win11/none) ")

        if theme_choice.lower() in ["win10", "win11", "none"]:
            config["original_os"] = theme_choice.lower()
        else:
            print("invalid option...")

        theme(config)

def win10(conf: dict) -> None:
    #install win10 lookalike theme

    #move/add launchers to taskbar/panel

    #set background image

    #set lockscreen image
    pass

def win11(conf: dict) -> None:
    #install win11 lookalike theme

    #move/add launchers to taskbar/panel

    #set background image

    #set lockscreen image
    pass

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    main()