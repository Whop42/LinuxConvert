# LinuxConvert

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://opensource.org/licenses/)
<!-- [![Github All Releases](https://img.shields.io/github/downloads/whop42/LinuxConvert/total.svg?style=flat)]() -->
[![GitHub commit activity the past week, 4 weeks](https://img.shields.io/github/commit-activity/w/whop42/LinuxConvert.svg?style=flat)]()

> (CSRSEF Project)
> WIP

Creates a personalized linux setup from a windows setup, with minimal user interaction.

It's currently designed to install on EndeavourOS XFCE (offline install.)

## Installation (For Testing/Development)

### Linux:

- Create a VM (or hardware machine) of the latest release of EndeavourOS with the offline install option
- Update the system (`yay -Syyu`)
- Clone this repository
- See below for running

### Windows:

- Create a VM (or hardware machine) of windows 10
- Set it up to your liking
- Clone this repository
- See below for running

## Running

### Linux side:

`python main.py /path-to-zip-file.zip/`

### Windows side:

`python main.py`

---
## Roadmap

- [x] Proof-of-concept for installing applications from config
- [X] Move documents/pictures/etc
- [ ] Windows application
    - [X] Create config folder + config file
    - [X] Get system personalization options
    - [X] Update each Software to get windows configs
    - [X] Backup Documents, Pictures, etc.
- [X] Theme XFCE to appear similar to original OS, along with personalization settings
- [X] Recommendation system for proprietary/bad software
- [ ] Create scripts to install popular applications w/configs
    - [X] Firefox
    - [X] Chromium
    - [X] Edge
    - [X] VSCode
    - [X] Office (LibreOffice or similar)
        - [X] Theme LibreOffice like MS Office
    - [X] Zoom
    - [X] Teams
    - [X] Discord, BetterDiscord
    - [X] OBS
    - [X] Steam
    - [X] Wine
    - [X] Bottles
    - [ ] Adobe Alternatives (Inkscape, GIMP, Shotcut/Kdenlive)
    - [ ] Blender
    - [ ] Epic Games
    - [ ] VPNs (proton, nord, openvpn, etc)
    - [ ] Tor
    - [ ] ClamAV
    - [ ] Virtualbox
    - [ ] IntelliJ, Eclipse, and jGRASP
- [ ] Make website with instructions for install
- [ ] Automate builds with PyInstaller
