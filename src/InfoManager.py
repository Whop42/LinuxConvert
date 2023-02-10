import software
from software import Software, neofetch, flameshot, vscode, backups, discord, betterdiscord, firefox, google_chrome, chromium, edge, libreoffice
from software import teams, zoom, steam, obs, notion, anki
class InfoManager(object):
    # list of possible softwares
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
        anki.anki()
    ]

    applications: list[Software.Software] = []

    config: dict = {}

    installed_softwares: list[str] = []

    # singleton
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(InfoManager, cls).__new__(cls)
        return cls.instance
