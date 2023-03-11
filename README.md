# LinuxConvert

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://opensource.org/licenses/)
[![Github All Releases](https://img.shields.io/github/downloads/whop42/LinuxConvert/total.svg?style=flat)]()
[![GitHub commit activity the past week, 4 weeks](https://img.shields.io/github/commit-activity/w/whop42/LinuxConvert.svg?style=flat)]()

> (CSRSEF Project)

Creates a personalized linux setup from a windows setup, with minimal user interaction.

To use, simply run `main.py` on Windows and move the .zip file over to Linux. Then, run again with the .zip as an argument to `main.py`.

It currently runs on EndeavourOS XFCE (offline install.)

## Join the Study!

LinuxConvert is designed for the purposes of a scientific study. To join it, see [here](https://linuxconvert.notion.site). This will be over by March 4th, 2023.

## Installation (For Testing/Development)

### Linux:

- Create a VM (or hardware machine) of the latest release of EndeavourOS with the offline install option
- Update the system (`yay -Syyu`)
- Clone this repository
- `python main.py /path-to-zip-file.zip/`

### Windows:

- Create a VM (or hardware machine) of windows 10
- Set it up to your liking
- Clone this repository
- `python main.py`

## Features

- Scrapes application info off of Windows into a .zip file
- Takes `C:\Users\$USERNAME\` directory backups
- Installs software from .zip file on EndeavourOS Linux
- Configures Linux system to appear like Windows
- Uses personalization settings from Windows on Linux
- Enables the use of all this by simply running two commands

## Selected Supported Software (and their packages)

> Does not include Windows applications that are only moved to OSS versions, personalization themes/icon themes/bash configs/some default applications that are installed as utilities

- Anki (anki-bin)
- BetterDiscord (betterdiscordctl)
- Bottles (bottles) + Wine
- Chromium (chromium)
- Discord (discord)
- Microsoft Edge (microsoft-edge-stable-bin) (recommends Firefox)
- Firefox (firefox)
- Flameshot (flameshot)
- GIMP (gimp) (replaces photo editor)
- Google Chrome (google-chrome) (recommends Chromium)
- Inkscape (inkscape) (replaces Adobe Illustrator)
- Kdenlive (kdenlive) (replaces Adobe Premiere Pro)
- LibreOffice (libreoffice-fresh) with English Dictionary + MS Office Theming
- Minecraft Launcher (minecraft-launcher)
- Neofetch (neofetch)
- Notion (notion-app)
- OBS Studio (obs-studio)
- Okular (okular) (replaces PDF viewer)
- Opera (opera) (including Opera GX)
- Pamac (pamac-all)
- Spotify (spotify-launcher)
- Steam Runtime (steam) + Proton
- Microsoft Teams (teams)
- Vivaldi (vivaldi)
- Visual Studio Code OSS (code + code-marketplace) (replaces vscode proprietary)
- Zoom (zoom)
