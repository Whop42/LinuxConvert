from software import Software, backups, flameshot, neofetch, vscode, discord

def get_softwares() -> list[str]:
        output = []

        output.append(neofetch.neofetch())
        output.append(flameshot.flameshot())
        output.append(vscode.vscode())
        output.append(backups.backups())
        output.append(discord.discord())

        return output