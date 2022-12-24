import software
from software import Software, neofetch, flameshot, vscode, backups, discord, betterdiscord

class InfoManager(object):
    def __init__(self):
        # list of possible softwares
        self.softwares: list[Software.Software] = [
            neofetch.neofetch(),
            flameshot.flameshot(),
            vscode.vscode(),
            backups.backups(),
            discord.discord(),
            betterdiscord.betterdiscord()
        ]

        self.installed_softwares: list[str] = []

        self.config = {}

    # singleton
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(InfoManager, cls).__new__(cls)
        return cls.instance
