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

- Create a vm of the latest release of EndeavourOS with the offline install option
- Update the system (`yay -Syyu && sudo grub-install`) <!-- delete this after the grub issue fixed -->
- Clone this repository
- See below for running

### Windows:

- Clone this repository
- See below for running

## Running

### Linux side:

`sudo python linux_setup.py` in the directory with the config folder

### Windows side:

`python windows10_setup.py` in the directory where you want the config folder to generate

---
## Roadmap

- [x] Proof-of-concept for installing applications from config
- [X] Move documents/pictures/etc
- [ ] Windows application
    - [X] Create config folder + config file
    - [X] Get system personalization options
    - [X] Update each Software to get windows configs
    - [X] Backup Documents, Pictures, etc.
        - [X] Make each of them a software
    - [ ] GUI
- [_] Theme XFCE to appear similar to original OS, along with personalization settings
- [_] Recommendation system for proprietary/bad software
- [ ] Create scripts to install popular applications w/configs
    - [ ] Firefox
    - [ ] Chromium
    - [ ] Edge
    - [X] VSCode
    - [ ] Office (LibreOffice or similar)
        - [ ] Theme LibreOffice like MS Office
    - [ ] Zoom
    - [ ] Teams
    - [ ] Discord
    - [ ] OBS
    - [ ] Steam
- [ ] Create GUI for install
- [ ] Make website with instructions for install
- [ ] Create scripts to install more applications
