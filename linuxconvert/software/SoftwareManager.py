import Software, neofetch, flameshot, vscode, backups, discord, betterdiscord, firefox, google_chrome, chromium, edge, libreoffice
import teams, zoom, steam, obs, notion, anki, minecraft, spotify, bottles, okular, gimp, inkscape, kdenlive, vivaldi, opera, pamac

# list of possible Softwares
softwares: list[Software.Software] = [
        neofetch.neofetch(),
        flameshot.flameshot(),
        vscode.vscode(),
        backups.backups(),
        discord.discord(),
        betterdiscord.betterdiscord(),
        firefox.firefox(),
        google_chrome.google_chrome(),
        chromium.chromium(),
        edge.edge(),
        libreoffice.libreoffice(),
        teams.teams(),
        zoom.zoom(), 
        steam.steam(),
        obs.obs(),
        notion.notion(),
        anki.anki(),
        minecraft.minecraft(),
        spotify.spotify(),
        bottles.bottles(),
        okular.okular(),
        gimp.gimp(),
        inkscape.inkscape(),
        kdenlive.kdenlive(),
        vivaldi.vivaldi(),
        opera.opera(),
        pamac.pamac()
    ]

class SoftwareManager(object):
    found_applications: list[Software.Software] = []

    config: dict = {}

    installed_softwares: list[str] = []
