import software
from software import Software, neofetch, flameshot, vscode, backups, discord, betterdiscord, firefox, google_chrome, chromium, edge, libreoffice

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
        libreoffice.libreoffice()
    ]

    applications: list[Software.Software] = []

    config: dict = {}

    installed_softwares: list[str] = []

    # singleton
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(InfoManager, cls).__new__(cls)
        return cls.instance
