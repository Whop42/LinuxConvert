import subprocess
from install_software import Install_Software
import os
import shutil
import sys
from utils import eprint, dprint, cmd
import utils
import logging
from InfoManager import InfoManager
import requests
import urllib
import zipfile


logger: logging.Logger = logging.getLogger(__name__ + "::" + __file__)

install_software: Install_Software = Install_Software()
im: InfoManager = InfoManager()

def main(zip_path) -> None:
    if not zip_path:
        logger.error("argument for zip file...")
        exit()

    final_conf_path: str = unzip(zip_path)
    install_software.load_files(final_conf_path)
    config: dict = InfoManager.config
    logger.info("loaded config from " + os.path.join(final_conf_path, "windows-config.json") + " (" + str(config) + ")")

    install_software.install_from_list()

    theme(config)

    dprint("removing " + final_conf_path + "...")
    shutil.rmtree(final_conf_path)
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
    try:
        original_os: str = config["original_os"]
    except TypeError as e:
        config["original_os"] = "???"
        original_os: str = config["original_os"]
    if(original_os == "win10"):
        win10(config)
    elif(original_os == "win11"):
        win11(config)
    elif(original_os == "none"):
        pass
    else:
        logger.error("config doesn't specify OS (may be corrupt)")

        theme_choice: str = input("which theme would you like? (win10/none) ")

        if theme_choice.lower() in ["win10", "none"]:
            config["original_os"] = theme_choice.lower()
        else:
            print("invalid option...")

        theme(config)

def download_zip(url: str, fdir: str, name: str) -> None:
    zip_ = requests.get(url).content

    zip_file = open(name, "wb")
    with zip_file as f:
        f.write(zip_)

    cmd(['unzip', "-o", name, '-d', fdir], sudo=True)

    fdir: str = os.path.expandvars(fdir)
    os.remove(name)

    dprint(f"downloaded {url} to {fdir}")

def win10(conf: dict) -> None:
    # download theme as zip
    theme_name = "Windows-10-3.2.1"
    boomerang_url: str = "https://github.com/B00merang-Project/Windows-10/archive/refs/tags/3.2.1.zip"
    if conf["personalization"]["theme_mode"] == "dark":
        theme_name = "Windows-10-Dark-3.2.1-dark"
        boomerang_url = "https://github.com/B00merang-Project/Windows-10-Dark/archive/refs/tags/3.2.1-dark.zip"

    themes_dir = "/usr/share/themes"
    name = "boomerang"

    download_zip(boomerang_url, themes_dir, name + ".zip")

    # install gtk theme in Xfce
    utils.xfconf("xfwm4", "/general/theme", theme_name)
    utils.xfconf("xsettings", "/Net/ThemeName", theme_name)

    # icons
    download_zip("https://github.com/B00merang-Artwork/Windows-10/archive/master.zip", "/usr/share/icons", "win10-icons")
    utils.xfconf("xsettings", "/Net/IconThemeName", "Windows-10-master")

    # cursors
    utils.xfconf("xsettings", "/Gtk/CursorThemeName", "elementary")


    taskbar(conf)
    bkg_images(conf)

def taskbar(conf: dict) -> None:
    os.system("xfconf-query -c xfce4-panel -p /panels/panel-1/background-rgba -n -t double -t double -t double -t double -s 0 -s 0 -s 0 -s 1")

    utils.cmd(["yay", "-Syyu", "--noconfirm", "xfce4-panel-profiles"])

    utils.cmd(["xfce4-panel-profiles", "load", os.path.join(os.getcwd(), "src", "media", "lc-light.tar.bz2")])

    # move/add launchers to panel
    # xfconf-query -c xfce4-panel -p /panels/panel-1/position
    if conf["personalization"]["theme_mode"] == "dark":
        os.system("xfconf-query -c xfce4-panel -p /panels/dark-mode -s true")
    else:
        os.system("xfconf-query -c xfce4-panel -p /panels/dark-mode -s false")
    
    # change terminal color
    terminalrc_path = os.path.expanduser("~/.config/xfce4/terminal/terminalrc")
    if os.path.exists(terminalrc_path):
        os.remove(terminalrc_path)
    utils.copy_file(os.path.join(os.getcwd(), "src", "media", "terminalrc"), terminalrc_path)


def bkg_images(conf: dict) -> None:
    # set background image
    file = InfoManager.config["personalization"]["background_image"]

    final_path = os.path.expanduser(os.path.join("~/Pictures", file))
    
    utils.cmd(["cp", os.path.join(utils.get_root_folder(), file), final_path])
    utils.xfconf("xfce4-desktop", "/backdrop/screen0/monitorVirtual1/workspace0/last-image", final_path)
    dprint("set background image")
    # set lockscreen image
    pass

def win11(conf: dict) -> None:
    #install win11 lookalike theme

    #move/add launchers to taskbar/panel

    #set background image

    #set lockscreen image
    pass

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    main(sys.argv[1])