from Software import Software
from os import system as cmd

class neofetch(Software):
    
    def __init__(self):
        super(Software, self).__init__("neofetch")
    
    def install(self):
        cmd("apt install neofetch -y")
    
    def uninstall(self):
        cmd("apt remove neofetch")