from Software import Software
from os import system as cmd

class neofetch(Software):
    
    def __init__(self):
        super(Software, self).__init__("neofetch")
    
    def install(self):
        cmd("dpkg -i neofetch -y")
    
    def uninstall(self):
        cmd("dpkg -remove neofetch")